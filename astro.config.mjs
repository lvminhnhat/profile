// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://lvminhnhat.github.io',
  base: '/profile',
  output: 'static',
  build: {
    assets: '_assets'
  }
});
