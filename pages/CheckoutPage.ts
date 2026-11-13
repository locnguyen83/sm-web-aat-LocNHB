import { Page, expect } from '@playwright/test';

// Các bước checkout của Toolshop: giỏ hàng → đăng nhập/khách → địa chỉ → thanh toán.
// data-test đã xác nhận (10/2026): email, password, login-submit, guest-email, country, postal_code,
// street, city, state, proceed-3, payment-method, finish. Kiểm tra lại nếu Toolshop đổi phiên bản.
export class CheckoutPage {
  constructor(private page: Page) {}

  async open() { await this.page.goto('/checkout'); }

  async login(email: string, password: string) {
    await this.page.getByTestId('email').fill(email);
    await this.page.getByTestId('password').fill(password);
    await this.page.getByTestId('login-submit').click();
  }

  async choosePayment(value: 'bank-transfer' | 'cash-on-delivery' | 'credit-card' | 'buy-now-pay-later' | 'gift-card') {
    await this.page.getByTestId('payment-method').selectOption(value);
  }

  async expectPaymentOptions() {
    const opts = await this.page.getByTestId('payment-method').locator('option').allTextContents();
    expect(opts).toEqual(expect.arrayContaining(['Bank Transfer', 'Cash on Delivery', 'Credit Card', 'Buy Now Pay Later', 'Gift Card']));
  }
}
