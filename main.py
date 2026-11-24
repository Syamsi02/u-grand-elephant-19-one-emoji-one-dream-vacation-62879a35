#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a desert island, the
whole dream vacation in a single glyph -- palm, sand and sea, a faraway
place a stranger can see at a glance.

Pure Python 3.13 standard library. No network, no input files, no
secrets; everything the entry runs is in this file.
"""

import sys
from pathlib import Path

# U+1F3DD DESERT ISLAND: one code point, no variation selector and no
# trailing newline. The gate allows 1 to 8 characters, and an exact tie
# goes to the smaller text, so the file holds exactly these 4 bytes.
EMOJI = "\U0001F3DD"

DEFAULT_OUTPUT = Path("/output/entry.txt")


def pick_output(argv):
    """Return the output path: argv[1] when given, else the gate path."""
    if len(argv) > 2:
        raise SystemExit("usage: python3 main.py [output-path]")
    if len(argv) == 2:
        return Path(argv[1])
    return DEFAULT_OUTPUT


def check_emoji(text):
    """Hold the entry to the gate before anything is written."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 8:
        raise ValueError("entry must be 1 to 8 characters")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji")
    text.encode("utf-8")


def main(argv):
    output = pick_output(argv)
    check_emoji(EMOJI)
    data = EMOJI.encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "wb") as handle:
        handle.write(data)
    print(f"wrote {EMOJI} ({len(data)} bytes) to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
