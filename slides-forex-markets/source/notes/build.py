import re, html, sys, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.html")

from slides_data import SLIDES, TOTAL, HEADER, END_NEXT


def fmt(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"<n>(.+?)</n>", r'<span class="n">\1</span>', s)
    s = re.sub(r"<g>(.+?)</g>", r'<span class="n plus">\1</span>', s)
    s = re.sub(r"<b>(.+?)</b>", r'<span class="n minus">\1</span>', s)
    s = re.sub(r"<b2>(.+?)</b2>", r"<strong>\1</strong>", s)
    s = s.replace("<q>", "“").replace("</q>", "”")
    return s


def chunk(s):
    m = re.fullmatch(r"<t>(.+?)\|(.+?)</t>", s)
    if m:
        return f'<div class="tl"><div class="k">{fmt(m.group(1))}</div><div class="v">{fmt(m.group(2))}</div></div>'
    cls = "c lead" if s == SLIDES[0][3][0] else "c"
    return f'<p class="{cls}">{fmt(s)}</p>'


pages = []
for i, (num, title, dur, chunks) in enumerate(SLIDES):
    nxt = SLIDES[i + 1] if i + 1 < len(SLIDES) else None
    body = "\n".join(chunk(c) for c in chunks)
    if nxt:
        first = re.sub(r"<[^>]+>|\*\*", "", nxt[3][0])
        first = first if len(first) < 70 else first[:first.rfind(" ", 0, 68)] + "…"
        foot = f'<div class="next"><span class="lbl">Next ▸ Slide {nxt[0]}</span><span class="nt">{nxt[1]}</span><span class="cue">“{html.escape(first)}”</span></div>'
    else:
        foot = f'<div class="next"><span class="lbl">Next ▸ Slide {END_NEXT[0]}</span><span class="nt">{END_NEXT[1]}</span><span class="cue">“{END_NEXT[2]}”</span></div>'
    pages.append(f"""
<section class="page">
  <header>
    <div class="meta">
      <div class="who">{HEADER}</div>
      <div class="num">Slide {num}<span>/{TOTAL}</span></div>
      <h1>{title}</h1>
      <div class="dur">{dur}</div>
    </div>
    <img class="thumb" src="thumbs/s{num}.jpg" alt="">
  </header>
  <main>
{body}
  </main>
  {foot}
</section>""")

doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Wassim — Forex speaker notes</title>
<link rel="stylesheet" href="fonts/fonts.css">
<style>
@page {{ size: A4; margin: 0; }}
:root {{ --navy:#1a2b78; --mag:#b3155f; --cyan:#a6e3fa; --ink:#14193a; --muted:#5d6588; --line:#dde2f0; --soft:#f1f4fb; --hl:#fde7f0; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:'DM Sans',Inter,sans-serif; color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
.page {{ width:210mm; height:297mm; padding:13mm 15mm 12mm; display:flex; flex-direction:column; break-after:page; position:relative; overflow:hidden; }}
.page:last-child {{ break-after:auto; }}
.page::before {{ content:""; position:absolute; left:0; top:0; bottom:0; width:5mm; background:var(--navy); }}
header {{ display:flex; gap:7mm; align-items:center; padding-bottom:6mm; border-bottom:2px solid var(--line); margin-bottom:6mm; }}
.meta {{ flex:1; }}
.who {{ font-size:10.5pt; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--mag); }}
.num {{ font-family:'Lora',serif; font-weight:700; font-size:40pt; line-height:1; color:var(--navy); margin-top:2mm; }}
.num span {{ font-size:16pt; color:var(--muted); font-weight:500; margin-left:2px; }}
h1 {{ font-family:'Lora',serif; font-weight:600; font-size:20pt; line-height:1.15; color:var(--navy); margin-top:2mm; }}
.dur {{ display:inline-block; margin-top:3mm; font-size:11pt; font-weight:600; color:var(--muted); background:var(--soft); padding:1mm 3mm; border-radius:99px; }}
.thumb {{ width:72mm; border-radius:2mm; box-shadow:0 0 0 1px var(--line), 0 4px 14px rgba(26,43,120,.15); }}
main {{ flex:1; display:flex; flex-direction:column; gap:var(--gap,4.2mm); }}
p.c {{ font-size:var(--fs,17pt); line-height:1.42; padding-left:5mm; border-left:3px solid var(--line); }}
p.c.lead {{ font-family:'Lora',serif; font-style:italic; font-size:var(--fs,17pt); color:var(--navy); border-left-color:var(--mag); }}
strong {{ font-weight:700; color:var(--navy); background:var(--hl); padding:0 .5mm; border-radius:1mm; box-decoration-break:clone; -webkit-box-decoration-break:clone; }}
.n {{ display:inline-grid; place-items:center; width:8mm; height:8mm; border-radius:50%; background:var(--mag); color:#fff; font-weight:700; font-size:13pt; margin-right:2mm; vertical-align:1px; }}
.n.plus {{ background:#2f55c8; }}
.n.minus {{ background:var(--mag); }}
.tl {{ display:grid; grid-template-columns:62mm 1fr; gap:4mm; align-items:baseline; font-size:var(--fs,17pt); line-height:1.38; padding:2.6mm 0 2.6mm 5mm; border-left:3px solid var(--mag); background:var(--soft); border-radius:0 2mm 2mm 0; }}
.tl .k strong {{ background:none; padding:0; }}
.next {{ margin-top:5mm; display:grid; grid-template-columns:auto 1fr; column-gap:4mm; row-gap:1mm; align-items:baseline; background:var(--navy); color:#fff; border-radius:3mm; padding:4mm 5mm; }}
.next .lbl {{ font-size:10.5pt; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--cyan); white-space:nowrap; }}
.next .nt {{ font-family:'Lora',serif; font-size:15pt; font-weight:600; }}
.next .cue {{ grid-column:2; font-size:12pt; color:rgba(255,255,255,.75); font-style:italic; }}
.next.end {{ background:var(--mag); }}
.next.end .lbl {{ color:#fff; }}
</style></head><body>
{''.join(pages)}
</body></html>"""
open(OUT, "w").write(doc)
print(OUT)
