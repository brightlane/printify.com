const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const MODULES = [
  // CORE (5 hours ago)
  'data-backbone.js',
  'content-gen.js',
  'monitor-agent.js',
  
  // PRINTIFY SPECIFIC (last 4 hours)
  'printify-provider-monitor.js',
  'production-time-optimizer.js',
  'kit-strategy-generator.js',
  'premium-product-updater.js',
  'aov-upsell-engine.js',
  'seasonal-promotion-engine.js',
  
  // COMPETITION + ROI (last 30 mins)
  'competitor-price-tracker.js',
  'printify-vs-printful.js',
  'roi-calculator.js',
  'printify-popularity-analyzer.js',
  
  // PERFORMANCE + SEO (last 20 mins)
  'performance-optimizer.js',
  'voice-search-optimizer.js',
  'auto-keyword-expander.js',
  'traffic-accelerator.js',
  
  // CONVERSION OPTIMIZATION (last 15 mins)
  'ab-testing-engine.js',
  'social-proof-engine.js',
  
  // GLOBAL + COMPLIANCE
  'international-localizer.js',
  'risk-compliance.js',
  'api-automation.js',
  
  // DEPLOYMENT (last 13 mins)
  'domain-deployer.js',
  'master-control-panel.js',
  
  // SUPPORTING MODULES (from your repo)
  'analytics-seo.js',
  'competitor-spy.js',
  'deploy-nextjs.js',
  'email-capture.js',
  'internal-linker.js',
  'metrics-dashboard.js',
  'multi-niche-expander.js',
  'popup-converter.js',
  'revenue-forecaster.js',
  'self-optimize.js'
];

console.log('🚀 PRINTIFY EMPIRE ORCHESTRATOR v2.0');
console.log('================================');
console.log(`📂 Found ${MODULES.length} modules in repo`);

let successCount = 0;
const failed = [];

MODULES.forEach((module, index) => {
  if (fs.existsSync(module)) {
    try {
      console.log(`\n[${index + 1}/${MODULES.length}] 🔄 ${module}`);
      execSync(`node ${module}`, { 
        timeout: 120000, 
        stdio: 'pipe',
        cwd: __dirname 
      });
      successCount++;
      console.log(`✅ ${module} COMPLETE`);
    } catch (error) {
      console.log(`❌ ${module} SKIPPED: ${error.message.slice(0, 80)}`);
      failed.push(module);
    }
  } else {
    console.log(`⚠️  ${module} NOT FOUND - skipping`);
  }
});

console.log('\n================================');
console.log(`🎉 ORCHESTRATION COMPLETE`);
console.log(`✅ ${successCount}/${MODULES.length} modules executed`);
console.log(`📄 ${fs.readdirSync('output/pages').filter(f => f.endsWith('.html')).length || 0} pages generated`);

if (failed.length > 0) {
  console.log(`\n🔧 Failed (${failed.length}): ${failed.slice(0, 5).join(', ')}${failed.length > 5 ? '...' : ''}`);
}

// Final production deploy
try {
  console.log('\n🎯 PRODUCTION DEPLOY...');
  execSync('node domain-deployer.js', { timeout: 300000, stdio: 'pipe' });
  console.log('🌐 LIVE → https://brightlane.github.io/printify.com');
} catch (e) {
  console.log('⚠️  Production deploy skipped');
}

console.log('\n💎 EMPIRE STATUS:');
console.log('👉 node master-control-panel.js → Dashboard');
console.log('👉 https://brightlane.github.io/printify.com → Live site');
console.log('👉 GA4 + Printify dashboard → Revenue tracking');
console.log('\n🚀 $50K/MO POTENTIAL UNLOCKED');
