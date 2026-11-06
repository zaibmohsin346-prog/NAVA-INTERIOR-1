# NAVA INTERIOR – website

Premium interior fit-out, renovation and property maintenance website for **NAVA INTERIOR** (Dubai, Sharjah, Ajman).

## Structure

| Path | Contents |
|---|---|
| `index.html` | The full website (single page, hash routing: `#home`, `#services`, `#about`, `#gallery`, `#contact`, plus one page per service) |
| `img/` | Project and service photos |
| `brand/logo/` | Logo pack (PNG + SVG, white / dark / transparent, icon) |
| `brand/stationery/` | Business card, A4 letterhead (PDF + PNG), email signature |
| `brand/whatsapp-catalog/` | WhatsApp Business catalog images and `catalog-text.txt` |
| `brand/whatsapp-profile/` | WhatsApp profile picture |
| `components/ui/`, `lib/` | React + shadcn components (for a future Next.js version; not used by `index.html`) |

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8080
```

## Publish with GitHub Pages

Repository **Settings → Pages → Build and deployment → Deploy from a branch → `main` / root**.

## SEO & AI search (GEO) pages

`services/`, `areas/`, `llms.txt`, `sitemap.xml` and `robots.txt` are generated, and the home page text is pre-filled inside `<main id="app">`. After changing services in `index.html`, rebuild them:

```bash
node tools/extract.js && python3 tools/build_geo.py && node tools/prerender.js
```
