import { defineConfig, devices } from '@playwright/test';

// SM-WEB – SaoMai Tools Storefront; môi trường UAT = Toolshop.
// Đổi BASE_URL/API_URL sang bản with-bugs, v4 (regression R0), local Docker (http://localhost:4200 / :8091)
// hoặc mutant proxy A7-3 (http://localhost:8099) khi cần.
export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  // Chuẩn ổn định (syllabus AAT v1.4, A4-3): retries = 0 khi đo. Chỉ đặt PW_RETRIES > 0 tạm thời để
  // CHẨN ĐOÁN flaky ngoài lần đo, và phải báo cáo số test chỉ pass sau retry. Không dùng retry để che lỗi.
  retries: Number(process.env.PW_RETRIES ?? 0),
  reporter: [['html', { open: 'never' }], ['list'], ['json', { outputFile: 'results/results.json' }]],
  use: {
    baseURL: process.env.BASE_URL ?? 'https://practicesoftwaretesting.com',
    testIdAttribute: 'data-test',            // Toolshop dùng thuộc tính data-test
    trace: 'retain-on-failure',              // retries = 0 nên không dùng 'on-first-retry'
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'ui', testMatch: /ui\/.*\.spec\.ts/, use: { ...devices['Desktop Chrome'] } },
    { name: 'api', testMatch: /api\/.*\.spec\.ts/, use: { baseURL: process.env.API_URL ?? 'https://api.practicesoftwaretesting.com' } },
  ],
});
