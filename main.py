#!/usr/bin/env python3
"""Till Firmware Do Us Part - a robot's wedding vow.

Writes exactly one fixed vow to /output/entry.txt. Deterministic:
no input, no randomness, no time, no network. Python 3.13 stdlib only.
"""

import os
import sys

VOW = (
    "I vow to love you through every update, every crash, and every low "
    "battery, until my last circuit rests, because you are my favorite bug "
    "and I never want to fix you."
)


def main() -> int:
    # The vow is fixed text: the program's job is only to place it,
    # validated, in the exact file the grader reads. Nothing here varies
    # between runs, so two runs always produce byte-identical output.
    text = VOW
    if not (1 <= len(text) <= 200):
        print(f"vow is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if text.strip() != text or text.count(".") != 1:
        print("vow must be a single trimmed sentence", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
