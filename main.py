#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh entry (account A).

Writes one line, 133 characters, roasting a smart fridge to
/output/entry.txt. Deterministic, stdlib only, no network, no secrets.

The joke: the fridge's 3 a.m. firmware update locks the door behind a
terms-and-conditions screen — written by the leftovers inside it.
Specific to smart fridges (firmware updates, app-style consent screens),
with a surprise turn, and it dodges the obvious cracks about the fridge
ordering groceries or watching you eat.
"""

import os

# The roast: a firmware update that holds the fridge hostage until you
# sign terms written by your own leftovers.
ROAST = (
    "My smart fridge pushed a firmware update at 3 a.m., and now it "
    "won't open until I accept the terms and conditions my leftovers wrote."
)

MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def verify(text: str) -> str:
    """Return the roast, stripped, after enforcing the gate."""
    line = text.strip()
    if not line:
        raise ValueError("roast is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"roast is {len(line)} chars, must be at most {MAX_CHARS}")
    if "\n" in line:
        raise ValueError("roast must be a single line")
    return line


def write_entry(text: str, path: str = OUT_PATH) -> str:
    """Verify the roast and write it to the output file."""
    line = verify(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    return line


def main() -> None:
    line = write_entry(ROAST)
    print(f"Wrote {len(line)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
