require('dotenv').config();
const OpenAI = require('openai');
const fs = require('fs');
const path = require('path');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const PAGES_DIR = 'output/pages';
const GLOBAL_ENGINES = {
  baidu: { sitemap: 'baidu-sitemap.xml', langs: ['zh'] },
  yandex: { sitemap: 'yandex-sitemap.xml', langs: ['ru'] },
  google: { sitemap: 'sitemap.xml', langs: ['en','es','fr','de','it','pt'] },
  bing: { sitemap: 'bing-sitemap.xml', langs: ['en','es','fr'] }
};

const REGION_CTAS = {
  'cn': '立即开始 Printify（百度优化）',
  'ru': 'Начать с Printify (Yandex)',
  'br': 'Comece com Printify (Mercado Livre)',
  'global': 'Start Printify Free'
};

// Translate page to lang/region
async function translatePage(pageFile, targetLang, region = 'global') {
  const enHtml = fs.readFileSync(path.join(PAGES_DIR, pageFile), 'utf8');
  
  const prompt = `Translate this HTML to ${targetLang} (${region}). Keep:
- Affiliate: https://try.printify.com/r3xsnwqufe8t
- Structure/tables/schema
- SEO: Update title/meta/alt
- CTA: "${REGION_CTAS[region] || REGION_CTAS.global}"

${enHtml.substring(0, 8000)}...

Output ONLY full <html>`;

  const translated = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: prompt }]
  });
  
  const newFile = pageFile.replace('.html', `-${targetLang}-${region}.html`);
  fs.writeFileSync(path.join(PAGES_DIR, newFile), translated.choices[0].message.content);
  return newFile;
}

// Generate engine sitemaps
function generateGlobalSitemaps() {
  Object.entries(GLOBAL_ENGINES).forEach(([engine, config]) => {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
`;
    
    config.langs.forEach(lang => {
      fs.readdirSync(PAGES_DIR)
        .filter(f => f.includes(`-${lang}-`) && f.endsWith('.html'))
        .forEach(file => {
          sitemap += `  <url><loc>https://yourdomain.com/${file}</loc><lastmod>${new Date().toISOString().split('T')[0]}</lastmod></url>\n`;
        });
    });
    
    sitemap += '</urlset>';
    fs.writeFileSync(`output/${config.sitemap}`, sitemap);
  });
  
  // robots.txt for engines
  const robots = `User-agent: BaiduSpider\nAllow: /\nSitemap: https://yourdomain.com/output/baidu-sitemap.xml\n\nUser-agent: Yandex\nAllow: /\nSitemap: https://yourdomain.com/output/yandex-sitemap.xml`;
  fs.writeFileSync('output/robots-global.txt', robots);
}

// Main: Translate top pages
async function main() {
  const topPages = ['printify-review.html', 'best-pod-2026.html']; // From dashboard
  
  // Global langs
  const globalLangs = ['es','fr','de','it','pt','ru','zh'];
  for (const page of topPages) {
    for (const lang of globalLangs) {
      console.log(`Translating ${page} → ${lang}`);
      await translatePage(page, lang);
    }
  }
  
  // Region-specific (BR/CN/RU)
  await translatePage(topPages[0], 'pt', 'br');
  await translatePage(topPages[0], 'zh', 'cn');
  await translatePage(topPages[0], 'ru', 'ru');
  
  generateGlobalSitemaps();
  console.log('International SEO complete: Baidu/Yandex ready.');
}

// Run
main().catch(console.error);
