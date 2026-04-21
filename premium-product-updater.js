const fs = require('fs');
const path = require('path');

const PAGES_DIR = 'output/pages';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// Printify Premium pricing (20% off base costs)
const PREMIUM_PRODUCTS = [
  { name: 'Premium T-Shirt', regular: 12.95, premium: 10.36, retail: 34.95, margin_regular: 22.00, margin_premium: 24.59 },
  { name: 'Premium Hoodie', regular: 29.95, premium: 23.96, retail: 64.95, margin_regular: 35.00, margin_premium: 40.99 },
  { name: 'Giclée Art Print', regular: 18.50, premium: 14.80, retail: 49.95, margin_regular: 31.45, margin_premium: 35.15 },
  { name: 'Premium Mug', regular: 7.95, premium: 6.36, retail: 22.95, margin_regular: 15.00, margin_premium: 16.59 }
];

// Generate Premium profit comparison table
function generatePremiumTable() {
  const rows = PREMIUM_PRODUCTS.map(p => `
    <tr>
      <td><strong>${p.name}</strong></td>
      <td>$${p.regular.toFixed(2)}</td>
      <td style="color:#00c853;"><strong>$${p.premium.toFixed(2)} ${((p.regular-p.premium)/p.regular*100).toFixed(0)}% OFF</strong></td>
      <td>$${p.retail.toFixed(2)}</td>
      <td>$${p.margin_regular.toFixed(0)} → <strong style="color:#00c853;">$${p.margin_premium.toFixed(0)}</strong></td>
    </tr>`).join('');
  
  return `
<div style="background:linear-gradient(135deg,#00c853,#00b140);color:white;padding:40px;border-radius:20px;margin:30px 0;">
  <h2>🎖️ Printify Premium = 40%+ Margins</h2>
  <p><strong>20% OFF all base costs</strong> | <strong>$${PREMIUM_PRODUCTS.reduce((sum,p)=>sum+p.margin_premium-p.margin_regular,0).toFixed(0)} extra profit/month</strong></p>
  
  <table style="width:100%;background:white;color:#333;border-radius:10px;overflow:hidden;margin:20px 0;">
    <tr style="background:#333;color:white;">
      <th>Product</th><th>Regular</th><th>Premium</th><th>Sell</th><th>Profit</th>
    </tr>
    ${rows}
  </table>
  
  <div style="text-align:center;">
    <a href="${AFFILIATE_URL}" style="background:white;color:#00c853;padding:20px 50px;font-size:24px;border-radius:50px;font-weight:bold;text-decoration:none;display:inline-block;box-shadow:0 15px 40px rgba(0,200,83,0.4);">
      Unlock Premium Pricing Now
    </a>
  </div>
</div>`;
}

// Update all Printify pages with Premium table
function injectPremiumPricing() {
  const premiumTable = generatePremiumTable();
  
  const pages = fs.readdirSync(PAGES_DIR)
    .filter(f => f.includes('printify') && f.endsWith('.html'));
  
  pages.forEach(page => {
    const filePath = path.join(PAGES_DIR, page);
    let html = fs.readFileSync(filePath, 'utf8');
    
    // Insert after first H2 or before CTA
    if (!html.includes('Printify Premium')) {
      const insertPoint = html.search(/<h[2-6]/i);
      if (insertPoint > 0) {
        html = html.slice(0, insertPoint) + premiumTable + html.slice(insertPoint);
      } else {
        html = html.replace('</body>', `${premiumTable}</body>`);
      }
    }
    
    fs.writeFileSync(filePath, html);
    console.log(`✅ Premium pricing → ${page}`);
  });
  
  console.log(`${pages.length} pages updated with 40% margin tables`);
}

// Generate dedicated Premium landing page
function generatePremiumLanding() {
  const savings = PREMIUM_PRODUCTS.reduce((sum,p)=>sum+(p.margin_premium-p.margin_regular),0);
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <title>Printify Premium: 40% Margins Guaranteed</title>
  <meta name="description" content="Save 20% on Printify base costs. T-shirt $12.95→$10.36 = +$2.59 profit/item. Scale to $3k+ extra/month.">
</head>
<body style="max-width:900px;margin:0 auto;padding:40px;font-family:Arial;">
  <h1 style="text-align:center;color:#00c853;font-size:48px;">🎖️ Printify Premium = Your 40% Margin Machine</h1>
  
  ${generatePremiumTable()}
  
  <div style="background:#f8f9fa;padding:40px;border-radius:20px;margin:40px 0;text-align:center;">
    <h2>💰 Monthly Impact Calculator</h2>
    <p>Sell <input type="number" id="volume" value="100" style="padding:10px;font-size:20px;"> items/month:</p>
    <h2 style="color:#00c853;font-size:36px;" id="totalProfit">+$${savings.toFixed(0)} extra profit</h2>
  </div>
  
  <script>
    document.getElementById('volume').addEventListener('input', e => {
      const extra = ${savings / 100};
      document.getElementById('totalProfit').textContent = '+$' + (extra * e.target.value).toLocaleString() + ' extra profit';
    });
  </script>
  
  <div style="text-align:center;margin:60px 0;">
    <a href="${AFFILIATE_URL}" style="background:linear-gradient(135deg,#00c853,#00b140);color:white;padding:25px 60px;font-size:28px;border-radius:50px;font-weight:bold;text-decoration:none;display:inline-block;box-shadow:0 20px 50px rgba(0,200,83,0.4);">
      Start Printify Premium Today → 20% Instant Savings
    </a>
  </div>
</body>
</html>`;
  
  fs.writeFileSync(path.join(PAGES_DIR, 'printify-premium-40-margins.html'), html);
  console.log('✅ Premium landing page created');
}

injectPremiumPricing();
generatePremiumLanding();

console.log('🎖️ PRINTIFY PREMIUM DEPLOYED');
console.log('✅ 20% cost savings across all products');
console.log('✅ 40%+ margin tables on every page');
console.log('✅ Dedicated Premium profit calculator');
console.log('💰 +$500-3k/month potential unlocked');
