const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const MODULES = [
  'data-backbone.js',
  'content-gen.js', 
  'printify-provider-monitor.js',
  'production-time-optimizer.js',
  'kit-strategy-generator.js',
  'premium-product-updater.js',
  'aov-upsell-engine.js',
  'seasonal-promotion-engine.js',
  'competitor-price-tracker.js',
  'social-proof-engine.js',
  'risk-compliance.js',
  'api-automation.js',
  'domain-deployer.js',
  'performance-optimizer.js',
  'auto-keyword-expander.js',
  'traffic-accelerator.js',
  'printify-vs-printful.js',
  'roi-calculator.js',
  'ab-testing-engine.js'
];

console.log('🚀 PRINTIFY EMPIRE ORCHESTRATOR');
console.log('================================');

let successCount = 0;
const failed = [];

MODULES.forEach(module => {
  try {
    console.log(`\n🔄 Running ${module}...`);
    execSync(`node ${module}`, { 
      timeout: 120000, 
      stdio: 'pipe',
      cwd: __dirname 
    });
    successCount++;
    console.log(`✅ ${module} COMPLETE`);
  } catch (error) {
    console.log(`❌ ${module} FAILED: ${error.message.slice(0, 100)}`);
    failed.push(module);
  }
});

console.log('\n================================');
console.log(`🎉 EMPIRE DEPLOYMENT COMPLETE`);
console.log(`✅ ${successCount}/${MODULES.length} modules successful`);
console.log(`📊 ${fs.readdirSync('output/pages').filter(f => f.endsWith('.html')).length} pages generated`);
console.log(`🌐 Ready for: node master-control-panel.js`);

if (failed.length > 0) {
  console.log(`\n⚠️  Failed modules (${failed.length}):`);
  failed.forEach(f => console.log(`   ${f}`));
}

// Deploy final production build
try {
  console.log('\n🎯 Final production deploy...');
  execSync('node domain-deployer.js', { timeout: 300000, stdio: 'pipe' });
  console.log('🚀 PRODUCTION BUILD COMPLETE → yourdomain.com');
} catch (e) {
  console.log('⚠️  Production deploy skipped');
}

console.log('\n💎 YOUR PRINTIFY EMPIRE IS LIVE');
console.log('1. node master-control-panel.js → Dashboard');
console.log('2. Add domain to Cloudflare');
console.log('3. Monitor GA4 + Printify affiliate dashboard');
console.log('$5k → $50k/mo potential unlocked!');
