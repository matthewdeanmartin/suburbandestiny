import argparse
import shutil
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--posts", required=True)
    parser.add_argument("--site", required=True)
    parser.add_argument("--engine", required=True, choices=["hugo", "eleventy"])
    args = parser.parse_args()

    posts = Path(args.posts)
    site = Path(args.site)

    if args.engine == "hugo":
        target = site / "content" / "posts"
    else:
        target = site / "src" / "posts"

    target.mkdir(parents=True, exist_ok=True)

    count = 0
    for md_file in posts.glob("*.md"):
        shutil.copy2(md_file, target / md_file.name)
        count += 1

    print(f"Copied {count} posts into: {target}")

if __name__ == "__main__":
    main()
