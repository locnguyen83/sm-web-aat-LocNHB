# AAT starter – Playwright cho SM-WEB – SaoMai Tools Storefront (môi trường UAT: Toolshop)

1. `npm install` rồi `npx playwright install chromium` (mạng công ty có thể chặn playwright.dev nhưng npm vẫn cài được; nếu tải trình duyệt bị chặn, dùng Codespaces hoặc runner GitHub nội bộ).
2. `npm run test:api` – 3 logical test case API mẫu (API-TC-01…03, TC-03 data-driven); `npm run test:ui` – 1 test UI mẫu.
3. Đổi môi trường bằng biến:
   - Bản có lỗi: `BASE_URL=https://with-bugs.practicesoftwaretesting.com API_URL=https://api-with-bugs.practicesoftwaretesting.com npm test`
   - Bản R0 (regression, RP): `BASE_URL=https://v4.practicesoftwaretesting.com API_URL=https://api-v4.practicesoftwaretesting.com`
   - Local Docker (khi không truy cập được bản hosted – xem `00_README.md`): `BASE_URL=http://localhost:4200 API_URL=http://localhost:8091`
   - Mutant proxy A7-3: chạy `../aat-api-mutant-proxy` rồi `API_URL=http://localhost:8099 npm run test:api`
4. **Chuẩn ổn định CI (A4-3):** chạy workflow `stability-10x` (Actions → Run workflow): 10 lần chạy **toàn suite**, retries = 0, đạt khi ≥ 9/10 lần đúng expected (job `summary`). Không dùng retry/self-healing/skip để che lỗi. `PW_RETRIES` chỉ dùng tạm khi chẩn đoán flaky ngoài lần đo.
5. Quy tắc: locator bằng `getByTestId` (thuộc tính `data-test`) hoặc role/label; không `waitForTimeout`; không commit mật khẩu/token – dùng biến môi trường/Secrets; dữ liệu đăng ký dùng email `@example.com`.
6. Ghi chú môi trường: Toolshop hỗ trợ **guest checkout** – khác REQ-SF-11 (bắt buộc đăng nhập). Ghi thành Open Question/defect ở A1-4.
7. GitHub Projects (A3-2): `scripts/import_tc_to_project.sh <project-number> <owner> A3_GitHub_Projects_Import.csv` (cần gh CLI; kiểm tra lại trên GitHub nội bộ).
8. Phiên bản thư viện ghim trong package.json; nâng cấp có review. Repo học viên đặt tên `sm-web-aat-<mã HV>`.
