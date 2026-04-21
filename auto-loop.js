require('dotenv').config();
const cron = require('node-cron');
const { execSync } = require('child_process');
const fs = require('fs');

const STEPS = [
  { name: 'data-backbone', cmd: 'node data-backbone.js' },
  { name: 'content-gen', cmd: 'node content-gen.js' },
  { name: 'monitor-agent', cmd: 'node monitor-agent.js' },
  { name: 'deploy-nextjs', cmd: 'node deploy-nextjs.js' }
];

async function runPipeline() {
  console.log('=== Pipeline run started (April 2026) ===');
  
  for (const step of STEPS) {
    try {
      console.log(`Running ${step.name}...`);
      execSync(step.cmd, { stdio: 'inherit', timeout: 300000 }); // 5min timeout
      console.log(`${step.name} OK`);
    } catch (e) {
      console.error(`${step.name} failed: ${e.message}`);
      // Self-heal: High prio obs → extra content-gen
      if (step.name === 'monitor-agent') {
        execSync('node content-gen.js', { stdio: 'inherit' });
      }
      return; // Stop on error
    }
  }
  
  // Post-run: Check observations for auto-scale
  const obs = fs.readFileSync('output/observations.csv', 'utf8').split('\n').filter(l => l.includes('high'));
  if (obs.length > 5) {
    console.log('High alerts: Scaling content-gen x2');
    execSync('node content-gen.js', { stdio: 'inherit' });
  }
  
  console.log('Pipeline complete. Pages live.');
}

// Run immediately
runPipeline();

// Schedule: Every 6 hours (adjust for 100-300 pages/day)
cron.schedule('0 */6 * * *', () => {
  console.log('Cron trigger: Full pipeline');
  runPipeline();
});

console.log('Auto-loop running. Ctrl+C to stop.');
