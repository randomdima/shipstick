using System.Text.Json;
using System.Text.Json.Serialization.Metadata;
using Shipstick.Codex;
using Shipstick.Economy;

namespace Shipstick.App.Host;

/// <summary>The codex's words for every item and every device, by id.</summary>
sealed record CodexWordsView(IReadOnlyDictionary<string, CodexWords> Items, IReadOnlyDictionary<string, CodexWords> Devices)
{
    public static CodexWordsView Of(CodexBook book) =>
        new(book.Items.ToDictionary(i => i.Id, i => i.Words), book.Devices.ToDictionary(d => d.Id, d => d.Words));
}

/// <summary>
/// The codex (<see cref="CodexBook"/>) as the host sends it, in two: the book less its items' and devices' words
/// (<c>codex.json</c>), which every page needs for the names and ways it shows; and those words
/// (<c>codex-words.json</c>, <see cref="CodexWordsView"/>), which only the codex's window shows, fetched when it first
/// opens — prose, so more than half the book's bytes over the line.
/// </summary>
static class CodexJson
{
    const string WordsProperty = "words";

    static readonly JsonSerializerOptions Unworded = new(HostJson.Default.Options)
    {
        TypeInfoResolver = HostJson.Default.WithAddedModifier(type =>
        {
            if (type.Type != typeof(ItemEntry) && type.Type != typeof(DeviceEntry)) return;
            foreach (var property in type.Properties.Where(p => p.Name == WordsProperty))
                property.ShouldSerialize = static (_, _) => false;
        }),
    };

    public static byte[] Book(CodexBook book) =>
        JsonSerializer.SerializeToUtf8Bytes(book, (JsonTypeInfo<CodexBook>)Unworded.GetTypeInfo(typeof(CodexBook)));

    public static byte[] Words(CodexBook book) =>
        JsonSerializer.SerializeToUtf8Bytes(CodexWordsView.Of(book), HostJson.Default.CodexWordsView);
}
