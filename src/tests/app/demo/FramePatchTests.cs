using System.Text.Json.Nodes;
using Shipstick.App.Demo;

namespace Shipstick.Tests.App.Demo;

/// <summary>
/// A frame patch (DEM-1) carries one JSON value to the next exactly. <see cref="Applied"/> is <c>demo.js</c>'s
/// <c>patched</c>, step for step.
/// </summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P5)]
public sealed class FramePatchTests
{
    static JsonNode? Applied(JsonNode? value, JsonNode patch)
    {
        var p = patch.AsObject();
        if (p.TryGetPropertyValue("=", out var whole)) return whole?.DeepClone();
        if (p.TryGetPropertyValue("o", out var keys))
        {
            var next = value is JsonObject old ? (JsonObject)old.DeepClone() : [];
            foreach (var (key, keyPatch) in keys!.AsObject()) next[key] = Applied(value?[key], keyPatch!);
            foreach (var gone in p["d"]?.AsArray() ?? []) next.Remove(gone!.GetValue<string>());
            return next;
        }

        var length = p["n"]!.GetValue<int>();
        var was = value as JsonArray;
        var array = new JsonArray([.. Enumerable.Range(0, length).Select(i => i < was?.Count ? was[i]?.DeepClone() : null)]);
        foreach (var (index, elementPatch) in p["a"]!.AsObject())
            array[int.Parse(index)] = Applied(was is not null && int.Parse(index) < was.Count ? was[int.Parse(index)] : null, elementPatch!);
        return array;
    }

    [Theory]
    [InlineData("""{"nowS": 1, "seat": {"slots": [1, 2, 3], "name": "a"}}""", """{"nowS": 2, "seat": {"slots": [1, 5], "name": "a"}}""")]
    [InlineData("""{"a": [1], "b": null}""", """{"a": [1, null, {"c": false}], "b": 0}""")]
    [InlineData("""{"a": 1, "gone": {"x": 1}}""", """{"a": 1}""")]
    [InlineData("""[{"a": 1}, 2]""", """{"a": 1}""")]
    public void CarriesAValueToTheNext(string from, string to)
    {
        var (before, after) = (JsonNode.Parse(from), JsonNode.Parse(to));

        Assert.True(JsonNode.DeepEquals(after, Applied(before, FramePatch.Between(before, after)!)));
    }

    [Fact]
    public void CarriesNothingToTheFirstFrameWhole()
    {
        var frame = JsonNode.Parse("""{"nowS": 0, "ship": {"capsules": [1, 2]}}""");

        Assert.True(JsonNode.DeepEquals(frame, Applied(null, FramePatch.Between(null, frame)!)));
    }

    [Fact]
    public void IsNothingBetweenEqualValues() =>
        Assert.Null(FramePatch.Between(JsonNode.Parse("""{"a": [1, {"b": 2}]}"""), JsonNode.Parse("""{"a": [1, {"b": 2}]}""")));
}
