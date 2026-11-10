namespace Shipstick.Items;

/// <summary>
/// A fixed row of slots, each holding one <see cref="Stack"/> behind one <see cref="SlotFilter"/>: a chest's, a
/// device's or a door's (GAM-5).
/// </summary>
/// <remarks>
/// Items change slots in three ways only: a player's <see cref="Move"/>, which honours every filter; the owner's
/// <see cref="TryAdd"/>/<see cref="TryTake"/>, which honour kind and <see cref="StackMost"/> but no filter; and an
/// admin's <see cref="Set"/>. Only <see cref="Set"/> makes or loses an item it does not report (ITM-1).
/// </remarks>
public sealed class Inventory
{
    readonly Stack[] stacks;
    readonly SlotFilter[] filters;

    public Inventory(ReadOnlySpan<SlotFilter> filters, int stackMost)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(stackMost);
        this.filters = filters.ToArray();
        stacks = new Stack[filters.Length];
        StackMost = stackMost;
    }

    /// <summary>An inventory of <paramref name="slots"/> universal slots.</summary>
    public static Inventory Open(int slots, int stackMost)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(slots);
        return new Inventory(new SlotFilter[slots], stackMost);
    }

    /// <summary>An inventory of no slots, for a fixture that holds nothing: a wall.</summary>
    public static Inventory Empty(int stackMost) => new([], stackMost);

    public int Slots => stacks.Length;

    /// <summary>The most of one item a slot here holds (ITM-2).</summary>
    public int StackMost { get; }

    public Stack this[int slot] => stacks[slot];

    public SlotFilter FilterOf(int slot) => filters[slot];

    /// <summary>Sets every slot's filter, as the owner does when it lays its slots out anew; what the slots hold stays.</summary>
    public void Refilter(ReadOnlySpan<SlotFilter> filters)
    {
        if (filters.Length != Slots) throw new ArgumentException($"{filters.Length} filters for {Slots} slots", nameof(filters));
        filters.CopyTo(this.filters);
    }

    /// <summary>How many of <paramref name="item"/> a run of slots holds.</summary>
    public int CountIn(Range slots, Item item)
    {
        var count = 0;
        foreach (var stack in stacks.AsSpan(slots))
            if (stack.Item == item) count += stack.Count;
        return count;
    }

    /// <summary>How many of <paramref name="item"/> a run of slots has room for.</summary>
    public int RoomIn(Range slots, Item item)
    {
        var room = 0;
        foreach (var stack in stacks.AsSpan(slots))
            if (stack.IsEmpty || stack.Item == item) room += StackMost - stack.Count;
        return room;
    }

    /// <summary>
    /// Adds <paramref name="count"/> of <paramref name="item"/> to one slot, all or nothing, as the slot's owner does.
    /// </summary>
    public bool TryAdd(int slot, Item item, int count)
    {
        var held = stacks[slot];
        if (item == Item.None || count <= 0) return false;
        if (!held.IsEmpty && held.Item != item) return false;
        if (held.Count + count > StackMost) return false;
        stacks[slot] = new Stack(item, held.Count + count);
        return true;
    }

    /// <summary>Takes <paramref name="count"/> from one slot, all or nothing, as the slot's owner does.</summary>
    public bool TryTake(int slot, int count)
    {
        var held = stacks[slot];
        if (count <= 0 || held.Count < count) return false;
        stacks[slot] = held.Count == count ? default : held with { Count = held.Count - count };
        return true;
    }

    /// <summary>
    /// Takes <paramref name="count"/> of <paramref name="item"/> from a run of slots, first slot first, all or nothing,
    /// as their owner does; another item in those slots is left where it is.
    /// </summary>
    public bool TryTakeFrom(Range slots, Item item, int count)
    {
        if (count <= 0 || CountIn(slots, item) < count) return false;
        var (start, length) = slots.GetOffsetAndLength(Slots);
        for (var slot = start; slot < start + length && count > 0; slot++)
        {
            if (stacks[slot].Item != item) continue;
            var taken = Math.Min(stacks[slot].Count, count);
            if (taken > 0) TryTake(slot, taken);
            count -= taken;
        }

        return true;
    }

    /// <summary>
    /// Adds <paramref name="count"/> of <paramref name="item"/> across a run of slots, first slot first, all or nothing,
    /// as their owner does.
    /// </summary>
    public bool TryAddTo(Range slots, Item item, int count)
    {
        if (item == Item.None || count <= 0 || RoomIn(slots, item) < count) return false;
        var (start, length) = slots.GetOffsetAndLength(Slots);
        for (var slot = start; slot < start + length && count > 0; slot++)
        {
            var held = stacks[slot];
            if (!held.IsEmpty && held.Item != item) continue;
            var added = Math.Min(StackMost - held.Count, count);
            if (added > 0) TryAdd(slot, item, added);
            count -= added;
        }

        return true;
    }

    /// <summary>Sets one slot's stack outright, whatever its filter, as an admin's edit does; a count of 0 empties it.</summary>
    /// <remarks>Whether the slot may hold the item is the caller's to check: the slot's filter binds only a player.</remarks>
    public void Set(int slot, Stack stack)
    {
        ArgumentOutOfRangeException.ThrowIfNegative(stack.Count);
        ArgumentOutOfRangeException.ThrowIfGreaterThan(stack.Count, StackMost);
        if (stack.Count > 0 && stack.Item == Item.None) throw new ArgumentException("a count of no item", nameof(stack));
        stacks[slot] = stack.Count == 0 ? default : stack;
    }

    /// <summary>
    /// A player's drag of one slot's stack onto another slot (ITM-3): onto an empty slot or the same kind it moves as
    /// many as fit and leaves the rest; onto another kind the two stacks swap; refused if either slot's filter refuses
    /// what it would receive (ITM-4).
    /// </summary>
    /// <returns>Whether anything moved.</returns>
    public static bool Move(Inventory from, int fromSlot, Inventory to, int toSlot)
    {
        if (ReferenceEquals(from, to) && fromSlot == toSlot) return false;
        var moving = from.stacks[fromSlot];
        var onto = to.stacks[toSlot];
        if (moving.IsEmpty || !to.filters[toSlot].Accepts(moving.Item)) return false;

        if (onto.IsEmpty || onto.Item == moving.Item)
        {
            var moved = Math.Min(moving.Count, to.StackMost - onto.Count);
            if (moved == 0) return false;
            to.stacks[toSlot] = new Stack(moving.Item, onto.Count + moved);
            from.stacks[fromSlot] = moved == moving.Count ? default : moving with { Count = moving.Count - moved };
            return true;
        }

        if (!from.filters[fromSlot].Accepts(onto.Item)) return false;
        if (moving.Count > to.StackMost || onto.Count > from.StackMost) return false;
        to.stacks[toSlot] = moving;
        from.stacks[fromSlot] = onto;
        return true;
    }
}
