using System.Buffers;
using System.Collections.Concurrent;
using System.Net.WebSockets;
using System.Text.Json;
using System.Threading.Channels;
using Shipstick.Ship;

namespace Shipstick.App.Host;

/// <summary>
/// One client on its socket (HST-4). It is sent a frame — <c>{"nowS", "rate", "seat" | "ship"}</c> — whenever its view or
/// the ship's rate changes, and sends actions — <c>{"id", "act", …}</c> — each answered <c>{"re": id, "ok"}</c> once it
/// has run. Between frames a client tells the ship's time itself, from the last frame's time and rate.
/// </summary>
/// <remarks>
/// <b>A slow line is sent the newest frame, not every frame</b>: a frame still waiting to go is replaced by the next, so
/// a stalled client catches up in one frame rather than a queue of them. Answers are never dropped.
/// </remarks>
abstract class Client
{
    readonly Channel<bool> wake = Channel.CreateBounded<bool>(new BoundedChannelOptions(1)
    {
        FullMode = BoundedChannelFullMode.DropWrite,
    });

    readonly ConcurrentQueue<byte[]> answers = new();
    byte[]? frame;

    // The view and rate last framed; read and written under the ship's gate.
    byte[] shown = [];
    double shownRate = double.NaN;

    /// <summary>The client a socket's query asks for: the admin's for <c>?admin</c>, else a player's at <c>?seat=column,row</c>; null for a seat with no capsule.</summary>
    public static Client? For(ServedShip ship, IQueryCollection query)
    {
        if (query.ContainsKey("admin")) return new AdminClient(ship.FirstCapsule());
        var seat = query["seat"].ToString().Split(',');
        return seat.Length == 2 && int.TryParse(seat[0], out var column) && int.TryParse(seat[1], out var row)
               && ship.Holds(new CapsuleAt(column, row))
            ? new SeatClient(new CapsuleAt(column, row))
            : null;
    }

    /// <summary>This client's view, named as the frame names it, and its JSON.</summary>
    protected abstract (string Kind, byte[] Json) Look(ServedShip ship);

    /// <summary>Runs one of this client's actions under the ship's gate; whether the game took it.</summary>
    protected abstract bool Act(ServedShip ship, ClientAction action);

    /// <summary>Frames this client's view if it or the rate changed since the last frame. Called under the ship's gate.</summary>
    public void Tell(ServedShip ship)
    {
        var (kind, view) = Look(ship);
        if (ship.Rate.Equals(shownRate) && view.AsSpan().SequenceEqual(shown)) return;
        (shown, shownRate) = (view, ship.Rate);
        Interlocked.Exchange(ref frame, Frame(ship.Vessel.NowS, ship.Rate, kind, view));
        wake.Writer.TryWrite(true);
    }

    /// <summary>Joins the ship, answers this client's actions until its socket closes, and leaves.</summary>
    public async Task Run(WebSocket socket, ServedShip ship, CancellationToken stopping)
    {
        using var leaving = CancellationTokenSource.CreateLinkedTokenSource(stopping);
        ship.Join(this);
        var sending = Send(socket, leaving.Token);
        try
        {
            var (status, why) = await Receive(socket, ship, leaving.Token);
            await leaving.CancelAsync();
            await sending.ConfigureAwait(ConfigureAwaitOptions.SuppressThrowing);
            if (socket.State is WebSocketState.Open or WebSocketState.CloseReceived)
                await socket.CloseAsync(status, why, stopping);
        }
        catch (Exception gone) when (gone is WebSocketException or OperationCanceledException)
        {
        }
        finally
        {
            ship.Leave(this);
        }
    }

    /// <summary>Reads actions until the client closes, or sends what is not one; how the socket is then closed.</summary>
    async Task<(WebSocketCloseStatus Status, string? Why)> Receive(WebSocket socket, ServedShip ship, CancellationToken leaving)
    {
        var buffer = new byte[ship.Config.Host.ActionBytesMost];
        while (true)
        {
            var read = 0;
            ValueWebSocketReceiveResult got;
            do
            {
                if (read == buffer.Length) return (WebSocketCloseStatus.MessageTooBig, "transmission refused: action too long");
                got = await socket.ReceiveAsync(buffer.AsMemory(read), leaving);
                if (got.MessageType == WebSocketMessageType.Close) return (WebSocketCloseStatus.NormalClosure, null);
                read += got.Count;
            } while (!got.EndOfMessage);

            ClientAction? action;
            try
            {
                action = JsonSerializer.Deserialize(buffer.AsSpan(0, read), HostJson.Default.ClientAction);
            }
            catch (JsonException)
            {
                action = null;
            }

            if (action is null) return (WebSocketCloseStatus.InvalidPayloadData, "transmission refused: malformed action");
            var taken = ship.Act(() => Act(ship, action));
            answers.Enqueue(Answer(action.Id, taken));
            wake.Writer.TryWrite(true);
        }
    }

    async Task Send(WebSocket socket, CancellationToken leaving)
    {
        while (await wake.Reader.WaitToReadAsync(leaving))
        {
            wake.Reader.TryRead(out _);
            while (answers.TryDequeue(out var answer))
                await socket.SendAsync(answer, WebSocketMessageType.Text, true, leaving);
            if (Interlocked.Exchange(ref frame, null) is { } next)
                await socket.SendAsync(next, WebSocketMessageType.Text, true, leaving);
        }
    }

    static byte[] Frame(double nowS, double rate, string kind, byte[] view) => Json(json =>
    {
        json.WriteNumber("nowS", nowS);
        json.WriteNumber("rate", rate);
        json.WritePropertyName(kind);
        json.WriteRawValue(view, skipInputValidation: true);
    });

    static byte[] Answer(int id, bool taken) => Json(json =>
    {
        json.WriteNumber("re", id);
        json.WriteBoolean("ok", taken);
    });

    static byte[] Json(Action<Utf8JsonWriter> write)
    {
        var buffer = new ArrayBufferWriter<byte>();
        using (var json = new Utf8JsonWriter(buffer))
        {
            json.WriteStartObject();
            write(json);
            json.WriteEndObject();
        }

        return buffer.WrittenSpan.ToArray();
    }
}

/// <summary>
/// What a client sends: one action named by <see cref="Act"/>, with the fields that action reads. <see cref="Id"/> is
/// the client's own, echoed in the answer.
/// </summary>
/// <param name="Act"><c>move</c> and <c>select</c> for anybody; <c>enter</c>, <c>rate</c> and <c>set</c> for the admin.</param>
sealed record ClientAction(
    int Id,
    string Act,
    int From,
    int FromSlot,
    int To,
    int ToSlot,
    int Inventory,
    int Slot,
    int Way,
    string? Item,
    int Count,
    int Column,
    int Row,
    double Rate);

/// <summary>
/// A player's client (WEB-7): sent their own cabin and the ship's walls round it, as <see cref="SeatView"/>, and acting
/// from their seat.
/// </summary>
sealed class SeatClient(CapsuleAt seat) : Client
{
    protected override (string, byte[]) Look(ServedShip ship) =>
        ("seat", JsonSerializer.SerializeToUtf8Bytes(SeatView.Of(ship.Vessel, seat, ship.Ways), HostJson.Default.SeatView));

    protected override bool Act(ServedShip ship, ClientAction action) => action.Act switch
    {
        "move" => ship.Vessel.Move(seat, action.From, action.FromSlot, action.To, action.ToSlot),
        "select" => ship.Select(seat, action.Inventory, action.Way),
        _ => false,
    };
}

/// <summary>
/// The admin's client (WEB-8): sent every cabin with one capsule entered, and taking the admin's own actions —
/// entering a capsule, setting the ship's rate, editing a slot (SHP-6) — beside a player's, made from the capsule
/// entered.
/// </summary>
sealed class AdminClient(CapsuleAt entered) : Client
{
    protected override (string, byte[]) Look(ServedShip ship) =>
        ("ship", JsonSerializer.SerializeToUtf8Bytes(ShipView.Of(ship.Vessel, entered, ship.Config.Items.StackMost, ship.Ways),
            HostJson.Default.ShipView));

    protected override bool Act(ServedShip ship, ClientAction action) => action.Act switch
    {
        "enter" => Enter(ship, new CapsuleAt(action.Column, action.Row)),
        "rate" => ship.SetRate(action.Rate),
        "set" => ship.Set(action.Inventory, action.Slot, action.Item ?? "", action.Count),
        "move" => ship.Vessel.Move(entered, action.From, action.FromSlot, action.To, action.ToSlot),
        "select" => ship.Select(entered, action.Inventory, action.Way),
        _ => false,
    };

    bool Enter(ServedShip ship, CapsuleAt at)
    {
        if (!ship.Holds(at)) return false;
        entered = at;
        return true;
    }
}
