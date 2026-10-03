"""CRÉA x Octobre Rose - annonce atelier bijoux. Frame-by-frame compositor.
Source talk is kept continuous (orig 1.80 -> 21.60), b-rolls replace picture only."""
import subprocess, numpy as np, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 24
SRC = "video.mov"
T0, TEND = 1.80, 21.60          # talk window in source
OUTRO = 2.6
TALK = TEND - T0
TOTAL = TALK + OUTRO
N = round(TOTAL * FPS)

NAVY = (0, 47, 108); CREAM = (244, 227, 193); GOLD = (217, 164, 65)
TERRA = (148, 72, 38); PINK = (229, 80, 140)
F_SANS = "fonts/Figtree.ttf"; F_SERIF = "fonts/Playfair.ttf"; F_ITAL = "fonts/PlayfairItalic.ttf"

def font(path, size, var):
    f = ImageFont.truetype(path, size); f.set_variation_by_name(var); return f

# ---------------- edit decisions (times in SOURCE seconds) ----------------
# punch-in scale over the talking-head, instantaneous on the cut / on the key word
SCALE = [(1.80, 1.00), (4.22, 1.10), (5.33, 1.00), (6.02, 1.08), (7.04, 1.00),
         (8.08, 1.12), (9.98, 1.04), (11.58, 1.00), (14.29, 1.08), (16.67, 1.00),
         (19.20, 1.10), (20.50, 1.00)]
# b-roll inserts: (orig_start, orig_end, broll_source_start)
BROLL = [(3.60, 4.22, 30.80),    # "de bijoux"            -> teal beads macro
         (12.70, 14.25, 24.35),  # "le matériel déjà fourni" -> pink pliers on cork
         (15.45, 16.50, 25.99),  # "les créations"        -> bead box
         (17.30, 18.75, 33.96)]  # "les informations"     -> wide workshop table
# captions: (start, end, [(word, accent)])
CAPS = [
    (1.86, 2.96, [("Un", 0), ("atelier", 0)]),
    (2.96, 3.60, [("de", 0), ("confection", 0)]),
    (3.60, 4.22, [("de", 0), ("bijoux", 0)]),
    (4.22, 5.40, [("pour", 0), ("Octobre", 1), ("Rose", 1), ("?", 0)]),
    (5.40, 6.02, [("Oui !", 0)]),
    (6.02, 7.08, [("Seulement", 0), ("chez", 0), ("CRÉA", 1), ("!", 0)]),
    (7.08, 8.08, [("W", 0), ("nzidolkom ?", 0)]),
    (9.44, 9.98, [("rayhin", 0), ("yroho", 0)]),
    (9.98, 11.50, [("l'les", 0), ("associations", 1)]),
    (11.58, 12.40, [("W", 0), ("ma", 0), ("tkhmmouch,", 0)]),
    (12.40, 13.36, [("le", 0), ("matériel", 0)]),
    (13.36, 14.29, [("déjà", 0), ("fourni", 1), ("!", 0)]),
    (14.36, 15.30, [("W", 0), ("nzidolkom :", 0)]),
    (15.30, 16.00, [("les", 0), ("créations", 1)]),
    (16.00, 16.70, [("tediwhom", 0), ("m3akom !", 0)]),
    (16.76, 17.50, [("Rah", 0), ("tl9aw", 0), ("ga3", 0)]),
    (17.50, 18.10, [("les", 0), ("informations", 0)]),
    (18.10, 18.90, [("f", 0), ("la", 0), ("description", 1)]),
    (19.20, 19.86, [("Venez", 0), ("nombreux", 0)]),
    (19.86, 20.50, [("et", 0), ("nombreuses", 1), ("!", 0)]),
    (20.50, 21.60, [("Marhba", 0), ("bikom", 1), ("!", 0)]),
]
G50 = (8.08, 11.58)  # big "50%" graphic

# ---------------- helpers ----------------
def ease_out_back(x, s=1.7):
    x = min(max(x, 0), 1) - 1; return 1 + x * x * ((s + 1) * x + s)

def ease_out(x):
    x = min(max(x, 0), 1); return 1 - (1 - x) ** 3

def scale_at(o):
    s = 1.0
    for t, v in SCALE:
        if o >= t: s = v
    return s

def punch(img, s, cy=760):
    if s == 1.0: return img
    w, h = W / s, H / s
    x0 = 540 - w / 2; y0 = min(max(cy - h / 2 * (cy / 960), 0), H - h)
    return img.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + w, y0 + h))

def read_frames(start, n):
    p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-i", SRC, "-frames:v", str(n),
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True)
    a = np.frombuffer(p.stdout, np.uint8).reshape(-1, H, W, 3)
    return [Image.fromarray(f) for f in a]

def text_layer(words, size, prog):
    """Render one caption card: Figtree ExtraBold, cream, navy stroke, pink accent; pop-in."""
    f = font(F_SANS, size, b"ExtraBold")
    sp = size * 0.28; stroke = max(6, size // 10)
    widths = [f.getlength(w) for w, _ in words]
    tw = sum(widths) + sp * (len(words) - 1)
    lay = Image.new("RGBA", (int(tw + 4 * stroke + 40), int(size * 1.6 + 4 * stroke)), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay); x = 2 * stroke + 20; y = 2 * stroke
    for (w, acc), ww in zip(words, widths):
        d.text((x, y), w, font=f, fill=PINK if acc else CREAM, stroke_width=stroke, stroke_fill=NAVY)
        x += ww + sp
    shadow = Image.new("RGBA", lay.size, (0, 0, 0, 0))
    shadow.paste((0, 20, 50, 140), mask=lay.split()[3].filter(ImageFilter.GaussianBlur(10)))
    out = Image.alpha_composite(shadow, lay)
    k = 0.78 + 0.22 * ease_out_back(prog)
    if k != 1: out = out.resize((max(1, int(out.width * k)), max(1, int(out.height * k))), Image.LANCZOS)
    return out

def paste_center(base, layer, cx, cy, alpha=1.0):
    if alpha < 1:
        a = layer.split()[3].point(lambda v: int(v * alpha)); layer = layer.copy(); layer.putalpha(a)
    base.alpha_composite(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)))

def fit_width(layer, maxw):
    if layer.width <= maxw: return layer
    k = maxw / layer.width
    return layer.resize((int(layer.width * k), int(layer.height * k)), Image.LANCZOS)

# ---------------- static assets ----------------
logo = Image.open("../src/logo-octobre-rose-creme.png").convert("RGBA")
logo = logo.crop(logo.getbbox())
_ls = logo.resize((250, int(250 * logo.height / logo.width)), Image.LANCZOS)
logo_small = Image.new("RGBA", (_ls.width + 56, _ls.height + 36), (0, 0, 0, 0))
ImageDraw.Draw(logo_small).rounded_rectangle((0, 0, logo_small.width - 1, logo_small.height - 1), radius=28, fill=NAVY + (215,))
logo_small.alpha_composite(_ls, (28, 18))

def motif_bg():
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((x - 540) / 900) ** 2 + ((y - 820) / 1300) ** 2)
    c0 = np.array([12, 66, 140], np.float32); c1 = np.array([0, 28, 70], np.float32)
    t = np.clip(r, 0, 1)[..., None]
    img = Image.fromarray((c0 * (1 - t) + c1 * t).astype(np.uint8)).convert("RGBA")
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov); step = 90; s = 20
    for j in range(-1, H // step + 2):
        for i in range(-1, W // step + 2):
            cx = i * step + (step // 2 if j % 2 else 0); cy = j * step
            d.polygon([(cx, cy - s), (cx + s, cy), (cx, cy + s), (cx - s, cy)], outline=(120, 160, 220, 38), width=2)
    return Image.alpha_composite(img, ov)
BG = motif_bg()

def g50_layer(prog, sub_prog):
    big = font(F_SERIF, 330, b"Black")
    lay = Image.new("RGBA", (W, 620), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.text((W / 2, 230), "50%", font=big, anchor="mm", fill=CREAM, stroke_width=14, stroke_fill=NAVY)
    sh = Image.new("RGBA", lay.size, (0, 0, 0, 0))
    sh.paste((0, 20, 50, 150), mask=lay.split()[3].filter(ImageFilter.GaussianBlur(16)))
    lay = Image.alpha_composite(sh, lay)
    # pill subtitle
    sf = font(F_SANS, 50, b"Bold"); txt = "des bénéfices aux associations"
    tw = sf.getlength(txt); pw, ph = tw + 70, 92
    pill = Image.new("RGBA", (int(pw), ph), (0, 0, 0, 0)); pd = ImageDraw.Draw(pill)
    pd.rounded_rectangle((0, 0, pw - 1, ph - 1), radius=46, fill=PINK + (255,))
    pd.text((pw / 2, ph / 2), txt, font=sf, anchor="mm", fill=(255, 255, 255))
    a = pill.split()[3].point(lambda v: int(v * ease_out(sub_prog))); pill.putalpha(a)
    lay.alpha_composite(pill, (int((W - pw) / 2), 450 + int(20 * (1 - ease_out(sub_prog)))))
    k = 0.6 + 0.4 * ease_out_back(prog)
    return lay.resize((int(W * k), int(620 * k)), Image.LANCZOS)

# ---------------- render ----------------
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                        "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-profile:v", "high", "-preset", "medium",
                        "-crf", "16", "-pix_fmt", "yuv420p", "video_only.mp4"], stdin=subprocess.PIPE)

talk = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", f"{T0:.3f}", "-i", SRC, "-f", "rawvideo",
                         "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
broll_cache = {}

for i in range(N):
    t = i / FPS
    if t < TALK:
        raw = talk.stdout.read(W * H * 3)
        frame = Image.frombuffer("RGB", (W, H), raw)
        o = T0 + t
        br = next((b for b in BROLL if b[0] <= o < b[1]), None)
        if br:
            if br not in broll_cache:
                broll_cache.clear(); broll_cache[br] = read_frames(br[2], math.ceil((br[1] - br[0]) * FPS) + 2)
            fr = broll_cache[br]; frame = fr[min(int(round((o - br[0]) * FPS)), len(fr) - 1)]
        else:
            frame = punch(frame, scale_at(o))
        img = frame.convert("RGBA")
        # discreet brand mark, top safe area
        paste_center(img, logo_small, W / 2, 250, 0.92)
        # 50% graphic
        if G50[0] <= o < G50[1]:
            p = (o - G50[0]) / 0.35; sp = (o - G50[0] - 0.25) / 0.35
            out_a = 1 - ease_out((o - (G50[1] - 0.15)) / 0.15) if o > G50[1] - 0.15 else 1
            paste_center(img, g50_layer(p, sp), W / 2, 700, out_a)
        # captions
        cap = next((c for c in CAPS if c[0] <= o < c[1]), None)
        if cap:
            lay = fit_width(text_layer(cap[2], 92, (o - cap[0]) / 0.18), W * 0.84)
            paste_center(img, lay, W / 2 - 20, H * 0.66)
        out = img.convert("RGB")
    else:
        to = t - TALK
        img = BG.copy()
        lp = ease_out_back(to / 0.45, 1.2)
        lw = int(820 * (0.85 + 0.15 * lp)); lg = logo.resize((lw, int(lw * logo.height / logo.width)), Image.LANCZOS)
        paste_center(img, lg, W / 2, 820, min(1, to / 0.25))
        sl = font(F_ITAL, 76, b"SemiBold Italic")
        a = ease_out((to - 0.5) / 0.4)
        lay = Image.new("RGBA", (W, 200), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        d.text((W / 2, 100), "Osez l'unique, osez CRÉA", font=sl, anchor="mm", fill=CREAM)
        paste_center(img, lay, W / 2, 1230 + 25 * (1 - a), a)
        a2 = ease_out((to - 0.9) / 0.4)
        lay2 = Image.new("RGBA", (W, 120), (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay2)
        d2.text((W / 2, 60), "ATELIER BIJOUX  ·  OCTOBRE ROSE", font=font(F_SANS, 40, b"Bold"), anchor="mm", fill=GOLD)
        paste_center(img, lay2, W / 2, 1360, a2)
        out = img.convert("RGB")
    enc.stdin.write(out.tobytes())
    if i % 48 == 0: print(f"{i}/{N}", flush=True)

talk.kill(); enc.stdin.close(); enc.wait()
print("done", N)
