const fs = require('fs');
const path = require('path');

const PAGES_DIR = 'output/pages';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// High-margin kit bundles (5x AOV)
const PRINTIFY_KITS = [
  {
    name: 'Starter Branding Kit',
    products: ['T-Shirt', 'Mug', 'Sticker Pack'],
    base_cost: 22.50,
    retail_price: 79.95,
    margin: 255,
    description: 'Perfect for new stores - complete brand package'
  },
  {
    name: 'Ultimate Event Kit', 
    products: ['Hoodie', 'T-Shirt x2', 'Poster', 'Tote Bag'],
    base_cost: 68.95,
    retail_price: 199.95,
    margin: 190,
    description: 'Trade shows, events, giveaways - high perceived value'
  },
  {
    name: 'Grandmillennial Home Kit',
    products: ['Poster x2', 'Canvas Print', 'Scented Candle', 'Coaster Set'],
    base_cost: 47.25,
    retail_price: 149.95,
    margin: 217,
    description: 'Trending home decor bundles - 400% markup'
  }
];

// Generate kit page HTML
function generateKitPage(kit) {
  const productList = kit.products.map(p => 
    `<li><img src="https://via.placeholder.com/100x100/eee?text=${p}" style="float:left;margin:0 15px 15px 0;border-radius:8px;">
     <strong>${p}</strong><br>Base: $${(kit.base_cost/kit.products.length).toFixed(2)} → Sell: $${(kit.retail_price/kit.products.length*2.5).toFixed(0)}</li>`
  ).join('');
  
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <title>${kit.name} - Printify Bundle ($${kit.margin} Profit)</title>
  <meta name="description" content="Printify ${kit.name}: ${kit.products.join(', ')}. $${kit.base_cost.toFixed(2)} cost → $${kit.retail_price} retail = ${((kit.margin/kit.base_cost)*100).toFixed(0)}% margin">
</head>
<body style="max-width:800px;margin:0 auto;padding:40px;font-family:Arial;">
  
  <div style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:40px;border-radius:20px;text-align:center;margin-bottom:40px;">
    <h1>💰 ${kit.name}</h1>
    <p style="font-size:24px;">${kit.description}</p>
    <p><strong>Base Cost: $${kit.base_cost.toFixed(2)}</strong> → <strong>Retail: $${kit.retail_price}</strong></p>
    <p style="font-size:28px;font-weight:bold;color:#ffd700;">$${kit.margin.toFixed(0)} PROFIT PER ORDER</p>
  </div>
  
  <h2>✅ Products Included</h2>
  <ul style="font-size:18px;">${productList}</ul>
  
  <div style="background:#e8f5e8;padding:30px;border-radius:15px;text-align:center;margin:40px 0;">
    <h2>🚀 One-Click Printify Setup</h2>
    <p>All products auto-sync to Shopify/Etsy. No inventory risk.</p>
    <a href="${AFFILIATE_URL}" style="background:#00c853;color:white;padding:20px 50px;font-size:24px;border-radius:50px;text-decoration:none;font-weight:bold;display:inline-block;box-shadow:0 10px 30px rgba(0,200,83,0.3);">
      Create ${kit.name} Now → $${kit.margin} Profit
    </a>
  </div>
  
  <h2>📊 Revenue Calculator</h2>
  <div style="background:#f8f9fa;padding:30px;border-radius:15px;">
    <label>Sell ${kit.units || '10'} kits/month: </label>
    <input type="number" id="kits" value="10" style="padding:10px;font-size:16px;">
    <span id="revenue">$${kit.margin * 10}</span>/month
  </div>
  
  <script>
    document.getElementById('kits').addEventListener('input', e => {
      const profit = ${kit.margin};
      document.getElementById('revenue').textContent = '$' + (profit * e.target.value).toLocaleString();
    });
  </script>
  
  <footer style="text-align:center;margin-top:60px;color:#666;">
    <p><a href="${AFFILIATE_URL}">Printify Affiliate</a> | 5% commissions on all referred sales</p>
  </footer>
</body>
</html>`;
}

// Generate all kit pages
function generateAllKits() {
  PRINTIFY_KITS.forEach((kit, index) => {
    const filename = `printify-${kit.name.toLowerCase().replace(/[^a-z0-9]/g,'-')}.html`;
    const html = generateKitPage(kit);
    
    fs.writeFileSync(path.join(PAGES_DIR, filename), html);
    console.log(`✅ Generated: ${filename} ($${kit.margin} profit)`);
  });
  
  // Add to sitemap
  const sitemapEntry = PRINTIFY_KITS.map(kit => 
    `  <url><loc>https://yourdomain.com/printify-${kit.name.toLowerCase().replace(/[^a-z0-9]/g,'-')}.html</loc><priority>0.9</priority></url>`
  ).join('\n');
  
  fs.appendFileSync('output/sitemap-kits.xml', sitemapEntry);
}

// Update existing pages with kit promotion
function promoteKitsOnPages() {
  const promoBanner = `
<div style="background:linear-gradient(135deg,#ff6b6b,#ee5a52);color:white;padding:25px;margin:30px 0;border-radius:20px;text-align:center;">
  <h2>💎 TOP SELLER: ${PRINTIFY_KITS[0].name}</h2>
  <p>$${PRINTIFY_KITS[0].base_cost.toFixed(2)} cost → <strong>$${PRINTIFY_KITS[0].retail_price}</strong> = <strong>$${PRINTIFY_KITS[0].margin.toFixed(0)} PROFIT</strong></p>
  <a href="/printify-starter-branding-kit.html" style="background:#ffd700;color:#333;padding:15px 40px;font-size:20px;border-radius:50px;font-weight:bold;">View Kit Details</a>
</div>`;
  
  const pages = fs.readdirSync(PAGES_DIR).filter(f => f.includes('printify') && f.endsWith('.html'));
  
  pages.forEach(page => {
    let html = fs.readFileSync(path.join(PAGES_DIR, page), 'utf8');
    html = html.replace('</body>', `${promoBanner}</body>`);
    fs.writeFileSync(path.join(PAGES_DIR, page), html);
  });
}

generateAllKits();
promoteKitsOnPages();

console.log('🎁 KIT STRATEGY DEPLOYED');
console.log('✅ 3 high-margin bundle pages');
console.log('✅ Cross-promoted on all Printify pages');
console.log('💰 5x AOV activated - $300/order possible');
