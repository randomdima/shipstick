using Shipstick.Core.Config;
using Shipstick.Devices;
using Shipstick.Items;
using Shipstick.Ship;
using static Shipstick.Tests.TestItems;

namespace Shipstick.Tests.Ship;

/// <summary>An admin's edit of one slot (SHP-6).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P2)]
public class VesselEditTests
{
    static readonly GameConfig Config = GameConfig.Default;
    static readonly CapsuleAt At = new(0, 0);

    [Fact]
    public void AnEditSetsAChestSlotToAnyItem()
    {
        var (vessel, chest, _) = OneCapsule();

        Assert.True(vessel.Set(vessel.IdOf(chest), 0, Food, Config.Items.StackMost));
        Assert.Equal(new Stack(Food, Config.Items.StackMost), chest[0]);
    }

    [Fact]
    public void AnEditSetsADevicesOutputSlotToWhatItMakes()
    {
        var (vessel, _, farm) = OneCapsule();
        var output = Group(farm, Food).Slots;

        Assert.True(vessel.Set(vessel.IdOf(farm.Inventory), output.Start.Value, Food, 1));
        Assert.Equal(1, farm.Inventory.CountIn(output, Food));
    }

    [Fact]
    public void AnEditIsRefusedAnItemTheDevicesSlotDoesNotHold()
    {
        var (vessel, _, farm) = OneCapsule();
        var output = Group(farm, Food).Slots.Start.Value;

        Assert.False(vessel.Set(vessel.IdOf(farm.Inventory), output, Water, 1));
        Assert.True(farm.Inventory[output].IsEmpty);
    }

    [Fact]
    public void AnEditIsRefusedMoreThanAStack()
    {
        var (vessel, chest, _) = OneCapsule();

        Assert.False(vessel.Set(vessel.IdOf(chest), 0, Food, Config.Items.StackMost + 1));
        Assert.True(chest[0].IsEmpty);
    }

    [Fact]
    public void AnEditOfNoneEmptiesTheSlot()
    {
        var (vessel, chest, _) = OneCapsule();
        chest.TryAdd(0, Food, 1);

        Assert.True(vessel.Set(vessel.IdOf(chest), 0, Food, 0));
        Assert.True(chest[0].IsEmpty);
    }

    static (Vessel Vessel, Inventory Chest, Device Farm) OneCapsule()
    {
        var vessel = new Vessel(new ShipGrid(1, 1), Config.Capsule.CellsAcross);
        vessel.Place(At);
        var chest = Inventory.Open(Config.Capsule.ChestSlots, Config.Items.StackMost);
        vessel.Install(At, new FloorArea(0, 0, 1, 1), chest, Chest);
        var farm = Farm(Config, vessel.NowS);
        vessel.Install(At, 1, 0, farm);
        return (vessel, chest, farm);
    }
}
