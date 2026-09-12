# gamedevtc.github.io — Taylor Christianson's Portfolio

A single-page, data-driven game-development portfolio hosted on **GitHub Pages** at
**https://gamedevtc.github.io**.

Almost everything on the page (projects, experience, profile, skills) is read at runtime from
**JSON data files** — so adding a project or updating a bio is an edit to a `.json` file, not the
HTML. This README documents how the site is put together and, most importantly, **how to add or edit
content by hand**.

> Originally built on the HTML5 UP "Read Only" template, but heavily customized since — the app-store
> project grid, the terminal-style Documents section, the JSON data layer, dark mode, and the social/
> store link pills are all bespoke. See **Credits & License** at the bottom.

---

## How it works (the 30-second version)

- **Static site.** Plain HTML + CSS + JS. No build step is needed to change content — you edit JSON.
- **`index.html`** holds all the markup, styles, and JavaScript (it's one big file). On load, its JS
  `fetch()`es the JSON data files and builds the page.
- **Content lives in JSON:** `games.json`, `experience.json`, `profile.json`, and one
  `slides.json` per project.
- **Deploy = push to `main`.** GitHub Pages serves the repo root. Changes are live within a minute.

### Page sections

| Section | Nav label | What it is |
|---|---|---|
| `#one`   | About     | Top card: portrait, name, role, degree, auto-computed **YRS EXP** + **PROJECTS** stats, and the bio blurb. Driven by `profile.json` (+ `experience.json` for the stats). |
| `#two`   | Projects  | App-store-style icon grid built from `games.json`. Click a game to open a detail sheet with its tags, link pills, roles, description, and an image/video/YouTube slideshow (`slides.json`). |
| `#three` | Documents | Terminal-style résumé: experience, education, and skills from `experience.json`, plus the Résumé and Letter-of-Reference download buttons. |

---

## Repository layout

```
/
├── index.html              ← all markup, CSS, and JS (single file)
├── games.json              ← the Projects grid (array of game objects)
├── experience.json         ← work / education / skills (Documents section)
├── profile.json            ← name, title, bio, portrait, social links, résumé path
├── .gitattributes          ← Git LFS rules for archived videos (see "Media & video")
├── downloads/              ← résumé + letter of reference (PDFs)
├── videos/                 ← site banner video
├── images/
│   ├── experience/         ← studio / school logos (halfbrick.png, panda-paw.png, fullsail.png …)
│   └── projects/<id>/      ← one folder per game (id must match games.json "id")
│       ├── slides.json     ← thumb, background, and the slideshow for that game
│       ├── <id>-thumb.png  ← grid/card thumbnail
│       ├── *.png / *.mp4   ← gallery media (served)
│       └── stored/         ← archived media too big to serve (Git LFS, NOT shown on the site)
└── assets/                 ← template CSS/JS, Font Awesome 6.5.2 (css + webfonts), Sass sources
```

---

## Data file reference

### `games.json` — the Projects grid

An **array** of game objects, shown in array order (top of the array = first card). Fields:

| Field | Type | Notes |
|---|---|---|
| `id` | string | **Required.** Must match the folder name in `images/projects/<id>/`. Used to find the thumbnail and slides. |
| `name` | string | Display title on the card and detail sheet. |
| `year` | string | e.g. `"2026"` or `"2023–2026"`. Shown on the card and next to `meta`. |
| `meta` | string | Studio / context line, e.g. `"Panda Paw Entertainment"`. |
| `tags` | string[] | Tech/skill pills (row 1 of the detail sheet). |
| `roles` | string[] | Your roles on the project (rendered as role pills). |
| `desc` | string | One-paragraph description. |
| `bullets` | string[] | Highlight bullet points. |
| `links` | object[] | Store/social pills (row 2). Each is `{ "type": "...", "url": "..." }`. See **Link types** below. Omit if none. |
| `experience` | string \| object | Ties the card to a studio. A **string** matches an `id` in `experience.json` (shows that studio's logo + name). An **object** `{ "label", "image?", "url?" }` is a one-off link. Omit for none. |
| `badge` | bool \| string | `true` shows a small "notification dot" on the icon; a string shows that text as a badge. Omit for none. |

**Link types** (the `type` in each `links` entry) map to a brand icon + colour automatically:
`steam`, `youtube`, `discord`, `twitter`, `x`, `instagram`, `tiktok`, `twitch`, `itch`, `bluesky`,
`website`. An unknown type falls back to a generic link icon. You can override per-link with an
optional `"label"` or `"icon"` (a Font Awesome class, e.g. `"fab fa-steam"`).

<details>
<summary>Minimal game entry template (copy/paste)</summary>

```json
{
  "id": "my-game",
  "name": "My Game",
  "year": "2026",
  "meta": "Studio Name",
  "tags": ["Unity 6", "C#", "PC"],
  "roles": ["Gameplay Programmer"],
  "desc": "One-paragraph description of the project.",
  "bullets": [
    "A notable thing I built",
    "Another notable thing"
  ],
  "links": [
    { "type": "steam", "url": "https://store.steampowered.com/app/…" }
  ],
  "experience": "panda-paw"
}
```
</details>

### `slides.json` — one per project (`images/projects/<id>/slides.json`)

Controls the card thumbnail and the detail-sheet slideshow.

```json
{
  "thumb": "images/projects/my-game/my-game-thumb.png",
  "background": "images/projects/my-game/my-game-background.png",
  "slides": [
    { "type": "image",   "src": "images/projects/my-game/shot-1.png", "alt": "" },
    { "type": "video",   "src": "images/projects/my-game/clip-1.mp4", "alt": "" },
    { "type": "youtube", "src": "VIDEO_ID",                            "alt": "Trailer" }
  ]
}
```

- `type: "image"` / `"video"` → `src` is a path in the repo.
- `type: "youtube"` → `src` is just the **YouTube video ID** (the part after `watch?v=`). Best choice
  for anything large — see **Media & video** below.

### `experience.json` — Documents section

Three arrays: `work`, `education`, `skills`.

- **work[]**: `{ id, company, image, roles[], date, startDate, endDate?, status?, progression[] }`
  - `startDate`/`endDate` are `"YYYY-MM"` and feed the auto-computed **YRS EXP** stat. Omit `endDate`
    to count a role as ongoing (to "now").
  - `status` (optional) renders a small badge next to the company name, e.g. `"Furloughed"`.
  - `progression[]` is the role timeline: `{ title, startDate, endDate?, date, promoted? }`.
    `promoted: true` adds an "↑ promoted" marker.
- **education[]**: `{ id, school, image, degree, graduated }`.
- **skills[]**: `{ key, value }` (rendered as a `"key": value` list).

The `id` on a work/education entry is what a game's `experience` string points at.

### `profile.json` — About card + sidebar

`{ name, title, image, bio, email, links[], resume }`

- `bio` is an **array of sentences**, joined with spaces into one paragraph. Keep specific numbers
  (years, project counts) **out** of it — those are shown as auto-computed stats.
- `links[]`: `{ label, url, icon, newTab }` (`icon` is a Font Awesome class like `"brands alt fa-github"`).
- `resume` is the path to the résumé PDF in `downloads/`.

---

## Adding a new project (checklist)

1. **Pick an `id`** (kebab-case, e.g. `my-game`).
2. **Add an entry** to `games.json` (see the template above). Position in the array = position in the grid.
3. **Create `images/projects/<id>/`** and add:
   - `<id>-thumb.png` (the card thumbnail),
   - a `slides.json` (thumb + background + slides),
   - the gallery images/videos it references.
4. If you set `"experience": "<id>"`, make sure that `id` exists in `experience.json` and its logo is
   in `images/experience/`.
5. **Preview locally** (see below), then commit + push.

---

## Media & video — important

**GitHub Pages does not serve Git LFS files** (it serves the tiny pointer text instead), and GitHub
**blocks any file over 100 MiB** and warns over 50 MiB. So videos are split by size:

- **≤ 50 MiB → normal Git.** Keep it in the project folder, reference it in `slides.json`
  (`type: "video"`). It's served and plays on the live site.
- **> 50 MiB → not served.** Move it into the project's **`stored/`** folder, **remove it from
  `slides.json`**, and let Git LFS track it (archive/backup only — it will *not* play on the site).
  To actually show a big video, **host it on YouTube and use `type: "youtube"`** instead.

`.gitattributes` tracks only archived videos, so nothing the site serves is ever turned into an LFS
pointer:

```gitattributes
**/stored/*.mp4  filter=lfs diff=lfs merge=lfs -text
**/stored/*.mov  filter=lfs diff=lfs merge=lfs -text
**/stored/*.webm filter=lfs diff=lfs merge=lfs -text
```

> Commit large `stored/` videos through a client that has Git LFS (e.g. GitHub Desktop), and commit
> `.gitattributes` before/with them so the LFS filter applies.

---

## Local preview

The page loads its data with `fetch()`, which browsers **block over `file://`** — opening
`index.html` directly will show an empty projects grid. Serve it over HTTP instead:

```bash
# from the repo root
python3 -m http.server 8000
# then open http://localhost:8000
```

(VS Code's "Live Server" extension works too.)

---

## Deployment

GitHub Pages serves the repo root of `gamedevtc.github.io` on push to **`main`**. No build step.
After pushing, allow ~1 minute and hard-refresh (Pages/CDN caching).

> **Line endings:** the working tree is CRLF while Git stores LF, so a fresh checkout may show large
> "every line changed" diffs on text files. It's cosmetic (doesn't affect the site); a one-time
> `.gitattributes` normalization pass would clean it up if it ever gets annoying.

---

## Tech stack

- Static **HTML / CSS / JavaScript** (vanilla + jQuery from the original template).
- **Font Awesome 6.5.2** (self-hosted in `assets/`; brand icons power the link pills).
- **Fira Code** (Google Fonts) for the terminal-style Documents section.
- **GitHub Pages** hosting; **Git LFS** for archived video.

---

## Credits & License

Built on the **"Read Only"** template by **HTML5 UP** (https://html5up.net · @ajlkn), used under the
**Creative Commons Attribution 3.0** license — full text in [`LICENSE.txt`](LICENSE.txt). Per that
license, this attribution is retained.

Bundled third-party components:

- **Font Awesome** — icons (https://fontawesome.com)
- **jQuery** — https://jquery.com
- **Scrollex** — https://github.com/ajlkn/jquery.scrollex

All portfolio content — text, project data, and images/video under `images/`, `videos/`, and
`downloads/` — © Taylor Christianson. Game screenshots and trailers remain the property of their
respective studios (Halfbrick Studios, Panda Paw Entertainment) and are shown as portfolio work.
