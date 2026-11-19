# Abu Horairah | Engineering Portfolio

A premium, static engineering portfolio website showcasing 14 AI / HPC / EDA / Networking / Storage infrastructure engineering projects. Built with plain HTML5, CSS3 and JavaScript, generated from a single JSON data source, and deployable on GitHub Pages at zero cost.

**Live demo:** _add your GitHub Pages URL here after deployment_

---

## 1. What this is

- A 21-page static site: Home, About, Projects overview (with search/filter), Technologies, Architecture, Contact, a custom 404, and **14 fully detailed project pages**.
- Every project page follows the same consistent structure: Overview → Business Value → Architecture (with a Mermaid diagram) → Technology Stack → Hardware Requirements → Software Architecture → Implementation Roadmap (with a Mermaid diagram) → Security & Reliability → Testing & Validation → Deliverables → Future Enhancements → Status → Call to Action.
- Dark navy / electric blue / cyan enterprise design system, with a light-mode toggle, responsive layout, and print-friendly project pages.
- No invented credentials, employment history, metrics, or completed test results anywhere on the site — placeholders are marked `[EDITABLE: ...]` or `[YOUR_...]`.

## 2. How the site is built

All page content lives in **`data/projects.json`**. The Python script **`build.py`** (pure standard library, no dependencies) reads that file and generates every HTML page into the repository root and `projects/`. This means:

- To edit a project's content, edit `data/projects.json`, then re-run the build.
- To edit shared design/layout, edit `assets/css/main.css`, `assets/js/main.js`, or the page templates inside `build.py`.

### Rebuilding the site locally

```bash
python3 build.py
```

This regenerates `index.html`, `about.html`, `projects.html`, `technologies.html`, `architecture.html`, `contact.html`, `404.html`, `sitemap.xml`, `robots.txt`, and all 14 files under `projects/`.

**Before your first deploy**, open `build.py` and set:

```python
BASE_URL = "https://engrabuhorairah.github.io/profile"
```

to your actual GitHub Pages URL (see step 5 below), then re-run `python3 build.py` so canonical URLs and the sitemap are correct.

## 3. Folder structure

```
.
├── index.html                 # Home page (generated)
├── about.html                 # About page (generated)
├── projects.html              # Projects overview with search/filter (generated)
├── technologies.html          # Technology stack overview (generated)
├── architecture.html          # Cross-project architecture diagram (generated)
├── contact.html                # Contact page (generated)
├── 404.html                   # Custom 404 page (generated)
├── sitemap.xml / robots.txt   # SEO files (generated)
├── build.py                   # Static site generator — EDIT THIS to change layout
├── data/
│   └── projects.json          # All project content — EDIT THIS to change content
├── projects/
│   └── *.html                 # 14 generated project detail pages
├── assets/
│   ├── css/main.css           # Design system
│   └── js/main.js             # Theme toggle, mobile nav, filters
└── .github/workflows/deploy.yml  # GitHub Pages deployment workflow
```

## 4. Editable personal information

Search the generated/source files for these placeholders and replace them with real information:

| Placeholder | Location | What to put there |
|---|---|---|
| `[YOUR_GITHUB_URL]` | `build.py` (footer, contact page) | Your GitHub profile URL |
| `[YOUR_LINKEDIN_URL]` | `build.py` | Your LinkedIn profile URL |
| `[YOUR_EMAIL_ADDRESS]` | `build.py` | Your contact email |
| `[YOUR_PERSONAL_SITE]` | `build.py` | Your personal website, if any |
| `[EDITABLE: ...]` blocks | `about.html` (via `build_about()` in `build.py`) | Your real professional introduction, background, and interests |
| `BASE_URL` | top of `build.py` | Your live GitHub Pages URL, for SEO metadata and the sitemap |

No academic qualifications, job history, certifications, or awards have been invented anywhere on this site — add your real ones in the About page section of `build.py` if you'd like them included.

## 5. Deploying to GitHub Pages

### Step 1 — Create the repository
1. Go to [github.com/new](https://github.com/new) and create a new repository (e.g. `engineering-portfolio`). Public repos get free GitHub Pages hosting.

### Step 2 — Push the project files
```bash
cd site                      # this folder
git init
git add .
git commit -m "Initial commit: Abu Horairah engineering portfolio"
git branch -M main
git remote add origin https://github.com/engrabuhorairah/profile.git
git push -u origin main
```

### Step 3 — Enable GitHub Pages
1. In your repository, go to **Settings → Pages**.
2. Under **Build and deployment → Source**, select **GitHub Actions**.
3. The included workflow (`.github/workflows/deploy.yml`) will run automatically on every push to `main`: it runs `python3 build.py` and publishes the result.

### Step 4 — Watch the deployment
1. Go to the **Actions** tab in your repository and confirm the "Deploy to GitHub Pages" workflow completes successfully (green check).
2. Once complete, your site is live.

### Step 5 — Open the live site
Your site will be available at:
```
https://engrabuhorairah.github.io/profile/
```
Go back and set this exact URL as `BASE_URL` in `build.py`, commit, and push again so SEO metadata and the sitemap are accurate.

### Updating project information later
1. Edit `data/projects.json` (content) and/or `build.py` (layout).
2. Run `python3 build.py` locally to verify the build succeeds with no errors.
3. Commit and push to `main` — GitHub Actions rebuilds and redeploys automatically.

## 6. License

See `LICENSE` (MIT, with editable attribution — update the copyright holder name if needed).

## 7. Known limitations

- All 14 projects are currently at **Concept** status, pending your real-world implementation updates; see `data/projects.json` → `"status"` field per project to update as work progresses.
- Hardware/software sizing figures throughout are explicitly labeled as planning estimates, not benchmarked results — replace with real figures as you complete testing.
- Social/contact links are placeholders and must be filled in before publishing.
- The Mermaid diagrams are intentionally simple, generic architecture/roadmap diagrams per project; consider customizing per-project diagrams further in `build.py` as each project matures.
