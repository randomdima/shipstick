using System.Buffers;
using System.Text.Json;
using Shipstick.App.Host;
using Shipstick.Core.Config;
using Shipstick.Economy;
using Shipstick.Ship;

namespace Shipstick.App.Demo;

/// <summary>
/// The demo (DEM-1) as a static site: the client's files and art, the codex and the asset list as the host serves them,
/// and a recording of the frame the host sends each seat and the admin entered in each capsule, with <c>demo.js</c>
/// standing in for the host's socket.
/// </summary>
/// <remarks>
/// <b>The recording is the host's own</b>: every frame is made by the host's clients from the starter ship, so the demo
/// shows what the game shows and holds no copy of its rules. Ship time is stopped before recording, so a page tells no
/// time on past the frame it was shown.
/// </remarks>
static class DemoSite
{
    /// <summary>The recording, by the path the page asks for it by: <c>{"seat": {"column,row": frame}, "ship": {…}}</c>.</summary>
    const string FramesPath = "demo/frames.json";
    const string Entry = """<script type="module" src="main.js"></script>""";
    const string StandIn = """<script src="demo.js"></script>""";

    /// <summary>Writes the site from the client's files in <paramref name="client"/> into the empty folder <paramref name="site"/>.</summary>
    public static void Write(string client, string site)
    {
        Copy(client, site);

        var ship = new ServedShip(GameConfig.Default, Catalogue.Embedded);
        if (!ship.SetRate(0)) throw new InvalidOperationException("the host refused to stop ship time");
        File.WriteAllBytes(Path.Combine(site, "codex.json"), ship.CodexJson);
        File.WriteAllBytes(Path.Combine(site, "assets.json"), JsonSerializer.SerializeToUtf8Bytes(AssetList.Of(site)));
        var frames = Path.Combine(site, FramesPath);
        Directory.CreateDirectory(Path.GetDirectoryName(frames)!);
        File.WriteAllBytes(frames, Recording(ship));

        var index = Path.Combine(site, "index.html");
        var page = File.ReadAllText(index);
        if (!page.Contains(Entry)) throw new InvalidOperationException($"index.html has no {Entry} for demo.js to load before");
        File.WriteAllText(index, page.Replace(Entry, $"{StandIn}\n  {Entry}"));
    }

    static byte[] Recording(ServedShip ship)
    {
        var buffer = new ArrayBufferWriter<byte>();
        using (var json = new Utf8JsonWriter(buffer))
        {
            json.WriteStartObject();
            Record(json, "seat", ship, at => new SeatClient(at));
            Record(json, "ship", ship, at => new AdminClient(at));
            json.WriteEndObject();
        }

        return buffer.WrittenSpan.ToArray();
    }

    /// <summary>One frame a capsule, in the ship's reading order: the admin's first is where the admin joins.</summary>
    static void Record(Utf8JsonWriter json, string kind, ServedShip ship, Func<CapsuleAt, Client> clientAt)
    {
        json.WriteStartObject(kind);
        foreach (var at in ship.Vessel.Capsules.Select(capsule => capsule.At))
        {
            json.WritePropertyName($"{at.Column},{at.Row}");
            json.WriteRawValue(clientAt(at).FrameNow(ship), skipInputValidation: true);
        }

        json.WriteEndObject();
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
}
