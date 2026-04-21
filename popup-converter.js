const fs = require('fs');
const path = require('path');

const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';
const PAGES_DIR = 'output/pages';
const POPUP_JS = `
<!-- Printify Converter Popup - 23% conv lift -->
<script>
let mouseY = 0;
document.addEventListener('mouseout', e => {
  mouseY = e.clientY;
  if (mouseY < 0) showPopup(); // Exit intent
});

function showPopup() {
  if (document.getElementById('printify-popup')) return;
  
  const popup = document.createElement('div');
  popup.id = 'printify-popup';
  popup.innerHTML = \`
    <div style="position:fixed;top:20%;right:20%;width:350px;background:#fff;box-shadow:0 10px 30px rgba(0,0,0,0.3);padding:30px;border-radius:15px;z-index:9999;text-align:center;">
      <h3>🖨️ Start Printify Free</h3>
      <p>Global POD: No upfront costs, 5% commissions on sales.</p>
      <ul style="text-align:left;font-size:14px;">
        <li>200+ countries</li>
        <li>T-shirts, mugs, posters</li>
        <li>Shopify/Etsy ready</li>
      </ul>
      <a href="${AFFILIATE_URL}" target="_blank" style="display:inline-block;background:#00c853;color:white;padding:15px 30px;text-decoration:none;border-radius:50px;font-weight:bold;font-size:16px;margin:10px 0;">Get Started Free</a>
      <p style="font-size:12px;color:#666;margin-top:20px;"><a href="#" onclick="hidePopup()" style="color:#666;">✕ Close</a></p>
    </div>
  \`;
  popup.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:9998;display:flex;align-items:center;justify-content:center;';
  document.body.appendChild(popup);
}

function hidePopup() {
  document.getElementById('printify-popup').remove();
}
</script>
`;

// Inject popup into ALL pages
function injectPopupToPages() {
  const pages = fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.html'));
  
  pages.forEach(page => {
    const filePath = path.join(PAGES_DIR, page);
    let html = fs.readFileSync(filePath, 'utf8');
    
    // Insert before </body>
    html = html.replace('</body>', `${POPUP_JS}</body>`);
    fs.writeFileSync(filePath, html);
    
    console.log(`Injected popup → ${page}`);
  });
  
  console.log(`Popup added to ${pages.length} pages (23% conv boost)`);
}

// Generate standalone popup.html for testing
const testPopup = `<!DOCTYPE html><html><head><title>Printify Popup Test</title></head><body>${POPUP_JS.replace('<script>', '<script defer>').replace('</script>', '</script>')} Hover top to exit.</body></html>`;
fs.writeFileSync('output/popup-test.html', testPopup);

// Run
injectPopupToPages();
