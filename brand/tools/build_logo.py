"""Generate Vieira Creations VI logo SVGs (geometry-exact master)."""
import sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = sys.argv[1]
FONT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

BLACK, IVORY, ORANGE = "#0B0B0B", "#F4EFE6", "#FF4D24"

# ---------- Mark geometry (units; mark is 640 x 400) ----------
H = 400.0          # cap height of the mark
ARM = 120.0        # horizontal thickness of V arms == width of I
S = 240.0 / H      # outer-edge slope dx/dy (apex at x=240, y=400)
CUT_Y, GAP = 140.0, 16.0   # horizontal cut through V, gap width (== I gaps)
TIP = 13.0         # small flat at the V's bottom tip
IW = 104.0         # I width = perpendicular stroke of the V arms (120*cos31deg), optically equal
I_X = 520.0        # I starts here (40-unit gap from V)
W = I_X + IW       # 624

def f(n): return f"{n:.2f}".rstrip("0").rstrip(".")
def poly(pts): return "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts) + " Z"

inner_apex_y = ARM / S                     # 200
y2 = CUT_Y + GAP                           # 156
v_left  = [(0, 0), (ARM, 0), (ARM + CUT_Y*S, CUT_Y), (CUT_Y*S, CUT_Y)]
v_right = [(W - I_X - 0 - 0 + 0, 0)]       # placeholder, built below
vx = 480.0                                 # V total width
v_right = [(vx - ARM, 0), (vx, 0), (vx - CUT_Y*S, CUT_Y), (vx - ARM - CUT_Y*S, CUT_Y)]
ty = H - TIP
v_bottom = [(y2*S, y2), (ARM + y2*S, y2), (240, inner_apex_y), (vx - ARM - y2*S, y2),
            (vx - y2*S, y2), (240 + ty*S*0 + (H-ty)*S, ty), (240 - (H-ty)*S, ty)]
bh = (H - 2*GAP) / 3
i_blocks = [[(I_X, y), (W, y), (W, y+bh), (I_X, y+bh)] for y in (0, bh+GAP, 2*(bh+GAP))]

v_solid = [(0, 0), (ARM, 0), (240, inner_apex_y), (vx-ARM, 0), (vx, 0), (240+(H-ty)*S, ty), (240-(H-ty)*S, ty)]


def mark_paths(fg, accent=None, simple=False):
    if simple:
        return (f'<path fill="{fg}" d="{poly(v_solid)}"/>'
                f'<path fill="{accent or fg}" d="{poly([(I_X,0),(W,0),(W,H),(I_X,H)])}"/>')
    parts = [f'<path fill="{fg}" d="{poly(p)}"/>' for p in (v_left, v_right, v_bottom)]
    for k, b in enumerate(i_blocks):
        parts.append(f'<path fill="{accent if (accent and k == 0) else fg}" d="{poly(b)}"/>')
    return "".join(parts)

# ---------- Wordmark (outlined Montserrat Regular, tracked) ----------
font = TTFont(FONT)
gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
CAP = 40.0
scale = CAP / font["OS/2"].sCapHeight
TRACK = 0.24 * font["head"].unitsPerEm

def wordmark(text):
    pen = SVGPathPen(gs); x = 0.0; names = []
    for ch in text:
        g = cmap[ord(ch)]; names.append((g, x)); x += hmtx[g][0] + TRACK
    width = (x - TRACK) * scale
    for g, gx in names:
        tp = TransformPen(pen, (scale, 0, 0, -scale, gx*scale, CAP))
        gs[g].draw(tp)
    return pen.getCommands(), width

WM_D, WM_W = wordmark("VIEIRA CREATIONS")

def svg(w, h, body, bg=None, title="Vieira Creations"):
    bgr = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {f(h)}" '
            f'role="img" aria-label="{title}"><title>{title}</title>{bgr}{body}</svg>\n')

def full_logo(fg, bg=None, accent=None, pad=80):
    gap = 56
    w = max(W, WM_W) + 2*pad; h = H + gap + CAP + 2*pad
    mx, wx = (w - W)/2, (w - WM_W)/2
    body = (f'<g transform="translate({f(mx)},{f(pad)})">{mark_paths(fg, accent)}</g>'
            f'<path fill="{fg}" transform="translate({f(wx)},{f(pad+H+gap)})" d="{WM_D}"/>')
    return svg(w, h, body, bg)

def mark_only(fg, bg=None, accent=None, simple=False, pad=0, square=False):
    w, h = W + 2*pad, H + 2*pad
    if square:
        side = max(w, h); ox, oy = (side - W)/2, (side - H)/2; w = h = side
    else:
        ox, oy = pad, pad
    body = f'<g transform="translate({f(ox)},{f(oy)})">{mark_paths(fg, accent, simple)}</g>'
    return svg(w, h, body, bg, "VI — Vieira Creations")

files = {
    "vi-logo-ivory-on-black.svg": full_logo(IVORY, BLACK),
    "vi-logo-black-on-ivory.svg": full_logo(BLACK, IVORY),
    "vi-logo-rec-ivory-on-black.svg": full_logo(IVORY, BLACK, ORANGE),
    "vi-logo-ivory-transparent.svg": full_logo(IVORY),
    "vi-logo-black-transparent.svg": full_logo(BLACK),
    "vi-mark-ivory.svg": mark_only(IVORY),
    "vi-mark-black.svg": mark_only(BLACK),
    "vi-mark-rec-ivory.svg": mark_only(IVORY, accent=ORANGE),
    "vi-mark-rec-black.svg": mark_only(BLACK, accent=ORANGE),
    "vi-mark-small-ivory.svg": mark_only(IVORY, simple=True),
    "vi-mark-small-black.svg": mark_only(BLACK, simple=True),
    "vi-icon-black.svg": mark_only(IVORY, BLACK, accent=ORANGE, simple=True, pad=90, square=True),
    "vi-icon-ivory.svg": mark_only(BLACK, IVORY, accent=ORANGE, simple=True, pad=90, square=True),
}
for name, s in files.items():
    open(os.path.join(OUT, name), "w").write(s)
print(f"wordmark width {WM_W:.1f}, files {len(files)}")
