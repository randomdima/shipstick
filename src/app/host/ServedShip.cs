using System.Diagnostics;
using System.IO.Compression;
using System.Security.Cryptography;
using System.Text.Json;
using Shipstick.Codex;
using Shipstick.Core.Config;
using Shipstick.Economy;
using Shipstick.Items;
using Shipstick.Ship;

namespace Shipstick.App.Host;

/// <summary>
/// The one ship the host runs (HST-3), its clock, and the clients watching it. The clock advances the ship every
/// <see cref="HostFigures.TickS"/>, and after each advance and each action every client is told what changed for it.
/// </summary>
/// <remarks>
/// <b>The ship is touched under one gate</b>: the clock's tick and every client's action take turns, so the game's types
/// stay single-threaded as they were written.
/// </remarks>
sealed class ServedShip : BackgroundService
{
    readonly Lock gate = new();
    readonly List<Client> clients = [];
    readonly Stopwatch real = Stopwatch.StartNew();
    double advancedRealS;

    public ServedShip(GameConfig config, Catalogue catalogue)
    {
        Config = config;
        Ways = new WayIndex(catalogue);
        Vessel = StarterShip.Lay(config, catalogue);
        CodexJson = JsonSerializer.SerializeToUtf8Bytes(CodexBook.Of(catalogue, config), HostJson.Default.CodexBook);
        CodexBrotli = Brotli(CodexJson);
        CodexTag = $"\"{Convert.ToHexString(SHA256.HashData(CodexJson))}\"";
        Catalogue = catalogue;
    }

    public GameConfig Config { get; }

    public Catalogue Catalogue { get; }

    public WayIndex Ways { get; }

    public Vessel Vessel { get; }

    /// <summary>Ship seconds a real second: 1, unless the admin has set it otherwise (WEB-2).</summary>
    public double Rate { get; private set; } = 1;

    /// <summary>The codex's JSON (<see cref="CodexBook"/>), made once: it is built from what the game was compiled with.</summary>
    public byte[] CodexJson { get; }

    /// <summary>
    /// <see cref="CodexJson"/> compressed once, at the smallest Brotli makes: it is most of what a client downloads, and
    /// compressing it per request at that size would cost each client seconds.
    /// </summary>
    public byte[] CodexBrotli { get; }

    /// <summary>The codex's entity tag, so a client already holding it is answered "not modified".</summary>
    public string CodexTag { get; }

    public bool Holds(CapsuleAt at) => Vessel.Grid.Holds(at) && Vessel.CapsuleOn(at) is not null;

    /// <summary>The first capsule in reading order: where the admin stands on joining.</summary>
    public CapsuleAt FirstCapsule()
    {
        for (var row = 0; row < Vessel.Grid.Rows; row++)
            for (var column = 0; column < Vessel.Grid.Columns; column++)
                if (Holds(new CapsuleAt(column, row))) return new CapsuleAt(column, row);
        throw new InvalidOperationException("the ship holds no capsule");
    }

    public void Join(Client client)
    {
        lock (gate)
        {
            clients.Add(client);
            client.Tell(this);
        }
    }

    public void Leave(Client client)
    {
        lock (gate) clients.Remove(client);
    }

    /// <summary>Runs one client's action at the ship's present, then tells every client what it changed.</summary>
    public bool Act(Func<bool> action)
    {
        lock (gate)
        {
            Advance();
            var taken = action();
            TellAll();
            return taken;
        }
    }

    /// <summary>
    /// A seat's choice of the way a device runs, <paramref name="way"/> its <see cref="WayIndex"/>; refused for a way the
    /// device does not run.
    /// </summary>
    public bool Select(CapsuleAt seat, int inventory, int way)
    {
        if (Vessel.DeviceOf(inventory) is not { } device || Ways.At(way) is not { } chosen) return false;
        for (var local = 0; local < device.Ways.Count; local++)
            if (ReferenceEquals(device.Ways[local], chosen))
                return Vessel.Select(seat, inventory, local);
        return false;
    }

    /// <summary>An admin's edit of one slot (SHP-6); an <paramref name="item"/> that names no item of the catalogue is refused.</summary>
    public bool Set(int inventory, int slot, string item, int count) =>
        (count == 0 || Catalogue.Item(item) is not null) && Vessel.Set(inventory, slot, new Item(item), count);

    /// <summary>The admin's rate for ship time, from a stop to <see cref="HostFigures.RateMost"/>.</summary>
    public bool SetRate(double rate)
    {
        if (!(rate >= 0 && rate <= Config.Host.RateMost)) return false;
        Rate = rate;
        return true;
    }

    protected override async Task ExecuteAsync(CancellationToken stopping)
    {
        using var ticks = new PeriodicTimer(TimeSpan.FromSeconds(Config.Host.TickS));
        while (await ticks.WaitForNextTickAsync(stopping))
            lock (gate)
            {
                Advance();
                TellAll();
            }
    }

    void Advance()
    {
        var realS = real.Elapsed.TotalSeconds;
        Vessel.AdvanceTo(Vessel.NowS + (realS - advancedRealS) * Rate);
        advancedRealS = realS;
    }

    void TellAll()
    {
        foreach (var client in clients) client.Tell(this);
    }

    static byte[] Brotli(byte[] bytes)
    {
        using var compressed = new MemoryStream();
        using (var brotli = new BrotliStream(compressed, CompressionLevel.SmallestSize)) brotli.Write(bytes);
        return compressed.ToArray();
    }
}

/// <summary>Each way's index in <see cref="Catalogue.Ways"/>, by reference: two ways may read alike. How a client names a way.</summary>
sealed class WayIndex
{
    readonly Catalogue catalogue;
    readonly Dictionary<WayEntry, int> indices = new(ReferenceEqualityComparer.Instance);

    public WayIndex(Catalogue catalogue)
    {
        this.catalogue = catalogue;
        for (var index = 0; index < catalogue.Ways.Count; index++) indices.Add(catalogue.Ways[index], index);
    }

    public int this[WayEntry way] => indices[way];

    public WayEntry? At(int index) => index >= 0 && index < catalogue.Ways.Count ? catalogue.Ways[index] : null;
}
