import { Page, expect } from '@playwright/test';

export class ProductPage {
  constructor(private page: Page) {}

  async openFirstProductByName(name: string) {
    await this.page.goto('/');
    await this.page.getByTestId('product-name').filter({ hasText: name }).first().click();
    await expect(this.page.getByTestId('add-to-cart')).toBeVisible();
  }

  async setQuantity(n: number) {
    await this.page.getByTestId('quantity').fill(String(n));
  }

  async addToCart() {
    await this.page.getByTestId('add-to-cart').click();
  }
}
