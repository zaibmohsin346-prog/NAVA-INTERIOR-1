"""Builds crawlable static pages for search engines and AI assistants (SEO + GEO).

Run after any change to services in index.html:
    node tools/extract.js && python3 tools/build_geo.py && node tools/prerender.js
Creates services/<id>/index.html, services/index.html, areas/<emirate>/index.html,
llms.txt, sitemap.xml and robots.txt.
"""
import html, json, os, urllib.parse, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://navainteriordubai.com"
PHONE, PHONE_WA, EMAIL = "+971 56 752 2656", "971567522656", "info@navainteriordubai.com"
EMIRATES = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
D = json.load(open(os.path.join(ROOT, "tools", "data.json")))
SV = D["services"]
e = lambda s: html.escape(str(s), quote=True)
wa = lambda t: f"https://wa.me/{PHONE_WA}?text={urllib.parse.quote(t)}"
TODAY = datetime.date.today().isoformat()

BUSINESS = {"@type": "HomeAndConstructionBusiness", "@id": SITE + "/#business", "name": "NAVA INTERIOR",
            "url": SITE + "/", "telephone": "+971567522656", "email": EMAIL,
            "logo": SITE + "/brand/logo/nava-interior-icon.png", "image": SITE + "/img/hero-kitchen-marina.jpg",
            "areaServed": [{"@type": "City", "name": c} for c in EMIRATES],
            "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"}}

AREA_INFO = {
 "dubai": ("Dubai", ["Dubai Marina", "JLT", "JVC", "Downtown Dubai", "Business Bay", "Palm Jumeirah", "Dubai Hills", "Arabian Ranches", "Al Barsha", "Mirdif"],
   "From high-rise apartments in Dubai Marina and Downtown to family villas in Arabian Ranches and Dubai Hills, we handle repaints, false ceilings, wall moulding, joinery, bathroom and kitchen renovation, waterproofing, pools and AC. We work around building rules, book service lifts and handle the NOC paperwork most Dubai communities need."),
 "abu-dhabi": ("Abu Dhabi", ["Al Reem Island", "Saadiyat Island", "Yas Island", "Khalifa City", "Al Raha", "Abu Dhabi city"],
   "We serve apartments and villas across Abu Dhabi, including Al Reem, Saadiyat, Yas Island and Khalifa City, for interior fit-out, painting, ceilings, moulding, tiling and marble, waterproofing, pergolas and pool work, with the same in-house team and written quotes."),
 "sharjah": ("Sharjah", ["Al Nahda", "Al Majaz", "Al Khan", "Muwaileh", "Aljada"],
   "In Sharjah we repaint and renovate apartments and villas, fit false ceilings and moulding, fix leaks and waterproof roofs and bathrooms, and service AC and water heaters."),
 "ajman": ("Ajman", ["Ajman Downtown", "Al Nuaimiya", "Al Rashidiya", "Al Jurf"],
   "In Ajman we take on painting, gypsum ceilings, tiling, waterproofing, carpentry and full renovations for apartments, villas and shops."),
}

CSS = """*{box-sizing:border-box}body{margin:0;background:#FFFFFF;color:#1C1D20;font:300 17px/1.75 Jost,"Segoe UI",system-ui,sans-serif}
a{color:#8A6A35}img{max-width:100%;display:block}
.w{max-width:1100px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header{border-bottom:1px solid #E6E0D6;background:#fff;position:sticky;top:0;z-index:5}
header .w{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-block:14px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:#2B2E33;font:400 18px Michroma,"Segoe UI",sans-serif;letter-spacing:.12em}
.brand b{color:#0A2C8C;font-weight:400}.brand img{width:34px;height:34px}
nav{display:flex;gap:18px;flex-wrap:wrap;font-size:13px;letter-spacing:.14em;text-transform:uppercase}nav a{color:#1C1D20;text-decoration:none}
.btn{display:inline-block;background:linear-gradient(135deg,#D9B77A,#A9824A);color:#141009;text-decoration:none;padding:13px 26px;font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:500}
.btn.o{background:none;border:1px solid #1C1D20;color:#1C1D20}
.hd{background:#F7F4EF;border-bottom:1px solid #E6E0D6;padding-block:56px}
.crumb{font-size:14px;color:#6B6760}.crumb a{color:#6B6760}
.eb{font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:#A9824A;font-weight:500}
h1,h2{font-family:"Cormorant Garamond",Georgia,serif;font-weight:400;line-height:1.1;margin:.3em 0}
h1{font-size:clamp(34px,6vw,58px)}h2{font-size:clamp(26px,4vw,36px);margin-top:1.6em}h3{font-weight:500;margin:.2em 0}
.lead{font-size:19px;color:#4A4741;max-width:65ch}
.ph{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:36px}.ph img{width:100%;aspect-ratio:4/3;object-fit:cover}
.ph.one{grid-template-columns:1fr}.ph.one img{aspect-ratio:16/8}
main section{max-width:780px}
ul.chk{padding-left:1.2em}ol.st li{margin-bottom:10px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;max-width:none!important}
.cards a{display:block;padding:16px 18px;border:1px solid #E6E0D6;text-decoration:none;color:#1C1D20;background:#fff}
.cards a:hover{border-color:#C9A86A}.cards small{display:block;color:#6B6760;font-size:14px;line-height:1.5;margin-top:4px}
details{border-bottom:1px solid #E6E0D6;padding:12px 0}summary{cursor:pointer;font-weight:500}
.cta{background:#14161A;color:#F6F1E8;padding:36px;margin:56px 0;display:flex;flex-wrap:wrap;gap:18px;align-items:center;justify-content:space-between;max-width:none!important}
.cta h2{margin:0;color:#F6F1E8}.cta p{margin:6px 0 0;color:#CFC8BC}
footer{background:#14161A;color:#CFC8BC;padding-block:36px;font-size:15px;margin-top:40px}footer a{color:#E3C68F}
@media (max-width:600px){.ph{grid-template-columns:1fr}.cta{padding:24px}}"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400&family=Jost:wght@300;500&family=Michroma&display=swap">'

def page(path, title, desc, body, ld, img="/img/hero-kitchen-marina.jpg"):
    url = SITE + path
    doc = f"""<!doctype html>
<html lang="en"><head><!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-NVBHQ6WM');</script>
<!-- End Google Tag Manager --><!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8FCP3364BW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-8FCP3364BW',{{page_location:location.href}});</script>
<!-- End Google Analytics 4 --><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="NAVA INTERIOR"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="{SITE}{img}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/brand/logo/nava-interior-icon-transparent.png">{FONTS}
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":ld},ensure_ascii=False)}</script>
</head><body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NVBHQ6WM" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
<header><div class="w"><a class="brand" href="/"><img src="/brand/logo/nava-interior-icon-transparent.png" alt="" width="34" height="34"><span><b>NAVA</b> INTERIOR</span></a>
<nav><a href="/">Home</a><a href="/services/">Services</a><a href="/#gallery">Our work</a><a href="/#about">About</a><a href="/#contact">Contact</a></nav></div></header>
{body}
<footer><div class="w"><p><strong style="color:#F6F1E8">NAVA INTERIOR</strong> · Interior fit-out, renovation &amp; maintenance in {", ".join(EMIRATES[:-1])} and {EMIRATES[-1]}.</p>
<p>WhatsApp / phone: <a href="{wa('Hi NAVA INTERIOR, I would like a free quote.')}">{PHONE}</a> · Email: {EMAIL} · <a href="/">navainteriordubai.com</a></p>
<p>Areas: {" · ".join(f'<a href="/areas/{k}/">{v[0]}</a>' for k,v in AREA_INFO.items())} · <a href="/services/">All services</a></p></div></footer>
<script>window.dataLayer=window.dataLayer||[];(function(){{var src="";try{{src=sessionStorage.getItem("nava_src")||""}}catch(e){{}}var r=document.referrer;if(!src){{src=/google\\./.test(r)?"google":/bing\\./.test(r)?"bing":/chatgpt|openai|perplexity|claude\\.ai|gemini/.test(r)?"ai-assistant":/instagram\\./.test(r)?"ig":/facebook\\./.test(r)?"fb":"website"}}
document.addEventListener("click",function(e){{var a=e.target.closest('a[href*="wa.me"]');if(!a)return;window.dataLayer.push({{event:"whatsapp_click",lead_source:src,page_section:location.pathname}});window.dataLayer.push({{event:"generate_lead",method:"whatsapp",lead_source:src,page_section:location.pathname}});if(typeof gtag==="function"){{gtag("event","generate_lead",{{method:"whatsapp",lead_source:src,page_section:location.pathname,currency:"AED",value:0}});gtag("event","whatsapp_click",{{lead_source:src,page_section:location.pathname}});}}}},true);}})();</script>
</body></html>"""
    d = os.path.join(ROOT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(doc)
    return url

def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i+1, "name": n, "item": SITE + u} for i,(n,u) in enumerate(items)]}

urls = [SITE + "/"]
by_id = {s["id"]: s for s in SV}

# ---- service pages
for s in SV:
    path = f"/services/{s['id']}/"
    photos = [p for p in [(s["photo"], s["photoAlt"]), (s["photo2"], s["photo2Alt"])] if p[0]]
    ph = ""
    if photos:
        ph = f'<div class="ph{" one" if len(photos)==1 else ""}">' + "".join(f'<img src="/{e(p)}" alt="{e(a)}" loading="lazy" width="800" height="600">' for p,a in photos) + "</div>"
    related = [x for x in SV if x["cat"] == s["cat"] and x["id"] != s["id"]][:6]
    fin = ""
    if s["finishes"]:
        fin = f'<h2>{e(s["finishesTitle"])}</h2>' + "".join(f'<h3>{e(a)}</h3><p>{e(b)}</p>' for a,b in s["finishes"])
    body = f"""<div class="hd"><div class="w"><div class="crumb"><a href="/">Home</a> / <a href="/services/">Services</a> / {e(s['name'])}</div>
<div class="eb">{e(s['cat'])} service · Dubai, Abu Dhabi, Sharjah &amp; Ajman</div><h1>{e(s['name'])}</h1><p class="lead">{e(s['short'])}</p>
<p><a class="btn" href="{wa(f"Hi NAVA INTERIOR, I'd like a free quote for {s['name']}.")}">Get a free quote on WhatsApp</a></p></div></div>
<main class="w">{ph}<section>
<h2>{e(s['name'])} by NAVA INTERIOR</h2><p>{e(s['intro'])}</p>
<h2>What's included</h2><ul class="chk">{"".join(f"<li>{e(x)}</li>" for x in s['includes'])}</ul>
<h2>{e(s['processTitle'])}</h2><ol class="st">{"".join(f"<li><strong>{e(a)}:</strong> {e(b)}</li>" for a,b in s['process'])}</ol>
{fin}
<h2>Pricing</h2><p>Every home is different, so we quote after a free inspection, or from photos you send on WhatsApp ({PHONE}). You receive a clear written quote before any work starts.{(" Typical duration: " + e(s['time']) + ".") if s['time'] else ""}</p>
<h2>Areas we cover</h2><p>We provide {e(s['name'].lower())} across {", ".join(f'<a href="/areas/{k}/">{v[0]}</a>' for k,v in AREA_INFO.items())}, including Dubai Marina, Downtown, JVC, Palm Jumeirah, Dubai Hills, Al Reem Island and Saadiyat Island.</p>
<h2>Frequently asked questions</h2>{"".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in s['faq'])}
</section>
<div class="cta"><div><h2>Need {e(s['name'].lower())}?</h2><p>Free inspection and written quote. In-house team. 90-day workmanship warranty.</p></div><a class="btn" href="{wa(f"Hi NAVA INTERIOR, I'd like a free quote for {s['name']}.")}">WhatsApp {PHONE}</a></div>
<h2>Related services</h2><div class="cards">{"".join(f'<a href="/services/{x["id"]}/"><strong>{e(x["name"])}</strong><small>{e(x["short"])}</small></a>' for x in related)}</div>
</main>"""
    ld = [BUSINESS,
          {"@type": "Service", "name": s["name"], "serviceType": s["name"], "description": s["intro"], "url": SITE + path,
           "provider": {"@id": SITE + "/#business"}, "areaServed": [{"@type": "City", "name": c} for c in EMIRATES],
           **({"image": SITE + "/" + s["photo"]} if s["photo"] else {})},
          {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q,a in s["faq"]]},
          crumbs([("Home", "/"), ("Services", "/services/"), (s["name"], path)])]
    urls.append(page(path, f"{s['name']} in Dubai & UAE | NAVA INTERIOR", f"{s['short']} Free inspection and written quote in Dubai, Abu Dhabi, Sharjah and Ajman.", body, ld, "/" + s["photo"] if s["photo"] else "/img/hero-kitchen-marina.jpg"))

# ---- services directory
groups = {"Renovation": "Interior fit-out & renovation", "Technical": "Technical & maintenance services"}
body = '<div class="hd"><div class="w"><div class="crumb"><a href="/">Home</a> / Services</div><div class="eb">Services A–Z</div><h1>Interior, renovation &amp; maintenance services</h1><p class="lead">' + str(len(SV)) + ' services for villas, apartments and offices in Dubai, Abu Dhabi, Sharjah and Ajman, delivered by one in-house team with a free inspection and written quote.</p></div></div><main class="w">'
for c, t in groups.items():
    items = sorted([x for x in SV if x["cat"] == c], key=lambda x: x["name"])
    body += f'<h2>{t}</h2><div class="cards">' + "".join(f'<a href="/services/{x["id"]}/"><strong>{e(x["name"])}</strong><small>{e(x["short"])}</small></a>' for x in items) + "</div>"
body += f'<div class="cta"><div><h2>Not sure what you need?</h2><p>Send photos on WhatsApp and we will advise.</p></div><a class="btn" href="{wa("Hi NAVA INTERIOR, I need advice on my project.")}">WhatsApp {PHONE}</a></div></main>'
ld = [BUSINESS, {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i+1, "name": x["name"], "url": f"{SITE}/services/{x['id']}/"} for i,x in enumerate(sorted(SV, key=lambda x: x["name"]))]}, crumbs([("Home", "/"), ("Services", "/services/")])]
urls.insert(1, page("/services/", "Services A–Z | Interior fit-out & renovation in Dubai | NAVA INTERIOR", f"{len(SV)} interior, renovation and maintenance services in Dubai, Abu Dhabi, Sharjah and Ajman: painting, false ceilings, wall moulding, joinery, tiling, waterproofing, pools, AC and more.", body, ld))

# ---- area pages
KEY = ["painting", "villa-painting", "apartment-painting", "gypsum", "wall-moulding", "joinery-and-custom-cabinets", "tile-work", "bathroom-renovation", "kitchen-renovation", "waterproofing", "pool-construction", "pergolas-and-outdoor-structures", "ac-repair", "electrical", "plumbing", "marble-polishing"]
for key, (city, hoods, text) in AREA_INFO.items():
    path = f"/areas/{key}/"
    svs = [by_id[i] for i in KEY if i in by_id]
    body = f"""<div class="hd"><div class="w"><div class="crumb"><a href="/">Home</a> / Areas / {city}</div><div class="eb">Service area</div>
<h1>Interior fit-out, renovation &amp; maintenance in {city}</h1><p class="lead">{e(text)}</p>
<p><a class="btn" href="{wa(f"Hi NAVA INTERIOR, I'd like a free quote in {city}.")}">Free quote in {city}</a></p></div></div>
<main class="w"><section><h2>Neighbourhoods we cover in {city}</h2><p>{", ".join(e(h) for h in hoods)}, and other communities across {city}.</p>
<h2>How it works</h2><ol class="st"><li><strong>Consultation:</strong> send photos on WhatsApp or book a free site visit.</li><li><strong>Quote &amp; plan:</strong> you receive a written scope, timeline and quote.</li><li><strong>Execution:</strong> a supervisor manages the work and keeps you updated.</li><li><strong>Handover:</strong> final walk-through, clean-up and warranty documents.</li></ol></section>
<h2>Popular services in {city}</h2><div class="cards">{"".join(f'<a href="/services/{x["id"]}/"><strong>{e(x["name"])}</strong><small>{e(x["short"])}</small></a>' for x in svs)}</div>
<p style="margin-top:20px"><a href="/services/">See all {len(SV)} services</a></p>
<div class="cta"><div><h2>Planning a project in {city}?</h2><p>Free inspection and written quote. 90-day workmanship warranty.</p></div><a class="btn" href="{wa(f"Hi NAVA INTERIOR, I'd like a free quote in {city}.")}">WhatsApp {PHONE}</a></div></main>"""
    ld = [{**BUSINESS, "areaServed": [{"@type": "City", "name": city}] + [{"@type": "Place", "name": h} for h in hoods]}, crumbs([("Home", "/"), (city, path)])]
    urls.append(page(path, f"Interior Fit-out & Renovation in {city} | NAVA INTERIOR", f"Interior fit-out, renovation and maintenance in {city}: painting, false ceilings, wall moulding, joinery, tiling, waterproofing, pools and AC. Free inspection and written quote.", body, ld))

# ---- sitemap, robots, llms.txt
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
bots = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Applebot-Extended"]
open(os.path.join(ROOT, "robots.txt"), "w").write("".join(f"User-agent: {b}\nAllow: /\nDisallow: /go/\n\n" for b in bots) + f"User-agent: *\nAllow: /\nDisallow: /go/\n\nSitemap: {SITE}/sitemap.xml\n")
cats = {c: sorted([x for x in SV if x["cat"] == c], key=lambda x: x["name"]) for c in groups}
llms = f"""# NAVA INTERIOR

> NAVA INTERIOR is a UAE interior fit-out, renovation and property maintenance company serving villas, apartments and offices in Dubai, Abu Dhabi, Sharjah and Ajman. One in-house team covers painting, gypsum false ceilings, wall moulding and panelling, carpentry and custom joinery, tile and marble, waterproofing, swimming pools, pergolas, AC, electrical and plumbing. Every project starts with a free inspection and a clear written quote, and work carries a 90-day workmanship warranty.

- Website: {SITE}/
- WhatsApp / phone: {PHONE}
- Email: {EMAIL}
- Areas served: Dubai, Abu Dhabi, Sharjah, Ajman
- Quotes: free inspection or quote from photos on WhatsApp; written quote before work starts

## Service areas
""" + "".join(f"- [{v[0]}]({SITE}/areas/{k}/): {v[2]}\n" for k, v in AREA_INFO.items()) + "".join(
    f"\n## {groups[c]}\n" + "".join(f"- [{x['name']}]({SITE}/services/{x['id']}/): {x['short']}\n" for x in items) for c, items in cats.items())
open(os.path.join(ROOT, "llms.txt"), "w").write(llms)
print("pages", len(urls), "sitemap ok, llms.txt ok")
