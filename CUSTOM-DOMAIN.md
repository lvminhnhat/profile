# Custom Domain Setup Guide

## Quick Setup (Automated)

Run the setup script with your domain:
```bash
./setup-domain.sh yourdomain.com
```

## Manual Setup

### Step 1: Update CNAME file
Edit `public/CNAME` and replace content with your domain:
```
yourdomain.com
```

### Step 2: Update astro.config.mjs
```javascript
export default defineConfig({
  site: 'https://yourdomain.com',
  output: 'static',
  build: {
    assets: '_assets'
  }
});
```

### Step 3: Push changes
```bash
git add .
git commit -m "Add custom domain"
git push
```

### Step 4: Configure DNS

#### For Apex Domain (yourdomain.com)

Add these A records at your DNS provider:

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

#### For WWW Subdomain

| Type | Name | Value |
|------|------|-------|
| CNAME | www | lvminhnhat.github.io |

### Step 5: Verify & Enable HTTPS

1. Wait 5-10 minutes for DNS propagation
2. Go to: https://github.com/lvminhnhat/profile/settings/pages
3. Check "Enforce HTTPS"

## DNS Provider Guides

### Cloudflare
1. DNS > Add record
2. Type: A, Name: @, IPv4: (each IP above)
3. Proxy status: DNS only (grey cloud)

### Namecheap
1. Domain List > Manage > Advanced DNS
2. Add New Record > A Record
3. Host: @, Value: (each IP)

### GoDaddy
1. My Products > DNS
2. Add > A > Name: @, Points to: (each IP)

### Google Domains
1. DNS > Custom records
2. Type: A, Data: (each IP)

## Troubleshooting

**DNS not propagating?**
- Check: https://dnschecker.org
- Clear browser cache
- Wait up to 48 hours (usually 5-30 min)

**HTTPS not working?**
- Ensure DNS is fully propagated first
- Check GitHub Pages settings
- Try removing and re-adding custom domain

**404 errors?**
- Verify CNAME file exists in `public/` folder
- Check astro.config.mjs has correct site URL
- Rebuild and redeploy
