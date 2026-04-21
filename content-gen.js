require('dotenv').config();
const OpenAI = require('openai');
const fs = require('fs');
const csv = require('csv-parser');
const path = require('path');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';
const PAGES_DIR = 'output/pages';

if (!fs.existsSync(PAGES_DIR)) fs.mkdirSync(PAGES_DIR);

// Load keywords (code_file:19)
async function loadKeywords() {
  return new Promise((resolve, reject) => {
    const keywords = [];
    fs.createReadStream('output/keywords.csv').pipe(csv()).on('data', row => keywords.push(row)).on('end', () => resolve(keywords)).on('error', reject);
  });
}

// Load Printify data
async function loadPrintify() {
  const products = await new Promise(r => { let p=[]; fs.createReadStream('output/products.csv').pipe(csv()).on('data',row=>p.push(row)).on('end',()=>r(p)); });
  const features = await new Promise(r => { let f=[]; fs.createReadStream('output/product_features.csv').pipe(csv()).on('data',row=>{if(row.product_id=='1')f.push(row)}).on('end',()=>r(f)); });
  return { printify: products[0], features };
}

// Generate page via LLM
async function generatePage(keyword) {
  const { printify, features } = await loadPrintify();
  const featureText = features.map(f => `${f.feature}: ${f.value}`).join('; ');
  
  const outlinePrompt = `Create JSON outline for "${keyword.keyword}" page (reference guide style):
- H1: Main title with keyword
- Sections: Specs table, Pros/Cons, Best for X, Pricing, CTA
- Use facts: ${featureText}. Regions: ${printify.regions}
- Affiliate CTA: "Start with Printify" linking https://try.printify.com/r3xsnwqufe8t
Output ONLY JSON: {"h1": "...", "sections": [{"h2":"...", "content":"..."}]} `;

  const outline = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{role: 'user', content: outlinePrompt}]
  });
  
  const outlineJson = JSON.parse(outline.choices[0].message.content);
  
  // Full content prompt
  const contentPrompt = `Write full HTML page from this outline for ${keyword.keyword} (EN, SEO schema):
${JSON.stringify(outlineJson, null, 2)}
Include:
- Hreflang /es/ /fr/
- Product schema with Printify facts
- Affiliate CTA button: <a href="https://try.printify.com/r3xsnwqufe8t">Get Started</a>
- Disclosure at bottom
No fluff, table-heavy, 800-1200 words.`;

  const content = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{role: 'user', content: contentPrompt}]
  });

  const html = `<!DOCTYPE html><html lang="en"><!-- full content here -->${content.choices[0].message.content}</html>`;
  const filename = `${keyword.keyword.replace(/[^a-z0-9]/gi, '-')}.html`;
  fs.writeFileSync(path.join(PAGES_DIR, filename), html);
  console.log(`Generated: ${filename}`);
}

// Main: Generate from all keywords
async function main() {
  const keywords = await loadKeywords();
  for (const kw of keywords.slice(0, 5)) { // First 5 for testing
    await generatePage(kw);
  }
  console.log('Content gen complete. Check output/pages/');
}

main().catch(console.error);
