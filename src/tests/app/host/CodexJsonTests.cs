using System.Text.Json;
using Shipstick.App.Host;
using Shipstick.Codex;
using Shipstick.Core.Config;
using Shipstick.Economy;

namespace Shipstick.Tests.App.Host;

/// <summary>The codex as the host sends it: the book every page needs, and its words apart for the codex's window.</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P8)]
public sealed class CodexJsonTests
{
    static readonly CodexBook Book = CodexBook.Of(Catalogue.Embedded, GameConfig.Default);

    [Fact]
    public void TheBookSendsEveryItemAndDeviceWithoutItsWords()
    {
        using var json = JsonDocument.Parse(CodexJson.Book(Book));
        var items = json.RootElement.GetProperty("items").EnumerateArray().ToArray();
        var devices = json.RootElement.GetProperty("devices").EnumerateArray().ToArray();

        Assert.Equal(Book.Items.Count, items.Length);
        Assert.Equal(Book.Devices.Count, devices.Length);
        Assert.DoesNotContain(items.Concat(devices), entry => entry.TryGetProperty("words", out _));
    }

    [Fact]
    public void TheWordsGiveEachItemsAndDevicesByItsId()
    {
        var (item, device) = (Book.Items[0], Book.Devices[0]);

        using var json = JsonDocument.Parse(CodexJson.Words(Book));

        Assert.Equal(item.Words.About, json.RootElement.GetProperty("items").GetProperty(item.Id).GetProperty("about").GetString());
        Assert.Equal(device.Words.Flavour,
            json.RootElement.GetProperty("devices").GetProperty(device.Id).GetProperty("flavour").GetString());
    }
}
