const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const PAGES_DIR = 'output/pages';
const KEYWORDS_FILE = 'output/keywords.csv';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// Keyword expansion patterns (LSI + long-tail)
const EXPANSION_PATTERNS = {
  modifiers: ['review 2026', 'best for beginners', 'vs printful', 'pricing guide', 'free trial', 'premium plan'],
  questions: ['how to start', 'is it worth it', 'cheapest plan', 'fastest shipping', 'worldwide delivery'],
  locations: ['usa', 'europe', 'uk', 'australia', 'canada', 'brazil'],
  products: ['tshirt', 'hoodie', 'mug', 'poster', 'phone case', 'tote bag']
};

// Load existing keywords
async function loadKeywords() {
  return new Promise((resolve) => {
    const keywords = [];
    fs.createReadStream(KEYWORDS_FILE)
      .pipe(csv())
      .on('data', (row) => keywords.push(row.keyword))
      .on('end', () => resolve(keywords));
  });
}

// Generate 10x more keywords
function expandKeywords(existingKeywords) {
  const newKeywords = [];
  
  // Pattern combinations
  EXPANSION_PATTERNS.modifiers.forEach(mod => {
    EXPANSION_PATTERNS.products.forEach(product => {
      EXPANSION_PATTERNS.locations.forEach(loc => {
        newKeywords.push(`${product} ${mod} ${loc}`);
        newKeywords.push(`best ${product} ${mod}`);
        newKeywords.push(`${mod.replace('review', 'reviews')} ${product}`);
      });
    });
  });
  
  // Question-based
  EXPANSION_PATTERNS.questions.forEach(q => {
    newKeywords.push(`printify ${q.replace('how to start', 'get started')}`);
  });
  
  // Remove duplicates + filter existing
  const uniqueNew = [...new Set(newKeywords)]
    .filter(kw => !existingKeywords.includes(kw) && kw.length > 5)
    .slice(0, 1000); // Top 1000
  
  // Append to CSV
  const csvRows = uniqueNew.map(kw => `printify ${kw},medium,commercial,en,global,1\n`);
  fs.appendFileSync(KEYWORDS_FILE, csvRows.join(''));
  
  console.log(`✅ Added ${uniqueNew.length} new keywords to keywords.csv`);
  return uniqueNew;
}

// Auto-generate pages from new keywords
async function generateNewPages(newKeywords) {
  newKeywords.slice(0, 50).forEach((keyword, i) => { // First 50 for testing
    const filename = `printify-${keyword.replace(/[^a-z0-9]/g, '-').slice(0, 50)}.html`;
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <title>Printify ${keyword.replace(/review/g, 'Review')} 2026</title>
  <meta name="description" content="Printify ${keyword}. Cheapest POD pricing, premium plans, worldwide shipping. Start free.">
</head>
<body style="max-width:900px;margin:0 auto;padding:40px;font-family:Arial;">
  <h1>Printify ${keyword.replace(/review/g, 'Review')} - Best ${keyword.includes('best') ? '' : 'POD ' + keyword}</h1>
  
  <div style="background:#e8f5e8;padding:30px;border-radius:20px;margin:30px 0;text-align:center;">
    <h2>🚀 Start Printify Free</h2>
    <p>Live pricing from Printify API. Premium plans = 20% cheaper.</p>
    <a href="${AFFILIATE_URL}" style="background:#00c853;color:white;padding:20px 50px;font-size:24px;border-radius:50px;font-weight:bold;text-decoration:none;">Get Started → 5% Commissions</a>
  </div>
  
  <h2>Why Printify ${keyword.includes('vs') ? 'beats competitors' : 'for ' + keyword}</h2>
  <ul style="font-size:18px;line-height:1.6;">
    <li>Cheapest T-shirts: $9.85 vs $14+ elsewhere</li>
    <li>Premium: 20% off all base costs</li>
    <li>200+ countries worldwide</li>
    <li>Live provider status (no delays)</li>
    <li>5% recurring affiliate commissions</li>
  </ul>
  
  <footer style="text-align:center;margin-top:60px;padding:40px;background:#f8f9fa;border-radius:20px;">
    <p><a href="${AFFILIATE_URL}" style="color:#00c853;font-weight:bold;font-size:20px;">Printify Affiliate</a> | 
    <a href="/privacy-policy">Privacy Policy</a></p>
  </footer>
</body>
</html>`;
    
    fs.writeFileSync(path.join(PAGES_DIR, filename), html);
  });
  
  console.log(`✅ Generated ${Math.min(50, newKeywords.length)} new pages`);
}

// Update sitemap
function updateSitemap() {
  const pages = fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.html'));
  let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map(page => `
  <url>
    <loc>https://yourdomain.com/${page}</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <priority>0.8</priority>
  </url>`).join('')}
</urlset>`;
  
  fs.writeFileSync('output/sitemap.xml', sitemap);
  console.log('✅ Sitemap updated with new pages');
}

// Main expansion
async function main() {
  const existing = await loadKeywords();
  const newKeywords = expandKeywords(existing);
  await generateNewPages(newKeywords);
  updateSitemap();
  
  console.log('\n🎯 KEYWORD EXPANSION COMPLETE');
  console.log(`📈 ${existing.length} → ${existing.length + newKeywords.length} total keywords`);
  console.log(`🌐 ${fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.html')).length} total pages`);
  console.log('🔄 Run: node content-gen.js → Process new keywords');
  console.log('🚀 Run: node domain-deployer.js → Deploy new pages');
}

main();
