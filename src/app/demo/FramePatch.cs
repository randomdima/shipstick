using System.Text.Json.Nodes;

namespace Shipstick.App.Demo;

/// <summary>
/// What turns one JSON value into the next, saying no more than changed: <c>{"=": value}</c> replaces it whole,
/// <c>{"o": {key: patch}, "d": [key]}</c> patches an object's changed keys and drops its gone ones, and
/// <c>{"a": {index: patch}, "n": length}</c> patches an array's changed elements at its new length. <c>demo.js</c>
/// applies it.
/// </summary>
/// <remarks>
/// A recording keeps a frame a client's view changes, and most of a frame is the frame before: whole, a few minutes
/// of the admin's frames are hundreds of megabytes; patched, kilobytes.
/// </remarks>
static class FramePatch
{
    /// <summary>The patch from <paramref name="from"/> to <paramref name="to"/>; null when they are equal.</summary>
    public static JsonNode? Between(JsonNode? from, JsonNode? to)
    {
        if (JsonNode.DeepEquals(from, to)) return null;
        if (from is JsonObject fromObject && to is JsonObject toObject) return Objects(fromObject, toObject);
        if (from is JsonArray fromArray && to is JsonArray toArray) return Arrays(fromArray, toArray);
        return Whole(to);
    }

    static JsonObject Whole(JsonNode? value) => new() { ["="] = value?.DeepClone() };

    static JsonObject Objects(JsonObject from, JsonObject to)
    {
        var changed = new JsonObject();
        foreach (var (key, value) in to)
            if (!from.TryGetPropertyValue(key, out var was)) changed[key] = Whole(value);
            else if (Between(was, value) is { } patch) changed[key] = patch;

        var patched = new JsonObject { ["o"] = changed };
        var gone = from.Select(entry => entry.Key).Where(key => !to.ContainsKey(key)).ToArray();
        if (gone.Length > 0) patched["d"] = new JsonArray([.. gone.Select(key => (JsonNode?)JsonValue.Create(key))]);
        return patched;
    }

    static JsonObject Arrays(JsonArray from, JsonArray to)
    {
        var changed = new JsonObject();
        for (var index = 0; index < to.Count; index++)
            if (index >= from.Count) changed[$"{index}"] = Whole(to[index]);
            else if (Between(from[index], to[index]) is { } patch) changed[$"{index}"] = patch;
        return new JsonObject { ["a"] = changed, ["n"] = to.Count };
    }
}
