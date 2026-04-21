const fs = require('fs');
const PDFDocument = require('pdfkit'); // npm i pdfkit
const path = require('path');

const PAGES_DIR = 'output/pages';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';
const EMAIL_FORM_HTML = `
<!-- Printify Lead Magnet -->
<div id="email-capture" style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:40px;margin:30px 0;border-radius:20px;text-align:center;">
  <h2>📋 Free: Printify Success Checklist 2026</h2>
  <p>Get <strong>7-figure POD store blueprint</strong> + exclusive tips</p>
  
  <form action="https://yourdomain.com/api/subscribe" method="POST" style="max-width:400px;margin:0 auto;">
    <input type="email" name="email" placeholder="your@email.com" required 
           style="width:100%;padding:15px;margin:10px 0;border:none;border-radius:30px;font-size:16px;">
    <input type="hidden" name="lead" value="printify-checklist">
    <button type="submit" style="background:#00c853;color:white;padding:15px 40px;border:none;border-radius:30px;font-size:18px;font-weight:bold;cursor:pointer;width:100%;">
      Download Free PDF
    </button>
  </form>
  
  <p style="font-size:14px;margin-top:20px;">✅ Instant download | ✅ Zero spam | <a href="${AFFILIATE_URL}" style="color:#ffd700;">Or start Printify</a></p>
</div>

<script>
document.querySelector('#email-capture form').addEventListener('submit', e => {
  gtag('event', 'lead_signup', { method: 'printify_checklist' });
});
</script>`;

// Generate lead magnet PDF
function generateChecklistPDF() {
  const doc = new PDFDocument({ margin: 50 });
  const pdfPath = 'output/printify-checklist.pdf';
  doc.pipe(fs.createWriteStream(pdfPath));
  
  doc.fontSize(24).text('Printify Success Checklist 2026', { align: 'center' });
  doc.moveDown();
  
  const checklist = [
    '✅ Connect Shopify/Etsy (5min)',
    '✅ Top products: T-shirts > Mugs > Hoodies',
    '✅ Price 30% above base + free ship',
    '✅ Global: 200+ countries',
    '✅ Affiliate: 5% recurring via [this link]',
    '✅ Mockups: Printify free generator',
    '✅ Scale: Automate with this hub 👇'
  ];
  
  checklist.forEach(item => {
    doc.fontSize(16).text(item, { lineGap: 8 });
  });
  
  doc.end();
  console.log('PDF generated:', pdfPath);
  return pdfPath;
}

// Inject form to pages
function injectEmailCapture() {
  const pages = fs.readdirSync(PAGES_DIR)
    .filter(f => f.includes('printify') && f.endsWith('.html'));
  
  pages.forEach(page => {
    const filePath = path.join(PAGES_DIR, page);
    let html = fs.readFileSync(filePath, 'utf8');
    
    // Insert after first H2
    const insertPoint = html.match(/(<h[2-3][^>]*>Printify[^<]*<\/h[2-3]>)/i);
    if (insertPoint) {
      html = html.replace(insertPoint[1], `${insertPoint[1]}${EMAIL_FORM_HTML}`);
    } else {
      html = html.replace('</body>', `${EMAIL_FORM_HTML}</body>`);
    }
    
    fs.writeFileSync(filePath, html);
    console.log(`Email capture → ${page}`);
  });
  
  console.log(`${pages.length} pages with lead magnet`);
}

// API endpoint mock (Next.js /pages/api/subscribe.js)
const apiCode = `// Next.js API: /pages/api/subscribe.js
export default function handler(req, res) {
  const { email, lead } = req.body;
  // SendGrid/Mailchimp webhook
  console.log('Lead:', email, lead);
  
  res.json({ success: true, download: '/printify-checklist.pdf' });
}`;

// Generate API file
fs.writeFileSync('printify-hub/pages/api/subscribe.js', apiCode);

generateChecklistPDF();
injectEmailCapture();
console.log('Email capture deployed. 10-20% list growth expected.');
