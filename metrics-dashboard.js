require('dotenv').config();
const fs = require('fs');
const { google } = require('googleapis'); // npm i googleapis
const path = require('path');

const GA4_PROPERTY = process.env.GA4_PROPERTY || 'GA4_MOCK';
const AFF_API_KEY = process.env.AFFILIATE_API_KEY; // Printify/LinkConnector
const PAGES_DIR = 'output/pages';

// Mock data (replace with real GA4 + Printify affiliate reports)
const mockMetrics = {
  pages: fs.readdirSync(PAGES_DIR).length,
  traffic: 5423, // Last 30d
  conversions: 87,
  revenue: 1245.60, // Affiliate commissions
  topPages: ['printify-review.html (23%)', 'best-pod-2026.html (18%)'],
  ctrTrend: [0.012, 0.015, 0.018, 0.022], // Up 83%
  issues: fs.readFileSync('output/observations.csv', 'utf8').split('\n').filter(l => l && !l.startsWith('type')).length
};

// Real GA4 fetch (uncomment with service-account.json)
async function fetchRealMetrics() {
  // const analytics = google.analyticsdata({ version: 'v1beta', auth: './service-account.json' });
  // const res = await analytics.properties.runReport({
  //   property: `properties/${GA4_PROPERTY}`,
  //   requestBody: {
  //     dateRanges: [{ startDate: '30daysAgo', endDate: 'today' }],
  //     dimensions: [{ name: 'pagePath' }, { name: 'sessionDefaultChannelGrouping' }],
  //     metrics: [{ name: 'activeUsers' }, { name: 'eventCount' }]
  //   }
  // });
  return mockMetrics;
}

// Printify affiliate mock (real: API call)
async function fetchAffCommissions() {
  // Fetch from https://affiliate.printify.com/reports?api_key=${AFF_API_KEY}
  return { clicks: 342, sales: 87, commissions: 1245.60 };
}

// Generate dashboard HTML with Chart.js
async function generateDashboard() {
  const metrics = await fetchRealMetrics();
  const aff = await fetchAffCommissions();
  
  const dashboard = `<!DOCTYPE html>
<html>
<head>
  <title>Printify Hub Dashboard - ${new Date().toLocaleDateString()}</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>body{font-family:Arial; max-width:1200px; margin:0 auto;} .card{background:#f5f5f5; padding:20px; margin:10px; border-radius:8px;}</style>
</head>
<body>
  <h1>🚀 Printify Global Hub Metrics</h1>
  
  <div class="card">
    <h2>Overview</h2>
    <p>Pages: <strong>${metrics.pages}</strong> | Traffic 30d: <strong>${metrics.traffic.toLocaleString()}</strong></p>
    <p>Conversions: <strong>${metrics.conversions}</strong> | Revenue: <strong>$${aff.commissions.toLocaleString()}</strong></p>
  </div>
  
  <div class="card">
    <h2>CTR Trend (Last 7d)</h2>
    <canvas id="ctrChart" width="400" height="200"></canvas>
  </div>
  
  <div class="card">
    <h2>Top Pages</h2>
    <ul>${metrics.topPages.map(p => `<li>${p}</li>`).join('')}</ul>
  </div>
  
  <div class="card">
    <h2>AI Alerts</h2>
    <p><strong>${metrics.issues}</strong> observations. Run monitor-agent.js</p>
    <a href="${AFFILIATE_URL}" target="_blank">Check Printify Commissions</a>
  </div>

  <script>
    const ctx = document.getElementById('ctrChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: { labels: ['Day1','Day2','Day3','Day4'], datasets: [{ label: 'CTR', data: ${JSON.stringify(mockMetrics.ctrTrend)}, borderColor: 'green' }] },
      options: { scales: { y: { beginAtZero: true } } }
    });
  </script>
</body>
</html>`;

  fs.writeFileSync('output/dashboard.html', dashboard);
  console.log('Dashboard generated: output/dashboard.html');
}

// Run
generateDashboard();

// Auto-refresh cron (daily)
const cron = require('node-cron');
cron.schedule('0 0 * * *', generateDashboard);

console.log('Metrics dashboard live.');
