# Suburban Destiny — recovered weblogs

The recovered weblogs of Matthew Martin, rebuilt from the Internet Archive
Wayback Machine and published as a single [Eleventy](https://www.11ty.dev/) site
with two sections:

- **Life** — 40 posts (2013–2020), originally `suburbandestiny.com`.
- **Tech** — 240 posts (2006–2020), originally `tech.wakayos.com`.

The two sections share one black / white / grey theme; the nav highlights
whichever blog you are currently reading.

> **Note:** recovery is incomplete. The non-`www` `suburbandestiny.com` capture
> referenced many category archives (`?cat=1..31+`) that were never crawled, so
> more posts likely remain to be backfilled from Wayback.

## Layout

| Path | What it is |
| --- | --- |
| `scripts/` | The recovery pipeline (fetch → normalize → extract → llm-pack → site). |
| `Makefile` | Drives the pipeline. `make help` for targets. |
| `data/extracted/posts_markdown/` | Recovered posts as Markdown (source of truth). |
| `site/src/life/`, `site/src/tech/` | The two blog sections. |
| `site/` | The Eleventy site. |

## Building the site locally

```sh
cd site
npm install
npm run build      # outputs to site/_site
npm start          # live preview at http://localhost:8080
```

Local builds and the deployed site are served under the `/suburbandestiny/`
path prefix (the GitHub Pages project-site subpath, which must match the repo
name — see `pathPrefix` in `site/eleventy.config.js`). To preview at the root:

```sh
cd site
npx @11ty/eleventy --serve --pathprefix=/
```

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the
Eleventy site and publishes it to GitHub Pages. After the first push, enable
Pages in the repository settings with **Source: GitHub Actions**.

The live URL will be `https://matthewdeanmartin.github.io/suburbandestiny/`.
