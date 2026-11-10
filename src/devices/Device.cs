using Shipstick.Core.Config;
using Shipstick.Economy;
using Shipstick.Items;

namespace Shipstick.Devices;

/// <summary>How a device's last cycle went.</summary>
public enum CycleOutcome : byte
{
    /// <summary>It has not cycled since it was laid or its way was chosen.</summary>
    NotYet,

    /// <summary>It had its tools and inputs, took the inputs and made its outputs.</summary>
    Ran,

    /// <summary>A tool or an input was short, so it took nothing.</summary>
    Starved,

    /// <summary>An output had no room, so it took nothing.</summary>
    Full,
}

/// <summary>What a run of a device's slots holds under the way it runs (DEV-4).</summary>
public enum SlotUse : byte
{
    /// <summary>A tool the way needs: kept through the cycle.</summary>
    Tool,

    /// <summary>An input the way takes: spent by the cycle.</summary>
    Input,

    /// <summary>An output the way makes: filled by the cycle, emptied by hand.</summary>
    Output,

    /// <summary>A slot this way does not use: it accepts nothing, and what is left in it may be taken out.</summary>
    Closed,
}

/// <summary>A run of slots holding one item of the way, <see cref="Count"/> of it a cycle.</summary>
public readonly record struct SlotGroup(SlotUse Use, Item Item, int Count, Range Slots);

/// <summary>
/// A device on a capsule's floor: one of the catalogue's, running one of its ways at a time. Each cycle turns what is
/// in its input slots into what goes in its output slots, while its tools sit in theirs (GAM-6, DEV-1).
/// </summary>
/// <remarks>
/// <para>
/// <b>The way it runs lays out every slot (DEV-4)</b>: tools, then inputs, then outputs, each item a run of slots
/// taking only it — at least <see cref="DeviceFigures.SlotsPerInput"/> or <see cref="DeviceFigures.OutputSlots"/>,
/// and enough stacks for one cycle's count — then closed slots. The inventory is as long as the device's largest
/// layout, so choosing another way only refilters it; what the old way left stays, to be taken out by hand.
/// </para>
/// <para>
/// The device keeps its own due time but never its clock: whoever runs the ship calls <see cref="Cycle"/> when
/// <see cref="DueS"/> comes, and the next due time is one <see cref="CycleS"/> after the last one due, however late the
/// call was made. Choosing a way restarts the wait from the moment it was chosen.
/// </para>
/// </remarks>
public sealed class Device
{
    readonly DeviceFigures figures;
    readonly int stackMost;

    public Device(DeviceEntry entry, IReadOnlyList<WayEntry> ways, GameConfig config, double startS)
    {
        if (ways.Count == 0) throw new ArgumentException($"{entry.Id} runs no way", nameof(ways));
        Entry = entry;
        Ways = ways;
        figures = config.Devices;
        stackMost = config.Items.StackMost;
        var slots = ways.Max(way => Groups(way).Sum(g => g.Slots));
        Inventory = new Inventory(new SlotFilter[slots], stackMost);
        Lay(0);
        DueS = startS + CycleS;
    }

    public DeviceEntry Entry { get; }

    /// <summary>Every way it may run, in the catalogue's order.</summary>
    public IReadOnlyList<WayEntry> Ways { get; }

    /// <summary>Which of <see cref="Ways"/> it runs.</summary>
    public int WayIndex { get; private set; }

    public WayEntry Way => Ways[WayIndex];

    /// <summary>Its slots, laid out by <see cref="Layout"/>.</summary>
    public Inventory Inventory { get; }

    /// <summary>The runs of slots the way it runs gives: tools, inputs, outputs, then the closed rest.</summary>
    public IReadOnlyList<SlotGroup> Layout { get; private set; } = [];

    /// <summary>The ship time one cycle of its way takes.</summary>
    public double CycleS => Way.Minutes * figures.CycleSPerWayMinute;

    /// <summary>The ship time its next cycle is due at.</summary>
    public double DueS { get; private set; }

    public CycleOutcome Last { get; private set; }

    /// <summary>How many times a way has been chosen: a cycle scheduled before the last choice is stale.</summary>
    public int Generation { get; private set; }

    /// <summary>Runs the <paramref name="way"/>th of <see cref="Ways"/> from <paramref name="nowS"/>, its first cycle one <see cref="CycleS"/> on.</summary>
    /// <returns>Whether there is such a way.</returns>
    public bool Select(int way, double nowS)
    {
        if (way < 0 || way >= Ways.Count) return false;
        Lay(way);
        DueS = nowS + CycleS;
        Last = CycleOutcome.NotYet;
        Generation++;
        return true;
    }

    /// <summary>The one item a slot holds under the way it runs, or <see cref="Item.None"/> for a closed slot.</summary>
    public Item SlotItem(int slot)
    {
        foreach (var group in Layout)
            if (slot >= group.Slots.Start.Value && slot < group.Slots.End.Value) return group.Item;
        return Item.None;
    }

    /// <summary>The first tool or input short of one cycle's worth, or <see cref="Item.None"/> when all are on hand.</summary>
    public Item ShortOf()
    {
        foreach (var group in Layout)
            if (group.Use is SlotUse.Tool or SlotUse.Input && Inventory.CountIn(group.Slots, group.Item) < group.Count)
                return group.Item;
        return Item.None;
    }

    /// <summary>Runs the cycle due at <see cref="DueS"/> and moves <see cref="DueS"/> on by one cycle.</summary>
    public CycleOutcome Cycle()
    {
        DueS += CycleS;
        Last = Turn();
        return Last;
    }

    CycleOutcome Turn()
    {
        if (ShortOf() != Item.None) return CycleOutcome.Starved;
        foreach (var group in Layout)
            if (group.Use == SlotUse.Output && Inventory.RoomIn(group.Slots, group.Item) < group.Count) return CycleOutcome.Full;

        foreach (var group in Layout)
            if (group.Use == SlotUse.Input) Inventory.TryTakeFrom(group.Slots, group.Item, group.Count);
        foreach (var group in Layout)
            if (group.Use == SlotUse.Output) Inventory.TryAddTo(group.Slots, group.Item, group.Count);
        return CycleOutcome.Ran;
    }

    void Lay(int way)
    {
        WayIndex = way;
        var layout = new List<SlotGroup>();
        var filters = new SlotFilter[Inventory.Slots];
        var next = 0;
        foreach (var (use, item, count, slots) in Groups(Ways[way]))
        {
            layout.Add(new SlotGroup(use, item, count, next..(next + slots)));
            var filter = use == SlotUse.Output ? SlotFilter.TakeOnly : SlotFilter.Only(item);
            for (var slot = next; slot < next + slots; slot++) filters[slot] = filter;
            next += slots;
        }

        if (next < filters.Length) layout.Add(new SlotGroup(SlotUse.Closed, Item.None, 0, next..filters.Length));
        for (var slot = next; slot < filters.Length; slot++) filters[slot] = SlotFilter.TakeOnly;
        Inventory.Refilter(filters);
        Layout = layout;
    }

    IEnumerable<(SlotUse Use, Item Item, int Count, int Slots)> Groups(WayEntry way)
    {
        foreach (var tool in way.Needs) yield return (SlotUse.Tool, new Item(tool.Item), tool.Count, Stacks(tool.Count, 1));
        foreach (var input in way.Takes)
            yield return (SlotUse.Input, new Item(input.Item), input.Count, Stacks(input.Count, figures.SlotsPerInput));
        foreach (var output in way.Makes)
            yield return (SlotUse.Output, new Item(output.Item), output.Count, Stacks(output.Count, figures.OutputSlots));
    }

    /// <summary>At least <paramref name="fewest"/> slots, and enough stacks to hold <paramref name="count"/>.</summary>
    int Stacks(int count, int fewest) => Math.Max(fewest, (count + stackMost - 1) / stackMost);
}
