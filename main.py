#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes exactly one sentence (110 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no clock, no environment variables, standard library only.
"""

import sys
from pathlib import Path

ENTRY = (
    "My grandmother said, 'If they gossip with you, they'll gossip "
    "about you,' and I have never once heard it fail."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main(argv=None):
    """Write ENTRY to the output path (default /output/entry.txt)."""
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) > 1:
        print("usage: main.py [output-path]", file=sys.stderr)
        return 2
    output = Path(args[0]) if args else DEFAULT_OUTPUT

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")

    # Self-check: read back and hold the entry to the gate.
    text = output.read_text(encoding="utf-8")
    assert text == ENTRY, "entry changed between write and read-back"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate needs 1-200"
    assert text.strip(), "entry must not be only whitespace"
    # One sentence: exactly one period, and it closes the sentence.
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    print(f"Wrote {len(text)} characters to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
