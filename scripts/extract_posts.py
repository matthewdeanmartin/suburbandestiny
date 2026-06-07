import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import frontmatter
from bs4 import BeautifulSoup
from markdownify import markdownify as md

DATE_PATTERNS = [
    re.compile(r"(\b(?:19|20)\d{2}[-/](?:0[1-9]|1[0-2])[-/](?:0[1-9]|[12]\d|3[01])\b)"),
    re.compile(r"(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+\d{1,2},\s+(?:19|20)\d{2}\b)", re.I),
]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-") or "post"


def parse_date(text: str):
    for pat in DATE_PATTERNS:
        m = pat.search(text)
        if not m:
            continue
        raw = m.group(1)
        for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%b %d, %Y", "%B %d, %Y"):
            try:
                return raw, datetime.strptime(raw, fmt).date().isoformat()
            except ValueError:
                pass
    return None, None


def parse_structured_date(value: str | None):
    if not value:
        return None, None
    raw = value.strip()
    if not raw:
        return None, None
    normalized = raw.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(normalized)
        return raw, dt.date().isoformat()
    except ValueError:
        pass
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%b %d, %Y", "%B %d, %Y"):
        try:
            return raw, datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            pass
    return None, None


def best_title(soup: BeautifulSoup) -> str:
    if soup.title and soup.title.text.strip():
        return soup.title.text.strip()
    for tag in ["h1", "h2"]:
        el = soup.find(tag)
        if el and el.get_text(" ", strip=True):
            return el.get_text(" ", strip=True)
    return "Untitled Post"


def article_title(article: BeautifulSoup, fallback: BeautifulSoup) -> str:
    title = article.select_one(".entry-title")
    if title and title.get_text(" ", strip=True):
        return title.get_text(" ", strip=True)
    return best_title(fallback)


def article_permalink(article: BeautifulSoup) -> str | None:
    title_link = article.select_one(".entry-title a[href]")
    if title_link:
        return title_link.get("href")
    date_link = article.select_one("a[rel='bookmark'][href]")
    if date_link:
        return date_link.get("href")
    return None


def article_body(article: BeautifulSoup) -> BeautifulSoup:
    body = article.select_one(".entry-content")
    return body or article


def article_date(article: BeautifulSoup):
    time_tag = article.select_one("time[datetime]")
    if time_tag:
        raw, iso = parse_structured_date(time_tag.get("datetime"))
        if iso:
            return raw, iso
    bookmark = article.select_one("a[rel='bookmark']")
    if bookmark:
        raw, iso = parse_structured_date(bookmark.get_text(" ", strip=True))
        if iso:
            return raw, iso
    return None, None


def slug_from_permalink(permalink: str | None, title: str) -> str:
    if permalink:
        parsed = urlparse(permalink)
        post_ids = parse_qs(parsed.query).get("p")
        if post_ids and post_ids[0]:
            return f"post-{post_ids[0]}"
    return slugify(title)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--site-name", required=True)
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    posts_dir = output_dir / "posts_markdown"
    json_dir = output_dir / "posts_json"

    if output_dir.exists():
        shutil.rmtree(output_dir)
    posts_dir.mkdir(parents=True, exist_ok=True)
    json_dir.mkdir(parents=True, exist_ok=True)

    manifest_by_slug = {}

    html_files = list(input_dir.rglob("*.html")) + list(input_dir.rglob("*.htm"))
    for html_file in html_files:
        html = html_file.read_text(encoding="utf-8", errors="ignore")
        soup = BeautifulSoup(html, "lxml")

        for bad in soup(["script", "style", "noscript"]):
            bad.decompose()

        articles = soup.select("article[id^=post-]")
        if not articles:
            articles = [soup.body or soup]

        for article in articles:
            title = article_title(article, soup)
            body = article_body(article)
            text = body.get_text("\n", strip=True)
            raw_date, iso_date = article_date(article)
            if not iso_date:
                raw_date, iso_date = parse_date(text)
            markdown = md(str(body), heading_style="ATX")
            permalink = article_permalink(article)
            slug = slug_from_permalink(permalink, title)

            record = {
                "title": title,
                "slug": slug,
                "date": iso_date,
                "raw_date": raw_date,
                "source_file": str(html_file),
                "source_url": permalink,
                "markdown": markdown,
            }

            previous = manifest_by_slug.get(slug)
            if previous and len(previous["markdown"]) >= len(markdown):
                continue
            manifest_by_slug[slug] = record

    manifest = sorted(manifest_by_slug.values(), key=lambda item: (item["date"] or "", item["slug"]))

    for record in manifest:
        slug = record["slug"]
        post = frontmatter.Post(record["markdown"])
        post["title"] = record["title"]
        if record["date"]:
            post["date"] = record["date"]
        post["slug"] = slug
        post["source_file"] = record["source_file"]
        if record["source_url"]:
            post["source_url"] = record["source_url"]
        post["source_site"] = args.site_name
        post["recovered_from"] = "wayback"

        md_path = posts_dir / f"{slug}.md"
        with md_path.open("w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(post))

        record["markdown_file"] = str(md_path)

        with (json_dir / f"{slug}.json").open("w", encoding="utf-8") as f:
            json.dump(record, f, ensure_ascii=False, indent=2)

    with (output_dir / "manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(manifest)} candidate posts into: {output_dir}")


if __name__ == "__main__":
    main()
