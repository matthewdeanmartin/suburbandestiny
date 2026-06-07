import argparse
import json
from pathlib import Path

SYSTEM_PROMPT = """You are cleaning up recovered blog posts from the Internet Archive.

Goals:
1. Preserve the author's voice.
2. Remove Wayback artifacts, nav junk, duplicate headers/footers, and broken boilerplate.
3. Fix obvious OCR/archive weirdness and formatting damage.
4. Keep code blocks intact.
5. Produce valid markdown with YAML frontmatter.
6. Do NOT invent facts. Mark uncertain dates as null.
7. Keep links only when they are meaningful.
"""

USER_TEMPLATE = """Clean this recovered blog post.

Return ONLY the cleaned markdown file with YAML frontmatter.

INPUT JSON:
{json_payload}
"""

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--site-name", required=True)
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = input_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    (output_dir / "SYSTEM_PROMPT.txt").write_text(SYSTEM_PROMPT, encoding="utf-8")

    batch_lines = []
    for item in manifest:
        payload = json.dumps(item, ensure_ascii=False, indent=2)
        prompt = USER_TEMPLATE.format(json_payload=payload)

        slug = item["slug"]
        prompt_path = output_dir / f"{slug}.prompt.txt"
        prompt_path.write_text(prompt, encoding="utf-8")
        batch_lines.append(json.dumps({
            "slug": slug,
            "title": item["title"],
            "prompt_file": str(prompt_path),
            "json_file": str(input_dir / "posts_json" / f"{slug}.json"),
        }, ensure_ascii=False))

    (output_dir / "batch.jsonl").write_text("\n".join(batch_lines) + "\n", encoding="utf-8")
    print(f"LLM pack written to: {output_dir}")

if __name__ == "__main__":
    main()
