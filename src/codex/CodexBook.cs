using System.Text.RegularExpressions;
using Shipstick.Core.Config;
using Shipstick.Economy;

namespace Shipstick.Codex;

/// <summary>One of the codex's own pages: how part of the ship works, as <c>codex/mechanics.md</c> writes it.</summary>
/// <param name="Text">Paragraphs and <c>- </c> lists, with <c>[[kind:id|words]]</c> links and <c>{figure}</c> tokens.</param>
public sealed record CodexPage(string Slug, string Title, string Text);

/// <summary>
/// Everything the codex shows: a page for every item and device the game holds, read off the catalogue the game was
/// built with; its own pages on how the ship works; and the figures those pages quote, read off
/// <see cref="GameConfig"/>. Nothing in it is written twice, so nothing in it can fall behind the game (WEB-3, ECO-12).
/// </summary>
/// <remarks>
/// The host sends it as <c>codex.json</c> and the client draws it — an item's or device's page with its words and every way that makes, uses or needs it
/// (WEB-5), opened from a device's window (WEB-4); which page links where, and how a way reads, are the page's. A link
/// or a figure that names nothing is caught by <see cref="Unresolved"/>, which the suite runs.
/// </remarks>
public sealed partial record CodexBook(
    IReadOnlyDictionary<string, double> Figures,
    CodexPage[] Pages,
    IReadOnlyList<SectionEntry> Sections,
    IReadOnlyList<SubsectionEntry> Subsections,
    IReadOnlyList<RoleEntry> Roles,
    IReadOnlyList<StatEntry> Stats,
    IReadOnlyList<ItemEntry> Items,
    IReadOnlyList<DeviceEntry> Devices,
    IReadOnlyList<WayEntry> Ways,
    string ByHand,
    string LifeSupport)
{
    const string PagesResource = "codex/mechanics.md";
    const string PageHeading = "## ";

    public static CodexBook Of(Catalogue catalogue, GameConfig config) =>
        new(FiguresOf(config), ReadPages(), catalogue.Sections, catalogue.Subsections, catalogue.Roles, catalogue.Stats,
            catalogue.Items, catalogue.Devices, catalogue.Ways, Catalogue.ByHand, Catalogue.LifeSupport);

    /// <summary>The figures a page may quote as <c>{name}</c>.</summary>
    static Dictionary<string, double> FiguresOf(GameConfig config) => new()
    {
        ["cellsAcross"] = config.Capsule.CellsAcross,
        ["doorSlots"] = config.DoorSlots,
        ["chestSlots"] = config.Capsule.ChestSlots,
        ["stackMost"] = config.Items.StackMost,
        ["slotsPerInput"] = config.Devices.SlotsPerInput,
        ["outputSlots"] = config.Devices.OutputSlots,
        ["cycleSPerWayMinute"] = config.Devices.CycleSPerWayMinute,
        ["roleDevicesMost"] = config.Starter.RoleDevicesMost,
    };

    /// <summary>Every link and figure of the codex's own pages that names nothing, as "slug: target".</summary>
    public IEnumerable<string> Unresolved()
    {
        foreach (var page in Pages)
        {
            foreach (Match link in LinkToken().Matches(page.Text))
                if (!Resolves(link.Groups["kind"].Value, link.Groups["id"].Value))
                    yield return $"{page.Slug}: [[{link.Groups["kind"].Value}:{link.Groups["id"].Value}]]";
            foreach (Match figure in FigureToken().Matches(page.Text))
                if (!Figures.ContainsKey(figure.Groups["name"].Value))
                    yield return $"{page.Slug}: {{{figure.Groups["name"].Value}}}";
        }
    }

    bool Resolves(string kind, string id) => kind switch
    {
        "item" => Items.Any(i => i.Id == id),
        "device" => Devices.Any(d => d.Id == id),
        "page" => Pages.Any(p => p.Slug == id),
        "section" => Sections.Any(s => s.Id == id),
        "sub" => Subsections.Any(s => s.Code == id),
        "role" => Roles.Any(r => r.Id == id),
        "stat" => Stats.Any(s => s.Id == id),
        _ => false,
    };

    static CodexPage[] ReadPages()
    {
        using var stream = typeof(CodexBook).Assembly.GetManifestResourceStream(PagesResource)
            ?? throw new InvalidDataException($"the game holds no {PagesResource}");
        using var reader = new StreamReader(stream);
        return ReadPages(reader.ReadToEnd());
    }

    /// <summary>The pages of a mechanics file: each <c>## slug: Title</c> heading and the text under it.</summary>
    public static CodexPage[] ReadPages(string text)
    {
        var pages = new List<CodexPage>();
        string? slug = null, title = null;
        var body = new List<string>();
        foreach (var line in text.Replace("\r", "", StringComparison.Ordinal).Split('\n'))
        {
            if (line.StartsWith(PageHeading, StringComparison.Ordinal))
            {
                Close();
                var heading = line[PageHeading.Length..];
                var colon = heading.IndexOf(':', StringComparison.Ordinal);
                if (colon < 0) throw new InvalidDataException($"page heading '{heading}' is not 'slug: Title'");
                (slug, title) = (heading[..colon].Trim(), heading[(colon + 1)..].Trim());
            }
            else if (slug is not null) body.Add(line);
        }

        Close();
        return [.. pages];

        void Close()
        {
            if (slug is not null) pages.Add(new CodexPage(slug, title!, string.Join('\n', body).Trim()));
            body.Clear();
        }
    }

    [GeneratedRegex(@"\[\[(?<kind>[a-z]+):(?<id>[^\]|]+)(\|[^\]]*)?\]\]")]
    private static partial Regex LinkToken();

    [GeneratedRegex(@"\{(?<name>[A-Za-z]+)\}")]
    private static partial Regex FigureToken();
}
