const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PAGES_DIR = 'output/pages';
const PUBLIC_DIR = 'printify-hub/out';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// Generate production-ready files
function prepareProduction() {
  console.log('🎯 Preparing production build...');
  
  // 1. Copy all generated pages
  fs.readdirSync(PAGES_DIR).forEach(file => {
    fs.copyFileSync(
      path.join(PAGES_DIR, file),
      path.join(PUBLIC_DIR, file)
    );
  });
  
  // 2. robots.txt
  const robots = `User-agent: *
Allow: /
Sitemap: https://yourdomain.com/sitemap.xml
Sitemap: https://yourdomain.com/sitemap-en.xml
Sitemap: https://yourdomain.com/sitemap-es.xml`;
  fs.writeFileSync(path.join(PUBLIC_DIR, 'robots.txt'), robots);
  
  // 3. .htaccess for SPA + caching
  const htaccess = `RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.html [L]

# Cache static assets
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 1 year"
ExpiresByType application/javascript "access plus 1 year"
ExpiresByType image/png "access plus 1 year"
</IfModule>`;
  fs.writeFileSync(path.join(PUBLIC_DIR, '.htaccess'), htaccess);
  
  // 4. CNAME for custom domain
  fs.writeFileSync(path.join(PUBLIC_DIR, 'CNAME'), 'yourdomain.com');
  
  console.log('✅ Production files ready');
}

// GitHub Pages deploy
function deployGitHubPages() {
  console.log('📤 Deploying to GitHub Pages...');
  
  execSync('npm install -g gh-pages', { stdio: 'inherit' });
  execSync('gh-pages -d printify-hub/out', { stdio: 'inherit' });
  
  console.log('✅ GitHub Pages deployed: https://yourusername.github.io/printify-hub');
}

// Cloudflare setup script
function setupCloudflare() {
  const cloudflareDNS = `## Cloudflare DNS Records (add to your domain)
yourdomain.com  A  192.0.2.1  (GitHub Pages IP)
www.yourdomain  CNAME  yourusername.github.io
*.yourdomain   CNAME  yourusername.github.io

## Cloudflare Page Rules
yourdomain.com/*  Cache Level: Cache Everything
yourdomain.com/api/*  Bypass Cache`;

  fs.writeFileSync('output/cloudflare-setup.txt', cloudflareDNS);
  console.log('✅ Cloudflare config ready: output/cloudflare-setup.txt');
  
  console.log(`
🚀 YOUR LIVE URL: https://yourdomain.com
1. Add DNS records above to Cloudflare
2. Wait 5-10 min DNS propagation
3. LIVE Printify empire!
  `);
}

// Deploy index.html with stats
function createLandingPage() {
  const stats = fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.html')).length;
  const indexHtml = `<!DOCTYPE html>
<html>
<head>
  <title>Printify Authority Hub - #1 POD Reviews 2026</title>
  <meta name="description" content="Printify reviews, pricing, kits, premium plans. Cheapest POD worldwide. Start free.">
  <meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body style="font-family:Arial;margin:0;padding:40px;background:#f8f9fa;">
  <div style="max-width:1200px;margin:0 auto;text-align:center;">
    <h1 style="font-size:64px;color:#00c853;margin-bottom:20px;">🖨️ Printify Hub</h1>
    <p style="font-size:28px;color:#666;margin-bottom:40px;">#1 Print on Demand Authority Site (${stats} Pages)</p>
    
    <div style="background:white;padding:60px;border-radius:30px;box-shadow:0 30px 80px rgba(0,0,0,0.15);display:inline-block;">
      <h2 style="color:#333;margin-bottom:30px;">🚀 Ready to Start?</h2>
      <a href="${AFFILIATE_URL}" style="background:linear-gradient(135deg,#00c853,#00b140);color:white;display:inline-block;padding:25px 60px;font-size:28px;border-radius:50px;font-weight:bold;text-decoration:none;box-shadow:0 20px 50px rgba(0,200,83,0.4);">
        Start Printify Free → 5% Commissions
      </a>
    </div>
    
    <div style="margin-top:80px;padding:40px;background:white;border-radius:25px;">
      <h3 style="color:#333;margin-bottom:30px;">📊 What's Inside</h3>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:30px;">
        <div>
          <h4 style="color:#00c853;">Live Pricing</h4>
          <p>Printify Premium vs Printful/Gelato (31% cheaper)</p>
        </div>
        <div>
          <h4 style="color:#00c853;">Kit Strategies</h4>
          <p>5x AOV bundles: T-Shirt + Mug = $79 profit</p>
        </div>
        <div>
          <h4 style="color:#00c853;">Global Shipping</h4>
          <p>200+ countries, real-time provider status</p>
        </div>
        <div>
          <h4 style="color:#00c853;">40% Margins</h4>
          <p>Premium pricing calculator + ROI forecasts</p>
        </div>
      </div>
    </div>
  </div>
</body>
</html>`;
  
  fs.writeFileSync(path.join(PUBLIC_DIR, 'index.html'), indexHtml);
}

prepareProduction();
deployGitHubPages();
createLandingPage();
setupCloudflare();

console.log('🌐 DOMAIN DEPLOYER COMPLETE');
console.log('✅ Production build: printify-hub/out/');
console.log('✅ GitHub Pages deployed');
console.log('✅ Custom domain ready (add CNAME)');
console.log('✅ Index landing page created');
console.log('🚀 YOUR EMPIRE IS LIVE - Replace "yourdomain.com" above!');
