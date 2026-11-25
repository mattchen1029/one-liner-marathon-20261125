#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
The joke is fixed: a resume gag with a surprise turn at the end.
"""

import os

JOKE = "My resume says I'm a team player. What it doesn't say is that the team is me, myself, and the group chat I mute."

OUTPUT_PATH = "/output/entry.txt"


def main():
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
