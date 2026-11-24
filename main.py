#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single funny line -- the excuse a robot vacuum gives after
eating a sock -- to /output/entry.txt.

Deterministic: the output is a fixed string, so every run produces
byte-identical output.
"""

import os

LINE = (
    "In my defense, that sock had been on the floor for three days -- "
    "under house law, that's abandoned property. I just filed the "
    "paperwork. Internally."
)

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(f"entry length {len(LINE)} outside 1..{MAX_CHARS}")
    if not LINE.strip():
        raise SystemExit("entry is blank")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
