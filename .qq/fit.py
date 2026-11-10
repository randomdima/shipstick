"""
Check the page shows every generated image at its own proportions, and repeats only images that tile (GAM-14).

Reads the client's stylesheet, which is where every image the page shows is placed and sized (GAM-9). A background is
stretched when it is sized on both axes (`100% 100%`); a border image when it is sliced with `stretch` (the default) or
`round`, or when its sides are scaled by different factors, so a corner or the middle is squeezed. What repeats is
measured: a region tiles when the step from its last row or column back to its first is no larger than the steps
inside it. A custom property resolves to every value the stylesheet gives it, so a source chosen by a class is checked
for each class. `seams` measures one image the same way, for choosing its slices.
"""

from __future__ import annotations

import argparse
import ast
import itertools
import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

from common import cli, paths

#: What a call may take: a few dozen images opened and their edges compared.
TIMEOUT_S = 60

STYLE = Path("src/app/web/wwwroot/style.css")
#: The page asks for `assets/…` and the host serves the project's `assets/` under that path (HST-3).
SERVED = Path(".")
#: How far apart the scale factors of a border image's sides may be before a corner or the middle reads squeezed.
SCALE_TOLERANCE = 0.02
#: How much larger the step across a repeat's seam may be than a usual step inside the region. Noise alone gives ~1;
#: a lighting gradient, a rim or a bolt cut by the edge gives several.
SEAM_RATIO = 1.8
#: Which of the steps between neighbouring rows or columns inside a region the seam is weighed against.
STEP_QUANTILE = 0.9
#: The share of each column pair's largest pixel steps left out of its step.
STEP_TRIM = 0.05
REPEATS = {"repeat", "repeat-x", "repeat-y", "no-repeat", "space", "round"}
URL = re.compile(r"""url\(\s*["']?([^"')]+)["']?\s*\)""")
VAR = re.compile(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^()]*))?\)")
SLICE = re.compile(r"^\d+(\.\d+)?(,\d+(\.\d+)?){0,3}$")


@dataclass
class Rule:
    line: int
    selector: str
    decls: list[tuple[int, str, str]]


def main():
    a = parse_args()
    root = paths.project_root()
    if a.action == "seams":
        return seams_of(root, a)
    style = paths.resolve_in_root(a.style or str(STYLE), root)
    found = audit(root, style)
    for f in found[: a.limit or None]:
        print(f)
    if a.limit and len(found) > a.limit:
        print(f"… {len(found) - a.limit} more")
    shown = style.relative_to(root)
    print(f"{len(found)} problem(s) in {shown}" if found else f"{shown}: GAM-14 holds")
    return 1 if found else 0


def parse_args():
    parser = argparse.ArgumentParser(
        prog="qq fit",
        description="Check the page shows every generated image at its own proportions, and repeats only images that "
                    "tile (GAM-14).",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("action", nargs="?", default="check", choices=["check", "seams"],
                        help="check: the stylesheet; seams: how well one image repeats, whole or as sliced")
    parser.add_argument("image", nargs="?", help="seams: the image, a path under the project")
    parser.add_argument("--slice", type=slice_px, default=None, metavar="T,R,B,L",
                        help="seams: the image's slice insets in pixels, as border-image-slice takes them")
    parser.add_argument("--style", default=None, help="check: the stylesheet, a path under the project "
                                                      f"(default {STYLE})")
    parser.add_argument("--limit", type=cli.counting, default=40, metavar="INT", help="max problems printed (0 = all)")
    return parser.parse_args()


def slice_px(text):
    if not SLICE.match(text):
        raise argparse.ArgumentTypeError("one to four numbers, comma-separated")
    return expand4([float(v) for v in text.split(",")])


def audit(root, style):
    """Every way the stylesheet stretches an image or repeats one that does not tile, one line each."""
    rules = parse(style.read_text())
    props = custom_props(rules)
    found = []
    for rule in rules:
        where = f"{style.relative_to(root)}:{rule.line}  {rule.selector}"
        for problem in backgrounds(root, rule, props) + border_images(root, rule, props):
            found.append(f"{where}  {problem}")
    return list(dict.fromkeys(found))


def parse(css):
    """The stylesheet's rules, comments blanked so line numbers hold."""
    css = re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group()), css, flags=re.S)
    rules, i = [], 0
    while (open_at := css.find("{", i)) >= 0:
        close_at = css.find("}", open_at)
        selector = " ".join(css[i:open_at].split())
        decls, start = [], open_at + 1
        for part in split_top(css[open_at + 1:close_at], ";"):
            if ":" in part.strip():
                prop, value = part.split(":", 1)
                line = css.count("\n", 0, start + len(part) - len(part.lstrip())) + 1
                decls.append((line, prop.strip().lower(), " ".join(value.split())))
            start += len(part) + 1
        rules.append(Rule(css.count("\n", 0, i + len(css[i:open_at]) - len(css[i:open_at].lstrip())) + 1,
                          selector, decls))
        i = close_at + 1
    return rules


def split_top(text, sep):
    """`text` split on `sep` outside parentheses."""
    parts, depth, start = [], 0, 0
    for i, c in enumerate(text):
        depth += c == "("
        depth -= c == ")"
        if c == sep and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    parts.append(text[start:])
    return parts


def custom_props(rules):
    props = {}
    for rule in rules:
        for _, prop, value in rule.decls:
            if prop.startswith("--"):
                props.setdefault(prop, []).append(value)
    return props


def resolve(value, props, local, depth=0):
    """Every value `value` can take, its custom properties replaced: the rule's own first, else each the sheet gives."""
    m = VAR.search(value)
    if not m or depth > 8:
        return [value]
    name, fallback = m.group(1), m.group(2)
    options = [local[name]] if name in local else props.get(name) or ([fallback] if fallback else [""])
    out = []
    for option in options:
        # Every use of one property in a value is the same value: a side's width never mixes two elements' sizes.
        out += resolve(value.replace(m.group(0), option), props, local, depth + 1)
    return list(dict.fromkeys(out))[:24]


def tokens(value):
    return [t for t in split_top(value, " ") if t]


def backgrounds(root, rule, props):
    local = {p: v for _, p, v in rule.decls if p.startswith("--")}
    found = []
    images, sizes, repeats = [], [], []
    for _, prop, raw in rule.decls:
        for value in resolve(raw, props, local):
            if prop == "background":
                images, sizes, repeats = [], [], []
                for layer in split_top(value, ","):
                    url = URL.search(layer)
                    images.append(url.group(1) if url else None)
                    words = tokens(URL.sub("", layer))
                    size = []
                    if "/" in words:
                        for w in words[words.index("/") + 1:]:
                            if w in REPEATS or len(size) == 2:
                                break
                            size.append(w)
                    sizes.append(size)
                    repeats.append(" ".join(w for w in words if w in REPEATS) or "repeat")
            elif prop == "background-image":
                images = [(u.group(1) if (u := URL.search(layer)) else None) for layer in split_top(value, ",")]
            elif prop == "background-size":
                sizes = [tokens(layer) for layer in split_top(value, ",")]
            elif prop == "background-repeat":
                repeats = [layer.strip() for layer in split_top(value, ",")]
            else:
                continue
            for i, url in enumerate(images):
                if not url:
                    continue
                size = sizes[i % len(sizes)] if sizes else []
                # An image given alone takes its size and repeat from another rule; this check reads one rule.
                repeat = repeats[i % len(repeats)] if repeats else "no-repeat"
                found += background_problems(root, url, size, repeat)
    return found


def background_problems(root, url, size, repeat):
    name = Path(url).name
    found = []
    if len(size) == 2 and "auto" not in size:
        found.append(f"{name}: sized on both axes ({' '.join(size)}): give one, or `auto` on the other")
    if "round" in repeat:
        found.append(f"{name}: `round` rescales each repeat to fit a whole count")
    across = repeat in ("repeat", "repeat-x") or repeat.startswith("repeat ") or repeat == "repeat repeat"
    down = repeat in ("repeat", "repeat-y") or repeat.endswith(" repeat")
    if across or down:
        image = load(root, url)
        if image is None:
            return found + [f"{url}: no such image"]
        for axis, on in (("across", across), ("down", down)):
            ratio = seam(image, axis) if on else 0
            if ratio > SEAM_RATIO:
                found.append(f"{name}: repeats {axis} and does not tile (seam {ratio:.1f}× the steps inside it)")
    return found


def border_images(root, rule, props):
    local = {p: v for _, p, v in rule.decls if p.startswith("--")}
    state = {"source": [], "slice": [["100%"]], "width": [["1"]], "repeat": [["stretch"]], "border": [None]}
    for _, prop, raw in rule.decls:
        values = resolve(raw, props, local)
        if prop == "border-image":
            state["source"] = [URL.search(v).group(1) if URL.search(v) else None for v in values]
            parsed = [shorthand(v) for v in values]
            state["slice"] = [p[0] for p in parsed]
            state["width"] = [p[1] for p in parsed]
            state["repeat"] = [p[2] for p in parsed]
        elif prop == "border-image-source":
            state["source"] = [URL.search(v).group(1) if URL.search(v) else None for v in values]
        elif prop == "border-image-slice":
            state["slice"] = [tokens(v) for v in values]
        elif prop == "border-image-width":
            state["width"] = [tokens(v) for v in values]
        elif prop == "border-image-repeat":
            state["repeat"] = [tokens(v) for v in values]
        elif prop in ("border-width", "border"):
            state["border"] = [[t for t in tokens(v) if px(t) is not None] or None for v in values]
    declared = {prop for _, prop, _ in rule.decls}
    if declared & {"border-image-source"} and not declared & {"border-image", "border-image-slice",
                                                              "border-image-width", "border-image-repeat"}:
        return []  # a source swapped in (a key pressed) is cut as the rule that slices it says; this check reads one rule
    found = []
    for url, cut, width, repeat, border in itertools.product(
            state["source"], state["slice"], state["width"], state["repeat"], state["border"]):
        if url:
            found += border_problems(root, url, cut, width, repeat, border)
    return found


def shorthand(value):
    """A `border-image` shorthand's slice, width and repeat, the source left out."""
    words = tokens(URL.sub("", value))
    groups, current = [[]], 0
    repeat = [w for w in words if w in REPEATS or w == "stretch"] or ["stretch"]
    for w in words:
        if w == "/":
            groups.append([])
            current += 1
        elif w not in repeat:
            groups[current].append(w)
    return groups[0] or ["100%"], (groups[1] if len(groups) > 1 and groups[1] else ["1"]), repeat


def border_problems(root, url, cut, width, repeat, border):
    name = Path(url).name
    image = load(root, url)
    if image is None:
        return [f"{url}: no such image"]
    found = [f"{name}: border image `{r}` {'rescales each repeat' if r == 'round' else 'stretches its edges'}"
             for r in dict.fromkeys(repeat) if r in ("stretch", "round")]
    fill = "fill" in cut
    insets = slice_insets([c for c in cut if c != "fill"], image.size)
    widths = expand4(width)
    borders = expand4(border) if border else None
    scales = []
    for side, (inset, w) in enumerate(zip(insets, widths)):
        if w == "auto":
            scales.append(1.0)
            continue
        drawn = px(w)
        if drawn is not None and re.fullmatch(r"[\d.]+", w) and borders:
            drawn = drawn * (px(borders[side]) or 0)
        if drawn is None:
            found.append(f"{name}: side width `{w}` is not a measure this check can resolve")
            continue
        if inset and drawn:
            scales.append(drawn / inset)
    if scales and max(scales) > min(scales) * (1 + SCALE_TOLERANCE):
        found.append(f"{name}: sides scaled unevenly ({', '.join(f'{s:.3f}' for s in scales)}): "
                     "a corner or the middle is squeezed")
    if any(r == "repeat" for r in repeat):
        found += [f"{name}: {problem}" for problem in sliced_seams(image, insets, fill)]
    return found


def slice_insets(cut, size):
    w, h = size
    values = expand4(cut or ["100%"])
    out = []
    for i, v in enumerate(values):
        whole = h if i in (0, 2) else w
        out.append(float(v[:-1]) / 100 * whole if v.endswith("%") else float(v))
    return out


def sliced_seams(image, insets, fill):
    """How the repeated regions of a sliced image meet themselves: the edges along, the middle both ways."""
    t, r, b, l = (round(v) for v in insets)
    w, h = image.size
    regions = [("top edge", (l, 0, w - r, t), "across"), ("bottom edge", (l, h - b, w - r, h), "across"),
               ("left edge", (0, t, l, h - b), "down"), ("right edge", (w - r, t, w, h - b), "down")]
    if fill:
        regions += [("middle", (l, t, w - r, h - b), "across"), ("middle", (l, t, w - r, h - b), "down")]
    found = []
    for name, box, axis in regions:
        if box[2] - box[0] < 2 or box[3] - box[1] < 2:
            continue
        ratio = seam(image.crop(box), axis)
        if ratio > SEAM_RATIO:
            found.append(f"{name} repeats {axis} and does not tile (seam {ratio:.1f}× the steps inside it)")
    return found


def seam(image, axis):
    """
    The step across a repeat's seam, as a multiple of a usual step between neighbouring columns (rows, `down`) inside.
    A seam is a line the whole way along — a fringe, a shift of tone — so the few largest pixel steps of each pair
    (a star or a scratch that happens to lie on it) are left out.
    """
    if axis == "down":
        image = image.transpose(Image.Transpose.ROTATE_90)
    w, h = image.size
    px_ = image.load()
    kept = max(1, round(h * (1 - STEP_TRIM)))

    def column(x):
        return [px_[x, y] for y in range(h)]

    def step(a, b):
        diffs = sorted(sum(abs(p - q) for p, q in zip(pa[:3], qa[:3])) * (pa[3] + qa[3]) / 510 for pa, qa in zip(a, b))
        return sum(diffs[:kept]) / (3 * kept)

    cols = [column(x) for x in range(w)]
    steps = sorted(step(cols[x], cols[x + 1]) for x in range(w - 1)) or [0.0]
    # Against the steps a picture often takes, not their mean: a sparse field's few bright columns are its own.
    inside = steps[int(STEP_QUANTILE * (len(steps) - 1))]
    return step(cols[-1], cols[0]) / max(inside, 1e-6)


def expand4(values):
    values = list(values)
    if len(values) == 3:
        return values + [values[1]]
    return values * (4 // len(values))


def px(text):
    """A length in pixels, `calc()` included, or None for what holds a percentage, a font size or a viewport unit."""
    text = text.replace("calc", "")
    if re.search(r"%|em\b|vw|vh|var\(", text):
        return None
    text = re.sub(r"(\d+(\.\d+)?)px", r"\1", text)
    try:
        return arithmetic(ast.parse(text, mode="eval").body)
    except (SyntaxError, ValueError):
        return None


def arithmetic(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -arithmetic(node.operand)
    if isinstance(node, ast.BinOp) and type(node.op) in (ast.Add, ast.Sub, ast.Mult, ast.Div):
        a, b = arithmetic(node.left), arithmetic(node.right)
        return {ast.Add: a + b, ast.Sub: a - b, ast.Mult: a * b}.get(type(node.op), a / b if b else 0.0)
    raise ValueError(ast.dump(node))


def load(root, url):
    path = root / SERVED / url
    return Image.open(path).convert("RGBA") if path.is_file() else None


def seams_of(root, a):
    if not a.image:
        cli.fail("seams needs an image")
    path = paths.resolve_in_root(a.image, root)
    image = Image.open(path).convert("RGBA")
    print(f"{path.relative_to(root)}  {image.width}×{image.height}")
    if a.slice:
        for line in sliced_seams(image, a.slice, True) or ["every region sliced tiles"]:
            print(f"  {line}")
        t, r, b, l = (round(v) for v in a.slice)
        for name, box in (("top edge", (l, 0, image.width - r, t)), ("left edge", (0, t, l, image.height - b)),
                          ("middle", (l, t, image.width - r, image.height - b))):
            crop = image.crop(box)
            print(f"  {name}: seam across {seam(crop, 'across'):.2f}, down {seam(crop, 'down'):.2f}")
    else:
        print(f"  whole: seam across {seam(image, 'across'):.2f}, down {seam(image, 'down'):.2f} "
              f"(tiles at ≤ {SEAM_RATIO})")
    return 0


if __name__ == "__main__":
    cli.entry(main)
