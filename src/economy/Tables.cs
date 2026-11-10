namespace Shipstick.Economy;

/// <summary>Every Markdown table of one catalogue file, by the lower-cased `##` heading above it.</summary>
/// <remarks>
/// The same reading as <c>qq economy</c>'s: a table's first row names its columns, its dash row is skipped, and a line
/// that does not start with <c>|</c> ends it. A cell is looked up by its column's name, so a column may be left out
/// (a Ways table that needs no tool has no <c>needs</c>) and reads as blank.
/// </remarks>
sealed class Tables
{
    readonly Dictionary<string, List<Row>> byHeading = [];

    Tables(string file) => File = file;

    public string File { get; }

    public IReadOnlyList<Row> this[string heading] => byHeading.TryGetValue(heading, out var rows) ? rows : [];

    public static Tables Read(string file, string text)
    {
        var tables = new Tables(file);
        string heading = "";
        string[]? header = null;
        var line = 0;
        foreach (var raw in text.Split('\n'))
        {
            line++;
            var trimmed = raw.TrimEnd('\r');
            if (trimmed.StartsWith("## ", StringComparison.Ordinal))
            {
                heading = trimmed[3..].Trim().ToLowerInvariant();
                header = null;
                continue;
            }

            if (!trimmed.StartsWith('|'))
            {
                header = null;
                continue;
            }

            var cells = trimmed.Trim().Trim('|').Split('|').Select(c => c.Trim()).ToArray();
            if (header is null) header = [.. cells.Select(c => c.ToLowerInvariant())];
            else if (!cells.All(c => c.All(ch => ch is '-' or ':' or ' ')))
            {
                if (!tables.byHeading.TryGetValue(heading, out var rows)) tables.byHeading[heading] = rows = [];
                rows.Add(new Row(tables.File, line, header, cells));
            }
        }

        return tables;
    }
}

/// <summary>One table row: its cells by column name, and where it was read, for a reader's error.</summary>
sealed class Row(string file, int line, string[] header, string[] cells)
{
    public string Where => $"{file}:{line}";

    /// <summary>The cell under <paramref name="column"/>, or "" where the table has no such column.</summary>
    public string this[string column]
    {
        get
        {
            var at = Array.IndexOf(header, column);
            return at >= 0 && at < cells.Length ? cells[at] : "";
        }
    }
}
