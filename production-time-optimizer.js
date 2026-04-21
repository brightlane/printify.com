const fs = require('fs');
const path = require('path');

const PAGES_DIR = 'output/pages';
const PROVIDER_STATUS = 'output/provider-status.json';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// Dynamic pricing/messaging based on production times
const URGENCY_MESSAGES = {
  fast: { days: 2, message: '🚀 Ships in 2 days - Order NOW', color: '#00c853' },
  normal: { days: 4, message: '✅ Ready in 4 days - Fast production', color: '#ffc107' },
  delayed: { days: 7, message: '⚠️ 7-day production - Plan ahead', color: '#ff6b6b' }
};

// Load current provider status
function getProductionStatus() {
  if (!fs.existsSync(PROVIDER_STATUS)) {
    return { avg_production_days: 3, delayed_providers: 0, status: 'normal' };
  }
  
  const status = JSON.parse(fs.readFileSync(PROVIDER_STATUS, 'utf8'));
  const avgDays = status.avg_production_days || 3;
  
  if (avgDays <= 2) return { avg_production_days: avgDays, status: 'fast' };
  if (avgDays >= 6) return { avg_production_days: avgDays, status: 'delayed' };
  return { avg_production_days: avgDays, status: 'normal' };
}

// Generate optimized pricing table
function generatePricingTable(status) {
  const urgency = URGENCY_MESSAGES[status.status];
  
  return `
<div style="background:#f8f9fa;padding:30px;border-radius:15px;margin:20px 0;">
  <h2>🕐 Current Production Times</h2>
  <table style="width:100%;border-collapse:collapse;">
    <tr style="background:#${urgency.color};color:white;">
      <th>Product</th><th>Base Cost</th><th>Your Price</th><th>Production</th>
    </tr>
    <tr><td>T-Shirt</td><td>$12.95</td><td><strong>$29.95</strong></td><td>${urgency.days} days</td></tr>
    <tr><td>Mug</td><td>$7.95</td><td><strong>$19.95</strong></td><td>${urgency.days} days</td></tr>
    <tr><td>Hoodie</td><td>$29.95</td><td><strong>$59.95</strong></td><td>${urgency.days+1} days</td></tr>
  </table>
  <p style="font-size:18px;margin-top:20px;">
    <strong>${urgency.message}</strong>
  </p>
  <a href="${AFFILIATE_URL}" style="background:#${urgency.color};color:white;padding:15px 40px;display:inline-block;border-radius:50px;font-size:18px;font-weight:bold;">
    Start Printify (${urgency.days} day delivery)
  </a>
</div>`;
}

// Update ALL Printify pages with live pricing
function optimizeAllPages() {
  const status = getProductionStatus();
  const pricingTable = generatePricingTable(status);
  
  const pages = fs.readdirSync(PAGES_DIR)
    .filter(f => f.includes('printify') && f.endsWith('.html'));
  
  pages.forEach(page => {
    const filePath = path.join(PAGES_DIR, page);
    let html = fs.readFileSync(filePath, 'utf8');
    
    // Replace any existing pricing table
    html = html.replace(/<div[^>]*production[^>]*>[\s\S]*?<\/div>/i, pricingTable);
    
    // Insert if no table exists
    if (!html.includes('Production Times')) {
      html = html.replace('</body>', `${pricingTable}</body>`);
    }
    
    fs.writeFileSync(filePath, html);
    console.log(`✅ Optimized ${page} → ${status.status} (${status.avg_production_days} days)`);
  });
  
  // Log pricing changes
  fs.appendFileSync('output/pricing-log.txt', 
    `${new Date().toISOString()}: ${status.status} (${status.avg_production_days}d) → ${pages.length} pages\n`);
}

// Auto-adjust urgency cron
const cron = require('node-cron');
cron.schedule('0 */1 * * *', optimizeAllPages); // Every hour

// Run now
optimizeAllPages();
console.log('🕐 Production Time Optimizer LIVE');
console.log('Pricing tables auto-adjust to Printify delays');
console.log('Fast = Green CTAs | Delayed = Red urgency');
