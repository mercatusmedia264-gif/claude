const { chromium } = require('playwright');
(async () => {
  const [html, pdf, shots] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 1.5 });
  await p.goto('file://' + html, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.$$eval('.page', ps => ps.forEach(x => {
    let fs = 17, gap = 4.2;
    while (x.scrollHeight > x.clientHeight && fs > 14) {
      if (gap > 2.6) gap -= 0.4; else fs -= 0.25;
      x.style.setProperty('--fs', fs + 'pt'); x.style.setProperty('--gap', gap + 'mm');
    }
    x.dataset.fs = fs;
  }));
  const fit = await p.$$eval('.page', ps => ps.map(x => {
    const m = x.querySelector('main'); const kids = [...m.children];
    const last = kids[kids.length - 1].getBoundingClientRect().bottom;
    return { fs: x.dataset.fs, over: x.scrollHeight - x.clientHeight, slack: Math.round(m.getBoundingClientRect().bottom - last) };
  }));
  console.log(JSON.stringify(fit));
  const els = await p.$$('.page');
  for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${shots}/n${i}.png` });
  await p.pdf({ path: pdf, preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
