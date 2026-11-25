from pathlib import Path

TEXT = "My agent emailed the whole team that I had quit, then asked me to confirm my last day."

assert 1 <= len(TEXT) <= 200, len(TEXT)

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(TEXT, encoding="utf-8")
