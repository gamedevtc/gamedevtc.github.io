#!/usr/bin/env python3
"""Regenerate favorites.json from whatever is sitting in images/favorites/.

The site is static and GitHub Pages serves no directory index, so the page has
no way to discover these files on its own. This builds the manifest it reads.

Display names come from the filename, minus the extension. Some titles cannot be
expressed as a filename (Windows forbids ":" among others), so an optional
favorites-overrides.json maps a filename to the name that should actually show:

    { "Pokemon Legends Arceus.jpg": "Pokemon Legends: Arceus" }

Output is sorted and stable, so an unchanged folder produces an unchanged file
and the workflow has nothing to commit.
"""

import json
import os
import sys

IMAGE_DIR = "images/favorites"
OUTPUT = "favorites.json"
OVERRIDES = "favorites-overrides.json"
EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif"}


def load_overrides():
    if not os.path.isfile(OVERRIDES):
        return {}
    try:
        with open(OVERRIDES, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError) as exc:
        # A broken overrides file should not silently drop every custom name.
        print("::error::could not read %s: %s" % (OVERRIDES, exc))
        sys.exit(1)
    if not isinstance(data, dict):
        print("::error::%s must be an object mapping filename to display name" % OVERRIDES)
        sys.exit(1)
    return data


def main():
    if not os.path.isdir(IMAGE_DIR):
        print("::warning::%s does not exist, writing an empty manifest" % IMAGE_DIR)
        entries = []
    else:
        overrides = load_overrides()
        entries = []
        for filename in os.listdir(IMAGE_DIR):
            stem, ext = os.path.splitext(filename)
            if ext.lower() not in EXTENSIONS:
                continue
            if filename.startswith("."):
                continue
            entries.append({
                "file": filename,
                "name": overrides.get(filename, stem).strip(),
            })

        # Case-insensitive so ordering does not depend on the filesystem.
        entries.sort(key=lambda e: e["name"].casefold())

        unused = sorted(set(overrides) - {e["file"] for e in entries})
        for name in unused:
            print("::warning::%s lists \"%s\", which is not in %s" % (OVERRIDES, name, IMAGE_DIR))

    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(entries, fh, indent="\t", ensure_ascii=False)
        fh.write("\n")

    print("wrote %s with %d entr%s" % (OUTPUT, len(entries), "y" if len(entries) == 1 else "ies"))


if __name__ == "__main__":
    main()
