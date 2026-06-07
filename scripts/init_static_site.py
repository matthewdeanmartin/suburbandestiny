import argparse
from pathlib import Path

HUGO_CONFIG = """baseURL = "/"
languageCode = "en-us"
title = "Recovered Blog"
"""

ELEVENTY_PACKAGE = """{
  "name": "recovered-blog",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "npx @11ty/eleventy --serve",
    "build": "npx @11ty/eleventy"
  }
}
"""

ELEVENTY_CONFIG = """export default function(eleventyConfig) {
  return {
    dir: {
      input: "src",
      output: "_site"
    }
  };
}
"""

INDEX_MD = """---
title: Home
---

Recovered blog content.
"""

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--site-name", required=True)
    parser.add_argument("--engine", required=True, choices=["hugo", "eleventy"])
    args = parser.parse_args()

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    if args.engine == "hugo":
        (out / "content" / "posts").mkdir(parents=True, exist_ok=True)
        (out / "layouts").mkdir(parents=True, exist_ok=True)
        (out / "hugo.toml").write_text(HUGO_CONFIG, encoding="utf-8")
        (out / "content" / "_index.md").write_text(INDEX_MD, encoding="utf-8")
    else:
        (out / "src" / "posts").mkdir(parents=True, exist_ok=True)
        (out / "package.json").write_text(ELEVENTY_PACKAGE, encoding="utf-8")
        (out / "eleventy.config.js").write_text(ELEVENTY_CONFIG, encoding="utf-8")
        (out / "src" / "index.md").write_text(INDEX_MD, encoding="utf-8")

    print(f"Initialized {args.engine} site at: {out}")

if __name__ == "__main__":
    main()
