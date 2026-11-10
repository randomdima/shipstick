using Shipstick.Codex;
using Shipstick.Core.Config;
using Shipstick.Economy;

namespace Shipstick.Tests.Codex;

/// <summary>The codex holds everything the game does, and none of its own pages points at nothing (WEB-3, ECO-12).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P6)]
public class CodexTests
{
    static readonly Catalogue Catalogue = Catalogue.Embedded;
    static readonly CodexBook Book = CodexBook.Of(Catalogue, GameConfig.Default);

    [Fact]
    public void EveryItemHasItsCodexWords()
    {
        var bare = Book.Items.Where(i => string.IsNullOrWhiteSpace(i.Words.About) || string.IsNullOrWhiteSpace(i.Words.Flavour));

        Assert.Empty(bare.Select(i => i.Id));
    }

    [Fact]
    public void EveryDeviceHasItsCodexWords()
    {
        var bare = Book.Devices.Where(d => string.IsNullOrWhiteSpace(d.Words.About) || string.IsNullOrWhiteSpace(d.Words.Flavour));

        Assert.Empty(bare.Select(d => d.Id));
    }

    [Fact]
    public void EveryLinkAndFigureOfTheCodexsOwnPagesNamesSomething()
    {
        Assert.NotEmpty(Book.Pages);
        Assert.Empty(Book.Unresolved());
    }
}
