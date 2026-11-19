# Photo Guide — Profile Photo, Home Carousel & Gallery

This site has three places for photos, and all of them work the same way: **drop the image file in, then list it in a JSON file, then rebuild.**

---

## 1. Profile Photo (About page, circular)

1. Pick a square-ish headshot (ideally at least 400×400px). Crop it close so your face fills the frame — the site crops it into a circle automatically.
2. Rename the file exactly to: `profile.jpg`
   - If your photo is a `.png`, either convert it to `.jpg`, or rename it `profile.png` **and** open `build.py`, find `assets/img/profile.jpg` (inside `build_about()`) and change it to `assets/img/profile.png`.
3. Place it at: `assets/img/profile.jpg`
4. Run `python3 build.py` and push. If the file isn't found, the site automatically shows an "AH" placeholder circle instead — it never breaks.

---

## 2. Home Page Auto-Scroll Carousel + Full Gallery Page

Both the home page carousel and the `/gallery.html` page pull from the same list: `data/gallery.json`.

### To add a new photo:

1. Put the image file in: `assets/img/gallery/your-photo-name.jpg`
   - Keep file sizes reasonable (under ~500KB each) so the site stays fast — resize/compress large photos first.
2. Open `data/gallery.json` and add a new entry to the `"photos"` list:
   ```json
   {
     "filename": "your-photo-name.jpg",
     "title": "Short title shown as caption",
     "description": "A sentence or two describing this photo — used on the Gallery page."
   }
   ```
3. Remove the three `sample-1.jpg` / `sample-2.jpg` / `sample-3.jpg` placeholder entries once you've added your own real ones (or just leave them out if you haven't added matching image files yet — a missing gallery image is simply hidden, not broken).
4. Run `python3 build.py`, then commit and push.

### Notes
- The home page carousel shows **all** photos from `gallery.json`, scrolling automatically and pausing on hover.
- The Gallery page (`/gallery.html`) shows the same photos in a grid, each with its title and description.
- There's no limit on how many photos you add — add as many as you like, in any order; newest can go at the top or bottom of the list, it's just a list.

---

## 3. Recommended photo specs

| Use | Recommended size | Format |
|---|---|---|
| Profile photo | 400×400px minimum, square | JPG |
| Gallery / carousel photos | 1200×800px (3:2) works well | JPG |

Compress photos before adding them (e.g. with [squoosh.app](https://squoosh.app) or any image editor's "export for web") to keep the site fast to load.

---

## 4. Full update checklist (every time)

```bash
# 1. Add your image file(s) under assets/img/...
# 2. Edit the matching JSON file (gallery.json) if adding gallery/carousel photos
# 3. Rebuild:
python build.py
# 4. Push:
git add .
git commit -m "Add new photo(s)"
git push
```

GitHub Actions redeploys automatically — check the **Actions** tab, and your changes go live in 1–2 minutes.
