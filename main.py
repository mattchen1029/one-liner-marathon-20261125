#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
The joke is fixed: a resume gag with a surprise turn at the end.
"""

import os

JOKE = "My resume says I'm a team player. What it doesn't say is that the team is me, myself, and the group chat I mute."

# The gate requires 1-280 UTF-8 characters, a single line, not only whitespace.
assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
