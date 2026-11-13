// F0-TS – bài tự kiểm 4: đoạn code "do AI sinh" có lỗi cố ý. Tìm và sửa ≥ 3 vấn đề.
// KHÔNG chạy file này trong CI (nằm ngoài testDir).
import { test, expect } from '@playwright/test';

test('AI sinh – thêm 3 sản phẩm vào giỏ', async ({ page }) => {
  page.goto('/');                                                        // (?) thiếu gì ở đây
  await page.locator('div.container > div:nth-child(2) > a:nth-child(1)').click(); // (?) locator có bền không
  await page.waitForTimeout(5000);                                       // (?) cách chờ này ổn không
  await page.getByTestId('quantity').fill(3);                            // (?) kiểu dữ liệu
  await page.getByTestId('add-to-cart').click();
  const badge = await page.getByTestId('cart-quantity').textContent();
  expect(badge).toBe('3');                                               // (?) có tự chờ không
});
