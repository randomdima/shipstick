using System.Security.Cryptography;
using System.Text.Json;

namespace Shipstick.App.Host;

/// <summary>
/// The art the host serves under <c>assets/</c>, by the path a page asks for it by: every image and texture, and every
/// device model the page draws live (GAM-10) — its <c>.mesh.json</c> and the triangles it names.
/// </summary>
/// <remarks>
/// <b>Sent as <c>assets.json</c></b> (<see cref="Json"/>): <c>files</c>, each path's version, and <c>meshes</c>, each
/// model's <c>.mesh.json</c> whole — so a page asks for a file at its version, which a browser keeps without asking
/// again (<see cref="Shipstick.Core.Config.HostFigures.VersionedKeptS"/>), and knows every model's looks before its
/// first draw, asking for its triangles and textures at once rather than a round trip later.
/// </remarks>
static class AssetList
{
    const string Folder = "assets";
    const string Mesh = ".mesh.json";
    static readonly string[] Listed = ["*.png", "*.webp", $"*{Mesh}", "*.mesh.bin"];

    // A version is this much of the file's SHA-256, in hex: enough that two builds of one file never share one.
    const int VersionBytes = 8;

    /// <summary>Every listed file under <paramref name="webRoot"/>'s <c>assets/</c>, relative to the web root, with forward slashes.</summary>
    public static string[] Of(string webRoot)
    {
        var root = Path.Combine(webRoot, Folder);
        if (!Directory.Exists(root)) return [];
        return [.. Listed.SelectMany(pattern => Directory.EnumerateFiles(root, pattern, SearchOption.AllDirectories))
            .Select(file => Path.GetRelativePath(webRoot, file).Replace('\\', '/'))
            .Order(StringComparer.Ordinal)];
    }

    /// <summary><c>assets.json</c>: <c>{"files": {path: version}, "meshes": {path: its .mesh.json}}</c>.</summary>
    public static byte[] Json(string webRoot)
    {
        using var stream = new MemoryStream();
        using (var json = new Utf8JsonWriter(stream))
        {
            var paths = Of(webRoot);
            json.WriteStartObject();
            json.WriteStartObject("files");
            foreach (var path in paths)
                json.WriteString(path, Convert.ToHexStringLower(SHA256.HashData(File.ReadAllBytes(Path.Combine(webRoot, path))), 0, VersionBytes));
            json.WriteEndObject();
            json.WriteStartObject("meshes");
            foreach (var path in paths.Where(path => path.EndsWith(Mesh, StringComparison.Ordinal)))
            {
                json.WritePropertyName(path);
                json.WriteRawValue(File.ReadAllBytes(Path.Combine(webRoot, path)));
            }

            json.WriteEndObject();
            json.WriteEndObject();
        }

        return stream.ToArray();
    }
}
