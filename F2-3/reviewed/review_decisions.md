# Review decisions – F2-3 – LocNHB

Bộ cuối: `conditions_final.json` (26 condition, 10/10 REQ). Validate bằng code: jsonschema 0 lỗi; mọi `req_id` thuộc 10 ID của fixture; mọi `source_quote` là chuỗi con nguyên văn của `fixture_srs_cart_checkout.md` (kiểm tra toàn chuỗi, chặt hơn kiểm tra 20 ký tự đầu của notebook).

## Nguồn
- **Giữ nguyên 22 condition của run2 v1.1** (`raw_ai_output/run2_v1.1_PR-F2-02.txt`, C-01…C-22): đều có căn cứ trong fixture, `source_quote` nguyên văn, đủ biên hợp lệ/không hợp lệ cho REQ-SF-03 và CVV (REQ-SF-22), có ca âm REQ-SF-10.
- **Không dùng run1 v1.1** (25 condition): toàn bộ bị kiểm soát `source_quote` đánh dấu vì P1 v1.1 diễn đạt lại tiêu chí chấp nhận và P2 trích theo bản diễn đạt → mất truy vết về câu SRS gốc. Không có yêu cầu bịa, nhưng không đạt tiêu chí "source_quote nguyên văn" → loại cả bộ.
- **Không dùng output v1.0** (run1/run2/injection): thiếu ca âm REQ-SF-10 và nhiều biên; được thay bằng v1.1.

## Bổ sung sau khi đối chiếu self-check với fixture
| ID cuối | req_id | Nội dung | Nguồn gợi ý | Căn cứ trong fixture |
|---|---|---|---|---|
| C-23 | REQ-SF-12 | Bỏ trống lần lượt các trường còn lại (địa chỉ, thành phố, tỉnh/bang, quốc gia) | Self-check run2 v1.1 | "Thiếu một trường → không sang bước 4, hiển thị lỗi tại trường." |
| C-24 | REQ-SF-22 | Bỏ trống tên chủ thẻ | Self-check run2 v1.1, injection v1.1 | "…; tên chủ thẻ." |
| C-25 | REQ-SF-22 | Ngày hết hạn sai định dạng MM/YYYY | Self-check run1 v1.1 | "Trường sai định dạng → không thanh toán, hiển thị lỗi." |
| C-26 | REQ-SF-22 | Ngày hết hạn = tháng/năm hiện tại (biên hợp lệ) | Self-check run1/run2 v1.0 | "ngày hết hạn MM/YYYY không ở quá khứ" |

## Loại (không có căn cứ trong fixture)
| Gợi ý | Nguồn | Lý do loại |
|---|---|---|
| REQ-SF-14: thanh toán thất bại thì không tạo hóa đơn | Self-check run2 v1.1 | Fixture chỉ mô tả trường hợp thành công; hành vi khi thất bại không được quy định → không đưa vào bộ cuối (có thể ghi thành Open Question cho BA) |
| REQ-SF-11: khách đã đăng nhập bỏ qua form ở bước 2 | Self-check injection v1.1 | Fixture chỉ quy định cho khách chưa đăng nhập → không đưa vào bộ cuối (Open Question) |
