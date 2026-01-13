#!/bin/bash
# Script to configure custom domain for GitHub Pages
# Usage: ./setup-domain.sh your-domain.com

DOMAIN=$1

if [ -z "$DOMAIN" ]; then
    echo "Usage: ./setup-domain.sh your-domain.com"
    echo "Example: ./setup-domain.sh minhnhat.dev"
    exit 1
fi

echo "Setting up custom domain: $DOMAIN"

echo "$DOMAIN" > public/CNAME

cat > astro.config.mjs << EOF
// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://$DOMAIN',
  output: 'static',
  build: {
    assets: '_assets'
  }
});
EOF

echo "Files updated!"
echo ""
echo "Next steps:"
echo "1. Run: git add . && git commit -m 'Add custom domain $DOMAIN' && git push"
echo "2. Configure DNS at your domain provider:"
echo ""
echo "   For apex domain ($DOMAIN):"
echo "   Type: A    Name: @    Value: 185.199.108.153"
echo "   Type: A    Name: @    Value: 185.199.109.153"
echo "   Type: A    Name: @    Value: 185.199.110.153"
echo "   Type: A    Name: @    Value: 185.199.111.153"
echo ""
echo "   For www subdomain:"
echo "   Type: CNAME    Name: www    Value: lvminhnhat.github.io"
echo ""
echo "3. Wait 5-10 minutes for DNS propagation"
echo "4. Go to https://github.com/lvminhnhat/profile/settings/pages"
echo "5. Enable 'Enforce HTTPS'"
echo ""
echo "Done! Your site will be live at https://$DOMAIN"
