using Shipstick.Economy;

namespace Shipstick.Tests.Economy;

/// <summary>The catalogue as the game reads it (ECO-13): every file there, every name resolving to something it holds.</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P8)]
public class CatalogueTests
{
    const int ItemsPerSubsection = 100;
    static readonly Catalogue Catalogue = Catalogue.Embedded;

    [Fact]
    public void TheGameHoldsAHundredItemsForEverySubsection()
    {
        Assert.Equal(Catalogue.Subsections.Count * ItemsPerSubsection, Catalogue.Items.Count);
    }

    [Fact]
    public void EveryWayIsRunByADeviceTheGameHoldsOrByHand()
    {
        var strays = Catalogue.Ways.Where(w => w.By != Catalogue.ByHand && Catalogue.Device(w.By) is null).Select(w => $"{w.Name} ({w.By})");

        Assert.Empty(strays);
    }

    [Fact]
    public void EveryItemAWayNamesIsAnItemTheGameHolds()
    {
        var strays = Catalogue.Ways.SelectMany(w => w.Needs.Concat(w.Takes).Concat(w.Makes).Select(c => (w.Name, c.Item)))
            .Where(p => Catalogue.Item(p.Item) is null);

        Assert.Empty(strays);
    }

    [Fact]
    public void EveryItemAnItemNamesIsOneTheGameHolds()
    {
        var named = Catalogue.Items.SelectMany(i => i.Leaves.Select(c => c.Item).Concat(i.DecaysTo is { } to ? [to] : []));
        var devices = Catalogue.Items.SelectMany(i => i.Fits.Concat(i.Installs));

        Assert.Empty(named.Where(id => Catalogue.Item(id) is null));
        Assert.Empty(devices.Where(id => Catalogue.Device(id) is null));
    }
}
