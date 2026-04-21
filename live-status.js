const fs = require('fs');
const path = require('path');
const express = require('express'); // npm i express socket.io
const { Server } = require('socket.io'); // npm i socket.io

const app = express();
const server = app.listen(3001);
const io = new Server(server);

const PAGES_DIR = 'output/pages';
const AFFILIATE_URL = 'https://try.printify.com/r3xsnwqufe8t';

// Live metrics
function getLiveStats() {
  const pages = fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.html')).length;
  const observations = fs.readFileSync('output/observations.csv', 'utf8')
    .split('\n').filter(l => l.includes('high')).length;
  const subscribers = fs.readFileSync('output/subscribers.csv', 'utf8')
    .split('\n').filter(l => l && !l.startsWith('email')).length;
  
  return {
    timestamp: new Date().toLocaleString(),
    pages_generated: pages,
    high_alerts: observations,
    email_list: subscribers,
    pipeline_status: '🟢 LIVE',
    est_revenue_today: `$${(pages * 0.15).toFixed(0)}`, // $0.15/page avg
    next_run: new Date(Date.now() + 6*60*60*1000).toLocaleTimeString()
  };
}

// Serve dashboard
app.use(express.static('output'));
app.get('/live', (req, res) => {
  const stats = getLiveStats();
  res.send(`
<!DOCTYPE html>
<html>
<head>
  <title>Printify Hub LIVE</title>
  <script src="/socket.io/socket.io.js"></script>
  <style>
    body { font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto; background: linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:white; margin:0; padding:20px; }
    .card { background:rgba(255,255,255,0.1); backdrop-filter:blur(10px); padding:30px; margin:20px 0; border-radius:20px; }
    .metric { font-size:48px; font-weight:bold; margin:10px 0; }
    .green { color:#00c853; } .red { color:#ff4444; }
  </style>
</head>
<body>
  <h1>🚀 Printify Empire - LIVE STATUS</h1>
  
  <div class="card">
    <div class="metric green">${stats.pages_generated}</div>
    <div>Pages Live</div>
  </div>
  
  <div class="card">
    <div class="metric">${stats.email_list}</div>
    <div>Email Subscribers</div>
  </div>
  
  <div class="card">
    <div class="metric ${stats.high_alerts > 0 ? 'red' : 'green'}">${stats.high_alerts}</div>
    <div>AI Alerts</div>
  </div>
  
  <div class="card">
    <div class="metric green">${stats.est_revenue_today}</div>
    <div>Est. Today</div>
  </div>
  
  <div style="text-align:center;margin:40px 0;">
    <a href="${AFFILIATE_URL}" style="background:#00c853;color:white;padding:20px 40px;font-size:24px;border-radius:50px;text-decoration:none;font-weight:bold;">Check Printify Dashboard</a>
  </div>
  
  <script>
    const socket = io();
    setInterval(() => socket.emit('stats'), 5000);
    socket.on('stats', stats => {
      document.querySelectorAll('.metric')[0].textContent = stats.pages_generated;
      document.querySelectorAll('.metric')[1].textContent = stats.email_list;
    });
  </script>
</body>
</html>`);
});

// Live updates
setInterval(() => {
  const stats = getLiveStats();
  io.emit('stats', stats);
}, 10000);

console.log('🌐 LIVE DASHBOARD: http://localhost:3001/live');
console.log('📊 Auto-refreshing every 10s');
