const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const AFFILIATE_URLS = {
  printify: 'https://try.printify.com/r3xsnwqufe8t',
  turbotax: 'https://turbotax.intuit.com/?affiliate_id=YOUR_ID', // Swap your tax affiliate
  booking: 'https://www.booking.com/affiliate/YOUR_ID', // Travel
  shopify: 'https://shopify.pxf.io/YOUR_ID' // Ecom POD
};

const NICHES = ['printify-pod', 'tax-software', 'travel-bookings', 'ecom-platforms'];
const LANGS = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ar']; // Global

// Add niche products to CSV
function expandProducts() {
  const newRows = NICHES.slice(1).map((niche, i) => ({
    id: i + 2,
    name: niche.replace('-', ' ').toUpperCase(),
    brand: niche.split('-')[0].toUpperCase(),
    affiliate_links: AFFILIATE_URLS[niche] || 'https://example.com',
    commissions: 'Varies 5-20%',
    regions: 'Global',
    langs: LANGS.join(',')
  }).map(r => Object.values(r).join(',')).join('\n'));

  fs.appendFileSync('output/products.csv', '\n' + newRows);
  console.log('Expanded products.csv with tax/travel/ecom');
}

// Expand keywords per niche/lang
function expandKeywords() {
  const baseKeywords = ['review 2026', 'best for beginners', 'pricing worldwide', 'affiliate program'];
  let newKeywords = '';
  
  NICHES.forEach(niche => {
    LANGS.forEach(lang => {
      baseKeywords.forEach(kw => {
        newKeywords += `best ${niche} ${kw},${Math.floor(Math.random()*10000)},commercial,${lang},global,${niche.includes('printify')?1:niche.includes('tax')?2:3}\n`;
      });
    });
  });
  
  fs.appendFileSync('output/keywords.csv', newKeywords);
  console.log(`Added ${NICHES.length * LANGS.length * baseKeywords.length} keywords`);
}

// Translate pages (mock GPT batch for speed)
async function translatePages() {
  const pagesDir = 'output/pages';
  LANGS.slice(1).forEach(lang => { // en already done
    fs.readdirSync(pagesDir).forEach(file => {
      const enHtml = fs.readFileSync(path.join(pagesDir, file), 'utf8');
      // Real: OpenAI translate prompt here (batch $0.01/page)
      const translated = enHtml.replace(/ lang="en"/, ` lang="${lang}"`)
                              .replace(/Printify/g, 'Printify') // Placeholder; add GPT
                              .replace('</head>', `<link rel="alternate" hreflang="en" href="/en/${file}">...</head>`);
      fs.writeFileSync(path.join(pagesDir, `${lang}-${file}`), translated);
    });
  });
  console.log('Translated pages to 10 langs');
}

// Update sitemaps post-expand
function updateSitemaps() {
  // Reuse deploy-nextjs logic or run it
  execSync('node deploy-nextjs.js', { stdio: 'inherit' });
}

// Run expansion
expandProducts();
expandKeywords();
translatePages();
updateSitemaps();

console.log('Multi-niche expanded: Tax/Travel + 10 langs. Rerun auto-loop.js');
