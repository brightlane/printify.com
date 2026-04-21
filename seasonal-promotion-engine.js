const fs = require('fs');
const path = require('path');

const PAGES_DIR = 'output/pages';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// Seasonal campaigns by month
const SEASONAL_PROMOS = {
  4: { // April - Earth Day
    banner: '🌍 Earth Day Printify Sale: 25% More Trees Planted',
    discount: 'Eco-bundle: T-Shirt + Tote = $39 (save $10)',
    urgency: 'Offer ends April 22nd'
  },
  7: { // July - Summer
    banner: '☀️ Summer Printify Drop: Beach bundle 3 shirts $69',
    discount: 'Tank tops + beach towels - Fast 3-day production',
    urgency: 'Ships by July 4th weekend'
  },
  11: { // November - Black Friday
    banner: '🖤 BLACK FRIDAY: Printify Premium + 33% new products FREE',
    discount: 'All kits 25% off base cost - $500+ savings/store',
    urgency: 'Nov 28-30 ONLY - 10k stores claimed'
  },
  12: { // December - Christmas
    banner: '🎄 Christmas Printify Rush: Guaranteed delivery by Dec 20th',
    discount: 'Holiday hoodies + ornaments bundle $89 (save $25)',
    urgency: 'Order by Dec 10th - Express production unlocked'
  }
};

// Detect current season
function getCurrentPromo() {
  const now = new Date();
  const month = now.getMonth() + 1;
  
  return SEASONAL_PROMOS[month] || {
    banner: '🚀 Printify Flash: Free Premium trial 7 days',
    discount: 'Starter kit T-Shirt + Mug just $29.95',
    urgency: 'Limited: First 500 visitors today'
  };
}

// Generate seasonal hero banner
function generateSeasonalBanner(promo) {
  return `
<div id="seasonal-promo" style="background:linear-gradient(135deg,#ff6b6b,#ee5a52);color:white;padding:40px;margin:20px 0;border-radius:25px;text-align:center;position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:repeating-linear-angle(45deg,transparent,transparent 10px,rgba(255,255,255,.1) 10px,rgba(255,255,255,.1) 20px);"></div>
  
  <h1 style="font-size:36px;margin:0 0 15px 0;text-shadow:2px 2px 4px rgba(0,0,0,0.3);position:relative;z-index:1;">${promo.banner}</h1>
  <p style="font-size:20px;margin:0 0 25px 0;position:relative;z-index:1;">${promo.discount}</p>
  
  <div style="display:inline-block;background:rgba(255,255,255,0.2);padding:20px 40px;border-radius:50px;font-size:22px;font-weight:bold;position:relative;z-index:1;">
    <a href="${AFFILIATE_URL}" style="color:white;text-decoration:none;display:block;" onclick="gtag('event','seasonal_click');">
      Claim ${promo.urgency} → Start Now
    </a>
  </div>
  
  <div style="position:absolute;bottom:20px;right:20px;font-size:12px;color:rgba(255,255,255,0.8);">
    Limited time - ${new Date().toLocaleDateString()}
  </div>
</div>`;
}

// Inject seasonal promo to ALL Printify pages
function deploySeasonalCampaign() {
  const promo = getCurrentPromo();
  const banner = generateSeasonalBanner(promo);
  
  const pages = fs.readdirSync(PAGES_DIR)
    .filter(f => f.includes('printify') && f.endsWith('.html'));
  
  pages.forEach(page => {
    const filePath = path.join(PAGES_DIR, page);
    let html = fs.readFileSync(filePath, 'utf8');
    
    // Insert after <h1> or top of body
    if (!html.includes('seasonal-promo')) {
      const insertPoint = html.search(/<h1/i);
      if (insertPoint > -1) {
        html = html.slice(0, insertPoint) + banner + html.slice(insertPoint);
      } else {
        html = html.replace('<body', `<body${banner.match(/style="[^"]*"/)?.[0] || ''}`);
      }
      
      fs.writeFileSync(filePath, html);
      console.log(`✅ ${promo.banner.slice(0,30)}... → ${page}`);
    }
  });
  
  // Track campaign performance
  fs.appendFileSync('output/seasonal-log.txt', 
    `${new Date().toISOString()},${promo.banner},${pages.length} pages\n`);
  
  console.log(`\n🎄 SEASONAL CAMPAIGN LIVE: ${promo.banner}`);
  console.log(`📱 ${pages.length} pages | Ends: ${promo.urgency}`);
}

// Auto-rotate campaigns monthly
const cron = require('node-cron');
cron.schedule('0 0 1 * *', deploySeasonalCampaign); // 1st of month

deploySeasonalCampaign();
console.log('🎯 Seasonal engine deployed - 3x urgency boost active');
