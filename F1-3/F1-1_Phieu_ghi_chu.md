# Phiếu ghi chú F1-1 – Cơ chế sinh output của LLM – LocNHB

Học liệu: DataCamp "Large Language Models (LLMs) Concepts" – phần LLM hoạt động thế nào + hạn chế/hallucination; demo trainer F1-1. Ví dụ lấy từ thí nghiệm F1-3 (REQ-SF-03, gemini-3.5-flash, 2026-11-13).

| # | Khái niệm | Hiểu ngắn gọn | Ví dụ QA trên SM-WEB |
|---|---|---|---|
| 1 | Token | Đơn vị văn bản model đọc/sinh (mảnh từ, không phải từ). Chi phí, giới hạn và độ dài output đều tính theo token. | Prompt E1 tốn 118 token đầu vào, output 78–110 token (`f1_llm_calls.csv`). `max_tokens` = 400 giới hạn độ dài câu trả lời; với model "thinking", token suy nghĩ cũng tính vào đó nên output từng bị cắt sau ~16 token. |
| 2 | Context window | Lượng token tối đa model xem được trong một lần gọi (system + prompt + tài liệu kèm + output). Ngoài cửa sổ này model "không biết". | E2: khi đặt đoạn REQ-SF-03 vào prompt, model trả lời đúng "tối đa 10"; bỏ đoạn đó ra thì model không có thông tin SM-WEB để dựa vào. |
| 3 | Temperature / top-p | Điều chỉnh độ ngẫu nhiên khi chọn token tiếp theo: temperature thấp → chọn token xác suất cao; top-p giới hạn tập token được xét. | Temp 1 (run 4–6) vẫn ra tập giá trị 0 / 5 / 11 như temp 0 nhưng đổi thứ tự, định dạng, câu chữ. Giữ top-p 0.95 cố định để chỉ đo tác động của temperature. |
| 4 | Non-determinism | Cùng prompt, cùng tham số vẫn có thể ra output khác nhau; temperature 0 chỉ giảm chứ không loại bỏ biến thiên. | 3 lần ở temp 0 (run 1–3) cho 3 hash khác nhau; run 2 còn ghi sai "11 (số lượng > 1)". → Không dùng một lần chạy AI làm expected result cố định. |
| 5 | Hallucination | Model sinh nội dung nghe hợp lý nhưng không có căn cứ trong nguồn (bịa giới hạn, quy tắc, API…). | Rủi ro: hỏi "tối đa bao nhiêu sản phẩm" mà không kèm SRS, model có thể bịa (ví dụ mẫu: "99"). Ở lần đo này (run 8) model trả lời "Không có trong tài liệu" nhờ system prompt yêu cầu chỉ dựa trên tài liệu. |

**Áp dụng cho QA:** luôn kèm đoạn SRS/req ID trong prompt; đối chiếu mọi expected do AI đề xuất với SRS; ghi lại model, version, tham số để tái lập; kiểm tra AI có bỏ sót giá trị biên không (cả 6 lần E1 đều thiếu biên 1 và 10).

**Câu hỏi còn mở:** <học viên tự điền>
