# Time log – F2-3 (luyện đo thời gian) – LocNHB

Protocol (bước 9 lab F2-3): bấm giờ **thật** – ghi start ngay khi bắt đầu và end ngay khi kết thúc, không ước lượng sau khi làm. So sánh trên **cùng phạm vi 5 condition tương đương**.

Phạm vi đề xuất (5 condition): REQ-SF-03 – số lượng = 0, 1, 10, 11; REQ-SF-12 – bỏ trống mã bưu chính.

| # | Cách làm | Phạm vi | Start (giờ:phút) | End (giờ:phút) | Tổng (phút) | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Thủ công (không dùng AI) | 5 condition ở trên, viết theo `tc_condition.schema.json` (có id, req_id, condition, technique, priority, source_quote) | | | | |
| 2 | Chuỗi prompt + review | Đọc output chuỗi, chọn và đối chiếu 5 condition tương đương với fixture, ghi quyết định giữ/sửa/loại | | | | Máy chạy chuỗi: ~49 s (run2 v1.1, xem `run_log_v1.1.txt`) |

Nhận xét (sau khi đo): …
