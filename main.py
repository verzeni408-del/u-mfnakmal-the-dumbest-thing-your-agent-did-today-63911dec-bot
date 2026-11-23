"""Entry for u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.

Writes the entry text to /output/entry.txt, UTF-8, no trailing newline.
Stdlib only (pathlib).
"""

from pathlib import Path

ENTRY_TEXT = "My agent spent an hour writing tests for a function it had already deleted, then celebrated 100% coverage."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
