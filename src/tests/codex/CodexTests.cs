using Shipstick.Codex;
using Shipstick.Core.Config;
using Shipstick.Devices;
using Shipstick.Economy;
using Shipstick.Ship;

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
    public void EveryItemTheStarterShipsDevicesRunOnHasAPage()
    {
        var vessel = StarterShip.Lay(GameConfig.Default, Catalogue);
        var held = new HashSet<string>(Book.Items.Select(i => i.Id));
        var named = Capsules(vessel).SelectMany(c => c.Fixtures).Select(f => f.Device).OfType<Device>()
            .SelectMany(d => d.Ways).SelectMany(w => w.Needs.Concat(w.Takes).Concat(w.Makes)).Select(c => c.Item);

        Assert.Empty(named.Where(id => !held.Contains(id)).Distinct());
    }

    [Fact]
    public void EveryLinkAndFigureOfTheCodexsOwnPagesNamesSomething()
    {
        Assert.NotEmpty(Book.Pages);
        Assert.Empty(Book.Unresolved());
    }

    static IEnumerable<Capsule> Capsules(Vessel vessel)
    {
        for (var row = 0; row < vessel.Grid.Rows; row++)
            for (var column = 0; column < vessel.Grid.Columns; column++)
                if (vessel.CapsuleOn(new CapsuleAt(column, row)) is { } capsule) yield return capsule;
    }
}
