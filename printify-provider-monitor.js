const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PAGES_DIR = 'output/pages';
const STATUS_URL = 'https://printify.com/network-fulfillment-status/';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// Scrape Printify provider status
async function scrapeProviderStatus() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(STATUS_URL, { waitUntil: 'networkidle2' });
  
  const statusTable = await page.evaluate(() => {
    const rows = Array.from(document.querySelectorAll('table tr'));
    return rows.slice(1).map(row => {
      const cells = row.querySelectorAll('td');
      return {
        provider: cells[0]?.innerText.trim(),
        status: cells[1]?.innerText.trim(),
        production_days: cells[2]?.innerText.trim()
      };
    });
  });
  
  await browser.close();
  
  // Summary for pages
  const delayed = statusTable.filter(p => p.status === 'Slight delay in production');
  const avgDays = Math.round(statusTable.reduce((sum, p) => {
    const days = parseInt(p.production_days.match(/\d+/)?.[0] || '3');
    return sum + days;
  }, 0) / statusTable.length);
  
  const statusSummary = {
    total_providers: statusTable.length,
    delayed_providers: delayed.length,
    avg_production_days: avgDays,
    top_delayed: delayed.slice(0, 3).map(p => p.provider),
    last_updated: new Date().toISOString()
  };
  
  fs.writeFileSync('output/provider-status.json', JSON.stringify(statusSummary, null, 2));
  return statusSummary;
}

// Inject status to all Printify pages
function updatePagesWithStatus(status) {
  const pages = fs.readdirSync(PAGES_DIR)
    .filter(f => f.includes('printify') && f.endsWith('.html'));
  
  const statusBadge = `
<div style="background:#fff3cd;border:1px solid #ffeaa7;padding:15px;margin:20px 0;border-radius:10px;">
  <h3>🖨️ Printify Network Status <small>(Live)</small></h3>
  <p><strong>${status.total_providers} providers</strong> | 
     ${status.delayed_providers > 0 ? `<span style="color:#ff6b6b">⚠️ ${status.delayed_providers} delayed</span>` : '✅ All on track'}
  </p>
  <p><strong>Avg production:</strong> ${status.avg_production_days} days | 
     ${status.top_delayed.map(d => `<code>${d}</code>`).join(', ')}
  </p>
  <p><em>Updated: ${new Date(status.last_updated).toLocaleString()}</em></p>
</div>`;

  pages.forEach(page => {
    const filePath = path.join(PAGES_DIR, page);
    let html = fs.readFileSync(filePath, 'utf8');
    
    // Insert after first H2
    html = html.replace(/(<h[2-3][^>]*>.*?<\/h[2-3]>)/i, `$1${statusBadge}`);
    
    fs.writeFileSync(filePath, html);
    console.log(`✅ Updated ${page} with live status`);
  });
  
  console.log(`${pages.length} pages updated with provider status`);
}

// Main monitor loop
async function monitorProviders() {
  console.log('🔍 Checking Printify provider status...');
  
  try {
    const status = await scrapeProviderStatus();
    console.log('📊 Status:', JSON.stringify(status, null, 2));
    
    updatePagesWithStatus(status);
    
    // Trigger deploy if delays found
    if (status.delayed_providers > 5) {
      console.log('🚨 High delays detected → Auto-deploying updates');
      execSync('node deploy-nextjs.js', { stdio: 'inherit' });
    }
  } catch (error) {
    console.error('❌ Provider check failed:', error.message);
  }
}

// Run now + every 2 hours
monitorProviders();

const cron = require('node-cron');
cron.schedule('0 */2 * * *', monitorProviders);

console.log('🖨️ Printify Provider Monitor LIVE - Updates every 2h');
console.log('Check output/provider-status.json');
