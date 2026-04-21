const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PAGES_DIR = 'output/pages';
const PUBLIC_DIR = 'printify-hub/public'; // Your Next.js public/
const LANGS = ['en', 'es', 'fr']; // Add more

// Copy pages to lang folders
function deployPages() {
  LANGS.forEach(lang => {
    const langDir = path.join(PUBLIC_DIR, lang);
    if (!fs.existsSync(langDir)) fs.mkdirSync(langDir, { recursive: true });
    
    fs.readdirSync(PAGES_DIR).forEach(file => {
      const src = path.join(PAGES_DIR, file);
      const dest = path.join(langDir, file);
      
      // Add hreflang to HTML
      let html = fs.readFileSync(src, 'utf8');
      html = html.replace('</head>', 
        LANGS.map(l => l === lang ? '' : `<link rel="alternate" hreflang="${l}" href="/${l}/${path.basename(file)}">`).join('') + '</head>'
      );
      html = html.replace('<html lang="en">', `<html lang="${lang}">`);
      fs.writeFileSync(dest, html);
    });
  });
  console.log('Pages deployed to multi-lang public/');
}

// Generate sitemaps (en.xml, es.xml)
function generateSitemaps() {
  LANGS.forEach(lang => {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
`;
    fs.readdirSync(path.join(PUBLIC_DIR, lang)).forEach(file => {
      if (file.endsWith('.html')) {
        sitemap += `  <url>
    <loc>https://yourdomain.com/${lang}/${file}</loc>
    ${LANGS.map(l => l !== lang ? `    <xhtml:link rel="alternate" hreflang="${l}" href="https://yourdomain.com/${l}/${file}"/>` : '').join('')}
  </url>\n`;
      }
    });
    sitemap += '</urlset>';
    fs.writeFileSync(path.join(PUBLIC_DIR, `sitemap-${lang}.xml`), sitemap);
  });
  console.log('Sitemaps generated: sitemap-en.xml etc.');
}

// Build & export Next.js static
function buildNext() {
  execSync('cd printify-hub && npm run build', { stdio: 'inherit' });
  console.log('Next.js static export complete.');
}

// Main
deployPages();
generateSitemaps();
buildNext();
console.log('Full deploy ready. Push to GitHub for Actions.');
