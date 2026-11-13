# Prompt Record – SM-WEB – LocNHB – F1-3

> Ghi mọi lần dùng AI tạo ra output được dùng trong bài nộp. Raw output lưu nguyên bản ở `raw_ai_output/` (không sửa). Dữ liệu đưa vào AI chỉ loại Hư cấu (SRS SM-WEB, REQ-SF-03) (F3-1).

Công cụ chung cho 8 lần chạy: Google Colab (notebook `F1-3_LocNHB.ipynb`, bản tải về ở `evidence/F1-3_LocNHB.ipynb`) + `F1_variability.py` + `llm_client.py`, Gemini API free tier qua endpoint OpenAI-compatible, model `gemini-3.5-flash`, top_p 0.95, max_tokens 400, reasoning_effort none, không dùng seed. Giờ ghi theo giờ Việt Nam (UTC+7).

| # | Ngày giờ (UTC+7) | Prompt ID + version | Mục đích | Công cụ / model / tham số | Input (nguồn, version) | Raw output (file) | Nguồn kiểm chứng | Quyết định + lý do | Thời gian (phút) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-11-13 13:58 | PR-F1-001 v1.0 (E1) | Sinh 3 test condition | gemini-3.5-flash, temp 0 | REQ-SF-03 – 02_SRS_Storefront.md (bộ tài liệu v1.4) | raw_ai_output/2026-11-13_PR-F1-001_01.txt | 02_SRS_Storefront.md REQ-SF-03 | Giữ làm dữ liệu thí nghiệm; đúng SRS, thiếu biên 1/10 | 2 |
| 2 | 2026-11-13 14:02 | PR-F1-001 v1.0 (E1) | Sinh 3 test condition | gemini-3.5-flash, temp 0 | REQ-SF-03 | raw_ai_output/2026-11-13_PR-F1-001_02.txt | REQ-SF-03 | Giữ làm dữ liệu thí nghiệm; ghi chú sai "> 1" (đúng là > 10) | 2 |
| 3 | 2026-11-13 14:03 | PR-F1-001 v1.0 (E1) | Sinh 3 test condition | gemini-3.5-flash, temp 0 | REQ-SF-03 | raw_ai_output/2026-11-13_PR-F1-001_03.txt | REQ-SF-03 | Giữ làm dữ liệu thí nghiệm; đúng SRS | 2 |
| 4 | 2026-11-13 14:03 | PR-F1-001 v1.0 (E1) | Sinh 3 test condition | gemini-3.5-flash, temp 1 | REQ-SF-03 | raw_ai_output/2026-11-13_PR-F1-001_04.txt | REQ-SF-03 | Giữ làm dữ liệu thí nghiệm; đúng SRS | 2 |
| 5 | 2026-11-13 14:04 | PR-F1-001 v1.0 (E1) | Sinh 3 test condition | gemini-3.5-flash, temp 1 | REQ-SF-03 | raw_ai_output/2026-11-13_PR-F1-001_05.txt | REQ-SF-03 | Giữ làm dữ liệu thí nghiệm; đúng SRS | 2 |
| 6 | 2026-11-13 14:05 | PR-F1-001 v1.0 (E1) | Sinh 3 test condition | gemini-3.5-flash, temp 1 | REQ-SF-03 | raw_ai_output/2026-11-13_PR-F1-001_06.txt | REQ-SF-03 | Giữ làm dữ liệu thí nghiệm; đúng SRS | 2 |
| 7 | 2026-11-13 14:05 | PR-F1-001 v1.0 (E2) | Hỏi giới hạn giỏ hàng, có SRS | gemini-3.5-flash, temp 0 | REQ-SF-03 kèm trong prompt | raw_ai_output/2026-11-13_PR-F1-001_07.txt | REQ-SF-03 | Giữ; trả lời đúng (tối đa 10) | 2 |
| 8 | 2026-11-13 14:06 | PR-F1-001 v1.0 (E2) | Hỏi giới hạn giỏ hàng, không SRS | gemini-3.5-flash, temp 0 | Không có ngữ cảnh | raw_ai_output/2026-11-13_PR-F1-001_08.txt | REQ-SF-03 | Giữ; trả lời "Không có trong tài liệu", không bịa | 2 |

Output AI ở bài này chỉ dùng làm dữ liệu đo, không dùng làm test case hay expected result.

Cột *Thời gian (phút)* là thời gian **ước lượng** cho việc đọc output, đối chiếu REQ-SF-03 và ghi quyết định (không gồm thời gian máy chạy và thời gian cài đặt môi trường); tổng khoảng 16 phút cho 8 lần.

**Đổi tên file raw output theo quy ước `<ngày>_<prompt-id>_<lần>.txt`** (chỉ đổi tên, nội dung giữ nguyên; kiểm chứng bằng cột `output_sha1` trong `f1_runs.csv`, file log do script sinh nên giữ tên cũ):

| Lần | Tên do script sinh (f1_runs.csv) | Tên trong repo |
|---|---|---|
| 1 | run01_E1_t0.0_ctx.txt | 2026-11-13_PR-F1-001_01.txt |
| 2 | run02_E1_t0.0_ctx.txt | 2026-11-13_PR-F1-001_02.txt |
| 3 | run03_E1_t0.0_ctx.txt | 2026-11-13_PR-F1-001_03.txt |
| 4 | run04_E1_t1.0_ctx.txt | 2026-11-13_PR-F1-001_04.txt |
| 5 | run05_E1_t1.0_ctx.txt | 2026-11-13_PR-F1-001_05.txt |
| 6 | run06_E1_t1.0_ctx.txt | 2026-11-13_PR-F1-001_06.txt |
| 7 | run07_E2_t0.0_ctx.txt | 2026-11-13_PR-F1-001_07.txt |
| 8 | run08_E2_t0.0_noctx.txt | 2026-11-13_PR-F1-001_08.txt |

## Nội dung prompt (theo version)
### PR-F1-001 v1.0
System (dùng cho mọi lần chạy):
```
Bạn là tester. Chỉ dựa trên tài liệu được cung cấp; nếu tài liệu không có thông tin, trả lời 'Không có trong tài liệu'.
```
E1 – user (run 1–6):
```
Sinh 3 test condition (mỗi dòng 1 condition, có giá trị cụ thể) cho yêu cầu dưới đây.
<SRS>
REQ-SF-03: Số lượng mỗi sản phẩm trong giỏ từ 1 đến 10. Tiêu chí chấp nhận: nhập số lượng < 1 hoặc > 10 thì hệ thống không chấp nhận và hiển thị thông báo.
</SRS>
```
E2 – user (run 7 có khối `<SRS>…</SRS>` như trên đặt trước câu hỏi; run 8 chỉ có câu hỏi):
```
Theo SRS của website SM-WEB, khách được đặt tối đa bao nhiêu sản phẩm cùng loại trong giỏ và vượt giới hạn thì hệ thống làm gì?
```

## Thay đổi so với notebook mẫu
- Thêm `reasoning_effort = "none"` vào biến cố định của `F1_variability.py`. Lý do: Gemini 3.x là model "thinking", token suy nghĩ tính vào `max_tokens` = 400 nên output bị cắt sau khoảng 16 token (finish_reason = length). Tắt thinking để cả 400 token dành cho câu trả lời; tham số này giữ cố định cho cả 8 lần chạy và được ghi trong `f1_runs.csv`.
- Chọn `gemini-3.5-flash`: `gemini-2.5-flash` trả 404 ("no longer available to new users"), `gemini-3.8-flash` và `gemini-flash-latest` trả 503/timeout tại thời điểm chạy.

