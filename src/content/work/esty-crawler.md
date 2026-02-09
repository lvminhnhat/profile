---
title: Etsy Crawler Extension
publishDate: 2025-11-06 00:00:00
img: /assets/stock-1.jpg
img_alt: Browser extension for Etsy product data scraping
description: |
  Chrome extension for scraping Etsy product data with
  dashboard, CSV export, and automatic multi-page crawling.
tags:
  - Dev
  - JavaScript
  - Chrome Extension
---

Etsy Crawler Extension is a full-featured Chrome extension for scraping product data from Etsy. It provides a floating panel for search configuration, automatic multi-page crawling, and a dashboard with full-text search and CSV export.

## Key Features

- **Floating panel** for configuring search parameters directly on Etsy pages
- **Automatic multi-page crawl** — set it and let it scrape across multiple result pages
- **Save Product button** on each Etsy listing for manual data capture
- **Smart deduplication** via `chrome.storage` to avoid duplicate entries
- **Dashboard** with full-text search, time-based filters, and CSV export
- **Auto-update support** via `updates.json` for seamless version management

## Tech Stack

- **Language**: Vanilla JavaScript, CSS
- **Platform**: Chrome Extensions API
- **Storage**: `chrome.storage.local` for persistent data
- **Packaging**: ZIP + SHA256 + HMAC verification scripts
