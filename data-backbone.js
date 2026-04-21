const fs = require('fs');
const csv = require('csv-parser'); // npm install csv-parser
const createCsvParser = require('csv-parser');

// Your affiliate link – hardcoded for global use
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// Load products CSV (download from code_file:23)
function loadProducts() {
  return new Promise((resolve, reject) => {
    const products = [];
    fs.createReadStream('output/products.csv')
      .pipe(csv())
      .on('data', (row) => products.push(row))
      .on('end', () => resolve(products))
      .on('error', reject);
  });
}

// Load features (code_file:22)
function loadFeatures(productId = 1) {
  return new Promise((resolve, reject) => {
    const features = [];
    fs.createReadStream('output/product_features.csv')
      .pipe(csv())
      .on('data', (row) => {
        if (row.product_id == productId) features.push(row);
      })
      .on('end', () => resolve(features))
      .on('error', reject);
  });
}

// Generate Printify review page (reference-style, SEO-ready)
async function generatePrintifyReview() {
  const products = await loadProducts();
  const printify = products.find(p => p.id === '1');
  const features = await loadFeatures(1);

  const featureList = features.map(f => `<li><strong>${f.feature}:</strong> ${f.value}</li>`).join('\n');

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <title>Printify Review 2026: Global POD Platform</title>
  <meta name="description" content="Printify specs, pricing, worldwide shipping. Best for ecom sellers. Affiliate disclosure.">
  <link rel="alternate" hreflang="es" href="/es/printify-review/">
  <!-- Schema.org Product -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "${printify.name}",
    "brand": "${printify.brand}"
  }
  </script>
</head>
<body>
  <h1>Printify Review: Print-on-Demand Worldwide</h1>
  
  <section>
    <h2>Key Specs</h2>
    <ul>${featureList}</ul>
    <p>Available in ${printify.regions}. No upfront costs.[code_file:22][web:3]</p>
  </section>
  
  <section>
    <h2>Pricing & Commissions</h2>
    <p>${printify.commissions}. Pay per order.</p>
    <a href="${AFFILIATE_URL}" class="cta-button" rel="sponsored">Start Selling with Printify</a>
  </section>
  
  <p><em>Affiliate disclosure: We earn from qualifying purchases.</em></p>
</body>
</html>`;

  fs.writeFileSync('output/printify-review-en.html', html);
  console.log('Generated: output/printify-review-en.html with affiliate link');
}

// Run it
generatePrintifyReview().catch(console.error);
