# Favorite game covers

Drop cover images straight into this folder. On push, a GitHub Action rebuilds
`favorites.json` at the repo root and the scrolling strip at the bottom of the
site picks them up. Nothing else to edit.

- **The filename is the display name.** `Titanfall 2.jpg` shows as "Titanfall 2".
  Spaces, apostrophes and accents are all fine.
- **Accepted formats:** png, jpg, jpeg, webp, avif, gif.
- **Sizing:** every cover is scaled to the same height and keeps its own
  proportions, so nothing gets cropped. Anything from roughly 300px tall upward
  looks good. Very large files just cost load time.
- **Order is randomised in the browser** on every page load, so the strip does not always open
  on the same few covers. `favorites.json` itself stays sorted alphabetically, which keeps the
  generated file stable and stops the Action committing a reshuffle on every run.

## Titles a filename cannot express

Windows forbids `:` in filenames, so for something like *Pokémon Legends: Arceus*
name the file without it and add an entry to `favorites-overrides.json` at the
repo root:

```json
{
  "Pokemon Legends Arceus.jpg": "Pokémon Legends: Arceus"
}
```

That file is optional. Without it, the filename is used as-is.

## Do not hand-edit favorites.json

It is generated. Any manual change is overwritten on the next push that touches
this folder.
