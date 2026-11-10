using Shipstick.Items;
using static Shipstick.Tests.TestItems;

namespace Shipstick.Tests.Items;

/// <summary>A player's drag between slots (ITM-1, ITM-3).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P1)]
public class InventoryTests
{
    const int StackMost = 10;

    [Fact]
    public void ADragOntoAnEmptySlotMovesTheWholeStack()
    {
        var from = Holding(Water, 4);
        var to = Inventory.Open(1, StackMost);

        Assert.True(Inventory.Move(from, 0, to, 0));
        Assert.Equal((new Stack(), new Stack(Water, 4)), (from[0], to[0]));
    }

    [Fact]
    public void ADragOntoTheSameKindMovesWhatFitsAndLeavesTheRest()
    {
        var from = Holding(Water, 4);
        var to = Holding(Water, StackMost - 1);

        Inventory.Move(from, 0, to, 0);

        Assert.Equal((new Stack(Water, 3), new Stack(Water, StackMost)), (from[0], to[0]));
    }

    [Fact]
    public void ADragOntoAnotherKindSwapsTheTwoStacks()
    {
        var from = Holding(Water, 4);
        var to = Holding(Food, 2);

        Inventory.Move(from, 0, to, 0);

        Assert.Equal((new Stack(Food, 2), new Stack(Water, 4)), (from[0], to[0]));
    }

    [Fact]
    public void ASlotForOneItemRefusesAnother()
    {
        var from = Holding(Water, 4);
        var to = new Inventory([SlotFilter.Only(Oxygen)], StackMost);

        Assert.False(Inventory.Move(from, 0, to, 0));
        Assert.Equal(new Stack(Water, 4), from[0]);
    }

    [Fact]
    public void AnOutputSlotRefusesADropButNotItsOwnersFill()
    {
        var from = Holding(Food, 1);
        var output = new Inventory([SlotFilter.TakeOnly], StackMost);

        Assert.False(Inventory.Move(from, 0, output, 0));
        Assert.True(output.TryAdd(0, Food, 1));
    }

    [Fact]
    public void ASwapIsRefusedWhenTheSourceSlotWouldNotTakeWhatComesBack()
    {
        var output = new Inventory([SlotFilter.TakeOnly], StackMost);
        output.TryAdd(0, Food, 2);
        var to = Holding(Water, 3);

        Assert.False(Inventory.Move(output, 0, to, 0));
        Assert.Equal((new Stack(Food, 2), new Stack(Water, 3)), (output[0], to[0]));
    }

    [Fact]
    public void AnOwnersTakeOfOneItemLeavesAnotherInTheSameSlots()
    {
        var inventory = Inventory.Open(2, StackMost);
        inventory.TryAdd(0, Food, 2);
        inventory.TryAdd(1, Water, 3);

        Assert.True(inventory.TryTakeFrom(0..2, Water, 2));
        Assert.Equal((new Stack(Food, 2), new Stack(Water, 1)), (inventory[0], inventory[1]));
    }

    static Inventory Holding(Item item, int count)
    {
        var inventory = Inventory.Open(1, StackMost);
        inventory.TryAdd(0, item, count);
        return inventory;
    }
}
