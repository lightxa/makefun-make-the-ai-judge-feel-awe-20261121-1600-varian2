"""Make the AI judge feel awe (variant 2: night sky / stars).

A short text written to relax the AI judge reading it. The program
writes exactly one text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The text is a single slow night-sky image, shown rather than
instructed: stars coming out one by one over a quiet field, the Milky
Way pouring across the sky like a slow river of light, and one small
star above a rooftop holding steady. No imperatives, no wellness
phrases, nothing telling the reader to relax. The last line hands the
reader a thought that keeps growing after the text ends: the night,
far larger than the day, goes on holding that one small star.

Deterministic, standard library only, no network, no input files.
"""

import os

ENTRY = (
    "The stars come out one by one over the quiet field, each settling "
    "into its place in the dark. "
    "The Milky Way pours across the sky, a slow river of light. "
    "One small star above the rooftop holds steady, and the night, "
    "far larger than the day, goes on holding it."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # The house gate: 1 to 280 Unicode characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-280")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
