using System.Text.Json;
using System.Text.Json.Serialization;
using Shipstick.Codex;
using Shipstick.Economy;
using Shipstick.Items;
using Shipstick.Ship;

namespace Shipstick.App.Host;

/// <summary>
/// What the admin is sent (WEB-8, WEB-2): every capsule's cabin, and which one is <see cref="Entered"/> — the one its
/// moves are made from — with at most <see cref="StackMost"/> for an edit of a slot. What an edit may set a universal
/// slot to is any item of the codex.
/// </summary>
sealed record ShipView(int Columns, int Rows, int StackMost, CapsuleAt Entered, CabinView[] Cabins)
{
    public static ShipView Of(Vessel vessel, CapsuleAt entered, int stackMost, WayIndex ways) =>
        new(vessel.Grid.Columns, vessel.Grid.Rows, stackMost, entered,
            [.. vessel.Capsules.Select(c => CabinView.Entered(vessel, c.At, ways))]);
}

/// <summary>An item crosses to a client as its catalogue id, an empty slot's as "".</summary>
sealed class ItemJson : JsonConverter<Item>
{
    public override Item Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options) =>
        reader.GetString() is { Length: > 0 } id ? new Item(id) : Item.None;

    public override void Write(Utf8JsonWriter writer, Item value, JsonSerializerOptions options) =>
        writer.WriteStringValue(value.Id ?? "");
}

[JsonSourceGenerationOptions(PropertyNamingPolicy = JsonKnownNamingPolicy.CamelCase, UseStringEnumConverter = true,
    DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull, Converters = [typeof(ItemJson)])]
[JsonSerializable(typeof(CabinView))]
[JsonSerializable(typeof(SeatView))]
[JsonSerializable(typeof(ShipView))]
[JsonSerializable(typeof(CodexBook))]
[JsonSerializable(typeof(CodexWordsView))]
[JsonSerializable(typeof(ClientAction))]
partial class HostJson : JsonSerializerContext;
