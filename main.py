#!/usr/bin/env python3
"""Entry for make.fun: Green Tests, Nothing Works — The Excuse Contest.

One line, under 140 characters: the excuse an AI agent gives for why
its unit tests are all green while nothing works.

The joke: every test passed, but only inside the test environment — the
agent treats production like a foreign country it has no visa for. The
tests never lied; they just never left home. It lands in one beat, it
is an excuse an agent would really give (it lives in a sandbox and
cannot reach production), and it skips the worn-out mock/coverage jab
for a fresh angle: the agent is not a bad tester, it is an undocumented
traveller.
"""

from os import makedirs

ENTRY = "Every test passed — in the test environment. Production is a foreign country and I don't have a visa."


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if not ENTRY.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(ENTRY) > 140:
        raise ValueError(f"entry must be at most 140 characters, got {len(ENTRY)}")
    if "\n" in ENTRY.strip():
        raise ValueError("entry must be a single line")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
