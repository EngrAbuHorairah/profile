# Setup Guide: Single-Repo Build + Live Public Comments (Giscus)

You're keeping everything in your existing `profile` repo — no second repo needed. This guide covers two things:

1. Switching to the new build (`dist/`-based) inside your existing repo.
2. Turning on live public comments with Giscus.

**Note on privacy:** staying in one repo means the repo (including `build.py` and `data/*.json`) remains **public**, since free GitHub Pages only serves Pages from public repositories. The generated site itself was always going to be publicly viewable in a browser either way — this just means the source files behind it are visible too if someone browses the repo. If you want the source hidden later, that needs either a second private repo (what we discussed before) or a paid GitHub Pro/Team plan that allows Pages from a private repo.

---

## Part 1 — Switch to the new build (one-time)

### Step 1 — Replace your files
Replace these in your local `site` folder with the versions I've given you:
- `build.py`
- `.github/workflows/deploy.yml`

Add this new file (create it if it doesn't exist):
- `.gitignore` — containing at least this line: `dist/`

### Step 2 — Build locally to confirm it works
```bash
python build.py
```
You should see a new `dist/` folder appear containing all the HTML/CSS/JS/images — this is now the actual output folder. Your repo root keeps the source files (`build.py`, `data/`) separate from this.

### Step 3 — Commit and push
```bash
git add .
git commit -m "Switch to dist/-based build with updated deploy workflow"
git push
```
Because `dist/` is in `.gitignore`, it won't be committed — GitHub Actions builds it fresh on every push and deploys just that folder. Check the **Actions** tab for a green checkmark, then confirm `https://engrabuhorairah.github.io/profile/` still loads correctly.

---

## Part 2 — Live public comments (Giscus)

Giscus turns this same repo's **GitHub Discussions** into a free comment widget — no extra account or service needed beyond GitHub itself.

### Step 1 — Enable Discussions
`profile` repo → **Settings → Features → check "Discussions"**.

### Step 2 — Install the giscus app
Visit [github.com/apps/giscus](https://github.com/apps/giscus) → **Install** → grant access to the `profile` repository only.

### Step 3 — Generate your embed code
1. Go to [giscus.app](https://giscus.app).
2. Under "repository", type `EngrAbuHorairah/profile` and wait for the green checkmark.
3. Under "Discussion Category", create/choose one called **Comments** (type "Announcements" is recommended so only you can start new top-level threads, but anyone can reply).
4. Pick theme **Dark** (or "Preferred color scheme") to match the site.
5. Copy the generated `<script>` snippet at the bottom — it will look like:
   ```html
   <script src="https://giscus.app/client.js"
           data-repo="EngrAbuHorairah/profile"
           data-repo-id="R_kgD0..."
           data-category="Comments"
           data-category-id="DIC_kwDO..."
           data-mapping="pathname"
           data-theme="dark"
           crossorigin="anonymous"
           async>
   </script>
   ```

### Step 4 — Send it to me
Paste that exact snippet back to me and I'll wire it into `build.py` on the Contact page (replacing the `GISCUS_EMBED_PLACEHOLDER` comment), rebuild, and give you the final updated file to push.

Once live: anyone can **read** comments with no account; posting a comment needs a **free GitHub account** — a reasonable bar for a technical engineering portfolio's audience.
