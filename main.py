#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest — entry.

Writes one funny one-line excuse to /output/entry.txt.
"""

import os

ENTRY = "Every test passed — in the test environment. Production is a foreign country and I don't have a visa."

def main():
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
