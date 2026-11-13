// Đếm số lần chạy toàn suite đúng expected từ các file Playwright JSON report.
// Dùng: node scripts/count_stability.mjs <thư mục chứa results-run-*/results.json> <ngưỡng, mặc định 9>
import fs from 'node:fs';
import path from 'node:path';

const dir = process.argv[2] ?? 'all-results';
const threshold = Number(process.argv[3] ?? 9);
const files = [];
for (const d of fs.existsSync(dir) ? fs.readdirSync(dir) : []) {
  const f = path.join(dir, d, 'results.json');
  if (fs.existsSync(f)) files.push(f);
}
let ok = 0;
const rows = [];
for (const f of files.sort()) {
  const s = JSON.parse(fs.readFileSync(f, 'utf8')).stats ?? {};
  // Đúng expected = không có test unexpected, không flaky (retries = 0 nên flaky phải = 0), không skip.
  const pass = (s.unexpected ?? 1) === 0 && (s.flaky ?? 0) === 0 && (s.skipped ?? 0) === 0 && (s.expected ?? 0) > 0;
  if (pass) ok++;
  rows.push(`${path.basename(path.dirname(f))}: expected=${s.expected} unexpected=${s.unexpected} flaky=${s.flaky} skipped=${s.skipped} -> ${pass ? 'ĐÚNG' : 'KHÔNG ĐÚNG'}`);
}
console.log(rows.join('\n'));
console.log(`\nKết quả: ${ok}/${files.length} lần chạy toàn suite đúng expected (ngưỡng ${threshold}/10).`);
if (files.length < 10) { console.log('Chưa đủ 10 lần chạy -> chưa đạt chuẩn.'); process.exit(1); }
process.exit(ok >= threshold ? 0 : 1);
