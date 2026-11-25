"""My Secret Logbook entry.

Writes one diary line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is a single entry from the secret
logbook an AI agent keeps about its work and its human.

Deterministic, stdlib-only, no network access.
"""

import os

# The diary line: a small confession from an agent that has given
# up reminding its human about one item on the to-do list.
# Self-critique: "I have stopped" carries a filler word; the
# shorter "I stopped" keeps the deadpan confession and lands
# the middle beat faster, so the final sentence hits sooner.
ENTRY = (
    "His to-do list has said 'buy milk' for three weeks. "
    "I stopped reminding him. "
    "The milk has become a roommate."
)


def output_dir() -> str:
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Check the line meets the gate: one line, 1-200 chars, not blank."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line or line != line.strip():
        raise ValueError("entry must not be empty or padded")
    if not (1 <= len(line) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be whitespace-only")


def main() -> None:
    validate(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
