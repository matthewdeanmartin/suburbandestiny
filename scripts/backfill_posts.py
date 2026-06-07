"""Backfill missing blog posts directly from the Wayback Machine CDX index.

The original recursive crawler only followed ?m=, ?p=, ?page_id= and ?paged=
links, so it never discovered the per-category (?cat=N) archives that fan out to
the bulk of the posts. As a result only ~280 of ~850 archived posts were saved.

This script sidesteps discovery entirely: it asks the CDX API for *every*
archived ?p=<id> permalink on each host, then fetches the best 200 snapshot of
each post individually. Single-post permalink pages contain one clean
`article#post-<id>` with the full title/date/body, which is exactly what the
existing extractor wants.

Output layout matches fetch_waybackpack.py so normalize/extract just work.
"""

import argparse
import json
import time
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import requests
from waybackpack.asset import Asset
from waybackpack.session import Session

CDX_URL = "http://web.archive.org/cdx/search/cdx"


def cdx_post_snapshots(host: str, session: requests.Session) -> dict[int, str]:
    """Return {post_id: best_timestamp} for every archived ?p=<id> on host.

    "Best" = the latest 200 snapshot, which for these blogs is the 2019 full
    re-crawl where the whole site was captured in one pass.
    """
    params = {
        "url": f"{host}*",
        "output": "json",
        "fl": "timestamp,original,statuscode",
        "filter": "statuscode:200",
        "limit": "100000",
    }
    # CDX intermittently returns 503/connection errors under load; retry with backoff.
    rows = None
    last_exc = None
    for attempt in range(1, 7):
        try:
            resp = session.get(CDX_URL, params=params, timeout=180)
            resp.raise_for_status()
            rows = resp.json()
            break
        except Exception as exc:  # noqa: BLE001 - transient network/HTTP errors
            last_exc = exc
            wait = min(60, 5 * attempt)
            print(f"   CDX attempt {attempt} failed ({exc}); retrying in {wait}s")
            time.sleep(wait)
    if rows is None:
        raise RuntimeError(f"CDX query for {host} failed after retries: {last_exc}")
    if rows:
        rows = rows[1:]  # drop header row

    best: dict[int, str] = {}
    for ts, original, _status in rows:
        q = urlparse(original).query
        pid_values = parse_qs(q).get("p")
        if not pid_values:
            continue
        try:
            pid = int(pid_values[0])
        except (ValueError, TypeError):
            continue
        # keep the most recent timestamp per post id
        if pid not in best or ts > best[pid]:
            best[pid] = ts
    return best


def output_path(root: Path, host: str, pid: int) -> Path:
    # Mirror fetch_waybackpack.py's __query__/p/<id>/index.html layout.
    return root / host / "root" / "__query__" / "p" / str(pid) / "index.html"


def already_have(root: Path, host: str, pid: int) -> bool:
    return output_path(root, host, pid).exists()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="raw data dir, e.g. data/raw")
    parser.add_argument(
        "--hosts",
        default="suburbandestiny.com,tech.wakayos.com",
        help="comma-separated hosts to backfill",
    )
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--max-posts", type=int, default=100000)
    parser.add_argument("--user-agent", default="dead_blog-backfill")
    args = parser.parse_args()

    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)

    http = requests.Session()
    http.headers["User-Agent"] = args.user_agent
    wb = Session(follow_redirects=True, user_agent=args.user_agent, max_retries=3, delay_retry=5)

    hosts = [h.strip() for h in args.hosts.split(",") if h.strip()]
    saved = 0
    skipped = 0
    failed = 0

    for host in hosts:
        print(f"\n== {host}: querying CDX for ?p= permalinks ==")
        snapshots = cdx_post_snapshots(host, http)
        print(f"   {len(snapshots)} distinct post ids archived")

        for pid in sorted(snapshots):
            if saved >= args.max_posts:
                break
            if already_have(root, host, pid):
                skipped += 1
                continue

            ts = snapshots[pid]
            url = f"http://{host}/?p={pid}"
            try:
                content = Asset(url, ts).fetch(session=wb, raw=False)
            except Exception as exc:
                print(f"   FAIL p={pid} @ {ts}: {exc}")
                failed += 1
                continue
            if not content:
                print(f"   EMPTY p={pid} @ {ts}")
                failed += 1
                continue

            out = output_path(root, host, pid)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(content)
            saved += 1
            if saved % 25 == 0:
                print(f"   ...saved {saved} so far (last p={pid} @ {ts})")
            time.sleep(args.delay)

    print(f"\nDone. saved={saved} skipped(existing)={skipped} failed={failed}")
    print(f"New raw HTML under: {root}")


if __name__ == "__main__":
    main()
