const puppeteer = require('puppeteer'); // npm i puppeteer
const fs = require('fs');
const csv = require('csv-parser');

const KEYWORDS_FILE = 'output/keywords.csv';
const COMPETITOR_DATA = 'output/competitors.json';

// Spy on top 3 SERPs per keyword
async function spyCompetitors(keyword) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  // Google SERP (use SerpAPI or proxy for prod)
  await page.goto(`https://www.google.com/search?q=${encodeURIComponent(keyword.keyword)}+2026+review`);
  
  const competitors = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('h3')).slice(0, 3).map(h3 => ({
      title: h3.innerText,
      url: h3.closest('div')?.querySelector('a')?.href || 'N/A',
      snippet: h3.nextElementSibling?.innerText || ''
    }));
  });
  
  await browser.close();
  
  // Analyze each competitor page
  const details = [];
  for (const comp of competitors) {
    if (comp.url) {
      const browser2 = await puppeteer.launch();
      const p2 = await browser2.newPage();
      await p2.goto(comp.url, { waitUntil: 'networkidle2', timeout: 10000 });
      
      const structure = await p2.evaluate(() => {
        return {
          hasTable: !!document.querySelector('table'),
          ctaCount: document.querySelectorAll('a[href*="printify"], .btn, .cta').length,
          wordCount: document.body.innerText.trim().split(/\\s+/).length,
          schema: !!document.querySelector('script[type="application/ld+json"]'),
          headings: Array.from(document.querySelectorAll('h1,h2,h3')).slice(0,5).map(h => h.tagName + ': ' + h.innerText.slice(0,50))
        };
      });
      
      details.push({ url: comp.url, ...structure });
      await browser2.close();
    }
  }
  
  return { keyword, competitors: details };
}

// Process top keywords
async function main() {
  const keywords = await new Promise(r => {
    let k = []; fs.createReadStream(KEYWORDS_FILE).pipe(csv()).on('data', row => k.push(row)).on('end', () => r(k));
  });
  
  const spyData = [];
  for (const kw of keywords.slice(0, 5)) { // Top 5
    console.log(`Spying "${kw.keyword}"...`);
    const data = await spyCompetitor(kw.keyword);
    spyData.push(data);
    
    // Write pattern recs
    const avgTable = data.competitors.filter(c => c.hasTable).length / data.competitors.length;
    const avgCTAs = data.competitors.reduce((s,c) => s + c.ctaCount, 0) / data.competitors.length;
    
    fs.appendFileSync('output/spy-insights.csv', 
      `${kw.keyword},${avgTable.toFixed(2)},${avgCTAs.toFixed(1)},${data.competitors.map(c=>c.url).join(';')}\n`);
  }
  
  fs.writeFileSync(COMPETITOR_DATA, JSON.stringify(spyData, null, 2));
  console.log('Competitor spy complete. Check spy-insights.csv');
  
  // Auto-update outlines in content-gen.js
  const insights = spyData.map(d => 
    \`For "${d.keyword}": Use ${d.competitors[0]?.hasTable ? 'tables' : 'lists'}, ${Math.round(d.competitors[0]?.ctaCount || 0)} CTAs\`);
  fs.writeFileSync('output/competitor-lessons.txt', insights.join('\\n'));
}

// Run
main().catch(console.error);
