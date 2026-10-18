"""CRÉA x Octobre Rose — témoignage d'une participante à l'atelier bijoux.
Écrit index.html (HyperFrames + GSAP). Un seul plan face caméra (déjà monté par le client),
pas de musique. Méthode et style : guide de montage CRÉA v7 / reel annonce atelier."""
import json

TALK = 37.37                 # durée du témoignage
END = 36.95                  # début de la fin B (juste après « Merci »)
DUR = round(END + 2.6, 2)
FADE_IN, XFADE, FADE_OUT = 0.5, 0.45, 0.45
GAPS_SPEC, INTER, OVER = [], [], []           # pas d'intermède : la voix reste continue
def q(t): return round(t, 3)                  # temps source = temps final
SEGS = [0.0, TALK]

# ---------------------------------------------------------------- b-rolls (atelier, 1re vidéo) en cartes de verre
CARDS = [
    [("pliers", 15.70, 16.90), ("beadbox", 16.90, 18.10),        # « créer un bijou à notre choix »
     ("teal", 18.10, 19.30), ("rackfocus", 19.30, 20.40)],       # « il y avait beaucoup de choix, c'était sympathique »
    [("tablewide", 23.00, 24.15), ("table", 24.15, 26.80),       # « l'ambiance très conviviale … des rencontres »
     ("hindwork", 26.80, 29.10)],                                # « et surtout Hind qui est magnifique »
]

# ---------------------------------------------------------------- caméra (un seul plan ; échelle posée sur chaque jump cut)
FACE = {"A": "500px 640px"}
CAM = [
    (0.00, 0.80, "A", 1.12, 1.00, "power3.inOut"),
    (0.80, 6.985, "A", None, 1.05, "sine.inOut"),
    (7.83, 1.955, "A", 1.10, 1.13, "sine.inOut"),
    (9.83, 0.80, "A", 1.00, 1.15, "power2.inOut"),     # « Octobre Rose »
    (10.63, 0.925, "A", None, 1.17, "sine.inOut"),
    (11.60, 1.255, "A", 1.06, 1.09, "sine.inOut"),
    (12.90, 1.955, "A", 1.00, 1.04, "sine.inOut"),
    (14.90, 7.425, "A", 1.10, 1.14, "sine.inOut"),
    (22.37, 6.785, "A", 1.00, 1.05, "sine.inOut"),
    (29.20, 0.55, "A", 1.08, 1.09, "sine.inOut"),
    (29.76, 0.80, "A", None, 1.20, "power2.inOut"),    # « très très bon moment »
    (30.56, 1.995, "A", None, 1.22, "sine.inOut"),
    (32.60, 1.685, "A", 1.00, 1.04, "sine.inOut"),     # insert : sa création
    (34.33, 0.65, "A", 1.06, 1.07, "sine.inOut"),
    (35.00, 0.80, "A", None, 1.18, "power2.inOut"),    # « bonne cause »
    (35.80, 0.455, "A", None, 1.19, "sine.inOut"),
    (36.30, 0.60, "A", 1.00, 1.04, "sine.inOut"),
]

# ---------------------------------------------------------------- sous-titres (mot@temps · * = mot fort)
CAPS = [
    (0.02, 3.10, ["Je@0.00 | viens@0.12 | de@0.30 | terminer@0.50", "l’atelier@0.80"], 1030, 68),
    (3.20, 5.46, ["un@3.34 | atelier@3.56 | qui a@3.98 | beaucoup@4.26", "de@4.48 | *sens@4.64 | pour nous@4.94"], 1150, 62),
    (5.46, 7.00, ["parce que@5.50 | c’est@6.04", "une@6.52 | *cause@6.84"], 1150, 72),
    (7.00, 9.40, ["qu’on doit@7.04 | être@7.74", "*présente@8.16 | pour@8.70"], 1150, 68),
    (9.60, 11.30, ["C’est@9.66", "*Octobre@9.86 | *Rose@10.34"], 1130, 84),
    (11.40, 12.86, ["donc@11.50 | on@11.78 | porte@12.00", "du@12.22 | *rose@12.44"], 1150, 74),
    (12.90, 15.62, ["L’atelier@12.96 | nous a@13.38 | permis@13.78", "*justement@14.02 | de@14.70"], 1150, 62),
    (15.70, 18.06, ["*créer@15.82 | un@16.08 | *bijou@16.40", "à notre@17.14 | choix@17.76"], 300, 62),
    (18.10, 20.36, ["Il y avait@18.16 | beaucoup@18.44 | de@18.76 | *choix,@18.98", "c’était@19.14 | sympathique@19.42"], 300, 54),
    (20.42, 22.50, ["et c’était@20.58 | *magnifique@20.88", "et de@21.34 | *qualité@21.64 | aussi@22.00"], 1150, 62),
    (22.56, 24.90, ["En plus,@22.58 | l’ambiance@23.02", "très@23.60 | *conviviale,@23.98"], 300, 60),
    (24.92, 26.82, ["*magnifique@24.98 | et on a@25.30", "fait des@25.80 | *rencontres@26.06"], 300, 58),
    (26.86, 29.06, ["Et surtout@26.92 | *Hind@27.48", "qui est@27.90 | *magnifique@28.44"], 300, 64),
    (29.08, 31.36, ["*Vraiment,@29.08 | j’ai passé@29.54", "un très très@29.90 | bon@30.48 | *moment@30.60"], 1150, 62),
    (31.40, 32.58, ["Ma@31.48 | *création@31.62", "est@32.08 | là@32.42"], 1150, 74),
    (34.40, 36.32, ["Et c’est pour@34.84 | la@35.30", "*bonne@35.44 | *cause@35.62 | en plus@35.88"], 1150, 66),
    (36.34, 36.95, ["*Merci@36.42"], 1150, 100),
]
HOOK_LOGO, HOOK_OUT = 1.56, 2.92        # le logo officiel remplace « Créa by Hind »

# ---------------------------------------------------------------- verre (bas de l'image, jamais sur le visage ni sous une carte)
GLASS = [
    ("disc", 40, 1420, 230, 230, 0.55, 5.40, 40, -30),
    ("capsule", 690, 1640, 420, 158, 0.85, 5.40, -50, -20),
    ("disc", 840, 1400, 200, 200, 9.90, 14.60, -30, -40),
    ("capsule", -60, 1620, 420, 158, 10.20, 14.60, 60, -25),
    ("disc", 830, 1440, 220, 220, 29.30, 32.40, -40, -30),
    ("capsule", -40, 1650, 400, 150, 34.50, 36.80, 50, -20),
]
SWEEPS = [15.70, 20.40, 23.00, 29.10]

PATHS = {
    "high": "M 1100 250 C 820 330, 420 170, -20 290",
    "side": "M 1010 1480 C 1070 1150, 950 820, 1030 420",
    "low": "M -20 1560 C 300 1470, 720 1650, 1100 1520",
    "logoL": "M 330 1300 L 90 1300",
    "logoR": "M 750 1300 L 990 1300",
    "card": "M 150 700 L 150 520 Q 150 445 225 445 L 520 445",
}
ARCS = [("high", 0.35, 1.3, 0.8, 0.3), ("logoL", HOOK_LOGO + 0.04, 0.4, 0.35, 0.3), ("logoR", HOOK_LOGO + 0.04, 0.4, 0.35, 0.3),
        ("side", 9.90, 1.4, 0.9, 0.35), ("card", 16.15, 0.9, 0.4, 0.4), ("card", 23.45, 0.9, 0.4, 0.4),
        ("low", 29.30, 1.4, 0.9, 0.35), ("high", 34.60, 1.3, 0.8, 0.3)]

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

# ---------------------------------------------------------------- SFX (discrets, pas de musique)
CUES = [("whoosh", 0.00, -15), ("whoosh", HOOK_LOGO - 0.12, -15), ("pop", 9.84, -15), ("pop", 16.38, -16),
        ("pop", 27.46, -15), ("pop", 36.40, -15),
        ("riser", END - 0.85, -17), ("boom", END + 0.35, -13), ("shutter", END + 1.15, -16)]
CUES += [("sideswoosh", t, -18) for t in (16.90, 18.10, 19.30, 24.15, 26.80)]
CUES += [("whoosh", t - 0.36, -16) for t in SWEEPS]
json.dump({"cues": CUES, "dur": DUR, "end": END, "voice": [(0.0, TALK, 0.0)], "gaps": []}, open("cues.json", "w"), indent=1)

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

CFG = dict(HOOK_OUT=HOOK_OUT, OVER=OVER, FADE_IN=FADE_IN, XFADE=XFADE, FADE_OUT=FADE_OUT, INTER=INTER, CARDS=CARDS, FACE=FACE, CAM=CAM, GLASS=GLASS, SWEEPS=SWEEPS, ARCS=ARCS, HOOK_LOGO=HOOK_LOGO, END=END, DUR=DUR)

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
  
  tl.to("#hooklogo", {{ opacity: 0, y: -14, filter: "blur(10px)", duration: 0.2, ease: "power2.in" }}, C.HOOK_OUT);

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
