import { test, expect } from '@playwright/test';
import { ProductPage } from '../../pages/ProductPage';

// TC mẫu – REQ-SF-01. Học viên viết thêm 9 TC (A4-3) theo cùng mẫu: page object, không sleep cứng.
test('REQ-SF-01 thêm sản phẩm còn hàng vào giỏ cập nhật số lượng trên biểu tượng giỏ', async ({ page }) => {
  const product = new ProductPage(page);
  await product.openFirstProductByName('Combination Pliers');
  await product.setQuantity(2);
  await product.addToCart();
  await expect(page.getByTestId('cart-quantity')).toHaveText('2');
});
