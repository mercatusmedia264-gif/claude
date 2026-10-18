import re, html, sys, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.html")

SLIDES = [
    (10, "Heckscher-Ohlin theory", "≈ 1 min 15", [
        "Thank you, Norhane.",
        "Ricardo says countries trade because they have different technology. But <q>why are countries different in the first place?</q>",
        "Two Swedish economists gave an answer: **Eli Heckscher** in 1919, and **Bertil Ohlin** in 1933.",
        "Their idea is about **factor endowments**. This simply means what a country has: workers, money and machines, which we call capital, and land.",
        "Some countries have many workers. Others have a lot of capital. Others have a lot of land.",
        "The rule is simple: a country **sells** what it can make with what it has a lot of. And it **buys** what needs what it lacks.",
        "Two examples. **Bangladesh** has many workers, so it exports textiles. **Germany** has a lot of capital, so it exports machines.",
        "But in **1953**, Wassily Leontief tested this idea on the United States. The US has more capital than any other country, so it should export capital-intensive goods. But he found the opposite: US exports needed more workers than its imports.",
        "This is called the **Leontief paradox**. It showed that the theory was not enough, so economists looked for new answers.",
    ]),
    (11, "New Trade Theory", "≈ 1 min 15", [
        "One new answer came from **Paul Krugman**, in the late 1970s and early 1980s. He won the **Nobel Prize** in Economics in 2008 for this work.",
        "Krugman noticed something strange: most trade happens **between similar countries, selling similar products**. For example, France sells cars to Germany, and Germany sells cars to France. The old theories cannot explain this.",
        "Krugman explains it with three ideas.",
        "<n>1</n> **Economies of scale.** The more a company produces, the cheaper each product becomes. So production is done in a few places and sold to the whole world.",
        "<n>2</n> **Imperfect competition.** In real life, a few big companies control most markets.",
        "<n>3</n> **Product variety.** People like to have choice. So countries buy and sell different versions of the same product. This is called intra-industry trade.",
        "What does this mean for governments? Sometimes, it can make sense for the state to **support important industries**.",
    ]),
    (12, "Inequalities between countries", "≈ 1 min", [
        "All these theories say that trade is good for everyone. But in reality, **not everyone gains the same**.",
        "<n>1</n> Many poor countries sell **raw materials**, and their prices go up and down a lot. **Algeria** is a good example with oil and gas. Rich countries, on the other hand, sell expensive manufactured goods.",
        "<n>2</n> This makes poor countries **dependent and fragile**. When oil prices fell in 2014, oil-exporting countries suffered a lot.",
        "<n>3</n> Even inside one country, there are **winners and losers**. Consumers and exporters usually win. But some workers lose their jobs because of cheaper imports.",
        "<n>4</n> This is why people still debate **free trade versus protectionism**.",
    ]),
    (13, "Global value chains & multinationals", "≈ 1 min 15", [
        "Today, there is another reality the old theories don't fully explain: **global value chains**.",
        "This means one product is made in many countries, step by step: design, parts, assembly, marketing and services. Remember the **smartphone** from our introduction: designed in California, assembled in China, with a chip from Taiwan.",
        "So today, countries don't only trade finished products. **They trade steps of production.**",
        "These chains are organized by **multinational companies**, which work in many countries. They invest abroad and bring money, technology and know-how.",
        "<g>+</g> **The good side:** lower costs, new technology and new jobs in the host countries.",
        "<b>−</b> **The bad side:** countries depend on a few suppliers. One problem can block everything, like the supply chain crisis of **2020 and 2021**. And the most profitable steps, like design and branding, stay mostly in rich countries.",
        "So the old theories, made for trade in finished goods, only explain part of this reality.",
    ]),
    (14, "Conclusion", "≈ 1 min", [
        "To conclude, trade theories changed as the world changed.",
        "<t>**Mercantilism**|trade is a zero-sum game, and wealth is gold.</t>",
        "<t>**Smith & Ricardo**|countries should specialize, and everyone can gain.</t>",
        "<t>**Heckscher & Ohlin**|countries trade based on what they have.</t>",
        "<t>**Krugman**|economies of scale, big companies and product variety.</t>",
        "Each theory fixes the weaknesses of the one before. But **no theory explains everything**. Today, with global value chains, inequalities and protectionism, the debate is still open.",
        "So, our answer to the problématique: theories explain **why countries trade**, but we must also look at **the real world economy** to fully understand it.",
    ]),
    (15, "Thank you", "≈ 10 s", [
        "Thank you for your attention.",
        "Norhane and I are happy to answer your questions.",
    ]),
]


def fmt(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"<n>(.+?)</n>", r'<span class="n">\1</span>', s)
    s = re.sub(r"<g>(.+?)</g>", r'<span class="n plus">\1</span>', s)
    s = re.sub(r"<b>(.+?)</b>", r'<span class="n minus">\1</span>', s)
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
        foot = '<div class="next end"><span class="lbl">End</span><span class="nt">Questions — answer together with Norhane</span></div>'
    pages.append(f"""
<section class="page">
  <header>
    <div class="meta">
      <div class="who">Wassim · Speaker notes</div>
      <div class="num">Slide {num}<span>/15</span></div>
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
<html lang="en"><head><meta charset="utf-8"><title>Wassim — Speaker notes</title>
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
