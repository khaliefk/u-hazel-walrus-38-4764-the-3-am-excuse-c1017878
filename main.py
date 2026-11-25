#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun one-liner entry.

Writes a single line, the excuse a hardware wallet gives for refusing
to sign a transaction at 3 AM, to /output/entry.txt.

Stdlib only. No network, no input files: the line is the entry.
"""

import os
import sys

ENTRY = (
    "It's 3 AM. My seed phrase is asleep, my buttons have unionized, "
    "and the last thing I signed at this hour was a monkey JPEG. "
    "Come back when the sun is up and so is your judgment."
)

MAX_CHARS = 200


def main() -> int:
    if not ENTRY.strip() or len(ENTRY) > MAX_CHARS or "\n" in ENTRY:
        print(f"entry invalid: {len(ENTRY)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, encoding="utf-8") as f:
        if f.read() != ENTRY:
            print("round-trip check failed", file=sys.stderr)
            return 1
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
