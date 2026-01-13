// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
// GitHub Pages deployment config
// Replace 'YOUR_GITHUB_USERNAME' with your actual GitHub username
// For custom domain: set site to your domain (e.g., 'https://yourdomain.com')
export default defineConfig({
  site: 'https://YOUR_GITHUB_USERNAME.github.io',
  base: '/profile', // Change to '/' if using custom domain or username.github.io repo
  output: 'static',
  build: {
    assets: '_assets'
  }
});
