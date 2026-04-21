const fs = require('fs');
const csv = require('csv-parser');
const cron = require('node-cron'); // npm i node-cron csv-parser

const PAGES_DIR = 'output/pages';
const OBS_FILE = 'output/observations.csv';

// Load live pages
function getLivePages() {
  return fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.html')).map(f => `${PAGES_DIR}/${f}`);
}

// Load keywords for ranking checks (code_file:19)
async function loadKeywords() {
  return new Promise(r => { let k=[]; fs.createReadStream('output/keywords.csv').pipe(csv()).on('data',row=>k.push(row)).on('end',()=>r(k)); });
}

// 5 Agents: Each scans & logs
const AGENTS = [
  { name: 'KeywordAgent', check: async (page, keywords) => {
    // Mock: Flag if keyword volume dropped
    if (Math.random() > 0.8) return { type: 'ranking_drop', severity: 'medium', action: 'rewrite' };
  }},
  { name: 'OutlineAgent', check: async (page) => {
    const content = fs.readFileSync(page, 'utf8');
    if (!content.includes('<table')) return { type: 'quality_warning', severity: 'low', action: 'edit' }; // Needs more tables
  }},
  { name: 'WriterAgent', check: async (page) => {
    const content = fs.readFileSync(page, 'utf8');
    if (!content.includes(AFFILIATE_URL)) return { type: 'low_CTR', severity: 'high', action: 'rewrite' }; // Missing CTA!
  }},
  { name: 'EditorAgent', check: async (page) => {
    // Mock price/freshness check
    if (Math.random() > 0.7) return { type: 'outdated_price', severity: 'high', action: 'rewrite' };
  }},
  { name: 'SEOAgent', check: async (page) => {
    const content = fs.readFileSync(page, 'utf8');
    if (!content.includes('hreflang')) return { type: 'quality_warning', severity: 'medium', action: 'edit' };
  }}
];

// Append to observations (code_file:20)
function logObservation(obs) {
  const row = `${obs.type},${path.basename(obs.page_url)},${obs.agent},${obs.severity},${obs.action}\n`;
  fs.appendFileSync(OBS_FILE, row);
  console.log(`Flagged: ${obs.type} on ${obs.page_url}`);
}

// Monitoring pass
async function monitoringPass() {
  console.log('Monitoring pass started...');
  const pages = getLivePages();
  const keywords = await loadKeywords();
  
  for (const page of pages.slice(0, 10)) { // Scan 10 pages
    for (const agent of AGENTS) {
      const issue = await agent.check(page, keywords);
      if (issue) {
        logObservation({ ...issue, page_url: page, agent: agent.name });
      }
    }
  }
  
  // Auto-remediate: High severity → regenerate
  const obs = await new Promise(r => {
    let o = []; fs.createReadStream(OBS_FILE).pipe(csv()).on('data', row => o.push(row)).on('end', () => r(o));
  });
  const highPriority = obs.filter(row => row.severity === 'high' && row.action === 'rewrite');
  console.log(`${highPriority.length} pages queued for rewrite. Run content-gen.js next.`);
}

// Schedule every 6 hours (or run manually)
cron.schedule('0 */6 * * *', monitoringPass);

// Run once now
monitoringPass().catch(console.error);
