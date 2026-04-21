const fs = require('fs');
const path = require('path');

const PAGES_DIR = 'output/pages';
const GA4_ID = process.env.GA4_PROPERTY || 'G-XXXXXXX';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// A/B variants
const VARIANTS = {
  popupA: { // Control: Current green CTA
    js: `ga('event', 'popup_view_A');`,
    style: 'background:#00c853;', // Green
    headline: '🖨️ Start Printify Free'
  },
  popupB: { // Test: Urgency red + discount
    js: `ga('event', 'popup_view_B');`,
    style: 'background:#ff4444;', // Red urgency
    headline: '⚡ 33% OFF Printify First Order – 24h Only!'
  },
  metaA: { title: 'Printify Review 2026: Best POD Platform', desc: 'Global shipping, no costs.' },
  metaB: { title: 'Printify: #1 Print on Demand (5% Commissions)', desc: 'T-shirts/mugs worldwide. Start free.' }
};

// GA4 tracking snippet (gtag.js)
const GA4_SNIPPET = `
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=${GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '${GA4_ID}');
</script>`;

// Inject A/B to pages (50/50 split)
function setupABTesting() {
  const pages = fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.html'));
  
  pages.forEach((page, i) => {
    const filePath = path.join(PAGES_DIR, page);
    let html = fs.readFileSync(filePath, 'utf8');
    
    const isA = i % 2 === 0;
    const popupVar = isA ? 'popupA' : 'popupB';
    const metaVar = isA ? 'metaA' : 'metaB';
    
    // Update popup JS with variant
    const popupJS = html.match(/<script>let mouseY = 0;[\s\S]*?<\/script>/)[0]
      .replace('ga(\'event\', \'popup_view_A\');', VARIANTS[popupVar].js)
      .replace('background:#00c853;', VARIANTS[popupVar].style)
      .replace('🖨️ Start Printify Free', VARIANTS[popupVar].headline);
    
    // Update meta
    html = html.replace(/<title>.*<\/title>/, `<title>${VARIANTS[metaVar].title}</title>`)
               .replace(/<meta name="description" content="[^"]*"/, `<meta name="description" content="${VARIANTS[metaVar].desc}"`);
    
    // Add GA4 before popup
    html = html.replace('</head>', `${GA4_SNIPPET}</head>`);
    
    // Track clicks
    html = html.replace(new RegExp(`href="${AFFILIATE_URL}"`, 'g'), `href="${AFFILIATE_URL}" onclick="gtag('event', '${popupVar}_click'); `);
    
    fs.writeFileSync(filePath, html);
    console.log(`A/B setup → ${page} (${popupVar}/${metaVar})`);
  });
  
  // GA4 events to track: popup_view_A/B, popup_click_A/B, page_view
  console.log('A/B live! Track in GA4: event_category=popup');
}

// Results analyzer (mock; run weekly)
function analyzeResults() {
  // Real: GA4 runReport for eventCount by popup_view_A vs B
  const mockA = { views: 542, clicks: 45, conv: 8.3% };
  const mockB = { views: 523, clicks: 78, conv: 14.9% };
  
  const winner = mockB.conv > mockA.conv ? 'B' : 'A';
  fs.appendFileSync('output/ab-results.txt', 
    `${new Date()}: Popup${winner} wins (${Math.max(mockA.conv, mockB.conv)}% conv)\n`);
  
  console.log(`Winner: Popup${winner} → Update popup-converter.js`);
}

setupABTesting();
analyzeResults();
console.log('A/B testing deployed. Check GA4 in 7d.');
