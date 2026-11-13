import { test, expect } from '@playwright/test';
import Ajv from 'ajv';
import cartCreateSchema from '../../schemas/cart_create.schema.json';

// Mẫu A7 – SM-WEB. Quy ước (05_Lab_Guides.md):
//  - 1 logical test case = 1 ID (API-TC-xx) + 1 oracle (status + schema + body). Nhiều bộ dữ liệu của cùng case (data-driven) tính 1.
//  - Oracle phân quyền: thiếu/sai token -> 401; truy cập tài nguyên của người khác -> 403 (REQ-API-02, REQ-SF-31).
//    Nếu UAT trả mã khác: giữ oracle 403 và đánh dấu test.fail() + link defect/Open Question.
//  - Học viên mở rộng lên >= 15 logical case (A7-3); ghi bằng chứng AI vào A7_API_AI_Evidence.csv.
//  - Chạy trên target lỗi: API_URL=https://api-with-bugs.practicesoftwaretesting.com hoặc mutant proxy http://localhost:8099.

const ajv = new Ajv();

async function anyInStockProductId(request: any): Promise<string> {
  const res = await request.get('/products?page=1');
  expect(res.ok()).toBeTruthy();
  const body = await res.json();
  const p = body.data.find((x: any) => x.in_stock);   // bản with-bugs/mutant M5 đổi tên trường -> case này lộ lỗi contract
  expect(p, 'Không tìm thấy sản phẩm có in_stock=true (kiểm tra contract trường in_stock)').toBeTruthy();
  return p.id;
}

test('API-TC-01 [REQ-API-01] tạo giỏ trả 201 và id đúng schema', async ({ request }) => {
  const res = await request.post('/carts');
  expect(res.status()).toBe(201);
  const validate = ajv.compile(cartCreateSchema);
  const body = await res.json();
  expect(validate(body), JSON.stringify(validate.errors)).toBe(true);
});

test('API-TC-02 [REQ-API-01] thêm sản phẩm còn hàng vào giỏ trả 200', async ({ request }) => {
  const cart = await (await request.post('/carts')).json();
  const productId = await anyInStockProductId(request);
  const res = await request.post(`/carts/${cart.id}`, { data: { product_id: productId, quantity: 1 } });
  expect(res.status()).toBe(200);
});

// API-TC-03 – data-driven: nhiều bộ dữ liệu, CÙNG 1 oracle -> tính 1 logical case.
// (Các bộ dữ liệu này đều phải trả 4xx; trainer đã chạy thử trên Toolshop trước khóa.)
for (const quantity of ['abc', null]) {
  test(`API-TC-03 [REQ-API-03] quantity không hợp lệ (${JSON.stringify(quantity)}) trả 4xx, không 5xx`, async ({ request }) => {
    const cart = await (await request.post('/carts')).json();
    const productId = await anyInStockProductId(request);
    const res = await request.post(`/carts/${cart.id}`, { data: { product_id: productId, quantity } });
    expect(res.status()).toBeGreaterThanOrEqual(400);
    expect(res.status()).toBeLessThan(500);
  });
}
