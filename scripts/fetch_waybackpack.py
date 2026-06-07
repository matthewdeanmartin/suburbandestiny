import argparse
import json
import time
from collections import deque
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, urljoin, urlparse, urlunparse

from bs4 import BeautifulSoup
from waybackpack.asset import Asset
from waybackpack.cdx import search
from waybackpack.session import Session

WAYBACK_PREFIX = "/web/"
ALLOWED_QUERY_KEYS = {"m", "p", "page_id", "paged"}
SKIP_PREFIXES = (
    "/wp-admin",
    "/wp-content",
    "/wp-includes",
    "/wp-json",
    "/feed",
    "/comments",
)
HTML_EXTENSIONS = {"", ".htm", ".html"}
STATE_FILE = "_waybackpack_state.json"


def canonicalize_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc.lower() == "web.archive.org" and parsed.path.startswith(WAYBACK_PREFIX):
        marker = parsed.path.find("http://", len(WAYBACK_PREFIX))
        secure_marker = parsed.path.find("https://", len(WAYBACK_PREFIX))
        candidates = [idx for idx in (marker, secure_marker) if idx != -1]
        if candidates:
            original = parsed.path[min(candidates):]
            if parsed.query:
                original = f"{original}?{parsed.query}"
            return canonicalize_url(original)
    scheme = parsed.scheme or "http"
    netloc = parsed.netloc.lower()
    path = parsed.path or "/"
    fragment = ""
    return urlunparse((scheme, netloc, path, "", parsed.query, fragment))


def is_html_like(parsed) -> bool:
    suffix = Path(parsed.path).suffix.lower()
    if suffix in HTML_EXTENSIONS:
        return True
    if parsed.query:
        return True
    return False


def is_candidate_url(url: str, allowed_hosts: set[str]) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    if parsed.netloc.lower() not in allowed_hosts:
        return False
    if any(parsed.path.startswith(prefix) for prefix in SKIP_PREFIXES):
        return False
    if not is_html_like(parsed):
        return False
    if parsed.query:
        keys = set(parse_qs(parsed.query).keys())
        if not keys.intersection(ALLOWED_QUERY_KEYS):
            return False
    return True


def pick_snapshot(url: str, session: Session, to_timestamp: str | None) -> str | None:
    try:
        snapshots = search(url, session=session, to_date=to_timestamp)
    except Exception as exc:
        print(f"Skipping {url}: CDX lookup failed ({exc})")
        return None
    good = [snap for snap in snapshots if snap.get("statuscode") == "200"]
    if not good:
        return None
    return good[-1]["timestamp"]


def output_path_for_url(root: Path, url: str) -> Path:
    parsed = urlparse(url)
    host = parsed.netloc.lower().replace(":", "_")
    parts = [part for part in parsed.path.split("/") if part]
    if not parts:
        parts = ["root"]
    base = root.joinpath(host, *parts)

    if parsed.query:
        query_bits = []
        for key, values in sorted(parse_qs(parsed.query).items()):
            if not values:
                query_bits.extend([key, ""])
                continue
            for value in values:
                query_bits.extend([key, value or ""])
        base = base.joinpath("__query__", *query_bits)

    if Path(parsed.path).suffix.lower() in {".htm", ".html"}:
        return base
    return base / "index.html"


def discover_links(html: bytes, page_url: str) -> Iterable[str]:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup.select("a[href]"):
        href = tag.get("href", "").strip()
        if not href:
            continue
        if href.startswith(("#", "mailto:", "javascript:")):
            continue
        yield canonicalize_url(urljoin(page_url, href))


def save_html(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def load_state(output_root: Path) -> dict:
    state_path = output_root / STATE_FILE
    if not state_path.exists():
        return {"pages": {}}
    try:
        return json.loads(state_path.read_text(encoding="utf-8"))
    except Exception:
        return {"pages": {}}


def save_state(output_root: Path, state: dict) -> None:
    state_path = output_root / STATE_FILE
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="")
    parser.add_argument("--seed-urls", default="")
    parser.add_argument("--output", required=True)
    parser.add_argument("--to-timestamp", default=None)
    parser.add_argument("--delay", type=float, default=1.0)
    parser.add_argument("--max-pages", type=int, default=250)
    parser.add_argument("--allow-hosts", default="")
    parser.add_argument("--user-agent", default="dead_blog-waybackpack")
    args = parser.parse_args()

    raw_seed_urls: list[str] = []
    if args.seed_urls:
        raw_seed_urls.extend(
            part.strip()
            for part in args.seed_urls.split(",")
            if part.strip()
        )
    if args.url:
        raw_seed_urls.append(args.url.strip())
    if not raw_seed_urls:
        parser.error("one of --url or --seed-urls is required")

    seed_urls: list[str] = []
    seen_seeds: set[str] = set()
    for raw_seed in raw_seed_urls:
        seed = canonicalize_url(raw_seed)
        if seed in seen_seeds:
            continue
        seed_urls.append(seed)
        seen_seeds.add(seed)

    output_root = Path(args.output)
    output_root.mkdir(parents=True, exist_ok=True)
    state = load_state(output_root)
    pages = state.setdefault("pages", {})

    allowed_hosts = {urlparse(seed_url).netloc.lower() for seed_url in seed_urls}
    allowed_hosts.update(
        host.strip().lower()
        for host in args.allow_hosts.split(",")
        if host.strip()
    )
    queue = deque(seed_urls)
    visited: set[str] = set()
    expanded: set[str] = set()
    saved = 0

    session = Session(
        follow_redirects=True,
        user_agent=args.user_agent,
        max_retries=3,
        delay_retry=max(5, int(args.delay)),
    )

    for url, metadata in list(pages.items()):
        path = output_root / metadata["relative_path"]
        if not path.exists():
            pages.pop(url, None)
            continue
        queue.append(url)

    while queue and saved < args.max_pages:
        current = queue.popleft()
        if current in expanded:
            continue

        parsed = urlparse(current)
        allowed_hosts.add(parsed.netloc.lower())

        existing = pages.get(current)
        if existing:
            path = output_root / existing["relative_path"]
            if path.exists():
                content = path.read_bytes()
                expanded.add(current)
                visited.add(current)
                for discovered in discover_links(content, current):
                    if discovered in expanded:
                        continue
                    if is_candidate_url(discovered, allowed_hosts):
                        queue.append(discovered)
                continue

        timestamp = pick_snapshot(current, session=session, to_timestamp=args.to_timestamp)
        if not timestamp:
            print(f"Skipping {current}: no archived 200 snapshot found")
            expanded.add(current)
            continue

        asset = Asset(current, timestamp)
        content = asset.fetch(session=session, raw=False)
        if not content:
            print(f"Skipping {current}: empty content")
            expanded.add(current)
            continue

        out_path = output_path_for_url(output_root, current)
        save_html(out_path, content)
        pages[current] = {
            "timestamp": timestamp,
            "relative_path": str(out_path.relative_to(output_root)),
        }
        save_state(output_root, state)
        saved += 1
        visited.add(current)
        expanded.add(current)
        print(f"Saved {current} @ {timestamp} -> {out_path}")

        for discovered in discover_links(content, current):
            if discovered in expanded:
                continue
            if is_candidate_url(discovered, allowed_hosts):
                queue.append(discovered)

        if args.delay:
            time.sleep(args.delay)

    print(f"Fetched {saved} archived HTML page(s) into: {output_root}")


if __name__ == "__main__":
    main()
