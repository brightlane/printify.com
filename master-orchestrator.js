const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🚀 PRINTIFY EMPIRE AUTO-DETECT ORCHESTRATOR v3.0');
console.log('================================');

// 🔥 AUTO-DETECT ALL .js FILES (excludes itself + control panel)
let allModules = fs.readdirSync(__dirname)
  .filter(f => f.endsWith('.js'))
  .filter(f => !['master-orchestrator.js', 'master-control-panel.js'].includes(f))
  .sort(); // Run alphabetically

console.log(`📂 AUTO-DETECTED: ${allModules.length} modules`);
console.log(`📋 Modules: ${allModules.slice(0, 10).join(', ')}${allModules.length > 10 ? '...' : ''}\n`);

let successCount = 0;
const failed = [];
const skipped = [];

// Run ALL detected modules
allModules.forEach((module, index) => {
  const exists = fs.existsSync(module);
  
  if (!exists) {
    skipped.push(module);
    return;
  }
  
  try {
    console.log(`\n[${String(index + 1).padStart(2, ' ')}/${allModules.length}] 🔄 ${module}`);
    execSync(`node ${module}`, { 
      timeout: 180000, // 3 min timeout
      stdio: 'pipe',
      cwd: __dirname 
    });
    successCount++;
    console.log(`✅ ${module.padEnd(30)} COMPLETE`);
  } catch (error) {
    console.log(`❌ ${module.padEnd(30)} FAILED: ${error.message.slice(0, 60)}`);
    failed.push(module);
  }
});

// Final stats
console.log('\n' + '='.repeat(60));
console.log(`🎉 ORCHESTRATION COMPLETE (${new Date().toLocaleTimeString()})`);
console.log(`✅ SUCCESS: ${successCount}/${allModules.length}`);
console.log(`📄 PAGES: ${fs.readdirSync('output/pages').filter(f => f.endsWith('.html')).length || 0}`);

if (failed.length) console.log(`❌ FAILED: ${failed.length} (${failed.slice(0,3).join(', ')}${failed.length>3?',...':''})`);
if (skipped.length) console.log(`⚠️  SKIPPED: ${skipped.length} (missing files)`);

// 🚀 FINAL PRODUCTION DEPLOY
try {
  console.log('\n🎯 FINAL PRODUCTION BUILD...');
  execSync('node domain-deployer.js', { timeout: 300000, stdio: 'pipe' });
  console.log('🌐 LIVE → https://brightlane.github.io/printify.com');
} catch (e) {
  console.log('⚠️  Production skipped (run manually)');
}

// 💎 EMPIRE DASHBOARD
console.log('\n💎 EMPIRE READY:');
console.log('👉 node master-control-panel.js → LIVE DASHBOARD');
console.log('👉 https://brightlane.github.io/printify.com → PUBLIC SITE');
console.log('👉 Add custom domain → Cloudflare');
console.log('\n🚀 NEW FILES AUTO-RUN - Add .js → Instantly included!');
console.log(`💰 $50K/MO POTENTIAL → LIVE`);
