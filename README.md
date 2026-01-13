# Personal Portfolio Website

A modern, responsive portfolio website built with Astro. Ready to deploy on GitHub Pages.

## Quick Start

```bash
npm install
npm run dev
```

Open http://localhost:4321 to see the site.

## Customization Guide

### 1. Update Personal Info

**Site Title & Name** - `src/components/Nav.astro`:
```typescript
// Line 36 - Change "Jeanine White" to your name
```

**Hero Section** - `src/pages/index.astro`:
- Title (your name)
- Tagline (your intro)
- Roles (Developer, Designer, etc.)

### 2. Social Links

Edit `src/components/Nav.astro`:
```typescript
const iconLinks = [
  { label: 'GitHub', href: 'https://github.com/YOUR_USERNAME', icon: 'github-logo' },
  { label: 'LinkedIn', href: 'https://linkedin.com/in/YOUR_USERNAME', icon: 'linkedin-logo' },
  { label: 'Twitter', href: 'https://twitter.com/YOUR_USERNAME', icon: 'twitter-logo' },
];
```

Available icons: `github-logo`, `linkedin-logo`, `twitter-logo`, `instagram-logo`, `youtube-logo`, `discord-logo`, `tiktok-logo`

### 3. Projects/Work

Add/edit markdown files in `src/content/work/`:
- `bloom-box.md`
- `h2o.md`
- `markdown-mystery-tour.md`
- `nested/duvet-genius.md`

Each project needs frontmatter:
```yaml
---
title: Project Name
publishDate: 2024-01-01
img: /assets/project-image.jpg
img_alt: Image description
description: Brief description
tags:
  - Design
  - Dev
---
```

### 4. About Page

Edit `src/pages/about.astro` with your:
- Background
- Education
- Skills

### 5. Images

Replace images in `public/assets/`:
- `portrait.jpg` - Your photo
- `at-work.jpg` - Action shot
- `stock-*.jpg` - Project images

## Deploy to GitHub Pages

### Option 1: Automatic (GitHub Actions)

1. Push to GitHub repository
2. Go to Settings > Pages
3. Source: GitHub Actions
4. Push to `main` branch triggers deploy

### Option 2: Manual

```bash
npm run build
# Upload ./dist folder to your hosting
```

### Configuration

Edit `astro.config.mjs`:
```javascript
export default defineConfig({
  site: 'https://YOUR_USERNAME.github.io',
  base: '/REPO_NAME',  // or '/' for custom domain
});
```

## Commands

| Command           | Action                              |
|-------------------|-------------------------------------|
| `npm run dev`     | Start dev server (localhost:4321)   |
| `npm run build`   | Build for production                |
| `npm run preview` | Preview production build            |

## Tech Stack

- [Astro](https://astro.build) - Static site generator
- CSS Variables - Theming & dark mode
- Phosphor Icons - Icon set

## License

MIT
