# Résumé Content — Taylor Christianson

**Working document.** Source content for the **1-page** (default / ATS workhorse) and **2-page**
(expanded) résumés. Copy the pieces you need into your résumé tool. This file is not served on the
site. No em dashes are used, per preference.

Structure:
1. Shared blocks (contact, title, summary, skills) — used by both versions.
2. **One-page version** — experience/projects, condensed.
3. **Two-page version** — experience/projects, expanded.
4. Notes & choices to review.

---

## 1. Shared blocks (both versions)

### Contact / header

```
TAYLOR CHRISTIANSON
Nampa, ID | (402) 770-8168 | tchristianson@alumni.fullsail.edu
Portfolio: GameDevTC.github.io | LinkedIn: linkedin.com/in/gamedevtaylor/
```

### Title (pick one — aligns with the LinkedIn headline)

- **Lead Programmer & Game Designer** | Multiplayer, Gameplay Systems & Tools  *(recommended, matches LinkedIn)*
- Game Developer & Technical Lead | Multiplayer, Systems & Gameplay
- Lead Programmer | Unity & C#  *(closest to your current résumé title)*

### Professional summary

**Short (for the 1-page):**
> Game developer and technical lead with 5 years shipping across two studios, taking projects from
> concept to release across gameplay, systems, netcode, AI, UI, tech art, tools, and design. Recently
> built a co-op multiplayer game to a live Steam demo in two months, and previously led a hex-grid
> roguelike from a one-week jam prototype to closed beta over three years.

**Long (for the 2-page):**
> Game developer and technical lead with 5 years of professional experience across two studios, and a
> track record of taking projects from pitch to release. Consistently move into lead roles, pitching
> ideas, building prototypes, and driving small teams from concept through production. Comfortable
> owning any layer of a game: gameplay, systems architecture, multiplayer netcode, AI, UI, tech art,
> tools, and design. Fluent with modern AI-assisted development workflows to ship at small-team speed.

### Skills

```
Languages:   C# | C++ | HLSL | HTML
Engines:     Unity (URP / HDRP / 6 / Cloud) | Photon Fusion | FMOD | iOS & Android
Tools:       Perforce | Plastic SCM | Git | TeamCity | JetBrains Rider | Visual Studio | Cursor AI | Claude Code
Specialties: Multiplayer & Netcode | Gameplay & Systems Architecture | Game AI | Procedural Generation |
             Editor Tooling | UI/UX Implementation | Shaders & Tech Art | Profiling & Optimization |
             Game & Systems Design | Team Leadership | Agile/Scrum | AI-Assisted Development
```

---

## 2. ONE-PAGE VERSION (default / ATS workhorse)

*Use the shared Contact + Title + Short Summary + Skills above, then:*

### EXPERIENCE

**Senior Unity Developer & Lead Designer — Panda Paw Entertainment** — MAR 2026 – PRESENT
- Pitched, designed, and built **CatchUp Showdown**, a co-op multiplayer climbing game, from concept to a live Steam demo in two months; releasing at Steam Next Fest, October 2026. Lead designer and systems/gameplay programmer on a four-person core team.
- Architected the multiplayer on Photon Fusion around a fully deterministic level system, so late-joining players rebuild a bit-identical world with minimal bandwidth, then built the host-authoritative scoring and trick-combo system on top.
- Built the entire uGUI front end (HUD widgets, main menu, pause menu, shop) on a generate-then-author workflow: code-generated for consistency, then hand-repainted and animated in-editor. Authored the visual polish myself.
- Owned the guard AI, gadget systems, and operator tooling for **Swipers**, an asymmetric co-op heist game (in development): a component-based state machine with dual-zone vision and audio-driven hearing (FMOD plus live voice chat).

**Lead Programmer / Project Lead — Halfbrick Studios** — OCT 2021 – MAR 2026
- Architected **Scraptics**, a tactical hex-grid roguelike in Unity 6, from a one-week jam prototype through three years of production to closed beta on iOS and Android, owning the full systems stack: recursive puzzle algorithms, enemy AI, turn management, and roguelike progression.
- Designed and implemented a modular, behavior-based enemy AI system that let the team prototype new enemy types without engineering dependencies.
- Completed a full performance overhaul in four weeks, taking the game from sub-20fps with device overheating to a stable 60fps ahead of beta.
- Led a team of four across the full production lifecycle (workload, technical direction, reviews, and mentoring), and pitched 4+ jam projects, two greenlit for full production and two shipped.

### EDUCATION
**B.S., Game Development** — Full Sail University, Winter Park, FL — NOV 2018 – JUN 2021

### SELECTED PROJECTS
- **Sumo Fight** (Unity, Photon) — 3D multiplayer party game, shipped in a 1-week Halfbrick jam as lead programmer (real-time customization sync + core gameplay over Photon).
- **To The Moon!** (Unity, Photon) — 3D multiplayer space shooter capstone; project lead on a team of 6; full Photon stack + compute-shader AI ships.

---

## 3. TWO-PAGE VERSION (expanded)

*Use the shared Contact + Title + Long Summary + Skills above, then:*

### PROFESSIONAL EXPERIENCE

**Senior Unity Developer & Lead Designer — Panda Paw Entertainment** — Remote — MAR 2026 – PRESENT
Systems programmer, gameplay developer, and lead designer on a small core team building co-op
multiplayer games from pitch to release.

*CatchUp Showdown (Unity, C#, Photon Fusion) — co-op multiplayer climbing game; Steam Next Fest, Oct 2026, demo live*
- Pitched, designed, and built the game from concept to a live Steam demo in two months as lead designer and systems/gameplay programmer.
- Architected the multiplayer on Photon Fusion around a fully deterministic level system (the entire level is a pure function of two networked values), so late-joining players rebuild a bit-identical world with minimal bandwidth.
- Designed and built a host-authoritative scoring pipeline: quality-weighted rewards, 25+ detectable trick combos, and a crowd "trick request" mechanic that feeds player performance back into level difficulty.
- Built the entire uGUI front end (HUD widgets, main menu, pause menu, and shop, with full controller support) on a generate-then-author workflow: each element is code-generated for consistency, then hand-repainted and animated in-editor. Authored the visual polish myself.
- Wrote custom URP shaders and render features (screen-space transition wipes, silhouette shadows, tile and combo-fire effects) and built a Tower Balance editor tool for stage authoring and difficulty tuning.
- Delivered the player-facing meta: progression, gacha cosmetics, encrypted Steam Cloud saves, leaderboards, and an event-driven live friends list wired to Steam lobby visibility.

*Swipers (Unity, C#, Photon Fusion, FMOD) — asymmetric co-op heist game (in development)*
- Owned the guard AI: a component-based state machine with dual-zone vision, audio-driven hearing (FMOD plus live voice chat), line-of-sight pursuit, and data-driven spawning and patrol routing.
- Built the gadget framework and gadgets (throwable teleporter, slow-motion beam, AI decoy) and the operator "command station," including map-marker puzzles and a custom render-feature X-ray lens.

**Lead Programmer / Project Lead — Halfbrick Studios** — Remote / Nampa, ID — OCT 2021 – MAR 2026
Grew into lead roles across every project as programmer, designer, and team lead. Pitched regularly in
internal jams, with multiple projects greenlit for full production.

*Scraptics (Unity 6, C#) — tactical hex-grid roguelike; team lead, lead programmer, lead designer, 2+ yrs*
- Architected and implemented the entire systems stack from prototype to closed beta: turn management, hex-grid logic, inventory-puzzle systems, and roguelike progression loops.
- Wrote complex recursive algorithms powering the core inventory/puzzle mechanic.
- Designed and programmed a modular enemy AI behavior system for varied combat encounters, usable by the team without engineering dependencies.
- Developed custom editor tools for content creation and streamlined team workflows, and implemented UI/UX across all screens and menus.
- Delivered cross-platform iOS and Android builds with a full performance overhaul (sub-20fps and overheating to a stable 60fps in four weeks).
- Built cross-platform save systems and leaderboard networking with metadata architecture on Unity Cloud Services.
- Led a team of four across production: workload, priorities, technical direction, reviews, and mentoring.

*Unannounced Mobile Project (Unity, C#) — 2D endless runner with a physics-driven swinging mechanic (paused)*
- Created the greenlit prototype that established the core loop and movement feel; led physics prototyping and iteration as project lead and lead programmer for a team of 4.

*Halfbrick game jams*
- **Sumo Fight** (Unity HDRP, Photon) — multiplayer party game, 1 week, lead programmer on a team of 5; built Photon networking for customization sync and core gameplay.
- **Survivors Aren't Dead** (Unity 6) — survivor-like action game, 1 week, project lead on a team of 4; pitch, core gameplay, enemy AI, and sound design.

### INDEPENDENT & ACADEMIC PROJECTS
- **To The Moon!** (Unity, Photon) — 3D multiplayer space shooter; Full Sail capstone, project lead on a team of 6. Built the full Photon stack (GameManager, MatchManager, weapons, procedural maps) and compute-shader AI fighter ships; programmed all multiplayer UI.
- **Retrospectre** (Unity) — 2.5D metroidvania; project lead on a team of 4. AI for 8+ enemy types, player/weapon systems, and all interactable systems (destructibles, climbables, moving platforms, puzzles).
- **Memoria Damnum** (Global Game Jam 2020) — programming lead on a 9-person, 48-hour team; object-pooling with persistent collection state, plus level design, audio, and VFX.

### EDUCATION
**B.S., Game Development** — Full Sail University, Winter Park, FL — NOV 2018 – JUN 2021

### FAVORITE TITLES
Guild Wars • God Of War • Slay The Spire • Ratchet and Clank • Ghost of Tsushima • Remnant • Backpack Hero • Pokémon Legends: Arceus • Returnal • Shadow Warrior • Titanfall 2 • Tenchu Z • Viva Piñata • Sly Cooper • Marvel Snap • Darkest Dungeon • Valheim • Helldivers 2

---

## 4. Notes & choices to review

- **Panda Paw shown as "Present," no furlough note.** Standard for a résumé; explain the furlough in a
  cover letter or interview, not on the page. (This differs from your portfolio, where we did surface it.)
- **Panda Paw location = "Remote"** is an assumption. Correct it if it was hybrid/on-site.
- **Title update:** changed from "Lead Software Engineer | Unity & C#" toward the broader
  positioning. Swap in whichever title line you prefer from Section 1.
- **New skills added** from the Panda Paw work: Photon Fusion, FMOD, Plastic SCM, Claude Code, plus
  Multiplayer/Netcode, Shaders & Tech Art, and AI-Assisted Development. Trim if any feel thin.
- **"Favorite Titles"** is now included at the end of the 2-page version (full list preserved),
  and cut from the 1-page for space. A nice personality touch some studios like; move or drop as you like.
- **Dates:** your current résumé says Halfbrick ended MAR 2026; the professional summary said FEB 2026.
  I used MAR 2026 (matches the portfolio). Fix if FEB is correct.
- **Ordering within Panda Paw:** CatchUp is first because it is the shipped/demoed, higher-impact title.
  Swap if you would rather lead with Swipers.
