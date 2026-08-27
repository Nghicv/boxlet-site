# boxlet.day

Landing page and legal pages for **Boxlet**, served by GitHub Pages at `boxlet.day` (see `CNAME`).

| File | What it is |
| --- | --- |
| `template.html` + `build.py` | The landing page. Copy for both languages lives in `build.py`; `python3 build.py` renders `index.html` (EN) and `vi/index.html` (VI). Edit the template or the strings, never the rendered files. |
| `style.css` | One stylesheet for every page. Tokens mirror the app's `docs/design-system.md` — same paper palette, same typeface, light + dark via `prefers-color-scheme`. |
| `tools/build_assets.py` | Exports `assets/` from the app repo: store screenshots → WebP, app icon, OG image, the Plus Jakarta Sans variable font → woff2. Re-run after the store screenshots change. |
| `privacy.html` `terms.html` `support.html` `delete-account.html` | Hand-written, bilingual. Linked from the stores and from the app. |

```bash
python3 tools/build_assets.py ../../KMM/daybox   # refresh assets from the app repo
python3 build.py                                 # render index.html + vi/index.html
python3 -m http.server 8765                       # preview — paths are root-absolute, file:// will not work
```

Rules the page follows, so it stays the app's ninth screen rather than a separate brand:

- Screenshots are the real app with the sample day from `aso/screenshot/README.md`; no mock UI.
- The "Ten kinds of paper" board is built in HTML with the exact `paper` tints per card type.
- One typeface, hierarchy by weight. Indigo only for interaction. No decorative gradients.
- Section headers are title + subtitle below — never an uppercase eyebrow above the title.
