using System.IO.Compression;
using System.Security.Cryptography;

namespace Shipstick.App.Host;

/// <summary>
/// A JSON document the host makes once and sends many times: compressed once, at the smallest Brotli makes — it is
/// most of what a client downloads, and compressing it per request at that size would cost each client seconds — and
/// tagged, so a client already holding it is answered "not modified".
/// </summary>
sealed record ServedJson(byte[] Json, byte[] Brotli, string Tag)
{
    public static ServedJson Of(byte[] json) => new(json, Compress(json), $"\"{Convert.ToHexString(SHA256.HashData(json))}\"");

    /// <summary>The answer to a request for it: revalidated on every load, and compressed when the client takes Brotli.</summary>
    public IResult Answer(HttpContext http)
    {
        var headers = http.Response.Headers;
        headers.CacheControl = "no-cache";
        headers.ETag = Tag;
        headers.Vary = "Accept-Encoding";
        if (http.Request.Headers.IfNoneMatch == Tag) return Results.StatusCode(StatusCodes.Status304NotModified);
        if (!http.Request.Headers.AcceptEncoding.ToString().Contains("br")) return Results.Bytes(Json, "application/json");
        headers.ContentEncoding = "br";
        return Results.Bytes(Brotli, "application/json");
    }

    static byte[] Compress(byte[] bytes)
    {
        using var compressed = new MemoryStream();
        using (var brotli = new BrotliStream(compressed, CompressionLevel.SmallestSize)) brotli.Write(bytes);
        return compressed.ToArray();
    }
}
