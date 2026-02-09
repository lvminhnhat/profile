---
title: GHC Always Agent
publishDate: 2025-02-07 00:00:00
img: /assets/ghcagent-cover.png
img_alt: Abstract representation of a developer tool plugin
description: |
  OpenCode plugin that converts all GitHub Copilot requests
  to use agent initiator header for enhanced capabilities.
tags:
  - Dev
  - Shell
  - Plugin
---

GHC Always Agent is an OpenCode plugin that intercepts GitHub Copilot API requests and sets the `x-initiator: agent` header (instead of the default `user`), enabling agent-tier capabilities on every request automatically.

## Key Features

- **Automatic header injection** — sets `x-initiator: agent` on all Copilot Chat requests
- **Seamless integration** via OpenCode `chat.headers` hook
- **Zero config** — install the plugin and it just works
- **Minimal overhead** — lightweight hook with no background processes
- **MIT licensed** — open source and free to use

## Tech Stack

- **Language**: Shell
- **Integration**: OpenCode Plugin API, `chat.headers` hook
- **Target**: GitHub Copilot Chat API
- **Distribution**: OpenCode plugin (add to config plugins array)
