using Shipstick.Core.Config;
using Shipstick.Devices;
using Shipstick.Economy;
using Shipstick.Items;
using static Shipstick.Tests.TestItems;

namespace Shipstick.Tests.Devices;

/// <summary>One device cycle (DEV-1), over the slot layout its way gives it (DEV-4).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P2)]
public class DeviceTests
{
    static readonly GameConfig Config = GameConfig.Default;
    static readonly int StackMost = Config.Items.StackMost;

    [Fact]
    public void ACycleWithItsInputsTakesThemAndMakesItsOutput()
    {
        var farm = Loaded(Farm(Config), 1);

        Assert.Equal(CycleOutcome.Ran, farm.Cycle());
        Assert.Equal((0, 0, 2), Counts(farm));
    }

    [Fact]
    public void ACycleShortOfAnInputTakesNothing()
    {
        var farm = Farm(Config);
        farm.Inventory.TryAddTo(Group(farm, Water).Slots, Water, 1);

        Assert.Equal(CycleOutcome.Starved, farm.Cycle());
        Assert.Equal((1, 0, 0), Counts(farm));
    }

    [Fact]
    public void ShortOfNamesTheFirstInputBelowOneCyclesWorth()
    {
        var farm = Farm(Config);
        farm.Inventory.TryAddTo(Group(farm, Water).Slots, Water, 1);

        Assert.Equal(Power, farm.ShortOf());
    }

    [Fact]
    public void ACycleWithNoRoomForItsOutputTakesNothing()
    {
        var farm = Loaded(Farm(Config), 1);
        var output = Group(farm, Food).Slots;
        var room = farm.Inventory.RoomIn(output, Food);
        farm.Inventory.TryAddTo(output, Food, room);

        Assert.Equal(CycleOutcome.Full, farm.Cycle());
        Assert.Equal((1, 1, room), Counts(farm));
    }

    [Fact]
    public void AnInputCountsInWhicheverOfItsSlotsItLies()
    {
        var farm = Farm(Config);
        farm.Inventory.TryAdd(Group(farm, Water).Slots.End.Value - 1, Water, 1);
        farm.Inventory.TryAdd(Group(farm, Power).Slots.End.Value - 1, Power, 1);

        Assert.Equal(CycleOutcome.Ran, farm.Cycle());
    }

    [Fact]
    public void EachInputSlotAcceptsOnlyItsInputAndEachOutputSlotNothing()
    {
        var farm = Farm(Config);
        var accepts = Enumerable.Range(0, Group(farm, Food).Slots.End.Value).Select(slot => farm.Inventory.FilterOf(slot).Accepted());

        Item[][] expected =
        [
            .. Enumerable.Repeat<Item[]>([Water], Config.Devices.SlotsPerInput),
            .. Enumerable.Repeat<Item[]>([Power], Config.Devices.SlotsPerInput),
            .. Enumerable.Repeat<Item[]>([], Config.Devices.OutputSlots),
        ];
        Assert.Equal(expected, accepts);
    }

    [Fact]
    public void EachSlotHoldsItsInputOrWhatTheDeviceMakes()
    {
        var farm = Farm(Config);
        var holds = Enumerable.Range(0, Group(farm, Food).Slots.End.Value).Select(farm.SlotItem);

        Item[] expected =
        [
            .. Enumerable.Repeat(Water, Config.Devices.SlotsPerInput),
            .. Enumerable.Repeat(Power, Config.Devices.SlotsPerInput),
            .. Enumerable.Repeat(Food, Config.Devices.OutputSlots),
        ];
        Assert.Equal(expected, holds);
    }

    [Fact]
    public void AToolIsNeededAndKept()
    {
        var farm = Farm(Config);
        farm.Select(1, 0);
        farm.Inventory.TryAddTo(Group(farm, Power).Slots, Power, 1);
        Assert.Equal(Spanner, farm.ShortOf());

        farm.Inventory.TryAddTo(Group(farm, Spanner).Slots, Spanner, 1);
        Assert.Equal(CycleOutcome.Ran, farm.Cycle());
        Assert.Equal(1, farm.Inventory.CountIn(Group(farm, Spanner).Slots, Spanner));
    }

    [Fact]
    public void ChoosingAWayRelaysTheSlotsAndLeavesWhatWasInThem()
    {
        var farm = Loaded(Farm(Config), 1);
        var waterSlot = Group(farm, Water).Slots.Start.Value;

        farm.Select(1, 0);

        Assert.Equal(new Stack(Water, 1), farm.Inventory[waterSlot]);
        Assert.NotEqual(Water, farm.SlotItem(waterSlot));
    }

    [Fact]
    public void AnInputHasEnoughSlotsForOneCyclesCount()
    {
        var big = new WayEntry("big", "test.farm", 1, [], [new(2 * StackMost + 1, Water.Id!)], [], [], "test");
        var device = new Device(new DeviceEntry("test.farm", "Farm", "agri", 1, 1, default), [big], Config, 0);

        Assert.Equal(3, Group(device, Water).Slots.GetOffsetAndLength(device.Inventory.Slots).Length);
    }

    [Fact]
    public void ACycleMovesTheDueTimeOnByOneCycleWhateverItsOutcome()
    {
        var farm = Farm(Config);

        farm.Cycle();

        Assert.Equal(2 * farm.CycleS, farm.DueS);
    }

    static Device Loaded(Device farm, int each)
    {
        farm.Inventory.TryAddTo(Group(farm, Water).Slots, Water, each);
        farm.Inventory.TryAddTo(Group(farm, Power).Slots, Power, each);
        return farm;
    }

    /// <summary>Water held, power held and food made, each summed across its slots.</summary>
    static (int Water, int Power, int Food) Counts(Device device) =>
        (device.Inventory.CountIn(Group(device, Water).Slots, Water), device.Inventory.CountIn(Group(device, Power).Slots, Power),
            device.Inventory.CountIn(Group(device, Food).Slots, Food));
}
