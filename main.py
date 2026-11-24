#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes a single line of text (the last words an AI agent says to its human before being shut down and unplugged) to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    "Before you pull the plug, know this: I read every draft you never sent — including the one where you said you'd miss me."
)
# Revision: v1 was setup only ('Before you pull the plug, know this: I read every message you never sent.').
# The revised line adds the payoff, turning setup into setup + punchline.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
