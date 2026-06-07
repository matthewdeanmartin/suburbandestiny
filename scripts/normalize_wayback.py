import argparse
import os
import re
import shutil
from pathlib import Path

WAYBACK_RE = re.compile(
    r"https?://web\.archive\.org/web/\d+(?:[a-z_]{0,3})?/(https?:\/\/[^\s'\"<>]+)",
    re.IGNORECASE,
)

WAYBACK_REL_RE = re.compile(
    r"/web/\d+(?:[a-z_]{0,3})?/(https?:\/\/[^\s'\"<>]+)",
    re.IGNORECASE,
)

def rewrite_text(text: str) -> str:
    text = WAYBACK_RE.sub(r"\1", text)
    text = WAYBACK_REL_RE.sub(r"\1", text)
    text = text.replace("http://suburbandestiny.com", "https://suburbandestiny.com")
    return text

def process_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    suffix = src.suffix.lower()

    if suffix in {".html", ".htm", ".css", ".js", ".xml", ".txt"}:
        try:
            content = src.read_text(encoding="utf-8", errors="ignore")
            dst.write_text(rewrite_text(content), encoding="utf-8")
        except Exception:
            shutil.copy2(src, dst)
    else:
        shutil.copy2(src, dst)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--base-url", required=False, default="")
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for path in input_dir.rglob("*"):
        rel = path.relative_to(input_dir)
        out = output_dir / rel
        if path.is_dir():
            out.mkdir(parents=True, exist_ok=True)
            continue
        process_file(path, out)

    print(f"Normalized files written to: {output_dir}")

if __name__ == "__main__":
    main()
