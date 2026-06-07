"""Split extracted posts into the site's two sections (life / tech).

Classification is by source host of each post:
  - tech.wakayos.com            -> tech
  - *.suburbandestiny.com       -> life
Undated "pages" (About, Comment Policy) are routed to a section too, so the
right header/footer shows. about / comment-policy -> tech; about-me -> life.

Writes Markdown into site/src/life and site/src/tech, replacing whatever was
there. The per-section directory data files (life.json / tech.json) and the
index/landing templates are left untouched.
"""

import argparse
import shutil
from pathlib import Path

import frontmatter

LIFE_PAGES = {"about-me"}
TECH_PAGES = {"about", "comment-policy"}
# Near-duplicate captures of pages we already keep under a cleaner slug.
SKIP_SLUGS = {"commenting-policy"}


def section_for(post: frontmatter.Post, slug: str) -> str:
    url = (post.get("source_url") or "").lower()
    if "tech.wakayos.com" in url:
        return "tech"
    if "suburbandestiny.com" in url:
        return "life"
    # Undated pages have no source_url; route by known slug.
    if slug in LIFE_PAGES:
        return "life"
    if slug in TECH_PAGES:
        return "tech"
    # Default: anything else with a date but no recognised host -> tech
    # (tech is the older/larger blog); this should be rare.
    return "tech"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--posts", required=True, help="data/extracted/posts_markdown")
    parser.add_argument("--site", required=True, help="site dir")
    args = parser.parse_args()

    posts = Path(args.posts)
    src = Path(args.site) / "src"
    life_dir = src / "life"
    tech_dir = src / "tech"

    # Clear existing markdown posts but keep templates and *.json config.
    for d in (life_dir, tech_dir):
        d.mkdir(parents=True, exist_ok=True)
        for md_file in d.glob("*.md"):
            md_file.unlink()

    counts = {"life": 0, "tech": 0}
    for md_file in posts.glob("*.md"):
        slug = md_file.stem
        if slug in SKIP_SLUGS:
            continue
        post = frontmatter.load(md_file)
        section = section_for(post, slug)
        target = (life_dir if section == "life" else tech_dir) / md_file.name
        shutil.copy2(md_file, target)
        counts[section] += 1

    print(f"life={counts['life']} tech={counts['tech']} "
          f"total={counts['life'] + counts['tech']}")


if __name__ == "__main__":
    main()
