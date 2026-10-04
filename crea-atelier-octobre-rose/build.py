"""CRÉA x Octobre Rose — annonce atelier bijoux.
Écrit index.html (HyperFrames + GSAP). Tous les temps sont en temps du cut
(cut = source 1.80 -> 21.60 s). Méthode : guide de montage CRÉA v7."""
import json

TALK = 19.80                 # durée du face caméra (temps du cut)

# ---------------------------------------------------------------- respirations (v3)
# Intermèdes plein cadre entre les phrases : boutique + atelier, coupes calées sur les temps de la musique.
# (temps du cut où l'on s'arrête, [(plan, durée souhaitée, durée du fichier)]) — rien n'est coupé dans la voix.
GAPS_SPEC = [
    (5.24,  [("hindwork", 1.3, 1.7), ("tablewide", 1.0, 1.208)]),    # après « Seulement chez CRÉA ! » : Hind au travail, la table
    (12.49, [("tablehrt", 0.5, 1.0), ("rackfocus", 1.0, 1.417)]),   # après « … déjà fourni ! » : l'atelier en détail
]
# b-rolls atelier PENDANT la fin du discours (sa voix continue, pas de coupe) :
# de « les informations » jusqu'à juste avant « Marhba bikom » (temps du cut)
OVER_SPEC = (15.10, 18.66, [("table", 1.0, 2.5), ("teal", 1.3, 1.542)])
BEATS = json.load(open("beats.json"))["grid"]          # temps forts de la musique (déjà calée à 0:30)
FADE_IN, XFADE, FADE_OUT = 0.5, 0.45, 0.45            # fondus flous des intermèdes

def beat_after(t, lo, hi):
    """premier temps de la musique >= t, sans dépasser hi (sinon le dernier temps <= hi)"""
    ok = [b for b in BEATS if lo <= b <= hi]
    after = [b for b in ok if b >= t - 1e-6]
    return after[0] if after else (ok[-1] if ok else min(t, hi))

import subprocess, numpy as np
_raw = subprocess.run(["ffmpeg", "-v", "error", "-i", "assets/voice.wav", "-f", "f32le", "-ac", "1", "-ar", "8000", "-"],
                      capture_output=True, check=True).stdout
_v = np.frombuffer(_raw, np.float32)
_db = 20 * np.log10(np.sqrt(np.convolve(_v ** 2, np.ones(80) / 80, "same")) + 1e-9)

def voice_end(at):
    """fin du dernier mot avant le point de coupe (temps du cut)"""
    i = int(at * 8000); loud = np.where(_db[max(0, i - 8000):i] > -38)[0]
    return round((max(0, i - 8000) + loud[-1]) / 8000, 3) if len(loud) else at

# Chaque intermède : le milieu du fondu d'entrée tombe sur le 1er temps après la fin de la phrase,
# chaque coupe interne et le retour sur Hind tombent sur un temps.
GAPS, GAPLEN, INTER, shift = [], [], [], 0.0
for at, shots in GAPS_SPEC:
    start = at + shift                                   # point de coupe (temps final)
    ve = voice_end(at) + shift
    B = next(b for b in BEATS if b >= ve + 0.05)        # 1er temps après la phrase
    v0 = round(B - FADE_IN / 2, 3)                       # début du fondu d'entrée
    t = B; plan = []
    for i, (name, want, flen) in enumerate(shots):
        st = v0 if i == 0 else t
        margin = 0.05            # les fondus de sortie passent sur l'image figée en fin de fichier
        end = beat_after(t + want, t + min(0.6, want), st + flen - margin)
        plan.append((name, round(st, 3), round(end - st, 3))); t = end
    g = round(t - start, 3)
    GAPS.append((at, plan)); GAPLEN.append(g); shift += g
    INTER.append((v0, round(t - v0, 3), plan))

def q(t):
    """temps du cut -> temps de la vidéo finale (décalé par les intermèdes)"""
    return round(t + sum(g for (at, _), g in zip(GAPS, GAPLEN) if t >= at - 1e-6), 3)

SEGS = [0.0] + [at for at, _ in GAPS] + [TALK]    # morceaux du face caméra
VOICE_END = q(TALK)          # fin de la voix
# b-rolls plein cadre par-dessus la voix : fondu d'entrée centré sur un temps, coupes et sortie sur les temps
_a, _b, _shots = OVER_SPEC
_B = next(x for x in BEATS if x >= q(_a) + FADE_IN / 2)
_v0 = round(_B - FADE_IN / 2, 3); _t = _B; _plan = []
for i, (name, want, flen) in enumerate(_shots):
    st = _v0 if i == 0 else _t
    hi = min(st + flen - 0.05, q(_b) - FADE_OUT / 2)
    end = beat_after(_t + want, _t + min(0.6, want), hi)
    _plan.append((name, round(st, 3), round(end - st, 3))); _t = end
OVER = [(_v0, round(_t - _v0, 3), _plan)]
END = VOICE_END              # début de la fin B
DUR = round(END + 2.6, 2)    # + fin B

# ---------------------------------------------------------------- b-rolls
# (nom, fichier, début, fin) — plans consécutifs = une seule carte
CARDS = [
    [("pliers", 10.50, 11.55), ("beadbox", 11.55, 12.50)],   # « le matériel déjà fourni »
    [("tableside", 13.50, 14.85)],                           # « les créations tediwhom m3akom »
]

# ---------------------------------------------------------------- caméra
# visage (origine du zoom) par plan du cut, en px dans le cadre 1080x1920
FACE = {"A": "583px 648px", "B": "670px 713px", "C": "693px 551px",
        "D": "713px 616px", "E": "638px 745px", "F": "612px 583px"}
# (début, durée, plan, échelle de départ ou None = continuer, échelle d'arrivée, easing)
CAM = [
    (0.00, 0.80, "A", 1.12, 1.00, "power3.inOut"),   # ouverture : sort d'un flou zoomé
    (0.80, 1.155, "A", None, 1.04, "sine.inOut"),    # dérive
    (2.00, 0.80, "A", None, 1.18, "power2.inOut"),   # « Octobre Rose »
    (2.80, 0.685, "A", None, 1.20, "sine.inOut"),
    (3.53, 0.90, "B", 1.20, 1.10, "power2.inOut"),   # angle 3/4 : dézoom
    (4.43, 0.765, "B", None, 1.14, "sine.inOut"),    # vers « CRÉA »
    (5.24, 0.615, "C", 1.00, 1.03, "sine.inOut"),
    (5.90, 0.80, "C", None, 1.22, "power2.inOut"),   # « 50 % »
    (6.70, 3.035, "C", None, 1.25, "sine.inOut"),
    (9.78, 0.90, "D", 1.12, 1.02, "power2.inOut"),
    (10.68, 1.765, "D", None, 1.05, "sine.inOut"),
    (12.49, 0.85, "E", 1.14, 1.00, "power2.inOut"),  # retour après b-roll
    (13.34, 1.485, "E", None, 1.03, "sine.inOut"),
    (14.87, 0.85, "F", 1.14, 1.00, "power2.inOut"),  # retour après b-roll
    (15.72, 1.295, "F", None, 1.03, "sine.inOut"),
    (17.06, 0.80, "F", None, 1.22, "power2.inOut"),  # « Venez nombreux » (même plan, pas de coupe)
    (17.86, 1.94, "F", None, 1.25, "sine.inOut"),
]

# ---------------------------------------------------------------- sous-titres
# mot@temps · * = mot fort · | sépare les mots · une chaîne = une ligne
CAPS = [
    (0.02, 2.12, ["Un@0.08 | atelier@0.64 | de@0.96 | confection@1.16", "de@1.58 | *bijoux@1.80"], 1150, 70),
    (2.12, 3.62, ["pour@2.16", "*Octobre@2.42 | *Rose ?@2.84"], 1130, 84),
    (3.62, 4.18, ["Oui !@3.66"], 1150, 86),
    (4.18, 5.22, ["Seulement@4.22 | chez@4.52"], 1110, 73),
    (5.30, 6.24, ["W@5.36 | nzidolkom ?@5.44"], 1150, 79),
    (6.24, 7.62, ["*50 %@6.30", "des@6.98 | bénéfices@7.18"], 1170, 100),
    (7.62, 9.74, ["rayhin@7.64 | yroho@7.94 | l’les@8.20", "*associations@8.32 | concernées@8.74"], 1150, 66),
    (9.79, 10.52, ["W@9.80 | ma@9.86 | tkhmmouch,@9.98"], 1150, 73),
    (10.54, 12.46, ["parce que@10.56 | le@10.92 | *matériel@11.04", "déjà@11.62 | fourni !@11.86"], 300, 59),
    (12.50, 13.46, ["W@12.60 | nzidolkom :@12.70"], 1150, 79),
    (13.50, 14.82, ["les@13.54 | *créations@13.62", "tediwhom@14.05 | m3akom !@14.30"], 300, 64),
    (14.88, 16.26, ["Rah@15.00 | tl9aw@15.20 | ga3@15.40", "les@15.56 | informations@15.70"], 1150, 68),
    (16.26, 17.36, ["f la@16.30 | *description@16.46 | ↓@16.66"], 1150, 70),
    (17.40, 18.66, ["Venez@17.46 | nombreux@17.74", "et@17.94 | *nombreuses !@18.10"], 1130, 73),
    (18.70, 19.70, ["*Marhba@18.75 | *bikom !@19.30"], 1150, 86),
]
HOOK_LOGO = 4.68                       # le logo entre au milieu de « Seulement chez … »

# ---------------------------------------------------------------- verre
# (forme, x, y, w, h, entrée, sortie, dérive x, dérive y)
GLASS = [
    ("disc", 40, 1420, 230, 230, 0.55, 3.45, 40, -30),
    ("capsule", 690, 1640, 420, 158, 0.85, 3.45, -50, -20),
    ("disc", 840, 1400, 200, 200, 5.45, 9.65, -30, -40),
    ("capsule", -60, 1620, 420, 158, 5.70, 9.65, 60, -25),
    ("disc", 830, 1440, 220, 220, 15.05, 19.60, -40, -30),
    ("capsule", -40, 1650, 400, 150, 17.20, 19.60, 50, -20),
]
SWEEPS = [10.50, 13.50, 14.86]   # balayage : entrées/sorties de carte + fin (temps du cut)

# ---------------------------------------------------------------- traits de lumière
PATHS = {
    "high": "M 1100 250 C 820 330, 420 170, -20 290",
    "side": "M 1010 1480 C 1070 1150, 950 820, 1030 420",
    "low": "M -20 1560 C 300 1470, 720 1650, 1100 1520",
    "logoL": "M 330 1300 L 90 1300",
    "logoR": "M 750 1300 L 990 1300",
    "card": "M 150 700 L 150 520 Q 150 445 225 445 L 520 445",
}
# (tracé, début, durée du tracé, durée du retrait, tenue avant retrait)
ARCS = [("high", 0.35, 1.3, 0.8, 0.35), ("logoL", HOOK_LOGO + 0.04, 0.4, 0.35, -0.12), ("logoR", HOOK_LOGO + 0.04, 0.4, 0.35, -0.12),
        ("side", 5.60, 1.4, 0.9, 0.35), ("card", 10.95, 0.9, 0.4, 0.2), ("low", 15.10, 1.4, 0.9, 0.35), ("high", 17.30, 1.3, 0.8, 0.3)]

# ---------------------------------------------------------------- passage en temps final
def shift_line(line):
    out = []
    for tok in line.split("|"):
        w, t = tok.strip().rsplit("@", 1)
        out.append(f"{w}@{q(float(t))}")
    return " | ".join(out)

_cards = []
for card in CARDS:
    nc = [[n, q(a), round(q(a) + (b - a), 3)] for n, a, b in card]
    hit = [k for k, (at, _) in enumerate(GAPS_SPEC) if abs(at - card[-1][2]) < 0.1]
    into = bool(hit)
    if into:
        nc[-1][2] = round(INTER[hit[0]][0] + FADE_IN + 0.05, 3)   # reste sous le fondu de l'intermède
    _cards.append({"shots": nc, "into": into})
CARDS = _cards
CAM = [(q(t), d, p, s0, s1, e) for t, d, p, s0, s1, e in CAM]
CAPS = [(q(a), q(a) + (b - a), [shift_line(l) for l in lines], y, sz) for a, b, lines, y, sz in CAPS]
GLASS = [(sh, x, y, w, h, q(a), q(a) + (b - a), dx, dy) for sh, x, y, w, h, a, b, dx, dy in GLASS]
SWEEPS = [q(t) for t in SWEEPS]
ARCS = [(k, q(t), d, r, hold) for k, t, d, r, hold in ARCS]
# intermèdes en temps final : (début, [(plan, début, durée)])
# morceaux du face caméra : (début final, durée, début dans talk.mp4)
TALKSEG = []
for i in range(len(SEGS) - 1):
    a, b = SEGS[i], SEGS[i + 1]
    if i == len(SEGS) - 2:
        d = b - a + 0.95                                          # passe sous la fin B
    else:                                                         # image figée jusqu'à ce que l'intermède couvre tout
        d = max(b - a, INTER[i][0] + FADE_IN + 0.05 - q(a))
    TALKSEG.append((q(a), round(d, 3), i))

# ---------------------------------------------------------------- SFX (pour mix.py)
CUES = [("whoosh", 0.00, -12), ("whoosh", HOOK_LOGO - 0.12, -12), ("pop", q(6.28), -11), ("pop", q(11.02), -13),
        ("sideswoosh", q(11.45), -13), ("pop", q(13.60), -13), ("tik", q(16.70), -12), ("tik", q(16.98), -14),
        ("pop", q(18.73), -12), ("riser", END - 0.85, -14), ("boom", END + 0.35, -10), ("shutter", END + 1.15, -13)]
CUES += [("whoosh", t - 0.36, -14) for t in SWEEPS]
CUES += [("sideswoosh", t0 - 0.05, -18) for t0, g, _ in INTER + OVER]          # entrée douce des intermèdes
json.dump({"cues": CUES, "dur": DUR, "end": END,
           "voice": [(a, round(b - a, 3), q(a)) for a, b in zip(SEGS[:-1], SEGS[1:])],
           "gaps": [(t0, g) for t0, g, _ in INTER]}, open("cues.json", "w"), indent=1)

# ================================================================= HTML
def media_for_cards():
    bg, inner = [], []
    for ci, cd in enumerate(CARDS):
        card = cd["shots"]
        for name, a, b in card:
            d = round(b - a + (0.30 if [name, a, b] == card[-1] else 0.25), 2)   # marge pour la sortie
            bg.append(f'<div class="bgb" id="bg-{name}"><video id="vb-{name}" class="clip" src="assets/shots/{name}.mp4" '
                      f'data-start="{a}" data-duration="{d}" data-media-start="0" muted playsinline></video></div>')
            inner.append(f'<div class="card-media" id="cm-{name}" style="opacity:0"><video id="vc-{name}" class="clip" '
                         f'src="assets/shots/{name}.mp4" data-start="{a}" data-duration="{d}" data-media-start="0" muted playsinline></video></div>')
    return "\n    ".join(bg), "\n        ".join(inner)

def lens_filters():
    sizes = {(g[0], g[3], g[4]) for g in GLASS} | {("capsule", 1600, 380), ("disc", 300, 300)}
    out = []
    for shape, w, h in sorted(sizes):
        out.append(f'<filter id="lf-{shape}-{w}x{h}" x="0" y="0" width="{w}" height="{h}" filterUnits="userSpaceOnUse" '
                   f'color-interpolation-filters="sRGB"><feImage href="assets/lens-{shape}.png" x="0" y="0" width="{w}" height="{h}" '
                   f'preserveAspectRatio="none" result="m"/><feDisplacementMap in="SourceGraphic" in2="m" scale="{int(min(w, h) * 0.32)}" '
                   f'xChannelSelector="R" yChannelSelector="G"/></filter>')
    return "\n      ".join(out)

def glass_div(gid, shape, x, y, w, h, extra=""):
    r = h / 2 if shape == "capsule" else w / 2
    return (f'<div class="glass" id="{gid}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{r}px;'
            f'backdrop-filter:url(#lf-{shape}-{w}x{h}) blur(1.5px);-webkit-backdrop-filter:url(#lf-{shape}-{w}x{h}) blur(1.5px);{extra}"></div>')

def caps_html():
    out = []
    for i, (a, b, lines, y, size) in enumerate(CAPS):
        ls = []
        for line in lines:
            ws = []
            for tok in [t.strip() for t in line.split("|")]:
                word, t = tok.rsplit("@", 1)
                strong = word.startswith("*"); word = word.lstrip("*")
                if word == "↓":
                    ws.append(f'<svg class="arrow" data-t="{t}" viewBox="0 0 30 40"><path d="M15 3 V33 M4 22 L15 35 L26 22" '
                              f'stroke="#D9A441" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
                else:
                    ws.append(f'<span class="w{" s" if strong else ""}" data-t="{t}">{word}</span>')
            ls.append(f'<div class="line">{"".join(ws)}</div>')
        out.append(f'<div class="cap" id="cap{i}" data-a="{a}" data-b="{b}" style="top:{y}px;font-size:{size}px">{"".join(ls)}</div>')
    return "\n    ".join(out)

def frise(y, fid):
    # frise inspirée du « I » du logo : points or + chevrons terracotta
    items, x, k = [], 10, 0
    while x < 750:
        if k % 2 == 0:
            items.append(f'<circle cx="{x}" cy="17" r="6" fill="#D9A441"/>')
        else:
            items.append(f'<path d="M{x-8} 9 L{x} 21 L{x+8} 9" stroke="#944826" stroke-width="4" fill="none" stroke-linejoin="round"/>')
        x += 26; k += 1
    return f'<svg class="frise" id="{fid}" style="top:{y}px" viewBox="0 0 760 34">{"".join(items)}</svg>'

MOTIF = ('<svg id="motif" viewBox="0 0 1080 2100"><defs><pattern id="los" width="120" height="120" patternUnits="userSpaceOnUse">'
         '<path d="M60 8 L112 60 L60 112 L8 60 Z" fill="none" stroke="#944826" stroke-width="5"/>'
         '<path d="M60 38 L82 60 L60 82 L38 60 Z" fill="#944826"/></pattern></defs>'
         '<rect width="1080" height="2100" fill="url(#los)"/></svg>')

SLOGAN = "".join(f'<span>{c if c != " " else "&nbsp;"}</span>' for c in "Osez l’unique, osez ") + \
         "".join(f'<span class="g">{c}</span>' for c in "CRÉA")

bg_html, card_html = media_for_cards()
talk_html = "\n      ".join(
    f'<video id="talk{i}" class="clip talk" src="assets/talk_s{m}.mp4" data-start="{a}" data-duration="{d}" data-media-start="0" muted playsinline></video>'
    for i, (a, d, m) in enumerate(TALKSEG))
inter_html = "\n      ".join(
    f'<div class="ish" id="ish-{n}"><video id="vi-{n}" class="clip" src="assets/shots/{n}.mp4" data-start="{t}" '
    f'data-duration="{round(d + FADE_OUT + 0.05, 3)}" data-media-start="0" muted playsinline></video></div>'
    for _, _, lst in INTER + OVER for n, t, d in lst)
glass_html = "\n    ".join(glass_div(f"g{i}", s, x, y, w, h) for i, (s, x, y, w, h, *_ ) in enumerate(GLASS))
sweep_html = "\n    ".join(glass_div(f"sw{i}", "capsule", -260, 2000, 1600, 380, "transform:rotate(-14deg);") for i in range(len(SWEEPS)))
strokes_html = "\n      ".join(
    f'<g id="arc{i}" opacity="0"><path class="st-halo" d="{PATHS[k]}" pathLength="1000"/>'
    f'<path class="st-core" d="{PATHS[k]}" pathLength="1000"/><path class="st-head" d="{PATHS[k]}" pathLength="1000"/></g>'
    for i, (k, *_ ) in enumerate(ARCS))

CFG = dict(OVER=OVER, FADE_IN=FADE_IN, XFADE=XFADE, FADE_OUT=FADE_OUT, INTER=INTER, CARDS=CARDS, FACE=FACE, CAM=CAM, GLASS=GLASS, SWEEPS=SWEEPS, ARCS=ARCS, HOOK_LOGO=HOOK_LOGO, END=END, DUR=DUR)

html = f"""<!doctype html>
<html lang="fr" data-resolution="portrait">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=1080, height=1920" />
  <script src="assets/gsap.min.js"></script>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
    <svg width="0" height="0" style="position:absolute"><defs>
      {lens_filters()}
    </defs></svg>

    <div id="camw"><div id="cam">
      {talk_html}
    </div></div>

    {bg_html}

    {glass_html}

    <div id="card"><div class="card-rim"><div class="card-in">
        {card_html}
        <div class="card-sheen"></div><div class="card-gloss" id="gloss"></div>
    </div></div></div>

    <div id="inter">
      {inter_html}
    </div>

    <svg id="strokes" viewBox="0 0 1080 1920">
      {strokes_html}
    </svg>

    {caps_html()}
    <img id="hooklogo" src="assets/logo/logo-bleu-crop.png" alt="CRÉA" />

    <div id="end">
      {MOTIF}
      <div id="endblock">
        {frise(345, "friseT")}
        {frise(1235, "friseB")}
        <div id="endlogo"><img src="assets/logo/logo-bleu-crop.png" alt="CRÉA by Hind" /></div>
        <div id="endshine"><div></div></div>
        <div class="filet" id="filetL"></div><div class="filet" id="filetR"></div>
        <div id="slogan">{SLOGAN}</div>
        <div id="endsub">ATELIER BIJOUX · OCTOBRE ROSE</div>
        <div id="endcta"><svg viewBox="0 0 30 40"><path d="M15 3 V33 M4 22 L15 35 L26 22" stroke="#944826" stroke-width="5"
          fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg><span>INFOS EN DESCRIPTION</span></div>
      </div>
      {glass_div("endlens", "disc", 60, 470, 300, 300, "opacity:0;")}
    </div>

    {sweep_html}
  </div>

  <script>
  const C = {json.dumps(CFG)};
  const tl = gsap.timeline({{ paused: true }});

  // ---------------- caméra : zooms lissés, jamais de saut dans un plan
  let curPlan = null;
  C.CAM.forEach(([t, d, plan, s0, s1, ease]) => {{
    if (plan !== curPlan) {{ tl.set("#cam", {{ transformOrigin: C.FACE[plan] }}, t); curPlan = plan; }}
    if (s0 !== null) tl.fromTo("#cam", {{ scale: s0 }}, {{ scale: s1, duration: d, ease, immediateRender: false }}, t);
    else tl.to("#cam", {{ scale: s1, duration: d, ease }}, t);
  }});
  tl.fromTo("#camw", {{ filter: "blur(16px)", scale: 1.06 }}, {{ filter: "blur(0px)", scale: 1, duration: 0.8, ease: "power3.inOut" }}, 0);
  tl.to("#camw", {{ filter: "blur(18px)", scale: 1.06, duration: 0.45, ease: "power2.inOut" }}, C.END - 0.25);

  // ---------------- intermèdes déco : fondu flou à l'entrée, poussée lente, fondu flou à la sortie
  C.INTER.concat(C.OVER).forEach(([t0, g, shots], k) => {{
    shots.forEach(([n, t, d], i) => {{
      const id = "#ish-" + n;
      tl.fromTo(id, {{ opacity: 0, filter: "blur(14px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: i ? C.XFADE : C.FADE_IN, ease: "sine.inOut", immediateRender: false }}, i ? t - C.XFADE / 2 : t);
      tl.fromTo(id + " video", {{ scale: 1.0 }}, {{ scale: 1.05, duration: d + C.FADE_OUT, ease: "sine.inOut", immediateRender: false }}, t);
      if (i === shots.length - 1) tl.to(id, {{ opacity: 0, filter: "blur(14px)", duration: C.FADE_OUT, ease: "sine.inOut" }}, t0 + g);
      else tl.set(id, {{ opacity: 0 }}, t + d + C.XFADE / 2 + 0.02);
    }});
  }});

  // ---------------- cartes de verre
  C.CARDS.forEach(cd => {{
    const card = cd.shots, into = cd.into;
    const a = card[0][1], b = card[card.length - 1][2];
    tl.set("#card", {{ opacity: 1 }}, a);
    tl.fromTo("#card", {{ y: 420, scale: 0.9, rotation: -3 }}, {{ y: 0, scale: 1, rotation: 0, duration: 0.8, ease: "power3.inOut", immediateRender: false }}, a);
    if (!into) tl.to("#card", {{ y: 520, rotation: 3, duration: 0.34, ease: "power2.inOut" }}, b - 0.34);
    tl.set("#card", {{ opacity: 0, y: 0, rotation: 0 }}, b);
    card.forEach(([name, s, e], i) => {{
      tl.set("#cm-" + name, {{ opacity: 1 }}, s);
      tl.fromTo("#cm-" + name, {{ scale: 1.0 }}, {{ scale: 1.05, duration: e - s + 0.25, ease: "sine.inOut", immediateRender: false }}, s);
      if (i > 0) {{   // changement de plan dans la carte : flou + reflet
        tl.fromTo("#cm-" + name, {{ filter: "blur(16px)" }}, {{ filter: "blur(0px)", duration: 0.3, ease: "power2.out", immediateRender: false }}, s);
        tl.fromTo("#gloss", {{ xPercent: -200 }}, {{ xPercent: 260, duration: 0.6, ease: "power2.inOut", immediateRender: false }}, s - 0.1);
      }}
      if (i < card.length - 1) tl.set("#cm-" + name, {{ opacity: 0 }}, e + 0.02);
      else tl.set("#cm-" + name, {{ opacity: 0 }}, e);
      // fond : le même plan flouté, plein cadre
      tl.fromTo("#bg-" + name, {{ opacity: 0 }}, {{ opacity: 1, duration: i ? 0.2 : 0.4, ease: "power2.out", immediateRender: false }}, s);
      if (i < card.length - 1) tl.to("#bg-" + name, {{ opacity: 0, duration: 0.2, ease: "power2.inOut" }}, e);
      else if (into) tl.set("#bg-" + name, {{ opacity: 0 }}, e);
      else tl.to("#bg-" + name, {{ opacity: 0, duration: 0.34, ease: "power2.inOut" }}, e - 0.34);
    }});
    tl.fromTo("#gloss", {{ xPercent: -200 }}, {{ xPercent: 260, duration: 0.8, ease: "power2.inOut", immediateRender: false }}, a + 0.45);
  }});

  // ---------------- verre liquide
  C.GLASS.forEach(([shape, x, y, w, h, a, b, dx, dy], i) => {{
    const id = "#g" + i;
    tl.fromTo(id, {{ opacity: 0, scale: 0.6, filter: "blur(10px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.6, ease: "power3.out", immediateRender: false }}, a);
    tl.fromTo(id, {{ x: 0, y: 0 }}, {{ x: dx, y: dy, duration: b - a, ease: "sine.inOut", immediateRender: false }}, a);
    tl.to(id, {{ opacity: 0, scale: 0.85, duration: 0.25, ease: "power2.in" }}, b - 0.25);
  }});
  C.SWEEPS.forEach((t, i) => {{
    const id = "#sw" + i;
    tl.set(id, {{ opacity: 1 }}, t - 0.375);
    tl.fromTo(id, {{ y: 300 }}, {{ y: -2700, duration: 0.75, ease: "power2.inOut", immediateRender: false }}, t - 0.375);
    tl.set(id, {{ opacity: 0 }}, t + 0.375);
  }});

  // ---------------- traits de lumière (comète, tracé et retrait en power4.inOut)
  C.ARCS.forEach(([k, t, d, r, hold], i) => {{
    const g = "#arc" + i;
    tl.set(g, {{ opacity: 1 }}, t);
    tl.fromTo(g + " .st-halo, " + g + " .st-core", {{ strokeDasharray: "1000 1000", strokeDashoffset: 1000 }},
              {{ strokeDashoffset: 0, duration: d, ease: "power4.inOut", immediateRender: false }}, t);
    tl.fromTo(g + " .st-head", {{ strokeDasharray: "45 2000", strokeDashoffset: 45, opacity: 1 }},
              {{ strokeDashoffset: -955, duration: d, ease: "power4.inOut", immediateRender: false }}, t);
    tl.to(g + " .st-head", {{ opacity: 0, duration: 0.2 }}, t + d - 0.1);
    tl.to(g + " .st-halo, " + g + " .st-core", {{ strokeDashoffset: -1000, duration: r, ease: "power4.inOut" }}, t + d + hold);
    tl.set(g, {{ opacity: 0 }}, t + d + hold + r);
  }});

  // ---------------- sous-titres mot à mot
  document.querySelectorAll(".cap").forEach(cap => {{
    const a = +cap.dataset.a, b = +cap.dataset.b;
    tl.set(cap, {{ opacity: 1, y: 0, filter: "blur(0px)" }}, a);
    cap.querySelectorAll("[data-t]").forEach(w => {{
      const t = Math.max(a, +w.dataset.t - 0.04);
      tl.fromTo(w, {{ opacity: 0, y: 22, scale: 1.08, filter: "blur(14px)" }},
                {{ opacity: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 0.45, ease: "power3.out", immediateRender: false }}, t);
      if (w.classList.contains("arrow")) {{
        tl.fromTo(w, {{ y: -26 }}, {{ y: 0, duration: 0.4, ease: "back.out(2.5)", immediateRender: false }}, t);
        tl.to(w, {{ y: 10, duration: 0.14, ease: "power1.out", yoyo: true, repeat: 3 }}, t + 0.3);
      }}
    }});
    tl.to(cap, {{ y: -14, opacity: 0, filter: "blur(10px)", duration: 0.28, ease: "power2.in" }}, b - 0.28);
  }});

  // ---------------- hook : logo officiel
  tl.fromTo("#hooklogo", {{ opacity: 0, scale: 1.3, filter: "blur(22px)" }},
            {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.34, ease: "expo.out", immediateRender: false }}, C.HOOK_LOGO);
  
  tl.to("#hooklogo", {{ opacity: 0, y: -14, filter: "blur(10px)", duration: 0.2, ease: "power2.in" }}, 5.04);

  // ---------------- fin B : fond crème, logo, slogan
  const E = C.END;
  tl.fromTo("#end", {{ clipPath: "circle(0% at 50% 50%)" }}, {{ clipPath: "circle(80% at 50% 50%)", duration: 0.8, ease: "power3.inOut", immediateRender: false }}, E + 0.05);
  tl.fromTo("#motif", {{ y: 0 }}, {{ y: -60, duration: DUR_END = 2.55, ease: "none", immediateRender: false }}, E + 0.05);
  tl.fromTo("#friseT, #friseB", {{ opacity: 0, scaleX: 0.4 }}, {{ opacity: 1, scaleX: 1, duration: 0.7, ease: "power3.inOut", immediateRender: false }}, E + 0.45);
  tl.fromTo("#endlogo", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 1.1, ease: "power3.inOut", immediateRender: false }}, E + 0.35);
  tl.set("#endlens", {{ opacity: 1 }}, E + 0.35);
  tl.fromTo("#endlens", {{ x: -40 }}, {{ x: 700, duration: 1.1, ease: "power3.inOut", immediateRender: false }}, E + 0.35);
  tl.to("#endlens", {{ opacity: 0, duration: 0.25 }}, E + 1.3);
  tl.fromTo("#endshine div", {{ x: 0 }}, {{ x: 1400, duration: 0.9, ease: "power2.inOut", immediateRender: false }}, E + 1.1);
  tl.to("#filetL, #filetR", {{ scaleX: 1, duration: 0.7, ease: "power3.inOut" }}, E + 1.0);
  document.querySelectorAll("#slogan span").forEach((s, i) =>
    tl.fromTo(s, {{ opacity: 0, y: 14, filter: "blur(8px)" }}, {{ opacity: 1, y: 0, filter: "blur(0px)", duration: 0.3, ease: "power3.out", immediateRender: false }}, E + 1.05 + i * 0.03));
  tl.fromTo("#endsub", {{ opacity: 0, y: 12 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "power3.out", immediateRender: false }}, E + 1.75);
  tl.fromTo("#endcta", {{ opacity: 0, y: 12 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "power3.out", immediateRender: false }}, E + 1.95);
  tl.to("#endcta svg", {{ y: 9, duration: 0.15, ease: "power1.out", yoyo: true, repeat: 3 }}, E + 2.1);
  tl.fromTo("#endblock", {{ scale: 1 }}, {{ scale: 1.035, duration: 2.55, ease: "sine.inOut", immediateRender: false }}, E + 0.05);

  tl.set({{}}, {{}}, C.DUR);
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;
  tl.seek(0);
  </script>
</body>
</html>
"""
html = html.replace("duration: DUR_END = 2.55", "duration: 2.55")
open("index.html", "w").write(html)
print("index.html written · DUR", DUR)
