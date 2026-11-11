# thedevpro.io

Static website for TheDevPro, hosted on Vercel. Plain HTML, CSS and JS — no build step.

## Structure

- `index.html` and one folder per page (`ai/`, `services/…/`, `work/`, `process/`, `about/`, `contact/`)
- `assets/` — CSS, JS, logo, link-preview image
- `<client>/index.html` — private proposals (one folder per client)
- `_templates/proposal/` — copy this to start a new proposal (not published)

## Adding a proposal for a client

1. Copy the folder `_templates/proposal` and rename the copy to the client, e.g. `thermal`.
2. Edit `thermal/index.html` (or drop in the client's finished `index.html`).
3. Keep `<meta name="robots" content="noindex, nofollow">` in it.
4. Commit and push. It is live at `https://thedevpro.io/thermal/`.

Proposals are private by design:
- they are never linked from the site and are not in `sitemap.xml`;
- `vercel.json` sends `X-Robots-Tag: noindex, nofollow` for every folder that is not a site page.

If you add a new public page, add its folder name to the list in `vercel.json` and to `sitemap.xml`.
