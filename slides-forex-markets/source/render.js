const { chromium } = require('playwright');
(async () => {
  const [html, outDir, pdf] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch());
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + html, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const n = await p.$$eval('.slide', s => s.length);
  const els = await p.$$('.slide');
  for (let i = 0; i < n; i++) await els[i].screenshot({ path: `${outDir}/s${String(i + 1).padStart(2, '0')}.png` });
  if (pdf) await p.pdf({ path: pdf, width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
  console.log('slides', n);
  await b.close();
})();
