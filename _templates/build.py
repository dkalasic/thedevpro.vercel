#!/usr/bin/env python3
"""Builds the static TheDevPro site into OUT. Every page is plain HTML (SEO + link previews)."""
import os, sys, json

OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/thedevpro-site"
SITE = "https://thedevpro.io"
PHONE = "+18013762721"
PHONE_TXT = "801.376.2721"
EMAIL = "hello@thedevpro.io"
WA = "https://wa.me/18013762721?text=" + "Hi%20Daniel%2C%20I%27d%20like%20to%20talk%20about%20my%20business."
MAIL = "mailto:hello@thedevpro.io?subject=New%20project&cc=dkalasic%40gmail.com"

SERVICES = [
    ("social-media", "Social media"),
    ("advertising", "Advertising"),
    ("whatsapp-crm-ai-agents", "WhatsApp, CRM & AI agents"),
    ("mobile-apps", "Mobile apps"),
    ("custom-software", "Custom software"),
]

WA_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21l1.6-4.6A8.5 8.5 0 1 1 8 20z"/></svg>'

def head(title, desc, path, robots="index, follow"):
    url = SITE + path
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="TheDevPro">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F2742">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Barlow+Semi+Condensed:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
<script src="/assets/js/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(active=""):
    def cur(key):
        return ' aria-current="page"' if key == active else ""
    svc = "".join(f'<a href="/services/{s}/">{n}</a>' for s, n in SERVICES)
    return f"""<header class="site-header">
<div class="wrap">
<a class="logo" href="/" aria-label="TheDevPro home"><img src="/assets/img/logo.png" alt="TheDevPro" width="163" height="30"></a>
<button class="nav-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
<nav class="nav" id="site-nav" aria-label="Main">
<div class="dropdown"><a href="/services/"{cur('services')}>Services</a><div class="dropdown-menu">{svc}</div></div>
<a href="/ai/"{cur('ai')}>AI</a>
<a href="/work/"{cur('work')}>Work</a>
<a href="/process/"{cur('process')}>Process</a>
<a href="/about/"{cur('about')}>About</a>
<a class="btn btn-outline" href="{WA}" rel="noopener">{WA_ICON} WhatsApp</a>
<a class="btn btn-primary" href="/contact/"{cur('contact')}>Contact</a>
</nav>
</div>
</header>
<main id="main">
"""

def footer():
    svc = "".join(f'<a href="/services/{s}/">{n}</a>' for s, n in SERVICES)
    return f"""</main>
<footer class="site-footer">
<div class="wrap">
<div class="stack" style="gap:12px">
<img src="/assets/img/logo.png" alt="TheDevPro" width="141" height="26" style="height:26px;width:auto">
<p class="muted small">Custom software, AI and marketing for service businesses. Senior full-stack developer, 20+ years. Utah · English &amp; Español.</p>
<p class="small muted">© 2026 TheDevPro · SoloDevPro</p>
</div>
<div><h2>Services</h2>{svc}<a href="/ai/">AI for your business</a></div>
<div><h2>Company</h2><a href="/work/">Work</a><a href="/process/">Process</a><a href="/about/">About</a><a href="/contact/">Contact</a></div>
<div><h2>Contact</h2><a href="{MAIL}">{EMAIL}</a><a href="tel:{PHONE}">{PHONE_TXT}</a><a href="{WA}" rel="noopener">WhatsApp</a></div>
</div>
</footer>
<nav class="qbar" aria-label="Quick contact"><a href="{WA}" rel="noopener">WhatsApp</a><a href="tel:{PHONE}">Call</a><a href="{MAIL}">Email</a></nav>
</body>
</html>
"""

def cta_dark(title="Let’s look at your setup.", sub="Free 30-minute call. I reply within 2 hours on business days."):
    return f"""<section class="sec-dark">
<div class="bp" aria-hidden="true">
<div class="bn" style="left:50%;top:34px">WALKTHROUGH</div>
<div class="wire-h" style="left:calc(50% + 130px);width:70px;top:52px"></div>
<div class="bn" style="left:calc(50% + 200px);top:34px">BUILD</div>
<div class="wire-h" style="left:calc(50% + 272px);width:70px;top:52px"></div>
<div class="bn hot" style="left:calc(50% + 342px);top:34px">WEEKLY DEMO</div>
</div>
<div class="wrap" style="padding-top:104px;padding-bottom:88px;display:flex;justify-content:space-between;align-items:center;gap:32px;flex-wrap:wrap">
<div class="stack" style="gap:10px"><h2>{title}</h2><p class="lede">{sub}</p></div>
<div class="row"><a class="btn btn-primary" href="/contact/">Book a free call</a><a class="btn btn-light" href="{WA}" rel="noopener">WhatsApp</a><a class="btn btn-light" href="tel:{PHONE}">{PHONE_TXT}</a></div>
</div>
</section>
"""

def write(path, html):
    full = os.path.join(OUT, path.strip("/"), "index.html") if path != "/404" else os.path.join(OUT, "404.html")
    if path == "/":
        full = os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)

PAGES = []
def page(path, title, desc, active, body):
    PAGES.append(path)
    write(path, head(title, desc, path) + header(active) + body + footer())

# ---------- shared blocks ----------
SCHEMATIC = """<figure class="dwg paper-grid reveal" role="img" aria-label="Diagram: ads and WhatsApp flow into a shared inbox with an AI agent, then into the CRM and projects, which feed estimates, the field app and QuickBooks">
<div class="dwg-cols">
<div class="dwg-col"><div class="node"><small>IN-01</small>Ads &amp; social</div><div class="node"><small>IN-02</small>WhatsApp · SMS · web chat</div></div>
<div class="wire-h"></div>
<div class="dwg-col"><div class="node hub"><small>HUB</small>Inbox + AI agent</div><div class="node core"><small>CORE</small>CRM + projects</div></div>
<div class="wire-h"></div>
<div class="dwg-col"><div class="node"><small>OUT-01</small>Estimates</div><div class="node"><small>OUT-02</small>Field app</div><div class="node"><small>OUT-03</small>QuickBooks</div></div>
</div>
<figcaption class="dwg-tag">DWG 001 — LEAD → PAID JOB</figcaption>
</figure>"""

BA_PO = """<div class="ba" role="img" aria-label="Purchase order example: five manual steps today versus three steps with AI in about five minutes">
<span class="ba-label">Today</span>
<div class="ba-track"><div class="ba-line manual"><span class="dot slow"></span></div>
<div class="ba-steps"><span>Open the estimate</span><span>Copy items to a spreadsheet</span><span>Email the supplier</span><span>Chase &amp; re-check</span><span>Retype in QuickBooks</span></div></div>
<span class="ba-label ai">With AI</span>
<div class="ba-track"><div class="ba-line auto"><span class="dot fast"></span></div>
<div class="ba-steps"><span class="s-strong">Estimate approved</span><span class="s-ai">AI drafts the PO</span><span class="s-ok">You approve → sent &amp; synced</span><span class="ba-result">≈ 5 minutes</span></div></div>
</div>"""

INTEGRATIONS = ["QuickBooks Online · two-way", "Housecall Pro · migration", "Oasis · scheduled API sync", "WhatsApp Business", "Chatwoot", "n8n", "Twilio SMS", "SendGrid", "Cloudflare R2", "Google &amp; Meta Ads"]
INTEG_HTML = '<div class="chips">' + "".join(f'<span class="chip">{x}</span>' for x in INTEGRATIONS) + "</div>"

ONBOARD = f"""<section class="sec sec-white" aria-labelledby="start-h">
<div class="wrap">
<div class="sec-head"><div><span class="eyebrow blue">How you get started</span><h2 id="start-h">From QuickBooks to your own system in days, not months.</h2></div><a class="btn btn-primary" href="/contact/">Book the free call</a></div>
<ol class="grid g4 lit" style="list-style:none;margin:0;padding:0">
<li class="card"><span class="num">1</span><h3 style="font-size:21px">Free 30-minute call</h3>
<div class="step-mini"><span class="muted">Thursday</span><span class="slot">9:00 — taken</span><span class="slot pick">10:30 — yours</span></div>
<p>We map how work flows today. You get a written plan — even if it says “not yet”.</p></li>
<li class="card"><span class="num">2</span><h3 style="font-size:21px">Connect QuickBooks</h3>
<div class="step-mini"><span class="qb-btn">Connect to QuickBooks</span><span>Customers <b class="ck" style="animation-delay:2.8s">✓</b></span><span>Items &amp; prices <b class="ck" style="animation-delay:3.4s">✓</b></span><span>Open invoices <b class="ck" style="animation-delay:4s">✓</b></span></div>
<p>One click. Your customers and prices come over — nothing retyped.</p></li>
<li class="card"><span class="num">3</span><h3 style="font-size:21px">Your own workspace</h3>
<div class="step-mini"><span class="url">yourcompany.thedevpro.io</span><div class="tiles"><span>Clients</span><span>Estimates</span><span>Projects</span><span>Invoices</span></div></div>
<p>Private to your company, with your logo. Backed up in your office.</p></li>
<li class="card"><span class="num hot">4</span><h3 style="font-size:21px">Send your first estimate</h3>
<div class="step-mini"><span style="display:flex;justify-content:space-between;gap:8px"><b>Estimate #1042</b><span class="status">Sent → Approved</span></span><span class="muted">3 line items from your QuickBooks prices</span><span style="color:var(--done);font-weight:600">→ Project created automatically</span></div>
<p>Approved estimates become projects with phases. Then a demo every week.</p></li>
</ol>
</div>
</section>
"""

FIT = f"""<section class="sec" aria-label="Who this is for">
<div class="wrap grid g2">
<div class="card" style="border-top:4px solid var(--ink)"><h2 style="font-size:30px">A good fit if you…</h2>
<ul class="clean"><li>run 5–50 people across office and field</li><li>live in six apps and spreadsheets that don’t talk to each other</li><li>want to own your system, not rent it forever</li><li>can give 30 minutes a week to see a demo</li></ul></div>
<div class="card" style="border-top:4px solid #8A97A8"><h2 style="font-size:30px">Not a fit if you…</h2>
<ul class="clean"><li>want an off-the-shelf tool with no changes — ServiceTitan or Jobber will serve you better</li><li>need a fixed price for a project nobody has mapped yet</li><li>want AI to send things without a person approving them</li></ul></div>
<div class="span-all" style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center;border:1.5px dashed #8A97A8;border-radius:6px;padding:20px 24px">
<span><b>How pricing works:</b> hourly, invoiced every week. No long contract — stop any week. You own the code.</span><a class="link" href="/process/">How I work →</a></div>
</div>
</section>
"""

# ---------- HOME ----------
home = f"""<section class="hero">
<div class="wrap">
<div class="stack">
<span class="eyebrow">For HVAC, construction &amp; service companies</span>
<h1>Your business, wired together the right way.</h1>
<p class="lede">Leads, WhatsApp, CRM, estimates, crews and QuickBooks — connected by a senior developer with 20+ years of experience. You own all of it.</p>
<div class="row"><a class="btn btn-primary" href="/contact/">Book a free 30-min call</a><a class="btn btn-outline" href="{WA}" rel="noopener">{WA_ICON} Message me on WhatsApp</a></div>
<p class="hero-note">You get a written recommendation after every call, even if it’s “you don’t need this yet.”</p>
</div>
{SCHEMATIC}
</div>
</section>

<div class="band" aria-label="Industries"><div class="wrap"><span>HVAC</span><i>/</i><span>Construction</span><i>/</i><span>Plumbing &amp; electrical</span><i>/</i><span>Radiant &amp; snowmelt</span><i>/</i><span>Home services</span></div></div>

{ONBOARD}

<section class="sec-dark" aria-labelledby="ai-h">
<div class="wrap"><div class="sec" style="display:flex;flex-direction:column;gap:36px">
<div class="sec-head" style="margin:0"><div><span class="eyebrow">What AI can do for your business</span><h2 id="ai-h">From manual work to processes that run themselves.</h2><p class="lede">I map how work flows today, find where hours get lost, and let AI take the repetitive part — while you approve what matters.</p></div><a class="btn btn-primary" href="/ai/">How AI fits your business →</a></div>
<div class="reveal" style="border:1.5px solid rgba(255,255,255,.35);padding:28px">{BA_PO}</div>
<div class="grid g4" style="font-size:15px">
<div style="border-top:2px solid var(--action);padding-top:12px"><b>Answers leads 24/7</b><p>WhatsApp, SMS and web chat</p></div>
<div style="border-top:2px solid rgba(255,255,255,.4);padding-top:12px"><b>Compares supplier bids</b><p>PDF quotes lined up item by item</p></div>
<div style="border-top:2px solid rgba(255,255,255,.4);padding-top:12px"><b>Drafts POs &amp; follow-ups</b><p>You approve, it sends</p></div>
<div style="border-top:2px solid rgba(255,255,255,.4);padding-top:12px"><b>Ask your business</b><p>Your numbers, in plain English</p></div>
</div>
</div></div>
</section>

<section class="sec" aria-labelledby="svc-h">
<div class="wrap">
<div class="sec-head"><div><h2 id="svc-h">Five services. One connected system.</h2></div><a class="link" href="/services/">All services →</a></div>
<div class="grid g2">
""" + "".join(f"""<a class="card card-link card-row reveal{' span-all' if s=='custom-software' else ''}" href="/services/{s}/">{ICON}<div class="stack" style="gap:8px"><h3>{n}</h3><p>{d}</p><span class="link">{n} →</span></div></a>
""" for (s, n), d, ICON in zip(SERVICES, [
    "Posts from your real jobs, account management and a monthly calendar you approve.",
    "Google &amp; Meta campaigns, landing pages, and every lead tracked to the booked job.",
    "One inbox for WhatsApp, SMS and web chat, an AI agent that books, n8n into your CRM.",
    "iOS &amp; Android apps for crews: jobs, checklists, photos, signatures — works offline.",
    "Your own platform for estimates, projects, schedules and crews, connected to QuickBooks."], [
    '<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="#0F2742" stroke-width="2" aria-hidden="true"><rect x="6" y="10" width="36" height="30" rx="2"/><path d="M6 18h36M14 6v8M34 6v8M14 26h6M26 26h8M14 32h12"/></svg>',
    '<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="#0F2742" stroke-width="2" aria-hidden="true"><path d="M8 40V28M18 40V20M28 40V24M38 40V10M6 42h36"/></svg>',
    '<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="#0F2742" stroke-width="2" aria-hidden="true"><path d="M8 40l2.5-7A16 16 0 1 1 16 38z"/><path d="M17 22h14M17 28h9"/></svg>',
    '<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="#0F2742" stroke-width="2" aria-hidden="true"><rect x="14" y="4" width="20" height="40" rx="3"/><path d="M21 38h6M19 14h10M19 20h10M19 26h6"/></svg>',
    '<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="#0F2742" stroke-width="2" aria-hidden="true"><rect x="6" y="8" width="36" height="24" rx="2"/><path d="M18 40h12M24 32v8M14 18l-4 4 4 4M34 18l4 4-4 4"/></svg>'])) + f"""</div>
</div>
</section>

<section class="sec" style="padding-top:0" aria-labelledby="case-h">
<div class="wrap">
<div class="card reveal" style="padding:0;flex-direction:row;flex-wrap:wrap;overflow:hidden;gap:0">
<div class="stack" style="flex:1 1 440px;min-width:0;padding:44px">
<span class="eyebrow">Case study · in production</span>
<h2 id="case-h" style="font-size:40px">An operations platform for a service company</h2>
<p>Projects, estimates, QuickBooks integration and a technician app replaced spreadsheets and disconnected tools.</p>
<div class="grid g2" style="border-top:1px solid var(--line);padding-top:16px;gap:16px 20px">
<div class="stat"><b>1+ year</b><span>in production, built week by week</span></div>
<div class="stat"><b>1 database</b><span>web, API and mobile app on one system</span></div>
<div class="stat"><b>Housecall Pro → own</b><span>migrated off Housecall Pro, data intact</span></div>
<div class="stat"><b>Two-way</b><span>QuickBooks sync, no retyping</span></div>
</div>
<span class="eyebrow blue" style="font-size:13px">Integrations I’ve built</span>
{INTEG_HTML}
<a class="link" href="/work/">Read the case study →</a>
</div>
<div class="paper-grid" aria-hidden="true" style="flex:1 1 360px;min-width:0;display:flex;align-items:center;justify-content:center;padding:32px;border-left:1px solid var(--line)">
<div class="phone"><b style="font-size:16px">Today · Crew 2</b><div class="job"><b>8:00</b> Service call<br><span class="muted">Customer · 1420 E Maple</span></div><div class="job now"><b>10:30</b> Install<br><span class="muted">Rooftop unit</span></div><div class="job"><b>2:00</b> Inspection</div><div class="go">Clock in</div></div>
</div>
</div>
</div>
</section>

<section class="sec-white sec" aria-labelledby="how-h">
<div class="wrap">
<h2 id="how-h" style="margin-bottom:40px">How the work runs, every week</h2>
<div class="grid g4" style="gap:0">
<div style="border-top:4px solid var(--ink);padding:20px 20px 0 0"><b style="font-family:var(--display);font-size:40px;color:var(--action)">1</b><h3 style="font-size:21px">Walkthrough</h3><p class="muted">We map how work flows today.</p></div>
<div style="border-top:4px solid var(--ink);padding:20px 20px 0"><b style="font-family:var(--display);font-size:40px;color:var(--action)">2</b><h3 style="font-size:21px">Build weekly</h3><p class="muted">Replies in under 2 hours.</p></div>
<div style="border-top:4px solid var(--ink);padding:20px 20px 0"><b style="font-family:var(--display);font-size:40px;color:var(--action)">3</b><h3 style="font-size:21px">Weekly demo</h3><p class="muted">See it working every week.</p></div>
<div style="border-top:4px solid var(--action);padding:20px 0 0 20px"><b style="font-family:var(--display);font-size:40px;color:var(--action)">4</b><h3 style="font-size:21px">Weekly invoice</h3><p class="muted">You own the code. Backups in your office.</p></div>
</div>
</div>
</section>

{FIT}
{cta_dark()}"""
page("/", "TheDevPro — Custom software, AI & marketing for service businesses",
     "Leads, WhatsApp, CRM, estimates, crews and QuickBooks connected into one system you own. Senior developer, 20+ years, Utah.", "", home)

# ---------- AI ----------
ai = f"""<section class="sec-dark dark-hero">
<div class="bp" aria-hidden="true">
<div class="bn" style="left:54%;top:62px">LEAD IN</div>
<div class="wire-h" style="left:calc(54% + 92px);width:calc(9% - 40px);top:80px"></div>
<div class="dm" style="left:calc(63% + 10px);top:54px"></div><div class="dm-label" style="left:calc(63% + 10px);top:70px">AI</div>
<div class="wire-h" style="left:calc(63% + 76px);width:calc(9% - 30px);top:80px"></div>
<div class="bn" style="left:73%;top:62px">CRM DEAL</div>
<div class="wire-v" style="left:calc(63% + 36px);top:120px;height:90px"></div>
<div class="bn" style="left:calc(63% - 8px);top:212px">YOUR TEAM</div>
<div class="wire-v" style="left:calc(73% + 50px);top:100px;height:110px"></div>
<div class="bn hot" style="left:73%;top:212px">ESTIMATE</div>
<div class="wire-h" style="left:calc(73% + 106px);width:calc(9% - 60px);top:230px"></div>
<div class="bn hot" style="left:82%;top:212px">PO · 5 MIN</div>
<div class="wire-v" style="left:calc(82% + 50px);top:250px;height:90px"></div>
<div class="bn" style="left:82%;top:342px">QUICKBOOKS</div>
<div class="bn" style="left:calc(63% - 8px);top:342px">SCHEDULE</div>
<div class="wire-v" style="left:calc(63% + 36px);top:380px;height:70px"></div>
<div class="bn" style="left:calc(63% - 8px);top:452px">KPIs · ASK YOUR BUSINESS</div>
<div class="tag">DWG 010 — MANUAL → AUTOMATED</div>
</div>
<div class="wrap"><div class="copy">
<span class="eyebrow">AI for service businesses</span>
<h1>Turn the work you do by hand into work that runs itself.</h1>
<p class="lede">AI that lives inside your process — reading estimates, drafting purchase orders, answering customers, and showing you where the money and the hours go. You stay in control of every decision.</p>
<div class="row"><a class="btn btn-primary" href="/contact/">Map my process — free call</a><a class="btn btn-light" href="{WA}" rel="noopener">Message me on WhatsApp</a></div>
</div></div>
</section>

<section class="sec" aria-labelledby="ba-h">
<div class="wrap stack" style="gap:28px">
<div class="stack" style="gap:12px"><span class="eyebrow">Before and after</span><h2 id="ba-h">Same job. Fewer steps. No retyping.</h2><p class="lede">Watch the dots: the gray one walks your process the way it runs today, the orange one runs it automated.</p></div>
<div class="card reveal"><div style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap"><h3>1 · Purchase orders from an approved estimate</h3><span class="muted" style="font-family:var(--display);letter-spacing:.08em">DWG 011</span></div>{BA_PO}</div>
<div class="grid g2">
<div class="card reveal"><h3>2 · Comparing supplier bids</h3><p>Drop in the PDF quotes. AI lines them up item by item, flags what’s missing or priced differently, and recommends one. You decide.</p></div>
<div class="card reveal"><h3>3 · Leads that arrive after hours</h3><p>A WhatsApp message at 9 p.m. gets answered in seconds, qualified and booked — instead of waiting until someone checks in the morning.</p></div>
</div>
</div>
</section>

<section class="sec" style="padding-top:0" aria-labelledby="calc-h">
<div class="wrap">
<form class="calc reveal" data-calc onsubmit="return false">
<div class="in">
<span class="eyebrow">Your numbers</span>
<h2 id="calc-h" style="font-size:36px">How many hours would purchase orders give back?</h2>
<label>Purchase orders per week: <span data-pos>10</span><input type="range" name="pos" min="1" max="60" value="10"></label>
<label>Minutes each one takes today: <span data-min>30</span><input type="range" name="min" min="10" max="90" step="5" value="30"></label>
<p class="small muted">Assumes about 5 minutes per PO once automated (review and approve).</p>
</div>
<div class="out sec-dark">
<div><div class="big"><span data-weekly>4.2</span> h</div><p>back every week</p></div>
<div><div class="mid"><span data-yearly>208</span> h</div><p>per year (50 weeks)</p></div>
<a class="btn btn-primary" href="/contact/" style="align-self:flex-start">Map this with me →</a>
</div>
</form>
</div>
</section>

<section class="sec sec-white" aria-labelledby="ask-h">
<div class="wrap grid g2" style="align-items:center;gap:56px">
<div class="stack"><span class="eyebrow">Ask your business</span><h2 id="ask-h">Get answers in plain English, from your own numbers.</h2><p class="lede">Jobs, estimates, hours and invoices in one place means you can simply ask — on your phone, in WhatsApp, or in your dashboard.</p></div>
<div class="paper-grid" style="border:1.5px solid var(--ink);padding:24px">
<div class="chat"><span class="chat-meta">EXAMPLE</span>
<div class="bubble in" style="align-self:flex-end;font-weight:600">Which jobs went over on labor this month?</div>
<div class="bubble out" style="align-self:flex-start;max-width:100%">Two jobs are over their estimated hours: the radiant install and the driveway snowmelt. Most of the extra time is driving to pick up missing materials.</div>
</div></div>
</div>
</section>

<section class="sec" aria-labelledby="find-h">
<div class="wrap">
<h2 id="find-h" style="margin-bottom:36px">How I find what to automate</h2>
<ol class="grid g5 lit5" style="list-style:none;margin:0;padding:0">
<li class="card"><b style="font-family:var(--display);font-size:32px;color:var(--action)">01</b><b>Map the process</b><p class="small">Draw how the work flows today, step by step.</p></li>
<li class="card"><b style="font-family:var(--display);font-size:32px;color:var(--action)">02</b><b>Find the bottleneck</b><p class="small">Where hours, money or customers get lost.</p></li>
<li class="card"><b style="font-family:var(--display);font-size:32px;color:var(--action)">03</b><b>Automate the repetitive</b><p class="small">AI and n8n take the copy-paste work.</p></li>
<li class="card"><b style="font-family:var(--display);font-size:32px;color:var(--action)">04</b><b>Keep a person in charge</b><p class="small">Nothing goes out without your approval.</p></li>
<li class="card"><b style="font-family:var(--display);font-size:32px;color:var(--action)">05</b><b>Measure it</b><p class="small">Hours saved, shown in the weekly demo.</p></li>
</ol>
</div>
</section>

<section class="sec" style="padding-top:0" aria-labelledby="prob-h">
<div class="wrap">
<h2 id="prob-h" style="margin-bottom:28px">Problems AI is good at solving</h2>
<div class="grid g3">
<div class="card"><b>Missed calls and messages</b><p>Answered and booked, day or night.</p></div>
<div class="card"><b>Retyping between apps</b><p>Data entered once, everywhere at once.</p></div>
<div class="card"><b>Slow quotes and POs</b><p>Drafted from the estimate in minutes.</p></div>
<div class="card"><b>No view of the whole business</b><p>KPIs and plain-English answers.</p></div>
<div class="card"><b>Know-how in one person’s head</b><p>Procedures written down and searchable.</p></div>
<div class="card"><b>Forgotten follow-ups</b><p>Reminders and nudges sent automatically.</p></div>
</div>
</div>
</section>

{cta_dark("Your data stays yours.", "Runs on a server you control, with a backup in your own office. You own the code — and if something happens to me, everything keeps running.")}"""
page("/ai/", "AI for service businesses — from manual work to automated processes | TheDevPro",
     "AI inside your process: purchase orders in minutes, supplier bids compared, leads answered 24/7, and plain-English answers from your own numbers.", "ai", ai)

# ---------- SERVICES ----------
def svc_page(slug, name, title, desc, h1, lede, includes, extra, faq):
    inc = "".join(f'<div class="card reveal"><b style="font-size:18px">{a}</b><p>{b}</p></div>' for a, b in includes)
    fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    others = "".join(f'<a class="chip" href="/services/{s}/">{n}</a>' for s, n in SERVICES if s != slug)
    body = f"""<section class="sec-dark dark-hero">
<div class="bp" aria-hidden="true">{extra.get('bp','')}</div>
<div class="wrap"><div class="copy">
<nav aria-label="Breadcrumb" class="small" style="color:var(--on-dark-2)"><a href="/services/">Services</a> / {name}</nav>
<h1>{h1}</h1>
<p class="lede">{lede}</p>
<div class="row"><a class="btn btn-primary" href="/contact/">Book a free 30-min call</a><a class="btn btn-light" href="{WA}" rel="noopener">WhatsApp</a></div>
</div></div>
</section>
{extra.get('after_hero','')}
<section class="sec" aria-labelledby="inc-h"><div class="wrap">
<h2 id="inc-h" style="margin-bottom:28px">What’s included</h2>
<div class="grid g3">{inc}</div>
</div></section>
{extra.get('middle','')}
<section class="sec sec-white" aria-labelledby="faq-h"><div class="wrap grid g2" style="gap:48px">
<div class="stack"><h2 id="faq-h">Common questions</h2><p class="muted">Other services:</p><div class="chips">{others}</div></div>
<div style="border-top:2px solid var(--ink)">{fq}</div>
</div></section>
{cta_dark()}"""
    page(f"/services/{slug}/", title, desc, "services", body)

BP_CHAT = """<div class="bn" style="left:60%;top:56px">WHATSAPP 9:47 PM</div>
<div class="wire-v" style="left:calc(60% + 70px);top:94px;height:70px"></div>
<div class="dm" style="left:calc(60% + 44px);top:166px"></div><div class="dm-label" style="left:calc(60% + 44px);top:182px">AI</div>
<div class="wire-h" style="left:calc(60% + 104px);width:calc(13% - 70px);top:192px"></div>
<div class="bn hot" style="left:73%;top:174px">BOOKED 8–10 AM</div>
<div class="wire-h" style="left:calc(60% - 90px);width:120px;top:192px"></div>
<div class="bn" style="left:calc(60% - 200px);top:174px">YOUR TEAM</div>
<div class="wire-v" style="left:calc(73% + 70px);top:212px;height:70px"></div>
<div class="bn" style="left:73%;top:284px">CRM DEAL · n8n</div>
<div class="tag">DWG 004 — AFTER-HOURS LEAD</div>"""

def bp_line(labels, tag):
    out, x = [], 56
    for i, (lab, hot) in enumerate(labels):
        out.append(f'<div class="bn{" hot" if hot else ""}" style="left:{x}%;top:{70 + i*90}px">{lab}</div>')
        if i < len(labels) - 1:
            out.append(f'<div class="wire-v" style="left:calc({x}% + 40px);top:{106 + i*90}px;height:54px"></div>')
    out.append(f'<div class="tag">{tag}</div>')
    return "".join(out)

svc_page("whatsapp-crm-ai-agents", "WhatsApp, CRM & AI agents",
    "WhatsApp, CRM & AI agents for service businesses | TheDevPro",
    "One inbox for WhatsApp, SMS and web chat with Chatwoot, an AI agent that answers and books, and n8n automations into your CRM.",
    "Never miss a customer message again.",
    "WhatsApp, SMS and web chat in one Chatwoot inbox, an AI agent that answers and books visits after hours, and n8n automations that put every lead into your CRM.",
    [("WhatsApp Business", "Official API on your number, approved templates for reminders and follow-ups."),
     ("Chatwoot inbox", "Every channel and every teammate in one place — on your server, not rented."),
     ("AI agent", "Trained on your services, areas and hours. Books visits and hands off to a person when unsure."),
     ("CRM that fills itself", "Contacts, deals and notes created from conversations — no copy-paste."),
     ("n8n automations", "Missed-call text-back, reminders, review requests, estimate follow-ups."),
     ("Your data, your server", "Self-hosted and backed up. You own the setup and the history.")],
    {"bp": BP_CHAT, "middle": """<section class="sec" style="padding-top:0"><div class="wrap grid g2" style="align-items:center;gap:48px">
<div class="stack"><span class="eyebrow">Example</span><h2>A 9:47 p.m. message, booked before morning.</h2><p class="lede">The AI agent answers from what you approve, books the visit, and n8n creates the CRM deal and calendar entry.</p></div>
<div class="card"><div class="chat"><span class="chat-meta">WHATSAPP · 9:47 PM</span>
<div class="bubble in">Hi! My heating stopped. Can someone come tomorrow?</div>
<div class="bubble out">Sorry to hear that. I can book a technician tomorrow 8–10 a.m. or 1–3 p.m. What’s the address?</div>
<div class="bubble in">8–10 please. 1420 E Maple St.</div>
<div class="bubble out">Booked for 8–10 a.m. You’ll get a text when the tech is on the way.</div></div>
<p class="small" style="border-top:1px solid var(--line);padding-top:10px;margin-top:6px"><b style="color:var(--done)">→</b> CRM deal created · calendar visit added</p></div>
</div></section>"""},
    [("What if the AI doesn’t know the answer?", "It hands the chat to a person on your team and tells the customer someone will follow up."),
     ("Can I keep my current CRM?", "Yes. n8n connects to most CRMs. If you don’t have one, your workspace includes one."),
     ("Where is my data stored?", "On a server you control, with a backup in your office. Nothing is locked in a vendor’s account.")])

svc_page("mobile-apps", "Mobile apps",
    "Mobile apps for crews and customers — iOS & Android | TheDevPro",
    "iOS and Android apps for technicians and crews: schedules, checklists, photos, signatures and clock-in, connected to your office system. Works offline.",
    "Mobile apps your crews actually use.",
    "iOS and Android apps for technicians, crews and customers — schedules, checklists, photos, signatures and clock-in, connected to the same system your office uses. Works without signal.",
    [("Works offline", "Basements and rural jobs included. Syncs when signal returns."),
     ("Photos, checklists, signatures", "Proof of work attached to the job and the invoice."),
     ("Clock-in & time", "Hours per job, ready for payroll."),
     ("Push notifications", "New jobs, schedule changes, customer messages."),
     ("One backend", "Same data as the office app, CRM and QuickBooks."),
     ("App Store & Google Play", "I handle publishing, updates and store reviews.")],
    {"bp": bp_line([("TODAY'S JOBS", False), ("CHECKLIST", False), ("PHOTOS + SIGNATURE", True), ("INVOICE", False)], "DWG 020 — JOB IN THE FIELD"),
     "middle": """<section class="sec" style="padding-top:0"><div class="wrap grid g2" style="gap:48px;align-items:center">
<div class="stack"><h2>Built on experience shipping apps in production.</h2><p class="lede">Years maintaining a corporate app used in several countries — biometric login, updates without waiting for the store, analytics — plus React Native apps for field crews.</p>
<div class="chips"><span class="chip">React Native</span><span class="chip">Ionic / Angular</span><span class="chip">Capacitor</span><span class="chip">.NET API</span><span class="chip">Offline sync</span><span class="chip">Biometrics</span></div></div>
<div style="display:flex;justify-content:center" aria-hidden="true"><div class="phone"><b style="font-size:16px">Service call</b><span class="muted">Checklist</span><div class="job">✓ Inspect system</div><div class="job">✓ Replace part</div><div class="job now">Photos before / after</div><div class="job">Customer signature</div><div class="go">Complete &amp; invoice</div></div></div>
</div></section>"""},
    [("iOS, Android, or both?", "Both, from one codebase. You get the source code and the store accounts in your name."),
     ("Does it work without signal?", "Yes. Jobs, checklists and photos are saved on the phone and sync when the signal comes back."),
     ("Can it connect to what we already use?", "Yes — your office system, QuickBooks, or a custom platform built with it.")])

svc_page("custom-software", "Custom software",
    "Custom software for service businesses — estimates, projects, QuickBooks | TheDevPro",
    "Your own platform for clients, estimates, projects, schedules and crews, connected to QuickBooks. Built on a proven core, weekly demos, you own the code.",
    "Software that fits how your business actually works.",
    "Clients, estimates, projects with phases, schedules, crews and invoices — in one system connected to QuickBooks, built on a proven core so you don’t pay to rebuild the basics.",
    [("Clients & estimates", "Estimates from your QuickBooks prices; approval turns them into projects."),
     ("Projects with phases", "Templates you can edit per job; schedules that move when the job moves."),
     ("QuickBooks, two-way", "Customers, items, invoices and payments without retyping."),
     ("Dashboards", "Jobs, hours and money at a glance — plus “ask your business”."),
     ("Migrations", "Move off rented platforms like Housecall Pro with your data intact."),
     ("Integrations", "Oasis, Twilio, SendGrid, WhatsApp, n8n and your other tools.")],
    {"bp": bp_line([("CLIENT", False), ("ESTIMATE", False), ("APPROVED", True), ("PROJECT + PHASES", False), ("QUICKBOOKS", False)], "DWG 030 — CLIENT → INVOICE"),
     "after_hero": ONBOARD},
    [("Why not just use ServiceTitan or Jobber?", "If they fit, use them. Custom makes sense when your process doesn’t fit a template or you’re paying for tools that don’t talk."),
     ("Who owns the code?", "You do, with shared rights: you can keep, change or sell it, and I can reuse the general parts."),
     ("What if something happens to you?", "Your system runs on a server you control, with backups in your office and documentation another developer can follow.")])

svc_page("social-media", "Social media",
    "Social media management for contractors and service businesses | TheDevPro",
    "Content from your real jobs, account management and a monthly posting calendar you approve.",
    "Show up every week without thinking about it.",
    "Content from your real jobs, account management and a monthly posting calendar you approve — so customers see your work, not a stock photo.",
    [("Monthly calendar", "Planned a month ahead; you approve before anything posts."),
     ("Content from your jobs", "Before/after photos and short videos from your crews."),
     ("Account management", "Facebook, Instagram, Google Business Profile."),
     ("Replies & reviews", "Comments answered, review requests sent after each job."),
     ("Monthly report", "What posted, what worked, what’s next — one page."),
     ("Connected", "Messages from social land in the same inbox as WhatsApp.")],
    {"bp": bp_line([("PLAN", False), ("CREATE", False), ("APPROVE", True), ("PUBLISH", False)], "DWG 040 — MONTHLY CALENDAR")},
    [("Do I need to provide photos?", "Your crews snap them on the job; I turn them into posts. The field app can collect them automatically."),
     ("How many posts per month?", "We set it together on the first call based on your goals."),
     ("Will you post without asking?", "No. You approve the monthly calendar first.")])

svc_page("advertising", "Advertising",
    "Google & Meta ads for service businesses, tracked to the booked job | TheDevPro",
    "Google and Meta campaigns, landing pages that convert, and every lead tracked from click to booked job.",
    "Every lead tracked from click to booked job.",
    "Google and Meta campaigns, landing pages built to convert, and lead tracking that shows which dollars turned into jobs.",
    [("Google & Meta campaigns", "Set up, run and adjusted weekly."),
     ("Landing pages", "Fast pages built for one offer and one action."),
     ("Lead tracking", "Every lead tagged with its source, all the way to the job."),
     ("Speed to lead", "New leads get an instant text or WhatsApp reply."),
     ("Weekly numbers", "Cost per lead and per booked job, in plain English."),
     ("No black box", "Ad accounts in your name — you keep them.")],
    {"bp": bp_line([("AD", False), ("LANDING PAGE", False), ("LEAD + INSTANT REPLY", True), ("BOOKED JOB", False)], "DWG 050 — CLICK → JOB")},
    [("Who owns the ad accounts?", "You do. I work inside your accounts, so nothing is lost if we stop."),
     ("What budget do I need?", "We size it on the first call from your area, services and goals."),
     ("How fast do leads get answered?", "Instantly — by text or WhatsApp — then handed to your team or the AI agent.")])

# services index
svc_idx = f"""<section class="sec-dark dark-hero">
<div class="bp" aria-hidden="true">{bp_line([("GET FOUND", False), ("WIN THE JOB", False), ("RUN IT", True)], "DWG 000 — ONE CONNECTED SYSTEM")}</div>
<div class="wrap"><div class="copy"><span class="eyebrow">Services</span><h1>Get found. Win the job. Run it on software that fits.</h1>
<p class="lede">Five services that work alone or together — all connected to one system you own.</p></div></div>
</section>
<section class="sec"><div class="wrap grid g2">
""" + "".join(f'<a class="card card-link reveal" href="/services/{s}/"><h2 style="font-size:30px">{n}</h2><p>{d}</p><span class="link">{n} →</span></a>' for (s, n), d in zip(SERVICES, [
    "Content from your real jobs, account management and a monthly calendar.",
    "Google &amp; Meta campaigns, landing pages, lead tracking to the booked job.",
    "Chatwoot inbox for WhatsApp, SMS and chat, an AI agent that books, n8n into your CRM.",
    "iOS &amp; Android apps for crews and customers, offline-ready.",
    "Estimates, projects, schedules and crews, connected to QuickBooks."])) + f"""
<a class="card card-link reveal" href="/ai/" style="background:var(--ink);color:#fff;border-color:var(--ink)"><h2 style="font-size:30px">AI for your business</h2><p style="color:var(--on-dark)">From manual work to processes that run themselves.</p><span class="link" style="color:var(--warm)">How AI fits →</span></a>
</div></section>
{cta_dark()}"""
page("/services/", "Services — social media, ads, WhatsApp & AI, mobile apps, custom software | TheDevPro",
     "Five services that work alone or together, all connected to one system you own.", "services", svc_idx)

# ---------- WORK ----------
work = f"""<section class="sec-dark dark-hero">
<div class="bp" aria-hidden="true">{bp_line([("HOUSECALL PRO", False), ("MIGRATION", True), ("ONE DATABASE", False), ("WEB · API · MOBILE", False)], "DWG 100 — RENTED → OWNED")}</div>
<div class="wrap"><div class="copy"><span class="eyebrow">Case study · in production</span><h1>An operations platform for a service company.</h1>
<p class="lede">A growing field-service business was running on spreadsheets and rented software. Today it runs on its own platform — built week by week, live in production.</p></div></div>
</section>
<section class="sec"><div class="wrap grid g4">
<div class="card stat"><b>1+ year</b><span>in production</span></div>
<div class="card stat"><b>1 database</b><span>web, API and mobile app</span></div>
<div class="card stat"><b>Housecall Pro → own</b><span>data migrated, nothing lost</span></div>
<div class="card stat"><b>Two-way</b><span>QuickBooks sync</span></div>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap grid g3">
<div class="card"><h3>The problem</h3><p>Estimates in spreadsheets, scheduling in one app, accounting in another, and crews calling the office for details. Nobody saw the whole job.</p></div>
<div class="card"><h3>What we built</h3><p>Clients, estimates, projects, scheduling and invoicing in one web app, a technician app for the field, and QuickBooks connected both ways.</p></div>
<div class="card"><h3>How it was delivered</h3><p>Small weekly releases with a live demo every week, code reviewed on every change, and releases to production at night.</p></div>
</div></section>
<section class="sec sec-white"><div class="wrap stack"><span class="eyebrow blue">Integrations I’ve built</span><h2>Connected to the tools service companies already use.</h2>{INTEG_HTML}</div></section>
{cta_dark("Want the same for your company?")}"""
page("/work/", "Case study: an operations platform for a service company | TheDevPro",
     "From spreadsheets and Housecall Pro to an owned platform: one database for web, API and mobile, two-way QuickBooks sync, live in production.", "work", work)

# ---------- PROCESS ----------
process = f"""<section class="sec-dark dark-hero">
<div class="bp" aria-hidden="true">{bp_line([("MON · INVOICE", False), ("TUE · LIVE DEMO", True), ("WED–SUN · BUILD", False)], "DWG 200 — THE WEEKLY LOOP")}</div>
<div class="wrap"><div class="copy"><span class="eyebrow">Process</span><h1>A weekly rhythm you can see.</h1>
<p class="lede">You see working software every week and pay for what you saw. No long contract, no black box.</p></div></div>
</section>
{ONBOARD}
<section class="sec"><div class="wrap">
<h2 style="margin-bottom:28px">Every week</h2>
<ol class="grid g4 lit" style="list-style:none;margin:0;padding:0">
<li class="card"><span class="num">1</span><h3 style="font-size:21px">Build</h3><p>Small changes, each reviewed before it reaches you.</p></li>
<li class="card"><span class="num">2</span><h3 style="font-size:21px">Under 2-hour replies</h3><p>You talk to the developer, not a ticket queue.</p></li>
<li class="card"><span class="num">3</span><h3 style="font-size:21px">Live demo</h3><p>Every Tuesday: what’s new, working, on screen.</p></li>
<li class="card"><span class="num hot">4</span><h3 style="font-size:21px">Simple invoice</h3><p>Every Monday, for the week before. Stop any week.</p></li>
</ol>
</div></section>
<section class="sec sec-white"><div class="wrap grid g3">
<div class="card"><h3>Quality on every change</h3><p>Each change has its own branch, automated checks and an AI-assisted code review, and a senior developer signs off before it ships.</p></div>
<div class="card"><h3>Releases at night</h3><p>Tested in staging first, released when nobody is using the system.</p></div>
<div class="card"><h3>You own everything</h3><p>Shared code rights, accounts in your name, a backup in your office and documentation another developer can follow.</p></div>
</div></section>
{FIT}
{cta_dark()}"""
page("/process/", "How I work — weekly demos, weekly invoices, you own the code | TheDevPro",
     "Free call, connect QuickBooks, your own workspace, then a live demo and a simple invoice every week. Stop any week. You own the code.", "process", process)

# ---------- ABOUT ----------
about = f"""<section class="sec-dark dark-hero">
<div class="bp" aria-hidden="true">{bp_line([(".NET · REACT", False), ("MOBILE", False), ("AI · n8n", True), ("SELF-HOSTED", False)], "DWG 300 — 20+ YEARS")}</div>
<div class="wrap"><div class="copy"><span class="eyebrow">About</span><h1>Hi, I’m Daniel Kalasic.</h1>
<p class="lede">Senior full-stack developer with 20+ years building production software. I work directly with owners of service businesses — one developer you can call, backed by a careful process and an AI-assisted team I supervise.</p></div></div>
</section>
<section class="sec"><div class="wrap grid g2" style="gap:48px">
<div class="stack"><h2>What I bring</h2>
<ul class="clean"><li>Platforms in production for service companies: estimates, projects, scheduling, QuickBooks</li><li>Years shipping a corporate mobile app used in several countries</li><li>Integrations: QuickBooks, Housecall Pro, Oasis, Twilio, SendGrid, WhatsApp, Chatwoot, n8n</li><li>My own servers, CI and backups — I don’t depend on rented tools</li><li>English and Spanish</li></ul></div>
<div class="stack"><h2>Stack</h2><div class="chips"><span class="chip">.NET / C#</span><span class="chip">React · Next.js</span><span class="chip">Angular / Ionic</span><span class="chip">React Native</span><span class="chip">PostgreSQL · SQL Server</span><span class="chip">n8n</span><span class="chip">Chatwoot</span><span class="chip">Twilio · SendGrid</span><span class="chip">Docker · self-hosted CI</span><span class="chip">AI agents</span></div>
<p class="lede">Hablo español — happy to work with your team in either language.</p></div>
</div></section>
{cta_dark("Let’s talk about your business.")}"""
page("/about/", "About Daniel Kalasic — senior full-stack developer, Utah | TheDevPro",
     "20+ years building production software. Platforms for service companies, mobile apps, integrations and AI. English & Español.", "about", about)

# ---------- CONTACT ----------
contact = f"""<section class="sec-dark dark-hero">
<div class="bp" aria-hidden="true">{bp_line([("YOUR MESSAGE", False), ("REPLY < 2 H", True), ("FREE 30-MIN CALL", False)], "DWG 400 — CONTACT")}</div>
<div class="wrap"><div class="copy"><span class="eyebrow">Contact</span><h1>Tell me what’s slowing your business down.</h1><p class="lede">I reply within 2 hours on business days.</p></div></div>
</section>
<section class="sec"><div class="wrap grid g2" style="gap:48px;align-items:start">
<div class="stack">
<a class="card card-link" href="{WA}" rel="noopener"><b style="font-size:20px;color:var(--done)">WhatsApp</b><span class="muted">Fastest — message me now</span></a>
<a class="card card-link" href="tel:{PHONE}"><b style="font-size:20px">{PHONE_TXT}</b><span class="muted">Call or text</span></a>
<a class="card card-link" href="{MAIL}"><b style="font-size:20px">{EMAIL}</b><span class="muted">Email</span></a>
</div>
<form class="form card" data-mailto action="{MAIL}" method="post" enctype="text/plain">
<h2 style="font-size:30px">Write me</h2>
<div class="grid g2" style="gap:14px"><label>Name<input name="name" autocomplete="name" required></label><label>Company<input name="company" autocomplete="organization"></label></div>
<label>Phone<input name="phone" type="tel" autocomplete="tel"></label>
<label>I’m interested in<select name="service"><option>Not sure yet</option><option>AI &amp; automation</option><option>WhatsApp, CRM &amp; AI agents</option><option>Custom software</option><option>Mobile app</option><option>Advertising</option><option>Social media</option></select></label>
<label>What’s going on?<textarea name="message" rows="5"></textarea></label>
<button class="btn btn-primary" type="submit">Open email draft →</button>
<p class="small muted">Opens your email app with everything filled in. Nothing is stored on this site.</p>
</form>
</div></section>"""
page("/contact/", "Contact — WhatsApp, call or email | TheDevPro",
     "Message on WhatsApp, call 801.376.2721 or email hello@thedevpro.io. Replies within 2 hours on business days.", "contact", contact)

# ---------- 404 ----------
write("/404", head("Page not found | TheDevPro", "This page doesn’t exist.", "/404", "noindex, nofollow") + header("") +
      f"""<section class="sec"><div class="wrap stack"><h1>That page doesn’t exist.</h1><p class="lede">If someone sent you a link to a proposal, check it with them — or reach me directly.</p><div class="row"><a class="btn btn-primary" href="/">Go home</a><a class="btn btn-outline" href="{WA}" rel="noopener">WhatsApp</a></div></div></section>""" + footer())

# ---------- sitemap ----------
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in PAGES:
        f.write(f"  <url><loc>{SITE}{p}</loc><lastmod>2026-11-11</lastmod></url>\n")
    f.write("</urlset>\n")
print("built", len(PAGES), "pages")
