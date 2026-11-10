using Shipstick.Items;
using static Shipstick.Tests.TestItems;

namespace Shipstick.Tests.Items;

/// <summary>What a slot accepts by hand (ITM-4).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P1)]
public class SlotFilterTests
{
    [Fact]
    public void ASlotNobodySetAFilterOnAcceptsEveryItem()
    {
        var filter = Inventory.Open(1, 1).FilterOf(0);

        Assert.True(filter.IsUniversal);
        Assert.All([Power, Water, Food, Oxygen, Spanner], item => Assert.True(filter.Accepts(item)));
    }

    [Fact]
    public void NoFilterAcceptsNoItem()
    {
        Assert.False(SlotFilter.Universal.Accepts(Item.None));
    }

    [Fact]
    public void AnOnlyFilterAcceptsTheItemsNamedAndNoOther()
    {
        var filter = SlotFilter.Only(Water, Food);

        Assert.Equal([Water, Food], filter.Accepted());
        Assert.False(filter.Accepts(Power));
    }

    [Fact]
    public void ATakeOnlyFilterAcceptsNothing()
    {
        Assert.Empty(SlotFilter.TakeOnly.Accepted());
        Assert.False(SlotFilter.TakeOnly.Accepts(Water));
    }
}
