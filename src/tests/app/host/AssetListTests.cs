using System.Text.Json;
using Shipstick.App.Host;

namespace Shipstick.Tests.App.Host;

/// <summary>The art the host says it serves (GAM-9, GAM-10): what a page may ask for, by the path it asks by.</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P8)]
public sealed class AssetListTests : IDisposable
{
    readonly DirectoryInfo root = Directory.CreateTempSubdirectory("shipstick-assets-");

    public void Dispose() => root.Delete(recursive: true);

    void Write(string path, string text = "")
    {
        var file = Path.Combine(root.FullName, path);
        Directory.CreateDirectory(Path.GetDirectoryName(file)!);
        File.WriteAllText(file, text);
    }

    [Fact]
    public void ListsEveryImageAndTextureUnderAssetsByItsPathFromTheWebRoot()
    {
        Write("assets/devices/any_bench.png");
        Write("assets/textures/tex_bare_steel.webp");
        Write("assets/app/web/fonts/Michroma-Regular.ttf");
        Write("style.css");

        Assert.Equal(["assets/devices/any_bench.png", "assets/textures/tex_bare_steel.webp"], AssetList.Of(root.FullName));
    }

    [Fact]
    public void ListsADeviceModelByItsMeshAndItsTriangles()
    {
        Write("assets/devices/any_bench.mesh.json");
        Write("assets/devices/any_bench.mesh.bin");

        Assert.Equal(["assets/devices/any_bench.mesh.bin", "assets/devices/any_bench.mesh.json"], AssetList.Of(root.FullName));
    }

    [Fact]
    public void VersionsAFileByWhatItHolds()
    {
        Write("assets/a.png", "one");
        Write("assets/b.png", "one");
        Write("assets/c.png", "two");

        var files = Files();

        Assert.Equal(files["assets/a.png"], files["assets/b.png"]);
        Assert.NotEqual(files["assets/a.png"], files["assets/c.png"]);
    }

    [Fact]
    public void SendsEachMeshWhole()
    {
        Write("assets/devices/any_bench.mesh.json", """{"bin": "any_bench.mesh.bin"}""");

        using var json = JsonDocument.Parse(AssetList.Json(root.FullName));

        Assert.Equal("any_bench.mesh.bin",
            json.RootElement.GetProperty("meshes").GetProperty("assets/devices/any_bench.mesh.json").GetProperty("bin").GetString());
    }

    Dictionary<string, string> Files()
    {
        using var json = JsonDocument.Parse(AssetList.Json(root.FullName));
        return json.RootElement.GetProperty("files").EnumerateObject().ToDictionary(file => file.Name, file => file.Value.GetString()!);
    }
}
