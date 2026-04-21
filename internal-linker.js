const fs = require('fs');
const path = require('path');
const natural = require('natural'); // npm i natural

const PAGES_DIR = 'output/pages';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// LSI keywords clusters (semantic linking)
const KEYWORD_CLUSTERS = {
  printify: ['print on demand', 'POD platform', 'custom merch', 'dropship printing', 'printify review'],
  products: ['t-shirts', 'mugs', 'hoodies', 'posters', 'phone cases'],
  comparison: ['printify vs printful', 'best POD 2026', 'printify alternatives'],
  global: ['printify worldwide', 'printify shipping', 'POD europe', 'POD brasil']
};

const SILO_STRUCTURE = {
  '/printify/': ['printify-review.html', 'printify-pricing.html'],
  '/products/': ['tshirts-printify.html', 'mugs-printify.html'],
  '/compare/': ['printify-vs-printful.html'],
  '/global/': ['printify-worldwide.html']
};

// Extract keywords from page
function extractKeywords(htmlContent) {
  const tokenizer = new natural.WordTokenizer();
  const words = tokenizer.tokenize(htmlContent.toLowerCase());
  const tfidf = new natural.TfIdf();
  tfidf.addDocument(words);
  
  const topKeywords = [];
  tfidf.tfidfs('printify', (i, measure) => {
    if (measure > 0.1) topKeywords.push({ word: 'printify', score: measure });
  });
  
  // Match to clusters
  const clusterMatches = Object.entries(KEYWORD_CLUSTERS).reduce((acc, [cluster, terms]) => {
    const score = terms.filter(term => htmlContent.toLowerCase().includes(term)).length;
    if (score > 0) acc[cluster] = score;
    return acc;
  }, {});
  
  return { topKeywords, clusterMatches };
}

// Find best link targets
function findLinkTargets(pageName, clusters) {
  const targets = [];
  
  Object.entries(clusters).forEach(([cluster, score]) => {
    if (score > 0) {
      // Find pages in same cluster
      Object.entries(SILO_STRUCTURE).forEach(([silo, pages]) => {
        if (pages.some(p => p.includes(cluster))) {
          targets.push({ url: silo + pages[0], anchor: cluster.replace(/s$/, '') });
        }
      });
    }
  });
  
  return targets.slice(0, 3); // Max 3 links/page
}

// Inject contextual links
function injectLinks(pageFile) {
  const filePath = path.join(PAGES_DIR, pageFile);
  let html = fs.readFileSync(filePath, 'utf8');
  const bodyContent = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i)?.[1] || '';
  
  const { clusterMatches } = extractKeywords(bodyContent);
  const linkTargets = findLinkTargets(pageFile, clusterMatches);
  
  linkTargets.forEach(({ url, anchor }) => {
    const linkHtml = `<a href="${url}" style="color:#007cba;text-decoration:none;font-weight:500;">${anchor.charAt(0).toUpperCase() + anchor.slice(1)}</a>`;
    
    // Inject after first H2/H3
    const insertPoint = html.match(/<(h[2-3][^>]*)>/i);
    if (insertPoint) {
      html = html.replace(insertPoint[0], `${insertPoint[0]} ${linkHtml}&nbsp;`);
    }
  });
  
  // Add nav silo links to header
  const siloNav = Object.entries(SILO_STRUCTURE).map(([silo, pages]) => 
    `<a href="${silo}">${silo.replace('/', '').toUpperCase()}</a> | `
  ).join('').slice(0, -3);
  
  html = html.replace('</head>', `<nav style="background:#f0f0f0;padding:10px;">Internal: ${siloNav}</nav></head>`);
  
  fs.writeFileSync(filePath, html);
  return linkTargets.length;
}

// Main crawler
function buildInternalLinks() {
  const pages = fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.html'));
  let totalLinks = 0;
  
  pages.forEach(page => {
    const linksAdded = injectLinks(page);
    totalLinks += linksAdded;
    console.log(`Linked ${page}: +${linksAdded} internal`);
  });
  
  // Update sitemap with silo priority
  const siloSitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset>
${Object.entries(SILO_STRUCTURE).map(([silo]) => 
  `<url><loc>https://yourdomain.com${silo}</loc><priority>0.8></priority></url>`
).join('')}
</urlset>`;
  
  fs.writeFileSync('output/silo-sitemap.xml', siloSitemap);
  
  console.log(`Internal linking complete: ${totalLinks} links added. Topical authority ↑`);
}

// Run
buildInternalLinks();
