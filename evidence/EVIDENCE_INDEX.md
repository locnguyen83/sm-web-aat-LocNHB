# Evidence Index – SM-WEB – LocNHB

> Mục lục bằng chứng. Tiêu chí rubric không có bằng chứng truy được ở đây → 0 điểm (insufficient evidence). Mọi link phải mở được bởi mentor (commit/run/file trong repo).

| ID | Lab/Task | Loại (ảnh / request-response / log / CI run / file / commit) | Mô tả ngắn | Link/đường dẫn | REQ/CR | Tiêu chí rubric chứng minh | Tự làm / tái sử dụng (ghi nguồn) | Ngày |
|---|---|---|---|---|---|---|---|---|
| E-01 | F1-3 | File | Bảng config + 8 lần chạy, đánh giá đúng/sai so SRS | F1-3/F1_Experiment_Log.csv | REQ-SF-03 | Ghi đủ biến cố định / biến thay đổi | Tự làm (template 08_Templates) | 2026-11-13 |
| E-02 | F1-3 | Log | Log script: config, hash output từng lần chạy | F1-3/f1_runs.csv | REQ-SF-03 | Ghi đủ biến cố định / biến thay đổi | Sinh bởi F1_variability.py | 2026-11-13 |
| E-03 | F1-3 | Log | Token in/out từng lần gọi | F1-3/f1_llm_calls.csv | REQ-SF-03 | Ghi đủ biến cố định | Sinh bởi llm_client.py | 2026-11-13 |
| E-04 | F1-3 | File | Raw output nguyên bản 8 lần chạy (không sửa) | F1-3/raw_ai_output/ | REQ-SF-03 | Đủ raw output 8 lần chạy | Sinh bởi Gemini, chạy trên Colab | 2026-11-13 |
| E-05 | F1-3 | File | Prompt PR-F1-001 v1.0, tham số, quyết định, thay đổi so với notebook mẫu | F1-3/prompt_record.md | REQ-SF-03 | Ghi đủ biến; tuân thủ dữ liệu | Tự làm (template 08_Templates) | 2026-11-13 |
| E-06 | F1-3 | File | Kết luận dựa trên số đo | F1-3/F1-3_Ket_luan.md | REQ-SF-03 | Kết luận đúng, dựa trên số đo | Tự làm | 2026-11-13 |
| E-07 | F1-3 | File | Script đã chạy (có thêm reasoning_effort) | F1-3/F1_variability.py, F1-3/llm_client.py | – | Tái lập thí nghiệm | Tái sử dụng 10_Starter_Kit/common, có chỉnh sửa | 2026-11-13 |
| E-08 | F1-1 | File | Phiếu ghi chú 1 trang (5 khái niệm + ví dụ SM-WEB) | F1-3/F1-1_Phieu_ghi_chu.md | REQ-SF-03 | Nộp kèm F1-3 | Tự làm | 2026-11-13 |
| E-09 | F1-3 | Log | Nhật ký dùng AI / escalation | F3_AI_Usage_Escalation_Log.csv | – | Tuân thủ dữ liệu | Tự làm | 2026-11-13 |
| E-10 | F1-3 | File | Notebook Colab đã chạy 8 lần (kèm output cell; key đọc từ Colab Secrets, không lưu trong file) | F1-3/evidence/F1-3_LocNHB.ipynb | REQ-SF-03 | Chạy trên Colab; đủ raw output 8 lần chạy | Tự làm | 2026-11-13 |
| E-11 | F2-3 | File | Đánh giá output: schema, truy vết, hallucination, tái lập, 3 ca injection, bảng đo thời gian | F2-3/AI_Output_Evaluation.md | 10 REQ fixture | JSON hợp lệ; truy vết req ID; hallucination; injection; tái lập; đo thời gian | Tự làm (template 08_Templates) | 2026-11-16 |
| E-12 | F2-3 | File | Raw output 3 prompt × 3 lần chạy × 2 version (run1_/run2_/injection_* = v1.0; *_v1.1_* = v1.1) – không sửa | F2-3/raw_ai_output/ | 10 REQ fixture | JSON hợp lệ; tái lập; ≥ 3 ca injection | Sinh bởi Gemini, chạy trên Colab | 2026-11-18 |
| E-13 | F2-3 | Log | Token in/out từng lần gọi (v1.0, v1.1) | F2-3/f2_llm_calls.csv, F2-3/f2_llm_calls_v1.1.csv | – | Config đủ để tái lập | Sinh bởi llm_client.py | 2026-11-18 |
| E-18 | F2-3 | Log | Log validate của notebook: schema_errors, n_conditions, req_covered, suspected_hallucination, injection_markers, self_check | F2-3/run_log_v1.0.txt, F2-3/run_log_v1.1.txt | 10 REQ fixture | JSON hợp lệ (có log validate); hallucination; tái lập | Sinh bởi F2_prompt_chain.py | 2026-11-18 |
| E-19 | F2-3 | File | Bộ condition cuối sau review (26 condition, 0 lỗi schema, source_quote nguyên văn) + quyết định giữ/bổ sung/loại | F2-3/reviewed/conditions_final.json, F2-3/reviewed/review_decisions.md | 10 REQ fixture | Truy vết req ID; loại hallucination – bộ cuối không còn condition bịa | Tự làm (nền: run2 v1.1) | 2026-11-18 |
| E-20 | F2-3 | File | Bảng đo thời gian: thủ công 5 condition vs chuỗi prompt + review (start/end) | F2-3/time_log.md | REQ-SF-03, REQ-SF-12 | Bảng đo thời gian | Tự làm | 2026-11-18 |
| E-14 | F2-3 | File | Prompt record PR-F2-01/02/03 v1.0, tham số, quyết định, thay đổi so với notebook mẫu | F2-3/prompt_record.md | 10 REQ fixture | Config/version đủ để tái lập | Tự làm (template 08_Templates) | 2026-11-16 |
| E-15 | F2-3 | File | Prompt library v1 (ID, mục đích, version, định dạng output) | prompts/PROMPT_LIBRARY.md | – | Prompt library v1 | Tự làm (template T05) | 2026-11-16 |
| E-16 | F2-3 | File | Script chuỗi prompt + fixture đã chạy (có sửa path, reasoning_effort, max_tokens) | F2-3/F2_prompt_chain.py, F2-3/llm_client.py, F2-3/f2_fixtures/ | 10 REQ fixture | Tái lập | Tái sử dụng 10_Starter_Kit, có chỉnh sửa | 2026-11-16 |
| E-17 | F2-3 | File | Notebook Colab đã chạy chuỗi v1.0 (Cell 2) và v1.1 (Cell 4), gồm cả lần lỗi max_tokens 2000 và cell gỡ lỗi; key đọc từ Colab Secrets, không lưu trong file | F2-3/evidence/F2-3_LocNHB.ipynb | 10 REQ fixture | Notebook nộp kèm; tái lập | Tự làm | 2026-11-18 |

## Khai báo đóng góp cá nhân (đồ án/RP)
- Phần tái sử dụng từ lab (ghi lab nguồn): …
- Phần làm mới trong RP/đồ án: …
- Phần có trao đổi/giúp đỡ (ghi người, nội dung): …
