using Shipstick.Core.Config;
using Shipstick.Devices;
using Shipstick.Economy;
using Shipstick.Items;

namespace Shipstick.Tests;

/// <summary>
/// The few items and the one device the unit tests turn over, by catalogue id but built by hand, so a test of a slot or a
/// cycle states its own recipe and fails for nothing the catalogue's files say.
/// </summary>
static class TestItems
{
    public static readonly Item Power = new("pwr-001");
    public static readonly Item Water = new("wat-001");
    public static readonly Item Food = new("veg-001");
    public static readonly Item Oxygen = new("gas-001");
    public static readonly Item Spanner = new("mec-062");

    /// <summary>A farm: water and power in, two food out, eight minutes.</summary>
    public static readonly WayEntry Grow = new("grow", "test.farm", 8, [], [new(1, Water.Id!), new(1, Power.Id!)],
        [new(2, Food.Id!)], [], "test");

    /// <summary>The farm's other way: a spanner kept, power in, oxygen out, three minutes.</summary>
    public static readonly WayEntry Tend = new("tend", "test.farm", 3, [new(1, Spanner.Id!)], [new(1, Power.Id!)],
        [new(1, Oxygen.Id!)], [], "test");

    /// <summary>A source: nothing in, one power out, three minutes.</summary>
    public static readonly WayEntry Catch = new("catch", "test.strip", 3, [], [], [new(1, Power.Id!)], [], "test");

    /// <summary>A fixture that only holds things, one cell.</summary>
    public static readonly DeviceEntry Chest = new("test.chest", "Chest", "any", 1, 1, default);

    public static Device Farm(GameConfig config, double startS = 0) =>
        new(new DeviceEntry("test.farm", "Farm", "agri", 3, 2, default), [Grow, Tend], config, startS);

    public static Device Strip(GameConfig config, double startS = 0) =>
        new(new DeviceEntry("test.strip", "Strip", "power", 1, 1, default), [Catch], config, startS);

    /// <summary>The run of a device's slots that holds <paramref name="item"/> under its way.</summary>
    public static SlotGroup Group(Device device, Item item) => device.Layout.Single(g => g.Item == item);
}
