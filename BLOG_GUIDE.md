# Blog Guide — Writing and Publishing Posts

All blog posts live in one file: **`data/blog.json`**. Each post is one entry in the `"posts"` list. There's already one example post in there (`welcome-to-my-engineering-blog`) showing every formatting option — open it side-by-side with this guide the first time.

---

## 1. Anatomy of a post

```json
{
  "slug": "my-new-post-url",
  "title": "My New Post Title",
  "date": "2026-11-20",
  "cover": "my-cover-image.jpg",
  "excerpt": "A one-sentence summary shown on the blog listing page and in search results.",
  "tags": ["HPC", "SLURM"],
  "content": "<p>Your full post HTML goes here.</p>"
}
```

| Field | What it does |
|---|---|
| `slug` | Used in the URL: `yoursite.com/blog/my-new-post-url.html`. Use lowercase, hyphens, no spaces. Must be unique. |
| `title` | Shown as the big heading and in the browser tab. |
| `date` | Format `YYYY-MM-DD`. Posts are sorted newest-first automatically. |
| `cover` | Filename of a cover image placed in `assets/img/blog/` (see below). Leave as `""` for no cover image. |
| `excerpt` | Short teaser shown on the blog listing page. |
| `tags` | A list of short topic labels. |
| `content` | The full post body, written as HTML (see formatting cheat-sheet below). |

---

## 2. Adding a cover image or in-post images

1. Put image files in: `assets/img/blog/`
2. For the **cover image** (shown at the top of the post and on the listing card): set `"cover": "filename.jpg"`.
3. For an **image inside the post body**, add this inside your `content` HTML:
   ```html
   <img src="../assets/img/blog/your-image.jpg" alt="Description of the image">
   ```
   Note the `../` — it's needed because posts live one folder deeper (`blog/post-name.html`) than the images folder.

---

## 3. Formatting cheat-sheet (for the `content` field)

Since `content` is plain HTML, here's what's styled and ready to use — just paste these snippets into your content string:

| What you want | HTML to use |
|---|---|
| Paragraph | `<p>Your text here.</p>` |
| Section heading | `<h2>Heading</h2>` or `<h3>Smaller heading</h3>` |
| Bold / italic | `<strong>bold</strong>` / `<em>italic</em>` |
| Quote block | `<blockquote>A quoted line or key takeaway.</blockquote>` |
| Code (inline) | `<code>sinfo -N -l</code>` |
| Code block | `<pre><code>sinfo -N -l\nsqueue --me</code></pre>` |
| Bullet list | `<ul><li>Point one</li><li>Point two</li></ul>` |
| Numbered list | `<ol><li>Step one</li><li>Step two</li></ol>` |
| Link | `<a href="https://example.com">link text</a>` |
| Image | `<img src="../assets/img/blog/file.jpg" alt="...">` |

Because JSON strings can't contain literal line breaks, write your `content` as **one long line** with `\n` only inside `<pre><code>` blocks where you need visible line breaks (see the example post).

---

## 4. Step-by-step: publishing a new post

1. Write your post content as HTML first (in a text editor), using the cheat-sheet above.
2. Open `data/blog.json`.
3. Add a new entry to the `"posts"` array (copy the example post's structure, comma-separate from the previous entry if it's not the last one).
4. Put any images in `assets/img/blog/`.
5. Rebuild:
   ```bash
   python build.py
   ```
6. Check it looks right by opening `blog.html` and your new post locally if possible, or just push and check live.
7. Commit and push:
   ```bash
   git add .
   git commit -m "Add blog post: My New Post Title"
   git push
   ```
8. GitHub Actions redeploys automatically (check the **Actions** tab) — live in 1–2 minutes.

---

## 5. Removing the example post

Once you've published your first real post, delete the `welcome-to-my-engineering-blog` entry from `data/blog.json` (or just leave it — it won't hurt anything, but it's meant as a reference, not a real post).