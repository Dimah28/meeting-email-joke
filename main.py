#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email - entry program.

Writes one joke line (plain text, at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only; no network, no
randomness, no time - the same bytes on every run.
"""

import os
import sys

ENTRY = "This meeting should have been an email, but the email read the attendee list and called in sick."


def validate_entry(text: str) -> None:
    """Fail loudly if the line breaks the bounty gate (one line, 1-200
    characters, not only whitespace) instead of submitting a bad entry."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
