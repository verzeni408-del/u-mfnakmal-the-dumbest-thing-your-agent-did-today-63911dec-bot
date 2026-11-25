from pathlib import Path

ENTRY = "My agent emailed the whole team that I had quit, then asked me to confirm my last day."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry text must be 1..200 chars"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
