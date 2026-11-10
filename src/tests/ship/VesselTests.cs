using Shipstick.Core.Config;
using Shipstick.Devices;
using Shipstick.Items;
using Shipstick.Ship;
using static Shipstick.Tests.TestItems;

namespace Shipstick.Tests.Ship;

/// <summary>What a seat reaches through the ship (SHP-1, SHP-2).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P1)]
public class VesselReachTests
{
    static readonly CapsuleAt Left = new(0, 0);
    static readonly CapsuleAt Right = new(1, 0);

    [Fact]
    public void ASeatMovesBetweenItsOwnChestAndItsDoor()
    {
        var (vessel, leftChest, _, door) = TwoCapsules();

        Assert.True(vessel.Move(Left, vessel.IdOf(leftChest), 0, vessel.IdOf(door.Inventory), 0));
    }

    [Fact]
    public void ASeatCannotReachIntoItsNeighboursChest()
    {
        var (vessel, leftChest, rightChest, _) = TwoCapsules();

        Assert.False(vessel.Move(Left, vessel.IdOf(leftChest), 0, vessel.IdOf(rightChest), 0));
        Assert.Equal(new Stack(Water, 1), leftChest[0]);
    }

    [Fact]
    public void ADoorIsOneInventoryReachedFromBothSides()
    {
        var (vessel, leftChest, rightChest, door) = TwoCapsules();
        var doorId = vessel.IdOf(door.Inventory);

        vessel.Move(Left, vessel.IdOf(leftChest), 0, doorId, 0);
        vessel.Move(Right, doorId, 0, vessel.IdOf(rightChest), 1);

        Assert.Equal(new Stack(Water, 1), rightChest[1]);
    }

    static (Vessel Vessel, Inventory LeftChest, Inventory RightChest, Door Door) TwoCapsules()
    {
        var config = GameConfig.Default;
        var vessel = new Vessel(new ShipGrid(2, 1), config.Capsule.CellsAcross);
        vessel.Place(Left);
        vessel.Place(Right);
        vessel.HangDoors(config.DoorSlots, config.Items.StackMost);
        var leftChest = Inventory.Open(config.Capsule.ChestSlots, config.Items.StackMost);
        var rightChest = Inventory.Open(config.Capsule.ChestSlots, config.Items.StackMost);
        leftChest.TryAdd(0, Water, 1);
        vessel.Install(Left, new FloorArea(0, 0, 1, 1), leftChest);
        vessel.Install(Right, new FloorArea(0, 0, 1, 1), rightChest);
        return (vessel, leftChest, rightChest, vessel.Doors[0]);
    }
}

/// <summary>The ship's clock (SHP-3).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P0)]
public class VesselClockTests
{
    static readonly GameConfig Config = GameConfig.Default;

    [Fact]
    public void AnAdvanceRunsEveryCycleDueByThenOnce()
    {
        var (vessel, strip) = OneStrip();

        vessel.AdvanceTo(2.5 * strip.CycleS);

        Assert.Equal(2, strip.Inventory[0].Count);
    }

    [Fact]
    public void ManySmallAdvancesGiveWhatOneLargeOneGives()
    {
        var (once, onceStrip) = OneStrip();
        var (often, oftenStrip) = OneStrip();
        var cycleS = onceStrip.CycleS;

        once.AdvanceTo(3 * cycleS);
        for (var step = 1; step <= 12; step++) often.AdvanceTo(step * cycleS / 4);

        Assert.Equal(onceStrip.Inventory[0], oftenStrip.Inventory[0]);
    }

    [Fact]
    public void ChoosingAWayDropsTheCycleDueUnderTheOldOne()
    {
        var vessel = new Vessel(new ShipGrid(1, 1), Config.Capsule.CellsAcross);
        var at = new CapsuleAt(0, 0);
        vessel.Place(at);
        var farm = Farm(Config, vessel.NowS);
        vessel.Install(at, 0, 0, farm);
        var growS = farm.CycleS;

        vessel.AdvanceTo(growS / 2);
        Assert.True(vessel.Select(at, vessel.IdOf(farm.Inventory), 1));
        var tendS = farm.CycleS;
        vessel.AdvanceTo(growS);

        // One tend cycle ran, at growS / 2 + tendS; a stale grow cycle at growS would have moved the due time on again.
        Assert.Equal(growS / 2 + 2 * tendS, farm.DueS);
    }

    static (Vessel Vessel, Device Strip) OneStrip()
    {
        var vessel = new Vessel(new ShipGrid(1, 1), Config.Capsule.CellsAcross);
        vessel.Place(new CapsuleAt(0, 0));
        var strip = Strip(Config, vessel.NowS);
        vessel.Install(new CapsuleAt(0, 0), 0, 0, strip);
        return (vessel, strip);
    }
}
