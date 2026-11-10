using System.IO.Compression;
using System.Net.WebSockets;
using System.Security.Cryptography;
using Microsoft.AspNetCore.ResponseCompression;
using Shipstick.App.Host;
using Shipstick.Core.Config;
using Shipstick.Economy;

// The game's host (HST-3): the one ship, a socket a client, and the client's files. Rooted at its own folder, so it
// reads its settings and finds the client's files from anywhere.
var builder = WebApplication.CreateBuilder(new WebApplicationOptions
{
    Args = args,
    ContentRootPath = AppContext.BaseDirectory,
    WebRootPath = "client",
});
// A model's triangles (.mesh.bin, application/octet-stream) shrink to a fifth compressed.
builder.Services.AddResponseCompression(compression =>
    compression.MimeTypes = [.. ResponseCompressionDefaults.MimeTypes, "application/octet-stream"]);
builder.Services.Configure<BrotliCompressionProviderOptions>(brotli => brotli.Level = CompressionLevel.Optimal);
builder.Services.AddSingleton(new ServedShip(GameConfig.Default, Catalogue.Embedded));
builder.Services.AddHostedService(services => services.GetRequiredService<ServedShip>());

var app = builder.Build();
app.UseResponseCompression();
app.UseWebSockets();

// A file asked for at its version (`?v=`, from assets.json) never changes at that address, so it is kept without
// asking. Every other file is revalidated on each load (a 304 when unchanged): without a Cache-Control a browser
// guesses a freshness and keeps the last build's client.
var versionedCache = $"public, max-age={GameConfig.Default.Host.VersionedKeptS}, immutable";
app.UseDefaultFiles();
app.UseStaticFiles(new StaticFileOptions
{
    OnPrepareResponse = served => served.Context.Response.Headers.CacheControl =
        served.Context.Request.Query.ContainsKey("v") ? versionedCache : "no-cache",
});

app.MapGet("/codex.json", (HttpContext http, ServedShip ship) =>
{
    var headers = http.Response.Headers;
    headers.CacheControl = "no-cache";
    headers.ETag = ship.CodexTag;
    headers.Vary = "Accept-Encoding";
    if (http.Request.Headers.IfNoneMatch == ship.CodexTag) return Results.StatusCode(StatusCodes.Status304NotModified);
    if (!http.Request.Headers.AcceptEncoding.ToString().Contains("br")) return Results.Bytes(ship.CodexJson, "application/json");
    headers.ContentEncoding = "br";
    return Results.Bytes(ship.CodexBrotli, "application/json");
});

// What the host serves under assets/ and at which version, so a page asks for a device's own art only when there is
// some and otherwise draws the shared art its kind falls back to. Listed once: the assets are the build's.
var assetList = AssetList.Json(app.Environment.WebRootPath);
var assetTag = $"\"{Convert.ToHexString(SHA256.HashData(assetList))}\"";
app.MapGet("/assets.json", (HttpContext http) =>
{
    http.Response.Headers.CacheControl = "no-cache";
    http.Response.Headers.ETag = assetTag;
    return http.Request.Headers.IfNoneMatch == assetTag
        ? Results.StatusCode(StatusCodes.Status304NotModified)
        : Results.Bytes(assetList, "application/json");
});

app.Map("/play", async (HttpContext http, ServedShip ship, IHostApplicationLifetime life) =>
{
    if (!http.WebSockets.IsWebSocketRequest)
    {
        http.Response.StatusCode = StatusCodes.Status400BadRequest;
        return;
    }

    // Compressed: a view is repetitive JSON, and nothing secret is ever framed beside what a client sent.
    using var socket = await http.WebSockets.AcceptWebSocketAsync(new WebSocketAcceptContext { DangerousEnableCompression = true });
    using var leaving = CancellationTokenSource.CreateLinkedTokenSource(http.RequestAborted, life.ApplicationStopping);
    if (Client.For(ship, http.Request.Query) is { } client)
        await client.Run(socket, ship, leaving.Token);
    else
        await socket.CloseAsync(WebSocketCloseStatus.PolicyViolation, $"seat refused: no capsule at seat {http.Request.Query["seat"]}",
            leaving.Token);
});

app.Run();
