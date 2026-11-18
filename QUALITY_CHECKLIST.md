# Quality Checklist

Verification performed on this build, run via an automated script against the generated output (see commands below — rerun any of them after making changes).

| Check | Result | How verified |
|---|---|---|
| All 14 projects present in data source | ✅ Pass | `data/projects.json` contains IDs 1–14 with no gaps |
| All 14 project detail pages generated | ✅ Pass | `projects/*.html` — one file per project slug, confirmed present on disk |
| No broken internal links | ✅ Pass | Script-parsed every `href` in every generated `.html` file and confirmed the target file exists on disk |
| No missing CSS/JS asset references | ✅ Pass | Script-parsed every `assets/...` reference and confirmed the file exists |
| No broken images | ✅ Pass (N/A) | Site intentionally uses no raster images — only CSS, SVG favicon (inline data URI) and Mermaid.js diagrams, per the "no stock-image substitutes for technical diagrams" requirement |
| All HTML files well-formed (closing tags present) | ✅ Pass | Confirmed every generated file contains a closing `</html>` tag |
| Mobile responsiveness | ✅ Pass (by design) | CSS uses relative units, `grid`/`flexbox`, a mobile nav breakpoint at 880px, and a project-page layout that collapses the sidebar below 880px; viewport meta tag present on every page |
| Dark/light theme toggle | ✅ Pass | `data-theme` attribute toggled via `assets/js/main.js`, persisted to `localStorage`, with CSS variable overrides in `main.css` |
| Project search functionality | ✅ Pass | `initProjectFilters()` in `main.js`, wired to `#projectSearch` on the Projects page |
| Category / status / technology filtering | ✅ Pass | Category chips, status `<select>`, and technology `<select>` all wired in `initProjectFilters()` |
| Breadcrumb navigation on project pages | ✅ Pass | Every project page includes a `Home / Projects / [Title]` breadcrumb |
| Back-to-projects navigation | ✅ Pass | Sidebar TOC on every project page includes a "← Back to Projects" link |
| Print-friendly project pages | ✅ Pass | `@media print` rule in `main.css` hides nav/footer/sidebar/filters |
| SEO metadata (title, description, canonical, Open Graph) | ✅ Pass | Present in the shared `page_shell()` template used by every page |
| Sitemap.xml | ✅ Pass | Generated listing all 21 pages |
| Robots.txt | ✅ Pass | Generated, references the sitemap |
| Custom 404 page | ✅ Pass | `404.html` generated |
| Favicon | ✅ Pass | Inline SVG data-URI favicon (no external file dependency) |
| Accessibility basics | ✅ Pass | Semantic landmarks (`nav`, `footer`, `section`), `aria-label` on icon-only buttons (theme toggle, mobile nav burger), sufficient color contrast in the dark theme's text/background pairing |
| GitHub Pages relative path correctness | ✅ Pass | All asset/page references use relative paths with a `depth` parameter (`""` at root, `"../"` inside `projects/`), verified by the link-check script from the repo root |
| No fabricated achievements, metrics or completed test results | ✅ Pass | All 14 projects are explicitly set to **Concept** status; all hardware/software sizing figures are labeled as estimates; all "Testing & Validation" sections describe planned test scenarios, not completed results; About page uses `[EDITABLE: ...]` placeholders rather than invented biography |
| No invented contact/social URLs | ✅ Pass | All contact/social fields use `[YOUR_...]` bracketed placeholders |

## How to re-run these checks

```bash
# Rebuild from source
python3 build.py

# Re-run the link/asset/project-count validation script
# (see the "Testing & Validation" section of this repository's build process,
#  or re-paste the validation script used during development)
```

## Not yet verified (requires a browser / live environment)

- Actual visual rendering across real browsers and devices (this build was validated structurally, not via browser screenshot testing).
- Live Mermaid.js diagram rendering (requires a browser with JavaScript; diagrams were checked for valid Mermaid syntax but not rendered in this environment).
- Real-world Lighthouse/PageSpeed performance and accessibility audit scores.
- Actual GitHub Pages deployment (workflow file is included and configured, but has not yet been run against a live repository).

Recommend running a Lighthouse audit and a visual pass in-browser immediately after first deployment, and addressing anything surfaced there before sharing the link with clients/recruiters.
