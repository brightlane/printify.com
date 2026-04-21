require('dotenv').config();
const express = require('express'); // npm i express
const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

const app = express();
const PORT = 3001;
app.use(express.static('output'));
app.use(express.json());

const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';
const ALL_MODULES = [
  'data-backbone.js', 'content-gen.js', 'monitor-agent.js', 'deploy-nextjs.js',
  'multi-niche-expander.js', 'analytics-seo.js', 'metrics-dashboard.js',
  'self-optimize.js', 'revenue-forecaster.js', 'popup-converter.js',
  'ab-testing.js', 'competitor-spy.js', 'international-seo.js',
  'voice-faq-schema.js', 'internal-linker.js', 'core-web-vitals.js',
  'email-capture.js', 'email-sequence.js', 'printify-provider-monitor.js',
  'production-time-optimizer.js', 'kit-strategy-generator.js',
  'premium-product-updater.js', 'aov-upsell-engine.js',
  'seasonal-promotion-engine.js', 'competitor-price-tracker.js',
  'social-proof-engine.js', 'risk-compliance.js'
];

// API endpoints
app.get('/api/stats', (req, res) => {
  const pages = fs.readdirSync('output/pages').filter(f => f.endsWith('.html')).length;
  const subscribers = fs.readFileSync('output/subscribers.csv', 'utf8').split('\n').filter(l => l && !l.startsWith('email')).length;
  
  res.json({
    pages, subscribers,
    modules: ALL_MODULES.length,
    estRevenue: `$${(pages * 0.25).toLocaleString()}/day`,
    status: '🟢 LIVE'
  });
});

app.post('/api/run-module', (req, res) => {
  const { module } = req.body;
  try {
    console.log(`🚀 Running ${module}...`);
    execSync(`node ${module}`, { timeout: 300000, stdio: 'pipe' });
    res.json({ success: true, message: `${module} completed` });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.post('/api/full-deploy', (req, res) => {
  execSync('node master-orchestrator.js', { timeout: 1800000, stdio: 'pipe' });
  res.json({ success: true, message: 'Full empire deployed!' });
});

app.get('/', (req, res) => {
  const stats = fs.existsSync('output/dashboard.html') ? 
    fs.readFileSync('output/dashboard.html', 'utf8') : '';
  
  res.send(`
<!DOCTYPE html>
<html>
<head>
  <title>Printify Empire Control Panel</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box;}
    body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#333;min-height:100vh;}
    .container{max-width:1400px;margin:0 auto;padding:30px;}
    .header{background:rgba(255,255,255,0.95);backdrop-filter:blur(20px);border-radius:25px;padding:40px;margin-bottom:40px;box-shadow:0 20px 60px rgba(0,0,0,0.1);}
    .metric-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:25px;margin:30px 0;}
    .metric-card{background:rgba(255,255,255,0.95);backdrop-filter:blur(20px);padding:30px;border-radius:20px;box-shadow:0 15px 40px rgba(0,0,0,0.1);text-align:center;transition:transform 0.3s;}
    .metric-card:hover{transform:translateY(-10px);}
    .metric-number{font-size:48px;font-weight:bold;background:linear-gradient(135deg,#00c853,#00b140);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:10px;}
    .deploy-btn{background:linear-gradient(135deg,#00c853,#00b140);color:white;border:none;padding:20px 50px;font-size:24px;border-radius:50px;font-weight:bold;cursor:pointer;box-shadow:0 15px 40px rgba(0,200,83,0.4);transition:all 0.3s;}
    .deploy-btn:hover{transform:scale(1.05);box-shadow:0 20px 50px rgba(0,200,83,0.5);}
    .module-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:15px;}
    .module-btn{background:rgba(255,255,255,0.9);border:2px solid #e0e0e0;padding:15px;border-radius:15px;cursor:pointer;font-weight:500;transition:all 0.3s;}
    .module-btn:hover{background:#00c853;color:white;border-color:#00c853;}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1 style="font-size:64px;background:linear-gradient(135deg,#00c853,#00b140);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:20px;">🚀 Printify Empire</h1>
      <p style="font-size:24px;color:#666;">Control Panel - ${new Date().toLocaleString()}</p>
      <button class="deploy-btn" onclick="fullDeploy()">⚡ FULL EMPIRE DEPLOY</button>
    </div>
    
    <div class="metric-grid" id="metrics"></div>
    
    <div style="background:rgba(255,255,255,0.95);backdrop-filter:blur(20px);padding:40px;border-radius:25px;margin:40px 0;box-shadow:0 20px 60px rgba(0,0,0,0.1);">
      <h2 style="margin-bottom:30px;">🎛️ Module Control (${ALL_MODULES.length} Modules)</h2>
      <div class="module-grid" id="modules"></div>
    </div>
    
    <div style="text-align:center;padding:40px;background:rgba(255,255,255,0.1);border-radius:25px;">
      <a href="${AFFILIATE_URL}" class="deploy-btn" style="display:inline-block;font-size:20px;">💰 Check Printify Dashboard</a>
    </div>
  </div>

  <script>
    async function loadStats() {
      const res = await fetch('/api/stats');
      const stats = await res.json();
      document.getElementById('metrics').innerHTML = \`
        <div class="metric-card">
          <div class="metric-number">\${stats.pages}</div>
          <div style="font-size:20px;color:#666;">Pages Live</div>
        </div>
        <div class="metric-card">
          <div class="metric-number">\${stats.subscribers}</div>
          <div style="font-size:20px;color:#666;">Subscribers</div>
        </div>
        <div class="metric-card">
          <div class="metric-number">\${stats.modules}</div>
          <div style="font-size:20px;color:#666;">Modules</div>
        </div>
        <div class="metric-card">
          <div class="metric-number">\${stats.estRevenue}</div>
          <div style="font-size:20px;color:#666;">Est. Daily</div>
        </div>
      \`;
    }
    
    async function fullDeploy() {
      const res = await fetch('/api/full-deploy', {method:'POST'});
      alert('Full empire deployed! 🚀');
      loadStats();
    }
    
    document.getElementById('modules').innerHTML = \`
      ${ALL_MODULES.map(m => 
        \`<button class="module-btn" onclick="runModule('\${m}')">\${m.split('.')[0].replace(/-/g,' ').replace(/\\b\\w/g,l=>l.toUpperCase())}</button>\`
      ).join('')}
    \`;
    
    async function runModule(module) {
      const res = await fetch('/api/run-module', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({module})
      });
      const result = await res.json();
      alert(result.message || result.error);
    }
    
    loadStats();
    setInterval(loadStats, 10000);
  </script>
</body>
</html>`);
});

app.listen(PORT, () => {
  console.log(`🎛️ CONTROL PANEL LIVE: http://localhost:${PORT}`);
  console.log('⚡ One-click empire management');
});
