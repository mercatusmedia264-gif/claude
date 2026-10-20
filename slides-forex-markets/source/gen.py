"""Builds the Foreign Exchange Markets deck (fx.html) in the same design system as the first deck."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "..", "..", "slides-relations-economiques", "source", "slides.html")
src = open(BASE).read()
base_css = src[src.index("<style>") + 7: src.index("</style>")]
base_syms = src[src.index("<defs>") + 6: src.index("</defs>")]

TOTAL = 23
N, W, A, K = "Norhane Benazala", "Wassim Sid", "Adam Sam", "Kamil Mohamed Ounis"

EXTRA_SYMS = """
<symbol id="i-plane" viewBox="0 0 24 24"><path d="M10.5 13.5L3 11l1.5-1.5 8 .5 4.5-4.5c1-1 2.6-1.2 3.2-.6s.4 2.2-.6 3.2L15 12.5l.5 8L14 22l-2.5-7.5L8 18v3l-1.5 1L5 18l-4-1.5L2 15h3z"/></symbol>
<symbol id="i-send" viewBox="0 0 24 24"><circle cx="7" cy="7" r="3"/><path d="M2 20c.5-3.5 2.5-5.5 5-5.5M13 13h8M18 10l3 3-3 3M13 19h8"/></symbol>
<symbol id="i-trend" viewBox="0 0 24 24"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></symbol>
<symbol id="i-bank" viewBox="0 0 24 24"><path d="M3 9.5L12 4l9 5.5M4.5 10v8M9.5 10v8M14.5 10v8M19.5 10v8M3 20.5h18"/></symbol>
<symbol id="i-building" viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h1.5M13.5 7H15M9 11h1.5M13.5 11H15M9 15h1.5M13.5 15H15M10.5 21v-3h3v3"/></symbol>
<symbol id="i-case" viewBox="0 0 24 24"><rect x="3" y="7.5" width="18" height="12.5" rx="2"/><path d="M9 7.5V5.5a1.5 1.5 0 011.5-1.5h3A1.5 1.5 0 0115 5.5v2M3 13h18"/></symbol>
<symbol id="i-pie" viewBox="0 0 24 24"><path d="M12 3a9 9 0 109 9h-9z"/><path d="M15 3.5A9 9 0 0120.5 9H15z"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M9 16l2.5-3 2 1.5L16 11M11 19h2"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
<symbol id="i-net" viewBox="0 0 24 24"><circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="18" r="2.5"/><circle cx="19" cy="18" r="2.5"/><path d="M10.8 7.2L6.2 15.8M13.2 7.2l4.6 8.6M7.5 18h9"/></symbol>
<symbol id="i-drop" viewBox="0 0 24 24"><path d="M12 3s6.5 7 6.5 11.5a6.5 6.5 0 01-13 0C5.5 10 12 3 12 3z"/></symbol>
<symbol id="i-lock" viewBox="0 0 24 24"><rect x="4.5" y="10.5" width="15" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 018 0v3M12 14.5v2.5"/></symbol>
<symbol id="i-cal" viewBox="0 0 24 24"><rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/></symbol>
<symbol id="i-swap" viewBox="0 0 24 24"><path d="M4 8h14l-3-3M20 16H6l3 3"/></symbol>
<symbol id="i-key" viewBox="0 0 24 24"><circle cx="8" cy="15" r="4.5"/><path d="M11.2 11.8L20 3M16.5 6.5l2.5 2.5M14 9l2 2"/></symbol>
<symbol id="i-up" viewBox="0 0 24 24"><path d="M12 20V5M6 11l6-6 6 6"/></symbol>
<symbol id="i-down" viewBox="0 0 24 24"><path d="M12 4v15M6 13l6 6 6-6"/></symbol>
<symbol id="i-cart" viewBox="0 0 24 24"><path d="M3 4h2.5l2.2 11h10.6L20.5 8H6.6"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/></symbol>
<symbol id="i-ship" viewBox="0 0 24 24"><path d="M3 15l2 5h14l2-5zM6 15V9h12v6M9 9V5h6v4"/></symbol>
"""

EXTRA_CSS = """
.pager i { width: 12px; height: 12px; }
.badge-part { position:absolute; z-index:6; background:var(--mag); color:#fff; padding:14px 26px; border-radius:0 0 10px 10px; top:0; font-size:15px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
.badge-part b { display:block; font-family:'Lora',serif; font-size:24px; letter-spacing:0; text-transform:none; font-weight:600; }
.key { position:absolute; left:120px; right:120px; bottom:96px; background:var(--mag); color:#fff; border-radius:10px; padding:18px 28px; font-size:21px; display:flex; gap:20px; align-items:center; z-index:4; }
.key .k { font-size:15px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; white-space:nowrap; opacity:.9; }
.card { background:#fff; border:1.5px solid var(--line); border-radius:14px; padding:26px 28px; }
.card h3 { font-size:26px; margin-bottom:8px; }
.card p { font-size:19px; color:var(--muted); line-height:1.45; }
.fic { width:56px; height:56px; border-radius:50%; background:var(--navy); color:#fff; display:grid; place-items:center; margin-bottom:14px; }
.fic.m { background:var(--mag); }
.fic.s { background:var(--soft); color:var(--navy); }
.lead { font-size:23px; color:var(--muted); }
.lead b { color:var(--ink); }
.big { font-family:'Lora',serif; font-weight:600; color:var(--navy); line-height:1; }
.qcard { background:var(--mag); color:#fff; border-radius:14px; padding:40px 48px; }
.qcard .q { font-family:'Lora',serif; font-style:italic; font-weight:500; font-size:30px; line-height:1.4; }
.qcard .by { margin-top:16px; font-size:18px; letter-spacing:.04em; color:rgba(255,255,255,.85); }
.qcard .ic { width:50px; height:50px; color:rgba(255,255,255,.5); }
.on-dark .card { background:rgba(255,255,255,.08); border-color:rgba(255,255,255,.22); }
.on-dark .card h3 { color:#fff; }
.on-dark .card p { color:rgba(255,255,255,.8); }
.calc { display:grid; grid-template-columns:1fr auto; align-items:baseline; gap:6px 24px; padding:16px 0; border-top:1.5px solid var(--line); }
.calc .l { font-size:20px; color:var(--muted); }
.calc .l b { color:var(--navy); }
.calc .v { font-family:'Lora',serif; font-weight:600; font-size:34px; color:var(--ink); text-align:right; }
"""

ICON = lambda i, cls="ic": f'<svg class="{cls}"><use href="#i-{i}"/></svg>'


def brand():
    return f'<div class="brand"><span class="logo">{ICON("globe")}</span>International Financial Markets</div>'


def pager(sec, dark=False):
    dots = "".join(f'<i class="{"on" if k == sec else ""}"></i>' for k in range(6))
    p = f'<div class="pager">{dots}</div>'
    return f'<div class="on-dark">{p}</div>' if dark else p


def foot(n, who=None, style=""):
    w = f'<span class="who">{who}</span>' if who else "<span></span>"
    return f'<div class="foot" style="{style}">{w}<span>{n:02d} / {TOTAL}</span></div>'


def eyebrow(t, light=False):
    return f'<div class="eyebrow{" light" if light else ""}">{t}</div>'


def bars(style):
    return f'<div class="bars" style="{style}"><i></i><i></i><i></i></div>'


S = []

# 1 · TITLE
S.append(f"""
<section class="slide on-dark" style="background:var(--navy)">
  <div class="photo" style="inset:0;background-image:url(img/cover.jpg)"></div>
  <div class="abs" style="inset:0;background:linear-gradient(90deg,rgba(26,43,120,.97) 0%,rgba(26,43,120,.86) 45%,rgba(26,43,120,.2) 100%)"></div>
  {brand()}{pager(0)}
  <div class="abs" style="left:120px;top:250px;width:1180px">
    {eyebrow("Course · International Financial Markets", True)}
    <h1 style="font-size:100px;color:#fff;line-height:1.05">Foreign Exchange Markets</h1>
    <p class="serif" style="font-size:52px;color:var(--cyan);font-weight:500;margin-top:14px">The price of money</p>
    <div style="display:flex;gap:22px;margin-top:56px;align-items:center">
      <span style="background:var(--mag);color:#fff;padding:18px 38px;border-radius:8px;font-size:22px;font-weight:600">International Financial Markets</span>
    </div>
  </div>
  <div class="abs" style="right:120px;bottom:130px;width:540px;background:rgba(20,33,96,.9);border:1px solid rgba(255,255,255,.25);border-radius:16px;padding:28px 34px;color:#fff">
    <div style="font-size:16px;letter-spacing:.18em;text-transform:uppercase;color:var(--cyan);font-weight:700;margin-bottom:16px">Presented by</div>
    {"".join(f'<div style="display:flex;align-items:center;gap:16px;margin-top:12px"><span style="width:50px;height:50px;border-radius:50%;background:{bg};color:{fg};display:grid;place-items:center;font-weight:700;font-size:17px">{ini}</span><span style="font-size:24px;font-family:Lora,serif;font-weight:600">{nm}</span></div>' for ini, nm, bg, fg in [("NB", N, "var(--mag)", "#fff"), ("WS", W, "#fff", "var(--navy)"), ("KO", K, "var(--blue-2)", "#fff"), ("AS", A, "var(--cyan)", "var(--navy)")])}
  </div>
  {bars("right:0;bottom:0")}
</section>""")

# 2 · PLAN
rows = [("00", "Introduction", ""), ("I", "Understanding the forex market", "Norhane"), ("II", "How currencies are traded", "Wassim"),
        ("III", "What moves exchange rates", "Kamil"), ("IV", "Risks and real-world impact", "Adam"), ("—", "Conclusion", "")]
S.append(f"""
<section class="slide">
  <div class="abs" style="left:0;top:0;width:700px;height:1080px;background:var(--navy)"></div>
  <div class="on-dark">{brand()}</div>
  <div class="photo" style="left:72px;top:170px;width:560px;height:740px;border-radius:6px;background-image:url(img/plan.jpg)"></div>
  {bars("left:72px;top:910px")}
  {pager(0)}
  <div class="abs" style="left:820px;top:140px;width:1000px">
    {eyebrow("Agenda")}
    <h2 style="font-size:84px;margin-bottom:40px">Plan</h2>
    {"".join(f'<div class="plan-row"><span class="num">{n}</span><span>{"<small>Part " + n + "</small>" if n in ("I","II","III","IV") else ""}{t}</span>{f"<span class=chip>{w}</span>" if w else "<span></span>"}</div>' for n, t, w in rows)}
  </div>
  <style>
    .plan-row {{ display:grid; grid-template-columns:92px 1fr auto; align-items:center; gap:10px; padding:20px 0; border-bottom:1.5px solid var(--line); font-size:29px; }}
    .plan-row:first-of-type {{ border-top:1.5px solid var(--line); }}
    .plan-row .num {{ font-size:32px; color:var(--mag); }}
    .plan-row small {{ display:block; font-size:15px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--muted); margin-bottom:2px; }}
    .plan-row .chip {{ font-size:17px; color:var(--muted); }}
  </style>
  <div class="foot right-only"><span>02 / {TOTAL}</span></div>
</section>""")

# 3 · INTRODUCTION
S.append(f"""
<section class="slide">
  {brand()}
  <div class="photo" style="left:1240px;top:0;width:680px;height:1080px;background-image:url(img/intro.jpg)"></div>
  {pager(0, True)}
  <div class="abs" style="left:120px;top:150px;width:1100px">
    {eyebrow("Introduction")}
    <div class="qcard" style="padding:36px 44px;margin-bottom:40px">
      {ICON("quote")}
      <p class="q" style="font-size:40px">The dollar is our currency, but it’s your problem.</p>
      <p class="by">— John Connally, US Treasury Secretary, to European finance ministers, 1971</p>
    </div>
    <p class="serif" style="font-size:34px;color:var(--navy);font-weight:600;line-height:1.3">A decision taken in Washington can change the price of bread in Algiers.</p>
    <div class="flow">
      <div class="fb"><span class="k">Algeria sells</span><b>Oil &amp; gas</b><span class="cur">in US dollars</span></div>
      {ICON("swap", "ic ar")}
      <div class="fb m"><span class="k">Algeria buys</span><b>Most imports</b><span class="cur">in euros</span></div>
      <div class="hits"><span class="k">Every move between them hits</span><span class="chip">the state budget</span><span class="chip">company costs</span><span class="chip">household purchasing power</span></div>
    </div>
    <p class="lead" style="margin-top:26px">Every day, <b>trillions of dollars</b> change hands to make this possible. Yet most people never see this market.</p>
  </div>
  <style>
    .flow {{ display:grid; grid-template-columns:auto auto auto; justify-content:start; align-items:center; gap:18px 22px; margin-top:28px; }}
    .flow .fb {{ background:var(--navy); color:#fff; border-radius:12px; padding:16px 26px; display:flex; flex-direction:column; min-width:260px; }}
    .flow .fb.m {{ background:var(--mag); }}
    .flow .fb .k {{ font-size:14px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; opacity:.8; }}
    .flow .fb b {{ font-family:'Lora',serif; font-size:30px; font-weight:600; }}
    .flow .fb .cur {{ font-size:19px; opacity:.9; }}
    .flow .ar {{ width:40px; height:40px; color:var(--blue-2); }}
    .flow .hits {{ grid-column:1/-1; display:flex; gap:12px; align-items:center; flex-wrap:wrap; }}
    .flow .hits .k {{ font-size:15px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--mag); margin-right:6px; }}
  </style>
  {bars("right:0;bottom:0")}
  {foot(3)}
</section>""")

# 4 · PROBLÉMATIQUE
parts = [("I", "Understanding the forex market"), ("II", "How currencies are traded"), ("III", "What moves exchange rates"), ("IV", "Risks and real-world impact")]
S.append(f"""
<section class="slide">
  {brand()}
  <div class="photo" style="left:540px;top:0;width:1380px;height:820px;background-image:url(img/prob.jpg)"></div>
  {bars("right:0;top:808px")}
  {pager(0, True)}
  <div class="abs on-dark" style="left:120px;top:290px;width:1300px;background:rgba(26,43,120,.95);padding:60px 70px 64px;color:#fff">
    {eyebrow("Problématique")}
    <h2 style="color:#fff;font-size:52px;line-height:1.22">How are exchange rates determined, what makes them change, and what risks do they create for economies, companies, and individuals?</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:34px;margin-top:44px">
      {"".join(f'<div><div class="num" style="font-size:44px;line-height:1;color:var(--cyan)">{n}</div><div style="font-size:21px;font-weight:600;margin-top:10px;line-height:1.3">{t}</div></div>' for n, t in parts)}
    </div>
  </div>
  {foot(4)}
</section>""")

# 5 · DEFINITION (Part I)
reasons = [("ship", "Trade in goods and services"), ("factory", "Foreign investment"), ("plane", "Tourism"), ("send", "Migrant remittances"), ("trend", "Speculation")]
S.append(f"""
<section class="slide on-dark">
  <div class="abs" style="left:0;top:0;width:1920px;height:560px;background:var(--mag)"></div>
  <div class="photo" style="left:1260px;top:0;width:660px;height:560px;background-image:url(img/def.jpg)"></div>
  <div class="abs" style="left:1260px;top:0;width:660px;height:560px;background:linear-gradient(90deg,var(--mag) 0%,rgba(179,21,95,0) 50%)"></div>
  {brand()}{pager(1)}
  <div class="badge-part" style="left:720px">Part I<b>{N}</b></div>
  <div class="abs" style="left:120px;top:170px;width:1100px;color:#fff">
    {eyebrow("Part I · Understanding the forex market", False).replace('class="eyebrow"', 'class="eyebrow" style="color:#fff"')}
    <h2 style="color:#fff;font-size:60px;margin-bottom:22px">What is the forex market?</h2>
    <p style="font-size:25px;color:rgba(255,255,255,.95)">The <b>foreign exchange market</b> (forex or FX) is the global market where currencies are bought and sold.</p>
    <p style="font-size:25px;color:rgba(255,255,255,.95);margin-top:14px">Its main function: to set the <b>exchange rate</b>, the price of one currency expressed in another.</p>
  </div>
  <div class="abs" style="left:120px;top:590px;font-size:17px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--navy)">Why it exists · international operations need currency conversion</div>
  <div class="abs" style="left:120px;top:640px;width:1680px;display:grid;grid-template-columns:repeat(5,1fr);gap:24px">
    {"".join(f'<div class="card" style="box-shadow:0 18px 50px rgba(26,43,120,.12);background:#fff;border-color:var(--line);height:250px;display:flex;flex-direction:column;justify-content:space-between;padding:32px 30px"><span class="fic" style="width:68px;height:68px">{ICON(i)}</span><h3 style="color:var(--navy);font-size:28px;margin:0">{t}</h3></div>' for i, t in reasons)}
  </div>
  {foot(5, N, "color:var(--muted)")}
</section>""")

# 6 · HISTORY
hist = [("1944", "Bretton Woods", "Currencies are pegged to the US dollar; the dollar is convertible into gold at $35 per ounce."),
        ("1971", "Nixon Shock", "The US ends the dollar’s convertibility into gold: Bretton Woods collapses."),
        ("1976", "Jamaica Accords", "Floating exchange-rate arrangements are formally accepted."),
        ("1990s →", "Electronic era", "Electronic trading and globalization make forex a highly interconnected market.")]
S.append(f"""
<section class="slide">
  {brand()}
  <div class="photo" style="left:540px;top:0;width:1380px;height:560px;background-image:url(img/history.jpg);background-position:center 45%"></div>
  {bars("right:0;top:548px")}
  {pager(1, True)}
  <div class="abs on-dark" style="left:120px;top:250px;width:1400px;background:rgba(26,43,120,.95);padding:52px 60px 56px;color:#fff">
    {eyebrow("Part I · Understanding the forex market")}
    <h2 style="color:#fff;font-size:56px;margin-bottom:40px">A brief history</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:36px">
      {"".join(f'<div class="tl"><div class="yr">{y}</div><b>{t}</b><p>{d}</p></div>' for y, t, d in hist)}
    </div>
  </div>
  <style>
    .tl {{ border-top:2px solid rgba(255,255,255,.3); padding-top:20px; position:relative; }}
    .tl::before {{ content:""; position:absolute; top:-8px; left:0; width:14px; height:14px; border-radius:50%; background:var(--mag); box-shadow:0 0 0 3px var(--navy); }}
    .tl .yr {{ font-family:'Lora',serif; font-size:46px; font-weight:600; line-height:1.05; margin-bottom:10px; }}
    .tl b {{ font-size:23px; color:var(--cyan); }}
    .tl p {{ font-size:20px; color:rgba(255,255,255,.82); line-height:1.45; margin-top:6px; }}
  </style>
  {foot(6, N)}
</section>""")

# 7 · KEY FEATURES
S.append(f"""
<section class="slide on-dark" style="background:var(--navy)">
  {brand()}{pager(1)}
  <div class="abs" style="left:120px;top:150px;width:1680px;color:#fff">
    {eyebrow("Part I · Understanding the forex market")}
    <h2 style="color:#fff;font-size:58px">Key features</h2>
  </div>
  <div class="abs" style="left:120px;top:330px;width:760px;height:540px;background:#fff;border-radius:16px;padding:46px 50px;color:var(--ink);display:flex;flex-direction:column">
    <div class="label">The largest financial market in the world</div>
    <div class="big" style="font-size:150px;margin-top:20px">$9.6<span style="font-size:60px;margin-left:10px">trillion</span></div>
    <div style="font-size:26px;color:var(--muted);margin-top:14px">traded <b style="color:var(--ink)">every day</b> on average · April 2025</div>
    <div style="margin-top:auto;display:flex;align-items:center;gap:18px">
      <span style="background:var(--mag);color:#fff;font-weight:700;font-size:28px;padding:10px 22px;border-radius:10px;display:flex;align-items:center;gap:8px">{ICON("up")}+28%</span>
      <span style="font-size:20px;color:var(--muted)">vs April 2022</span>
    </div>
    <div style="font-size:15px;color:var(--muted);margin-top:18px">Source: BIS Triennial Central Bank Survey, 2025</div>
  </div>
  <div class="abs fx7" style="left:940px;top:330px;width:860px;display:grid;gap:18px">
    <div class="card"><div style="display:flex;gap:20px;align-items:flex-start"><span class="fic m" style="flex:none">{ICON("net")}</span><div><h3>Decentralized</h3><p>No single central exchange: much trading takes place over the counter (OTC).</p></div></div></div>
    <div class="card"><div style="display:flex;gap:20px;align-items:flex-start"><span class="fic m" style="flex:none">{ICON("clock")}</span><div><h3>Open about 24 hours, 5 days a week</h3><p>Trading follows the major financial centers around the globe:</p>
      <div class="sessions"><span>Sydney</span><i></i><span>Tokyo</span><i></i><span>London</span><i></i><span>New York</span></div></div></div></div>
    <div class="card"><div style="display:flex;gap:20px;align-items:flex-start"><span class="fic m" style="flex:none">{ICON("drop")}</span><div><h3>Highly liquid</h3><p>Major currencies can generally be bought and sold quickly, in large volumes.</p></div></div></div>
  </div>
  <style>
    .fx7 .card {{ padding:20px 26px; }} .fx7 .card h3 {{ font-size:25px; margin-bottom:4px; }} .fx7 .card p {{ font-size:18px; }} .fx7 .fic {{ width:50px; height:50px; margin:0; }}
    .sessions {{ display:flex; align-items:center; gap:10px; margin-top:10px; }}
    .sessions span {{ font-size:17px; font-weight:600; color:#fff; background:rgba(255,255,255,.14); padding:6px 14px; border-radius:999px; }}
    .sessions i {{ flex:1; height:2px; background:repeating-linear-gradient(90deg,var(--cyan) 0 6px,transparent 6px 11px); min-width:16px; }}
  </style>
  {foot(7, N)}
</section>""")

# 8 · WHO TAKES PART
players = [("bank", "Central banks", "Manage their currency, set interest rates and hold foreign reserves."),
           ("building", "Commercial banks", "The core of the market: they trade with each other and for their clients."),
           ("case", "Companies", "Exchange currencies to pay suppliers and receive payments from abroad."),
           ("pie", "Investment funds", "Move capital between countries in search of returns."),
           ("phone", "Retail traders", "Individuals speculating through online platforms.")]
S.append(f"""
<section class="slide">
  {brand()}
  <div class="photo" style="left:1300px;top:0;width:620px;height:1080px;background-image:url(img/players.jpg)"></div>
  {pager(1, True)}
  <div class="abs" style="left:120px;top:140px;width:1100px">
    {eyebrow("Part I · Understanding the forex market")}
    <h2 style="font-size:58px;margin-bottom:30px">Who takes part?</h2>
    {"".join(f'<div class="pl{" core" if t == "Commercial banks" else ""}"><span class="fic s">{ICON(i)}</span><div><b>{t}</b>{" <em>the core</em>" if t == "Commercial banks" else ""}<p>{d}</p></div></div>' for i, t, d in players)}
  </div>
  <style>
    .pl {{ display:grid; grid-template-columns:72px 1fr; gap:6px; align-items:center; padding:13px 0; border-top:1.5px solid var(--line); }}
    .pl .fic {{ margin:0; }}
    .pl b {{ font-size:25px; color:var(--navy); }}
    .pl p {{ font-size:20px; color:var(--muted); }}
    .pl em {{ font-style:normal; font-size:13px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; background:var(--mag); color:#fff; padding:3px 10px; border-radius:999px; vertical-align:4px; margin-left:8px; }}
    .pl.core .fic {{ background:var(--mag); color:#fff; }}
  </style>
  <div class="key" style="right:740px;bottom:100px"><span class="k">Key takeaway</span><span>Forex makes international trade possible, and it is the largest market on the planet.</span></div>
  {foot(8, N, "right:740px")}
</section>""")

# 9 · CURRENCY PAIRS (Part II)
cats = [("Majors", "The US dollar and a major currency", ["EUR/USD", "USD/JPY", "GBP/USD"]),
        ("Minors", "Major currencies without the dollar", ["EUR/GBP", "EUR/JPY"]),
        ("Exotics", "A major currency against an emerging one", ["USD/TRY", "EUR/DZD"])]
S.append(f"""
<section class="slide">
  {brand()}{pager(2)}
  <div class="badge-part" style="left:1180px">Part II<b>{W}</b></div>
  <div class="abs" style="left:120px;top:150px;width:1680px">
    {eyebrow("Part II · How currencies are traded")}
    <h2 style="font-size:58px">Currency pairs</h2>
    <p class="lead" style="margin-top:14px">Currencies are always traded <b>in pairs</b>: the first is the <b>base</b> currency, the second is the <b>quote</b> currency.</p>
  </div>
  <div class="abs" style="left:120px;top:400px;width:1680px;height:270px;background:var(--navy);border-radius:16px;color:#fff;display:flex;align-items:center;justify-content:center;gap:70px">
    <div class="pair"><div class="t"><span class="b">EUR</span><span class="s">/</span><span class="q">USD</span><span class="s">=</span><span class="r">1.08</span></div>
      <div class="lbls"><span style="left:0;width:150px">Base</span><span style="left:196px;width:150px">Quote</span><span style="left:400px;width:180px">Rate</span></div></div>
    <div style="font-size:30px;font-family:Lora,serif;color:var(--cyan);border-left:2px solid rgba(255,255,255,.25);padding-left:60px;line-height:1.35">1 euro<br>= 1.08 US dollars</div>
  </div>
  <style>
    .pair {{ position:relative; }}
    .pair .t {{ font-family:'Lora',serif; font-weight:600; font-size:110px; line-height:1; display:flex; gap:20px; align-items:baseline; }}
    .pair .b {{ color:#fff; }} .pair .q {{ color:var(--cyan); }} .pair .s {{ color:rgba(255,255,255,.4); font-weight:500; }}
    .pair .r {{ color:#fff; background:var(--mag); padding:4px 20px; border-radius:10px; font-size:96px; }}
    .pair .lbls {{ position:relative; height:30px; margin-top:16px; }}
    .pair .lbls span {{ position:absolute; text-align:center; font-size:15px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; color:rgba(255,255,255,.7); border-top:2px solid rgba(255,255,255,.3); padding-top:6px; }}
  </style>
  <div class="abs" style="left:120px;top:710px;width:1680px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px">
    {"".join(f'<div class="card"><h3>{t}</h3><p>{d}</p><div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap">{"".join(f"<span class=chip style=font-weight:600;color:var(--navy)>{c}</span>" for c in ex)}</div></div>' for t, d, ex in cats)}
  </div>
  {foot(9, W)}
</section>""")

# 10 · BID ASK SPREAD
S.append(f"""
<section class="slide">
  {brand()}{pager(2)}
  <div class="abs" style="left:120px;top:150px;width:760px">
    {eyebrow("Part II · How currencies are traded")}
    <h2 style="font-size:58px;margin-bottom:26px">Bid, ask and spread</h2>
    <p class="lead" style="margin-bottom:22px">Every pair has <b>two prices</b>:</p>
    <div class="df"><b>Bid</b><span>The price at which the market <strong>buys from you</strong>.</span></div>
    <div class="df"><b>Ask</b><span>The price at which the market <strong>sells to you</strong>.</span></div>
    <div class="df m"><b>Spread</b><span>The difference: it is the <strong>cost of the transaction</strong>.</span></div>
    <div class="callout" style="margin-top:28px;font-size:20px"><div class="label">What is a pip?</div>The smallest standard price movement (the fourth decimal). The more traded the pair, the smaller the spread.</div>
  </div>
  <style>
    .df {{ display:grid; grid-template-columns:130px 1fr; gap:14px; padding:16px 0; border-top:1.5px solid var(--line); font-size:22px; align-items:baseline; }}
    .df b {{ font-family:'Lora',serif; font-size:28px; color:var(--navy); }}
    .df.m b {{ color:var(--mag); }}
    .df strong {{ color:var(--ink); }}
  </style>
  <div class="abs" style="left:980px;top:150px;width:820px;height:780px;background:var(--navy);border-radius:18px;padding:50px 56px;color:#fff">
    <div class="label" style="color:var(--cyan)">Example</div>
    <div class="serif" style="font-size:54px;font-weight:600;margin-bottom:40px">EUR/USD</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">
      <div class="tk"><span>Bid · you sell</span><b>1.08<u>00</u></b></div>
      <div class="tk a"><span>Ask · you buy</span><b>1.08<u>02</u></b></div>
    </div>
    <div class="spr">
      <div class="brk"></div>
      <div><span class="k">Spread</span><b>2 pips</b><span class="n">1.0802 − 1.0800 = 0.0002</span></div>
    </div>
  </div>
  <style>
    .tk {{ background:rgba(255,255,255,.08); border:1.5px solid rgba(255,255,255,.25); border-radius:14px; padding:24px 28px; }}
    .tk.a {{ background:#fff; color:var(--ink); }}
    .tk span {{ display:block; font-size:16px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; opacity:.75; }}
    .tk b {{ font-family:'Lora',serif; font-size:76px; font-weight:600; line-height:1.1; }}
    .tk u {{ text-decoration:none; color:var(--cyan); }}
    .tk.a u {{ color:var(--mag); }}
    .spr {{ margin-top:34px; display:grid; grid-template-columns:1fr; gap:14px; }}
    .spr .brk {{ height:26px; border:2px solid var(--cyan); border-top:none; border-radius:0 0 12px 12px; margin:0 20%; }}
    .spr > div:last-child {{ text-align:center; }}
    .spr .k {{ display:block; font-size:16px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--cyan); }}
    .spr b {{ display:inline-block; font-family:'Lora',serif; font-size:62px; font-weight:600; background:var(--mag); padding:2px 26px; border-radius:12px; margin:8px 0; }}
    .spr .n {{ display:block; font-size:19px; color:rgba(255,255,255,.7); }}
  </style>
  {foot(10, W)}
</section>""")

# 11 · TYPES OF TRANSACTIONS
tx = [("cal", "Spot", "Immediate exchange at the current rate, settled within <b>two business days</b>.", "Today", ""),
      ("lock", "Forward", "A rate agreed <b>today</b> for an exchange at a <b>future date</b>.", "Later", ""),
      ("swap", "Swap", "A spot and a forward combined, in <b>opposite directions</b>.", "Both", "Most traded"),
      ("key", "Options", "The <b>right, but not the obligation</b>, to exchange at a fixed rate.", "If useful", "")]
S.append(f"""
<section class="slide on-dark" style="background:var(--blue)">
  {brand()}{pager(2)}
  <div class="abs" style="left:120px;top:150px;width:1680px;color:#fff">
    {eyebrow("Part II · How currencies are traded")}
    <h2 style="color:#fff;font-size:58px">Types of transactions</h2>
  </div>
  <div class="abs" style="left:120px;top:340px;width:1680px;display:grid;grid-template-columns:repeat(4,1fr);gap:26px">
    {"".join(f'<div class="tx{" hot" if hot else ""}">{f"<em>{hot}</em>" if hot else ""}<span class="fic {"m" if hot else "s"}">{ICON(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d, w, hot in tx)}
  </div>
  <style>
    .tx {{ background:#fff; color:var(--ink); border-radius:16px; padding:44px 38px; height:480px; display:flex; flex-direction:column; position:relative; }}
    .tx.hot {{ box-shadow:inset 0 8px 0 var(--mag); }}
    .tx em {{ position:absolute; top:26px; right:26px; font-style:normal; background:var(--mag); color:#fff; font-size:14px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; padding:5px 12px; border-radius:999px; }}
    .tx h3 {{ font-size:50px; color:var(--navy); margin:34px 0 18px; }}
    .tx p {{ font-size:26px; color:var(--muted); line-height:1.45; }}
    .tx p b {{ color:var(--ink); }}
    .tx .when {{ margin-top:auto; font-size:15px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--blue-2); border-top:1.5px solid var(--line); padding-top:14px; }}
  </style>
  {foot(11, W)}
</section>""")

# 12 · REGIMES
S.append(f"""
<section class="slide">
  {brand()}{pager(2)}
  <div class="abs" style="left:120px;top:150px;width:1680px">
    {eyebrow("Part II · How currencies are traded")}
    <h2 style="font-size:58px">Exchange-rate regimes</h2>
  </div>
  <div class="abs" style="left:120px;top:370px;width:1680px">
    <div class="spec"><span>Market sets the rate</span><span>Central bank sets the rate</span></div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-top:30px">
      <div class="card"><h3>Floating</h3><p>The market sets the rate freely.</p><div class="eg">US dollar · euro · yen</div></div>
      <div class="card dz"><em>Algerian dinar</em><h3>Managed float</h3><p>The rate moves with the market, but the central bank intervenes to limit swings.</p><div class="eg">Algerian dinar</div></div>
      <div class="card"><h3>Fixed or pegged</h3><p>The central bank keeps a fixed value against another currency.</p><div class="eg">Saudi riyal against the dollar</div></div>
    </div>
  </div>
  <style>
    .spec {{ height:58px; border-radius:999px; background:linear-gradient(90deg,var(--cyan),var(--blue-2) 50%,var(--navy)); display:flex; justify-content:space-between; align-items:center; padding:0 30px; font-size:17px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; }}
    .spec span:first-child {{ color:var(--navy); }} .spec span:last-child {{ color:#fff; }}
    .card.dz {{ border:2.5px solid var(--mag); position:relative; }}
    .card em {{ position:absolute; top:-16px; left:26px; font-style:normal; background:var(--mag); color:#fff; font-size:14px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; padding:4px 12px; border-radius:999px; }}
    .card .eg {{ margin-top:16px; font-size:19px; color:var(--mag); font-weight:600; background:#fbeef4; padding:10px 16px; border-radius:8px; }}
    .card h3 {{ font-size:36px; }}
    .card p {{ font-size:23px; min-height:100px; }}
    .card {{ padding:34px 34px; }}
  </style>
  <div class="key"><span class="k">Key takeaway</span><span>An exchange rate is a price, and every transaction has a cost (the spread) and a time frame (spot or forward).</span></div>
  {foot(12, W)}
</section>""")

# 13 · SUPPLY AND DEMAND (Part III)
S.append(f"""
<section class="slide">
  {brand()}{pager(3)}
  <div class="badge-part" style="left:1180px">Part III<b>{K}</b></div>
  <div class="abs" style="left:120px;top:150px;width:1680px">
    {eyebrow("Part III · What moves exchange rates")}
    <h2 style="font-size:58px">Supply and demand</h2>
    <p class="lead" style="margin-top:14px">Like any price, an exchange rate depends on <b>supply and demand</b>.</p>
  </div>
  <div class="abs" style="left:120px;top:380px;width:1680px;display:grid;grid-template-columns:1fr 1fr;gap:34px">
    <div class="sd up"><div class="hd"><span class="arr">{ICON("up")}</span><div><span class="k">More demand for a currency</span><b>Its value rises</b></div></div>
      <div class="chips"><span class="chip">Exports</span><span class="chip">Foreign investment</span><span class="chip">Tourism</span></div></div>
    <div class="sd dn"><div class="hd"><span class="arr">{ICON("down")}</span><div><span class="k">More supply of a currency</span><b>Its value falls</b></div></div>
      <div class="chips"><span class="chip">Imports</span><span class="chip">Capital leaving the country</span></div></div>
  </div>
  <style>
    .sd {{ border-radius:18px; padding:44px 48px; color:#fff; height:400px; display:flex; flex-direction:column; }}
    .sd.up {{ background:var(--blue-2); }} .sd.dn {{ background:var(--mag); }}
    .sd .hd {{ display:flex; gap:26px; align-items:center; }}
    .sd .arr {{ width:96px; height:96px; border-radius:50%; background:#fff; display:grid; place-items:center; flex:none; }}
    .sd.up .arr {{ color:var(--blue-2); }} .sd.dn .arr {{ color:var(--mag); }}
    .sd .arr .ic {{ width:52px; height:52px; stroke-width:2.2; }}
    .sd .k {{ display:block; font-size:17px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; opacity:.85; }}
    .sd b {{ font-family:'Lora',serif; font-size:50px; font-weight:600; }}
    .sd .chips {{ margin-top:auto; display:flex; gap:12px; flex-wrap:wrap; }}
    .sd .chip {{ background:rgba(255,255,255,.15); color:#fff; border-color:rgba(255,255,255,.4); font-size:20px; }}
  </style>
  <p class="abs serif" style="left:120px;top:860px;width:1680px;font-size:38px;font-weight:600;color:var(--navy);text-align:center">The question is: <span style="color:var(--mag)">what drives this supply and demand?</span></p>
  {foot(13, K)}
</section>""")

# 14 · INTEREST RATES AND INFLATION
S.append(f"""
<section class="slide">
  {brand()}{pager(3)}
  <div class="abs" style="left:120px;top:150px;width:1680px">
    {eyebrow("Part III · What moves exchange rates")}
    <h2 style="font-size:58px">Interest rates and inflation</h2>
  </div>
  <div class="abs qcard" style="left:120px;top:340px;width:620px;height:560px;display:flex;flex-direction:column;justify-content:center">
    {ICON("quote")}
    <p class="q" style="font-size:38px">Inflation is always and everywhere a monetary phenomenon.</p>
    <p class="by">— Milton Friedman, Nobel Prize in Economics, 1976</p>
  </div>
  <div class="abs" style="left:800px;top:340px;width:1000px;display:grid;gap:28px">
    <div class="chain"><div class="lab">Interest rates</div>
      <div class="steps"><span>Country <b>raises</b> its rates</span>{ICON("arrow", "ic ar")}<span>Investors move money there to earn more</span>{ICON("arrow", "ic ar")}<span class="res up">{ICON("up")} Currency strengthens</span></div></div>
    <div class="chain"><div class="lab">Inflation</div>
      <div class="steps"><span>Prices rise <b>faster</b> than elsewhere</span>{ICON("arrow", "ic ar")}<span>The currency loses purchasing power</span>{ICON("arrow", "ic ar")}<span class="res dn">{ICON("down")} Value falls over time</span></div></div>
  </div>
  <style>
    .chain {{ border:1.5px solid var(--line); border-radius:16px; padding:30px 32px; height:266px; display:flex; flex-direction:column; justify-content:center; }}
    .chain .lab {{ font-family:'Lora',serif; font-size:34px; font-weight:600; color:var(--navy); margin-bottom:20px; }}
    .chain .steps {{ display:grid; grid-template-columns:1fr 34px 1fr 34px 1fr; align-items:center; gap:12px; }}
    .chain .steps > span {{ font-size:20px; color:var(--muted); line-height:1.35; }}
    .chain .steps b {{ color:var(--ink); }}
    .chain .ar {{ color:var(--blue-2); width:30px; height:30px; }}
    .chain .res {{ color:#fff !important; font-weight:600; border-radius:12px; padding:14px 16px; display:flex; gap:8px; align-items:center; }}
    .chain .res.up {{ background:var(--blue-2); }} .chain .res.dn {{ background:var(--mag); }}
  </style>
  {foot(14, K)}
</section>""")

# 15 · CENTRAL BANKS
S.append(f"""
<section class="slide on-dark" style="background:var(--navy)">
  <div class="photo" style="left:960px;top:0;width:960px;height:1080px;background-image:url(img/ecb.jpg)"></div>
  <div class="abs" style="left:960px;top:0;width:960px;height:1080px;background:linear-gradient(90deg,var(--navy) 0%,rgba(26,43,120,.35) 40%,rgba(26,43,120,.1) 100%)"></div>
  {brand()}{pager(3)}
  <div class="abs" style="left:120px;top:150px;width:1300px;color:#fff">
    {eyebrow("Part III · What moves exchange rates")}
    <h2 style="color:#fff;font-size:58px;margin-bottom:34px">The power of central banks</h2>
    <div class="qcard" style="width:1150px;padding:38px 46px">
      {ICON("quote")}
      <p class="q" style="font-size:34px">Within our mandate, the ECB is ready to do whatever it takes to preserve the euro. And believe me, it will be enough.</p>
      <p class="by">— Mario Draghi, President of the European Central Bank, July 2012</p>
    </div>
    <p style="font-size:23px;color:rgba(255,255,255,.88);margin-top:30px;max-width:780px">In 2012, markets feared the end of the euro. These few words were enough to <b style="color:#fff">restore confidence</b> and stabilize the currency.</p>
  </div>
  <div class="abs" style="left:120px;top:850px;display:flex;gap:16px;align-items:center">
    <span style="font-size:15px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--cyan);margin-right:6px">How they act</span>
    <span class="chip" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.4)">Interest rates</span>
    <span class="chip" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.4)">Direct intervention (buying or selling their currency)</span>
    <span class="chip" style="background:var(--mag);color:#fff;border-color:var(--mag);font-weight:700">Above all: credibility</span>
  </div>
  {bars("right:0;bottom:0")}
  {foot(15, K)}
</section>""")

# 16 · BREXIT
S.append(f"""
<section class="slide">
  {brand()}
  <div class="photo" style="left:1160px;top:0;width:760px;height:1080px;background-image:url(img/london.jpg)"></div>
  {pager(3, True)}
  <div class="abs" style="left:120px;top:150px;width:980px">
    {eyebrow("Part III · What moves exchange rates")}
    <h2 style="font-size:56px;margin-bottom:18px">Politics and confidence: the Brexit case</h2>
    <p class="lead">On <b>23 June 2016</b>, the United Kingdom voted to leave the European Union. The next day, the pound hit its lowest level in more than 30 years.</p>
  </div>
  <div class="abs" style="left:120px;top:470px;width:980px;display:flex;align-items:center;gap:30px">
    <div class="px"><span>Before the vote</span><b>$1.50</b><em>for £1 (about)</em></div>
    <div style="display:flex;flex-direction:column;align-items:center;color:var(--mag)">{ICON("arrow", "ic big-ar")}<span style="font-weight:700;font-size:22px">≈ −12%</span><span style="font-size:15px;color:var(--muted)">overnight</span></div>
    <div class="px m"><span>24 June 2016</span><b>$1.32</b><em>for £1</em></div>
  </div>
  <style>
    .px {{ flex:1; border:1.5px solid var(--line); border-radius:16px; padding:24px 30px; }}
    .px.m {{ background:var(--mag); color:#fff; border-color:var(--mag); }}
    .px span {{ display:block; font-size:15px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--muted); }}
    .px.m span, .px.m em {{ color:rgba(255,255,255,.85); }}
    .px b {{ font-family:'Lora',serif; font-size:84px; font-weight:600; line-height:1.1; color:var(--navy); }}
    .px.m b {{ color:#fff; }}
    .px em {{ font-style:normal; font-size:19px; color:var(--muted); }}
    .big-ar {{ width:64px; height:64px; stroke-width:2.2; }}
  </style>
  <div class="abs" style="left:120px;top:720px;width:980px">
    <p class="serif" style="font-size:30px;font-weight:600;color:var(--navy);line-height:1.35">Nothing had changed in the British economy overnight. <span style="color:var(--mag)">What changed was confidence.</span></p>
    <p class="lead" style="margin-top:10px">Exchange rates react to expectations as much as to facts.</p>
  </div>
  <div class="key" style="right:840px;bottom:96px;left:120px;display:none"></div>
  <div class="abs" style="left:1160px;bottom:96px;width:760px;background:var(--mag);color:#fff;padding:22px 36px;font-size:20px;line-height:1.4">
    <div style="font-size:15px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;opacity:.9;margin-bottom:4px">Key takeaway · Part III</div>
    Exchange rates are driven by interest rates, inflation, central banks and, above all, <b>confidence</b>.
  </div>
  {foot(16, K, "right:840px")}
</section>""")

# 17 · EXCHANGE-RATE RISK (Part IV)
S.append(f"""
<section class="slide">
  {brand()}{pager(4)}
  <div class="badge-part" style="left:1180px">Part IV<b>{A}</b></div>
  <div class="abs" style="left:120px;top:150px;width:780px">
    {eyebrow("Part IV · Risks and real-world impact")}
    <h2 style="font-size:58px;margin-bottom:24px">Exchange-rate risk</h2>
    <p class="lead">The possibility of <b>losing money</b> because a currency changes value between <b>signing a contract</b> and <b>paying it</b>.</p>
    <div class="callout" style="margin-top:34px"><div class="label">The case</div>An Algerian importer must pay <b>100,000 euros</b> in <b>three months</b>.</div>
  </div>
  <div class="abs" style="left:980px;top:200px;width:820px;background:var(--soft);border-radius:18px;padding:46px 52px">
    <div class="label" style="color:var(--muted)">Illustrative rates</div>
    <div class="calc" style="border-top:none"><span class="l"><b>At signing</b><br>1 EUR = 150 DZD</span><span class="v">15,000,000 DZD</span></div>
    <div class="calc"><span class="l"><b>Three months later</b><br>1 EUR = 160 DZD</span><span class="v">16,000,000 DZD</span></div>
    <div style="margin-top:30px;background:var(--mag);color:#fff;border-radius:14px;padding:28px 32px">
      <div style="font-size:15px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;opacity:.9">Loss</div>
      <div class="serif" style="font-size:72px;font-weight:600;line-height:1.1">−1,000,000 DZD</div>
      <div style="font-size:21px;opacity:.92">without doing anything wrong.</div>
    </div>
  </div>
  {foot(17, A)}
</section>""")

# 18 · HEDGING
S.append(f"""
<section class="slide on-dark" style="background:var(--navy)">
  {brand()}{pager(4)}
  <div class="abs" style="left:120px;top:150px;width:1680px;color:#fff">
    {eyebrow("Part IV · Risks and real-world impact")}
    <h2 style="color:#fff;font-size:58px;margin-bottom:18px">Hedging: how companies protect themselves</h2>
    <p style="font-size:24px;color:rgba(255,255,255,.88)"><b style="color:#fff">Hedging</b> means using financial tools to <b style="color:#fff">lock in a rate in advance</b>.</p>
  </div>
  <div class="abs" style="left:120px;top:420px;width:1680px;display:grid;grid-template-columns:1fr 1fr;gap:30px">
    <div class="hg"><div class="label" style="color:var(--muted)">Without hedging</div><h3>The cost depends on the market</h3>
      <div class="calc"><span class="l">If 1 EUR = 150 DZD</span><span class="v">15,000,000</span></div>
      <div class="calc"><span class="l">If 1 EUR = 160 DZD</span><span class="v">16,000,000</span></div>
      <p class="hn">Unknown until payment day.</p></div>
    <div class="hg on"><div class="label">With a forward contract</div><h3>Rate signed today: 1 EUR = 152 DZD</h3>
      <div class="calc"><span class="l">Whatever happens</span><span class="v">15,200,000</span></div>
      <div style="display:flex;gap:14px;align-items:center;margin-top:18px;font-size:21px;color:var(--navy);font-weight:600">{ICON("lock")} The cost is fixed today</div></div>
  </div>
  <style>
    .hg {{ background:#fff; color:var(--ink); border-radius:16px; padding:34px 40px; }}
    .hg.on {{ box-shadow:inset 0 8px 0 var(--mag); }}
    .hg h3 {{ font-size:30px; margin:4px 0 14px; }}
    .hg .hn {{ font-size:19px; color:var(--muted); margin-top:10px; }}
  </style>
  <p class="abs serif" style="left:120px;top:860px;width:1680px;font-size:30px;color:#fff;font-weight:500">The company gives up a possible gain to remove the risk of a loss. <span style="color:var(--cyan)">It buys certainty.</span></p>
  {foot(18, A)}
</section>""")

# 19 · SPECULATION & LEVERAGE
S.append(f"""
<section class="slide">
  {brand()}{pager(4)}
  <div class="abs" style="left:120px;top:150px;width:1000px">
    {eyebrow("Part IV · Risks and real-world impact")}
    <h2 style="font-size:58px;margin-bottom:20px">Speculation and leverage</h2>
    <p class="lead"><b>Leverage</b> allows a trader to control a large position with little capital.</p>
    <div class="lev">
      <div class="lv"><span>With leverage of 1:100</span><b>$1,000</b><em>controls</em><b>$100,000</b></div>
      <div class="lo up"><span>Rate moves 1% the right way</span><b>+$1,000</b><em>+100%</em></div>
      <div class="lo dn"><span>Rate moves 1% the wrong way</span><b>−$1,000</b><em>capital lost</em></div>
    </div>
  </div>
  <style>
    .lev {{ margin-top:30px; display:grid; grid-template-columns:1fr 1fr; gap:20px; }}
    .lev .lv {{ grid-column:1/-1; background:var(--navy); color:#fff; border-radius:14px; padding:22px 30px; display:flex; align-items:baseline; gap:20px; }}
    .lev .lv span {{ font-size:16px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--cyan); margin-right:auto; }}
    .lev .lv b {{ font-family:'Lora',serif; font-size:52px; font-weight:600; }}
    .lev .lv em {{ font-style:normal; font-size:20px; opacity:.8; }}
    .lo {{ border-radius:14px; padding:22px 28px; color:#fff; }}
    .lo.up {{ background:var(--blue-2); }} .lo.dn {{ background:var(--mag); }}
    .lo span {{ display:block; font-size:17px; opacity:.9; }}
    .lo b {{ font-family:'Lora',serif; font-size:54px; font-weight:600; line-height:1.15; }}
    .lo em {{ font-style:normal; display:block; font-size:19px; font-weight:700; letter-spacing:.06em; }}
  </style>
  <div class="abs qcard" style="left:1220px;top:150px;width:580px;padding:34px 38px">
    {ICON("quote")}
    <p class="q" style="font-size:31px">Derivatives are financial weapons of mass destruction.</p>
    <p class="by">— Warren Buffett, letter to Berkshire Hathaway shareholders, 2002</p>
  </div>
  <div class="abs" style="left:1220px;top:530px;width:580px;height:400px;border-radius:14px;overflow:hidden;background:var(--navy);color:#fff">
    <div class="photo" style="inset:0;background-image:url(img/boe.jpg);opacity:.45"></div>
    <div class="abs" style="left:34px;right:34px;bottom:30px">
      <div style="font-size:15px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--cyan)">Famous case · Black Wednesday</div>
      <div class="serif" style="font-size:34px;font-weight:600;margin:6px 0 8px">16 September 1992</div>
      <p style="font-size:19px;line-height:1.45;color:rgba(255,255,255,.92)">George Soros bet against the British pound. The Bank of England could not defend it, and Soros reportedly earned <b>around $1 billion in a single day</b>.</p>
    </div>
  </div>
  {foot(19, A)}
</section>""")

# 20 · EVERYDAY LIFE
S.append(f"""
<section class="slide">
  {brand()}{pager(4)}
  <div class="abs" style="left:120px;top:150px;width:1680px">
    {eyebrow("Part IV · Risks and real-world impact")}
    <h2 style="font-size:58px">Impact on everyday life</h2>
  </div>
  <div class="abs" style="left:120px;top:320px;width:820px;display:grid;gap:22px">
    <div class="ws"><div class="hd">{ICON("down")} A weak currency</div><div class="r"><span class="minus">Imports more expensive, prices rise</span><span class="plus">Exports more competitive</span></div></div>
    <div class="ws"><div class="hd">{ICON("up")} A strong currency</div><div class="r"><span class="plus">Imports are cheaper</span><span class="minus">Local producers struggle to export</span></div></div>
  </div>
  <style>
    .ws {{ border:1.5px solid var(--line); border-radius:16px; padding:26px 30px; }}
    .ws .hd {{ display:flex; gap:12px; align-items:center; font-family:'Lora',serif; font-size:32px; font-weight:600; color:var(--navy); margin-bottom:14px; }}
    .ws .hd .ic {{ width:34px; height:34px; color:var(--mag); }}
    .ws .r {{ display:grid; gap:10px; }}
    .ws .r span {{ font-size:21px; padding-left:36px; position:relative; color:var(--ink); }}
    .ws .r span::before {{ position:absolute; left:0; top:1px; width:24px; height:24px; border-radius:50%; color:#fff; font-weight:700; font-size:18px; display:grid; place-items:center; line-height:1; }}
    .ws .plus::before {{ content:"+"; background:var(--blue-2); }}
    .ws .minus::before {{ content:"−"; background:var(--mag); }}
  </style>
  <div class="abs on-dark" style="left:1000px;top:320px;width:800px;height:540px;background:var(--navy);border-radius:16px;overflow:hidden;color:#fff">
    <div class="photo" style="left:0;top:0;width:800px;height:200px;background-image:url(img/algiers.jpg)"></div>
    <div style="position:absolute;top:220px;left:40px;right:40px">
      <div style="font-size:15px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--cyan)">The Algerian case</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:14px 0 16px">
        <div style="background:rgba(255,255,255,.1);border-radius:12px;padding:14px 18px"><b style="font-family:Lora,serif;font-size:24px">Official rate</b><div style="font-size:17px;opacity:.85">set by the Bank of Algeria</div></div>
        <div style="background:var(--mag);border-radius:12px;padding:14px 18px"><b style="font-family:Lora,serif;font-size:24px">Parallel market</b><div style="font-size:17px;opacity:.9">“the square”, significantly higher</div></div>
      </div>
      <p style="font-size:19px;line-height:1.45;color:rgba(255,255,255,.88)">The gap reflects strong demand for foreign currency and limited official access to it. It directly affects the price of <b style="color:#fff">cars, travel and imported goods</b>.</p>
    </div>
  </div>
  <div class="key" style="bottom:96px"><span class="k">Key takeaway</span><span>Forex risk is real for companies and traders, and its effects reach everyone through prices.</span></div>
  {foot(20, A)}
</section>""")

# 21 · CONCLUSION
S.append(f"""
<section class="slide on-dark" style="background:var(--blue)">
  <div class="photo" style="left:1120px;top:0;width:800px;height:1080px;background-image:url(img/conclusion.jpg);clip-path:polygon(22% 0,100% 0,100% 100%,0 100%)"></div>
  {brand()}{pager(5)}
  <div class="abs" style="left:120px;top:150px;width:1060px;color:#fff">
    {eyebrow("Conclusion")}
    <h2 style="color:#fff;font-size:56px;margin-bottom:24px">The backbone of the global economy</h2>
    <p style="font-size:23px;color:rgba(255,255,255,.88)">Without the forex market, no country could trade, invest or borrow abroad.</p>
    <div class="cl"><span class="k">Exchange rates are prices shaped by</span><div>{"".join(f"<span class=chip>{c}</span>" for c in ["Supply &amp; demand", "Interest rates", "Inflation", "Central banks", "Confidence"])}</div></div>
    <div class="cl"><span class="k">They create</span><div><span class="chip">Opportunities</span><span class="chip">Risks managed through hedging</span><span class="chip">Risks amplified by leverage</span></div></div>
    <div style="margin-top:40px;background:#fff;color:var(--ink);border-radius:14px;padding:28px 34px;border-left:8px solid var(--mag)">
      <div class="label">From Bretton Woods to Brexit, one constant</div>
      <p class="serif" style="font-size:31px;font-weight:600;color:var(--navy);line-height:1.35">The value of a currency reflects the trust placed in the economy behind it.</p>
    </div>
  </div>
  <style>
    .cl {{ margin-top:26px; }}
    .cl .k {{ display:block; font-size:15px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--cyan); margin-bottom:10px; }}
    .cl > div {{ display:flex; gap:10px; flex-wrap:wrap; }}
    .cl .chip {{ background:transparent; color:#fff; border-color:rgba(255,255,255,.4); }}
  </style>
  {bars("right:0;bottom:0")}
  {foot(21, None, "right:900px")}
</section>""")

# 22 · THANK YOU
S.append(f"""
<section class="slide on-dark" style="background:var(--navy)">
  <div class="photo" style="left:900px;top:0;width:1020px;height:1080px;background-image:url(img/thanks.jpg);clip-path:polygon(30% 0,100% 0,100% 100%,0 100%)"></div>
  {brand()}{pager(5)}
  <div class="abs" style="left:120px;top:320px;color:#fff;width:960px">
    <h1 style="font-size:150px;line-height:1">Thank you</h1>
    <p class="serif" style="font-size:48px;color:var(--cyan);font-weight:500;margin-top:16px">Questions?</p>
    <div style="margin-top:60px;font-size:22px;color:rgba(255,255,255,.88)">Norhane Benazala · Wassim Sid · Kamil Mohamed Ounis · Adam Sam</div>
    <div style="font-size:19px;color:rgba(255,255,255,.6);margin-top:4px">Foreign Exchange Markets: The Price of Money</div>
  </div>
  {bars("left:120px;bottom:120px")}
</section>""")

# 23 · SOURCES
srcs = ["Bank for International Settlements (BIS), <i>Triennial Central Bank Survey</i>, 2025.",
        "Milton Friedman, <i>The Counter-Revolution in Monetary Theory</i>, 1970.",
        "Mario Draghi, speech at the Global Investment Conference, London, 26 July 2012.",
        "Warren Buffett, <i>Berkshire Hathaway Annual Letter</i>, 2002.",
        "Bank of Algeria, official exchange-rate publications."]
S.append(f"""
<section class="slide">
  {brand()}{pager(5)}
  <div class="abs" style="left:120px;top:150px;width:1680px">
    {eyebrow("References")}
    <h2 style="font-size:64px;margin-bottom:40px">Sources</h2>
    {"".join(f'<div class="src"><span class="num">{i + 1:02d}</span><span>{s}</span></div>' for i, s in enumerate(srcs))}
    <p style="margin-top:40px;font-size:16px;color:var(--muted)">Images: Unsplash (Unsplash License), tinted in blue duotone.</p>
  </div>
  <style>
    .src {{ display:grid; grid-template-columns:80px 1fr; padding:20px 0; border-top:1.5px solid var(--line); font-size:25px; align-items:baseline; }}
    .src .num {{ color:var(--mag); font-size:28px; }}
  </style>
  {foot(23)}
</section>""")

css = base_css + EXTRA_CSS
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Foreign Exchange Markets</title>
<link rel="stylesheet" href="fonts/fonts.css">
<style>{css}</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute"><defs>{base_syms}{EXTRA_SYMS}</defs></svg>
{"".join(S)}
</body>
</html>"""
open(os.path.join(HERE, "fx.html"), "w").write(html)
print("slides:", len(S))
