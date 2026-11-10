using System.Globalization;
using System.Reflection;
using System.Text.RegularExpressions;

namespace Shipstick.Economy;

/// <summary>
/// The item catalogue as the game holds it: every section, subsection, role, stat, device, item and way of
/// <c>economy/catalog/</c>, read from the Markdown tables compiled into the game, so the game and its codex hold what
/// the files say and nothing else (ECO-13).
/// </summary>
/// <remarks>
/// <para>
/// <b>The tables are checked by <c>qq economy</c>, not here.</b> This reader fails on a cell it cannot read and trusts
/// the rest: a way naming an item no file holds, an item no way makes, are the tool's to report (ECO-7, ECO-8).
/// </para>
/// <para>
/// Lists keep the files' order — sections.md's subsections, each file's rows — so a way's index here is the same on
/// every load, and a page may name a way by it.
/// </para>
/// </remarks>
public sealed partial class Catalogue
{
    /// <summary>The <c>by</c> of a way the crew runs with their own hands, anywhere.</summary>
    public const string ByHand = "crew";

    /// <summary>The subsection code and role of the universal fixtures, which every capsule has.</summary>
    public const string Universal = "any";

    /// <summary>The fixture whose cycle says whether a capsule is failing (DEV-3).</summary>
    public const string LifeSupport = "any.lifesupport";

    /// <summary>A cell of a capsule's wall (GAM-10): stood round its floor's edge, never furnished.</summary>
    public const string Wall = "any.wall";

    /// <summary>A door in a capsule's wall (GAM-10), standing on the edge cell where a neighbour is.</summary>
    public const string Door = "any.door";

    /// <summary>Whether a device is a capsule's structure — its wall or door — rather than something furnished.</summary>
    public static bool IsStructure(string device) => device is Wall or Door;

    const string Index = "sections.md";
    const string ResourcePrefix = "catalog/";

    static readonly Lazy<Catalogue> embedded = new(() => Parse(ReadEmbedded()));

    readonly Dictionary<string, ItemEntry> items = [];
    readonly Dictionary<string, DeviceEntry> devices = [];
    readonly Dictionary<string, List<WayEntry>> waysBy = [];

    Catalogue()
    {
    }

    /// <summary>The catalogue compiled into the game.</summary>
    public static Catalogue Embedded => embedded.Value;

    public IReadOnlyList<SectionEntry> Sections { get; private set; } = [];

    public IReadOnlyList<SubsectionEntry> Subsections { get; private set; } = [];

    public IReadOnlyList<RoleEntry> Roles { get; private set; } = [];

    public IReadOnlyList<StatEntry> Stats { get; private set; } = [];

    public IReadOnlyList<ItemEntry> Items { get; private set; } = [];

    /// <summary>The universal fixtures first, then each subsection's devices.</summary>
    public IReadOnlyList<DeviceEntry> Devices { get; private set; } = [];

    /// <summary>Every way, in the files' order: the universal fixtures' file first, then each subsection's.</summary>
    public IReadOnlyList<WayEntry> Ways { get; private set; } = [];

    public ItemEntry? Item(string id) => items.GetValueOrDefault(id);

    public DeviceEntry? Device(string id) => devices.GetValueOrDefault(id);

    /// <summary>The ways a device runs, in <see cref="Ways"/> order; none for a fixture that only holds things.</summary>
    public IReadOnlyList<WayEntry> WaysBy(string deviceId) => waysBy.TryGetValue(deviceId, out var ways) ? ways : [];

    /// <summary>Reads a catalogue from its files: <c>sections.md</c>, <c>any.md</c> and one file a subsection.</summary>
    /// <param name="files">Each file's name (<c>wat.md</c>) and text.</param>
    public static Catalogue Parse(IEnumerable<(string Name, string Text)> files)
    {
        var tables = files.ToDictionary(f => f.Name, f => Tables.Read(f.Name, f.Text));
        if (!tables.TryGetValue(Index, out var index)) throw new InvalidDataException($"the catalogue has no {Index}");

        var cat = new Catalogue
        {
            Sections = [.. index["sections"].Select(r => new SectionEntry(r["section"], r["name"], r["the need it serves"]))],
            Subsections = [.. index["subsections"].Select(r => new SubsectionEntry(r["sub"], r["name"], r["section"], List(r["roles"]), r["covers"]))],
            Roles = [.. index["roles"].Select(r => new RoleEntry(r["role"], r["name"]))],
            Stats = [.. index["stats"].Select(r => new StatEntry(r["stat"], r["of"], r["better"] != "lower", r["typical"], r["means"]))],
        };

        var items = new List<ItemEntry>();
        var devices = new List<DeviceEntry>();
        var ways = new List<WayEntry>();
        foreach (var code in cat.Subsections.Select(s => s.Code).Prepend(Universal))
        {
            if (!tables.TryGetValue($"{code}.md", out var file)) throw new InvalidDataException($"the catalogue has no {code}.md");
            var words = file["codex"].ToDictionary(r => r["id"], r => new CodexWords(r["about"], r["flavour"]));
            devices.AddRange(file["devices"].Select(r => ReadDevice(r, words)));
            items.AddRange(file["items"].Select(r => ReadItem(r, code, words)));
            ways.AddRange(file["ways"].Select(r => ReadWay(r, code)));
        }

        cat.Items = items;
        cat.Devices = devices;
        cat.Ways = ways;
        foreach (var item in items) cat.items.Add(item.Id, item);
        foreach (var device in devices) cat.devices.Add(device.Id, device);
        foreach (var way in ways)
        {
            if (!cat.waysBy.TryGetValue(way.By, out var list)) cat.waysBy[way.By] = list = [];
            list.Add(way);
        }

        return cat;
    }

    static IEnumerable<(string Name, string Text)> ReadEmbedded()
    {
        var assembly = typeof(Catalogue).Assembly;
        foreach (var name in assembly.GetManifestResourceNames().Where(n => n.StartsWith(ResourcePrefix, StringComparison.Ordinal)))
        {
            using var reader = new StreamReader(assembly.GetManifestResourceStream(name)!);
            yield return (name[ResourcePrefix.Length..], reader.ReadToEnd());
        }
    }

    static DeviceEntry ReadDevice(Row r, Dictionary<string, CodexWords> words)
    {
        var cells = CellsCell().Match(r["cells"]);
        if (!cells.Success) throw Bad(r, "cells", r["cells"]);
        return new DeviceEntry(r["id"], r["device"], r["role"], Int(cells.Groups[1].Value), Int(cells.Groups[2].Value),
            words.GetValueOrDefault(r["id"]));
    }

    static ItemEntry ReadItem(Row r, string sub, Dictionary<string, CodexWords> words)
    {
        var effects = new List<StatChange>();
        var leaves = new List<Counted>();
        var fits = new List<string>();
        var installs = new List<string>();
        foreach (var token in List(r["use"]))
        {
            if (EffectCell().Match(token) is { Success: true } e)
                effects.Add(new StatChange(e.Groups["stat"].Value, Number(e.Groups["amount"].Value), e.Groups["rate"].Success));
            else if (LeavesCell().Match(token) is { Success: true } l)
                leaves.Add(new Counted(Int(l.Groups["count"].Value), l.Groups["id"].Value));
            else if (PointsAtCell().Match(token) is { Success: true } p)
                (p.Groups["verb"].Value == "fits" ? fits : installs).Add(p.Groups["device"].Value);
            else throw Bad(r, "use", token);
        }

        double? decayH = null;
        string? decaysTo = null;
        if (!Blank(r["decays"]))
        {
            var d = DecaysCell().Match(r["decays"]);
            if (!d.Success) throw Bad(r, "decays", r["decays"]);
            decayH = Number(d.Groups["h"].Value);
            decaysTo = d.Groups["into"].Success ? d.Groups["into"].Value : null;
        }

        return new ItemEntry(r["id"], r["item"], sub, [.. effects], [.. leaves], [.. fits], [.. installs], decayH, decaysTo,
            words.GetValueOrDefault(r["id"]));
    }

    static WayEntry ReadWay(Row r, string sub)
    {
        var gives = new List<StatChange>();
        foreach (var token in List(r["gives"]))
        {
            var e = EffectCell().Match(token);
            if (!e.Success || e.Groups["rate"].Success) throw Bad(r, "gives", token);
            gives.Add(new StatChange(e.Groups["stat"].Value, Number(e.Groups["amount"].Value), false));
        }

        return new WayEntry(r["way"], r["by"], Number(r["min"]), CountedList(r, "needs"), CountedList(r, "takes"),
            CountedList(r, "makes"), [.. gives], sub);
    }

    static Counted[] CountedList(Row r, string column) =>
    [
        .. List(r[column]).Select(token => CountedCell().Match(token) is { Success: true } m
            ? new Counted(Int(m.Groups["count"].Value), m.Groups["id"].Value)
            : throw Bad(r, column, token)),
    ];

    static bool Blank(string cell) => cell.Trim() is "" or "—" or "-";

    static string[] List(string cell) =>
        Blank(cell) ? [] : [.. cell.Split(',').Select(t => t.Trim()).Where(t => t.Length > 0)];

    static int Int(string text) => int.Parse(text, CultureInfo.InvariantCulture);

    static double Number(string text) => double.Parse(text, CultureInfo.InvariantCulture);

    static InvalidDataException Bad(Row r, string column, string cell) => new($"{r.Where}: {column} '{cell}' cannot be read");

    [GeneratedRegex(@"^(\d+)x(\d+)$")]
    private static partial Regex CellsCell();

    [GeneratedRegex(@"^(?<stat>[a-z][a-z0-9.]*) (?<amount>[+-]\d+(?:\.\d+)?)(?<rate>/h)?$")]
    private static partial Regex EffectCell();

    [GeneratedRegex(@"^leaves (?<count>\d+) (?<id>[a-z]{3}-\d{3})$")]
    private static partial Regex LeavesCell();

    [GeneratedRegex(@"^(?<verb>fits|installs) (?<device>[a-z]{3}\.[a-z0-9]+)$")]
    private static partial Regex PointsAtCell();

    [GeneratedRegex(@"^(?<h>\d+(?:\.\d+)?) h(?: → (?<into>[a-z]{3}-\d{3}))?$")]
    private static partial Regex DecaysCell();

    [GeneratedRegex(@"^(?<count>\d+) (?<id>[a-z]{3}-\d{3})$")]
    private static partial Regex CountedCell();
}
