require('dotenv').config();
const OpenAI = require('openai');
const fs = require('fs');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Load all system state
async function loadState() {
  const dashboard = fs.readFileSync('output/dashboard.html', 'utf8');
  const observations = fs.readFileSync('output/observations.csv', 'utf8');
  const keywords = await new Promise(r => {
    let k = []; require('csv-parser'); fs.createReadStream('output/keywords.csv').pipe(require('csv-parser')()).on('data', row => k.push(row)).on('end', () => r(k));
  });
  
  return { dashboard, observations, keywords };
}

// AI self-analysis
async function selfAnalyze() {
  const state = await loadState();
  
  const analysisPrompt = `Analyze this affiliate hub state and recommend optimizations:

Dashboard: ${state.dashboard.substring(0, 2000)}...
Observations (last 10): ${state.observations.split('\\n').slice(-10).join('; ')}
Keywords count: ${state.keywords.length}

CRITIQUE:
1. Top issues (low CTR/bounce)?
2. Weak pages/niches?
3. New keywords to add (high vol, low comp)?
4. Prompt improvements for content-gen.js?
5. Scale suggestions (langs/products)?

Output JSON:
{
  "issues": ["..."],
  "new_keywords": [{"keyword": "...", "volume": 5000, "niche": "printify"}],
  "prompt_fixes": {"contentPrompt": "Updated version..."},
  "scale_actions": ["Add niche: hats", "Translate to Hindi"]
}`;

  const response = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [{ role: 'user', content: analysisPrompt }]
  });
  
  const optimizations = JSON.parse(response.choices[0].message.content);
  return optimizations;
}

// Apply optimizations
async function applyOptimizations(opts) {
  // 1. Add new keywords
  if (opts.new_keywords) {
    const newRows = opts.new_keywords.map(kw => `${kw.keyword},${kw.volume},commercial,en,global,1`).join('\n') + '\n';
    fs.appendFileSync('output/keywords.csv', newRows);
    console.log(`Added ${opts.new_keywords.length} keywords`);
  }
  
  // 2. Update prompts.json for agents
  const prompts = fs.existsSync('prompts.json') ? JSON.parse(fs.readFileSync('prompts.json')) : { contentPrompt: '', outlinePrompt: '' };
  if (opts.prompt_fixes) {
    Object.assign(prompts, opts.prompt_fixes);
    fs.writeFileSync('prompts.json', JSON.stringify(prompts, null, 2));
    console.log('Prompts optimized');
  }
  
  // 3. Log scale actions
  fs.appendFileSync('output/scale-log.txt', `${new Date()}: ${JSON.stringify(opts.scale_actions)}\n`);
  
  // Trigger pipeline
  require('child_process').execSync('node auto-loop.js', { stdio: 'inherit' });
}

// Run self-optimization
async function main() {
  console.log('🤖 Self-optimizing...');
  const opts = await selfAnalyze();
  console.log('Optimizations:', JSON.stringify(opts, null, 2));
  await applyOptimizations(opts);
  console.log('System improved. Restart agents.');
}

main().catch(console.error);

// Daily cron
const cron = require('node-cron');
cron.schedule('0 2 * * *', main); // 2AM

console.log('Self-optimizer active.');
