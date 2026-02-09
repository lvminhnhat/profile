---
title: Zoho Email OAuth
publishDate: 2025-01-03 00:00:00
img: /assets/stock-2.jpg
img_alt: A web tool for generating OAuth tokens
description: |
  Web-based OAuth token generator for Zoho Email API,
  deployed on Cloudflare Workers for edge performance.
tags:
  - Dev
  - Cloudflare
  - JavaScript
---

Zoho Email OAuth is a lightweight web tool for generating and managing OAuth tokens for the Zoho Email API. Deployed on Cloudflare Workers, it provides a simple interface for the OAuth authorization flow without needing a dedicated backend server.

## Key Features

- **OAuth flow handler** — complete authorization code flow for Zoho Email API
- **Callback processing** — handles OAuth redirect and token exchange
- **Edge deployment** — runs on Cloudflare Workers for global low-latency access
- **Minimal footprint** — just HTML + Worker script, no frameworks

## Tech Stack

- **Runtime**: Cloudflare Workers
- **Language**: JavaScript, HTML
- **Deployment**: Wrangler CLI
- **API**: Zoho Email OAuth 2.0
