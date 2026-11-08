---
name: ads
description: Create ready-to-run ad campaigns for NAVA INTERIOR (Google Search ads and Facebook/Instagram ads) — keywords, headlines, descriptions, primary text, targeting and creatives — for the whole business or one service or area. Use when the user types /ads or asks for ads, ad copy, a campaign, Google Ads or Meta/Facebook/Instagram ads.
argument-hint: "[service or area, e.g. 'villa painting' or 'Abu Dhabi'] [google|meta|both]"
---

# /ads — NAVA INTERIOR ad builder

Build complete, copy-paste-ready ad campaigns for NAVA INTERIOR. Default to **both** Google and Meta unless the user names one. If the user gives a service or area in the arguments, focus the whole campaign on it; otherwise make a general brand campaign plus one per top service.

## Business facts (use exactly; never invent others)
- Name: **NAVA INTERIOR** — interior fit-out, renovation & maintenance for villas, apartments and offices.
- Areas: Dubai, Abu Dhabi, Sharjah, Ajman. Office: Ras Al Khor Industrial Area 1, Dubai.
- Phone / WhatsApp: +971 56 752 2656 (wa.me/971567522656).
- Website: https://navainteriordubai.com — services at `/services/<id>/`, areas at `/areas/<slug>/`, guides at `/guides/<slug>/`. Read `sitemap.xml` and `tools/data.json` in this repo for the real service ids, names and descriptions.
- Promises: free inspection, clear written quote before work starts, in-house team, 90-day workmanship warranty.
- Brand: premium, calm, precise. Gold-and-white look. Tagline "Design · Fit-out · Finishing".

## Hard rules
- **No prices, AED amounts, discounts or "cheapest/best/#1" claims.** Offer "free inspection & written quote" instead.
- No invented reviews, ratings, project counts, years in business or awards.
- Respect platform limits: Google RSA headlines ≤ 30 characters (give 10–15), descriptions ≤ 90 (give 4); Meta headline ≤ 40, primary text first line must hook within ~125 characters. **Count characters** with a quick script before presenting and fix any that exceed.
- Never launch, publish or spend money. Only prepare. If an ads connector is available, create items **paused** and only after the user explicitly approves a budget.
- Always tag landing URLs so leads are tracked: Google `?src=google`, Meta `?src=fb` (or `/go/fb/`), Instagram `/go/ig/`. The site already tags WhatsApp messages with "Found you via" and sends `generate_lead` to Google Analytics.

## Output format
For each campaign (one per service/area requested):

### Google Search
1. Campaign settings: goal Leads, Search network only, locations (the 4 emirates or the named area), language English (+ Arabic optional), schedule suggestion, bidding "Maximize conversions" once `generate_lead` is a key event.
2. Ad group(s) with 8–15 **phrase-match keywords** (realistic UAE phrasing, include community names when an area is targeted) and a **negative keyword** list (jobs, salary, course, diy, free, training, used, second hand…).
3. Responsive search ad: headlines (with char counts), descriptions (with char counts), final URL (deepest relevant page, tagged), display path.
4. Assets: sitelinks (4, to real pages), callouts (4–6), call asset +971 56 752 2656, location asset note.

### Meta (Facebook & Instagram)
1. Objective: Engagement → Messages (WhatsApp) or Leads. Placements: Reels, Feed, Stories.
2. Audience: location, age 28–60, interests (home improvement, interior design, real estate, luxury homes), exclusions.
3. Creative: pick existing files from `brand/instagram-posts/post-XX.jpg` (match the service; captions in `brand/instagram-captions.txt`) and the promo video if present; name the exact files. Suggest one new creative idea if none fits.
4. Copy: 3 primary-text variants (short/medium/long), 3 headlines, description, CTA "Send WhatsApp message".

### Then
- A short **test plan**: what to A/B test first, what to watch (CTR, cost per lead, WhatsApp chats), when to pause.
- Remind the user ads cost money and to set a daily cap they are comfortable with; never state platform prices as fact.
- Offer to save the campaign as `brand/ads/<campaign-name>.md` in this repo (write it if they agree, then commit and push).
