using System.Buffers;
using System.Text.Json;
using System.Text.Json.Nodes;
using Shipstick.App.Host;
using Shipstick.Core.Config;
using Shipstick.Economy;
using Shipstick.Ship;

namespace Shipstick.App.Demo;

/// <summary>
/// The demo (DEM-1) as a static site: the client's files and art, the codex and the asset list as the host serves them,
/// and a recording of the frames the host sends each seat and the admin entered in each capsule over the starter ship's
/// first <see cref="DemoFigures.RecordedS"/>, with <c>demo.js</c> standing in for the host's socket.
/// </summary>
/// <remarks>
/// <b>The recording is the host's own</b>: the ship is advanced a host's tick at a time, at one ship second a real
/// second, and each client keeps the frame the host would send whenever its view changes — so the demo shows what the
/// game shows, cycles turning and stock running down, and holds no copy of its rules. Each frame is kept as a
/// <see cref="FramePatch"/> on the one before.
/// </remarks>
static class DemoSite
{
    /// <summary>
    /// The recording, by the path the page asks for it by: <c>{"loopS", "seat": {"column,row": timeline}, "ship": {…}}</c>,
    /// a timeline being <c>[[nowS, patch], …]</c> from no frame at all.
    /// </summary>
    const string RecordingPath = "demo/recording.json";
    const string Entry = """<script type="module" src="main.js"></script>""";
    const string StandIn = """<script src="demo.js"></script>""";

    /// <summary>Writes the site from the client's files in <paramref name="client"/> into the empty folder <paramref name="site"/>.</summary>
    public static void Write(GameConfig config, string client, string site)
    {
        Copy(client, site);

        var ship = new ServedShip(config, Catalogue.Embedded);
        File.WriteAllBytes(Path.Combine(site, "codex.json"), ship.CodexJson);
        File.WriteAllBytes(Path.Combine(site, "assets.json"), JsonSerializer.SerializeToUtf8Bytes(AssetList.Of(site)));
        var recording = Path.Combine(site, RecordingPath);
        Directory.CreateDirectory(Path.GetDirectoryName(recording)!);
        File.WriteAllBytes(recording, Record(ship, config.Demo.RecordedS, config.Host.TickS));

        var index = Path.Combine(site, "index.html");
        var page = File.ReadAllText(index);
        if (!page.Contains(Entry)) throw new InvalidOperationException($"index.html has no {Entry} for demo.js to load before");
        File.WriteAllText(index, page.Replace(Entry, $"{StandIn}\n  {Entry}"));
    }

    static byte[] Record(ServedShip ship, double recordedS, double tickS)
    {
        var watching = ship.Vessel.Capsules.Select(capsule => capsule.At)
            .SelectMany(at => new[] { new Watched("seat", at, new SeatClient(at)), new Watched("ship", at, new AdminClient(at)) })
            .ToArray();
        var ticks = (int)Math.Round(recordedS / tickS);
        for (var tick = 0; tick <= ticks; tick++)
        {
            if (tick > 0) ship.Vessel.AdvanceTo(tick * tickS);
            foreach (var watched in watching) watched.Look(ship);
        }

        var buffer = new ArrayBufferWriter<byte>();
        using (var json = new Utf8JsonWriter(buffer))
        {
            json.WriteStartObject();
            json.WriteNumber("loopS", ticks * tickS);
            foreach (var kind in watching.GroupBy(watched => watched.Kind))
            {
                json.WriteStartObject(kind.Key);
                foreach (var watched in kind)
                {
                    json.WritePropertyName($"{watched.At.Column},{watched.At.Row}");
                    watched.Timeline.WriteTo(json);
                }

                json.WriteEndObject();
            }

            json.WriteEndObject();
        }

        return buffer.WrittenSpan.ToArray();
    }

    static void Copy(string from, string to)
    {
        foreach (var file in Directory.EnumerateFiles(from, "*", SearchOption.AllDirectories))
        {
            var target = Path.Combine(to, Path.GetRelativePath(from, file));
            Directory.CreateDirectory(Path.GetDirectoryName(target)!);
            File.Copy(file, target);
        }
    }

    /// <summary>One client recorded: its view last seen, the frame made of it, and every change as a patch on the last.</summary>
    sealed class Watched(string kind, CapsuleAt at, Client client)
    {
        byte[]? seen;
        JsonNode? framed;

        public string Kind => kind;

        public CapsuleAt At => at;

        public JsonArray Timeline { get; } = [];

        public void Look(ServedShip ship)
        {
            var (name, view) = client.ViewNow(ship);
            if (seen is not null && view.AsSpan().SequenceEqual(seen)) return;
            seen = view;
            var nowS = ship.Vessel.NowS;
            var frame = JsonNode.Parse(Client.Frame(nowS, ship.Rate, name, view));
            Timeline.Add(new JsonArray(nowS, FramePatch.Between(framed, frame)));
            framed = frame;
        }
    }
}
