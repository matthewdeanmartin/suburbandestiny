# Makefile for recovering an archived blog from the Wayback Machine,
# converting it into LLM-friendly content, and staging it for a static site.
#
# Designed to work from common Windows shells as well as POSIX shells.
#
# Usage examples:
#   make help
#   make bootstrap
#   make fetch URL=https://suburbandestiny.com/Tech
#   make normalize
#   make extract
#   make llm-pack
#   make site-init
#   make all URL=https://suburbandestiny.com/Tech
#
# Optional variables:
#   URL=http://suburbandestiny.com/
#   FETCH_URLS=http://suburbandestiny.com/,http://suburbandestiny.com/Tech/
#   TIMESTAMP=20120101000000
#   SITE_NAME=suburbandestiny-tech
#   STATIC_SITE=eleventy   # or hugo
#   FETCH_DELAY=1
#   FETCH_MAX_PAGES=1000
#   FETCH_ALLOW_HOSTS=suburbandestiny.com,www.suburbandestiny.com,tech.wakayos.com
#   PYTHON=python

URL ?= http://suburbandestiny.com/
FETCH_URLS ?= http://suburbandestiny.com/,http://suburbandestiny.com/Tech/
TIMESTAMP ?=
SITE_NAME ?= suburbandestiny-tech
STATIC_SITE ?= eleventy
FETCH_DELAY ?= 1
FETCH_MAX_PAGES ?= 1000
FETCH_ALLOW_HOSTS ?= suburbandestiny.com,www.suburbandestiny.com,tech.wakayos.com

PYTHON ?= python
PIP := .venv/Scripts/pip.exe
PY := .venv/Scripts/python.exe

ROOT := $(CURDIR)
DATA_DIR := $(ROOT)/data
RAW_DIR := $(DATA_DIR)/raw
RAW_FETCH_DIR := data/raw
NORMALIZED_DIR := $(DATA_DIR)/normalized
EXTRACTED_DIR := $(DATA_DIR)/extracted
LLM_DIR := $(DATA_DIR)/llm
SITE_DIR := $(ROOT)/site
WAYBACKPACK_UA := dead_blog-waybackpack

.PHONY: help bootstrap py-bootstrap clean dirs \
	fetch normalize extract llm-pack \
	site-init site-copy all diagnose

help:
	@echo ""
	@echo "Targets:"
	@echo "  make bootstrap              Install Python venv deps"
	@echo "  make fetch URL=...          Crawl archived HTML with waybackpack"
	@echo "  make normalize              Rewrite Wayback links and clean HTML"
	@echo "  make extract                Extract posts into markdown + json"
	@echo "  make llm-pack               Build LLM-ready prompt/input files"
	@echo "  make site-init              Create a starter static site scaffold"
	@echo "  make site-copy              Copy extracted markdown into the static site"
	@echo "  make all URL=...            Run the full pipeline"
	@echo "  make clean                  Remove generated files"
	@echo "  make diagnose               Print environment info"
	@echo ""
	@echo "Variables:"
	@echo "  URL=$(URL)"
	@echo "  FETCH_URLS=$(FETCH_URLS)"
	@echo "  TIMESTAMP=$(TIMESTAMP)"
	@echo "  SITE_NAME=$(SITE_NAME)"
	@echo "  STATIC_SITE=$(STATIC_SITE)"
	@echo "  FETCH_DELAY=$(FETCH_DELAY)"
	@echo "  FETCH_MAX_PAGES=$(FETCH_MAX_PAGES)"
	@echo "  FETCH_ALLOW_HOSTS=$(FETCH_ALLOW_HOSTS)"
	@echo ""

dirs:
	"$(PYTHON)" -c "from pathlib import Path; [Path(p).mkdir(parents=True, exist_ok=True) for p in [r'$(DATA_DIR)', r'$(RAW_DIR)', r'$(NORMALIZED_DIR)', r'$(EXTRACTED_DIR)', r'$(LLM_DIR)', r'$(SITE_DIR)']]"

diagnose:
	@echo "Ruby:"
	-@ruby --version
	@echo ""
	@echo "Python:"
	-@$(PYTHON) --version
	@echo ""
	@echo "Node:"
	-@node --version
	@echo ""
	@echo "URL=$(URL)"
	@echo "FETCH_URLS=$(FETCH_URLS)"
	@echo "TIMESTAMP=$(TIMESTAMP)"
	@echo "STATIC_SITE=$(STATIC_SITE)"
	@echo "FETCH_DELAY=$(FETCH_DELAY)"
	@echo "FETCH_MAX_PAGES=$(FETCH_MAX_PAGES)"
	@echo "FETCH_ALLOW_HOSTS=$(FETCH_ALLOW_HOSTS)"

bootstrap: dirs py-bootstrap

py-bootstrap:
	@echo "==> Creating Python venv"
	"$(PYTHON)" -c "from pathlib import Path; import subprocess, sys; sys.exit(0 if Path(r'$(PY)').exists() else subprocess.call([sys.executable, '-m', 'venv', '.venv']))"
	"$(PY)" -m pip install --upgrade pip
	"$(PY)" -m pip install -r requirements.txt

fetch: dirs
	@echo "==> Fetching archived site with waybackpack"
	"$(PY)" scripts/fetch_waybackpack.py \
		--seed-urls "$(FETCH_URLS)" \
		--output "$(RAW_DIR)" \
		--user-agent "$(WAYBACKPACK_UA)" \
		--delay "$(FETCH_DELAY)" \
		--max-pages "$(FETCH_MAX_PAGES)" \
		--allow-hosts "$(FETCH_ALLOW_HOSTS)" \
		$(if $(TIMESTAMP),--to-timestamp "$(TIMESTAMP)",)

normalize: dirs
	@echo "==> Normalizing downloaded HTML/assets"
	"$(PY)" scripts/normalize_wayback.py \
		--input "$(RAW_DIR)" \
		--output "$(NORMALIZED_DIR)" \
		--base-url "$(URL)"

extract: dirs
	@echo "==> Extracting posts into markdown/json"
	"$(PY)" scripts/extract_posts.py \
		--input "$(NORMALIZED_DIR)" \
		--output "$(EXTRACTED_DIR)" \
		--site-name "$(SITE_NAME)"

llm-pack: dirs
	@echo "==> Packaging extracted content for LLM cleanup"
	"$(PY)" scripts/build_llm_pack.py \
		--input "$(EXTRACTED_DIR)" \
		--output "$(LLM_DIR)" \
		--site-name "$(SITE_NAME)"

site-init: dirs
	@echo "==> Initializing static site scaffold"
	"$(PY)" scripts/init_static_site.py \
		--output "$(SITE_DIR)" \
		--site-name "$(SITE_NAME)" \
		--engine "$(STATIC_SITE)"

site-copy: dirs
	@echo "==> Copying markdown content into static site"
	"$(PY)" scripts/copy_into_site.py \
		--posts "$(EXTRACTED_DIR)/posts_markdown" \
		--site "$(SITE_DIR)" \
		--engine "$(STATIC_SITE)"

all: bootstrap fetch normalize extract llm-pack site-init site-copy
	@echo ""
	@echo "Done."
	@echo "Look at:"
	@echo "  $(EXTRACTED_DIR)"
	@echo "  $(LLM_DIR)"
	@echo "  $(SITE_DIR)"
	@echo ""

clean:
	"$(PYTHON)" -c "import shutil; from pathlib import Path; [shutil.rmtree(Path(p), ignore_errors=True) for p in [r'.venv', r'vendor', r'$(DATA_DIR)', r'$(SITE_DIR)', r'-p', r'C%3a']]"
