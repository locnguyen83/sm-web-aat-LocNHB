# F1-3 - Kết luận (LocNHB, 2026-11-13)

Biến cố định: gemini-3.5-flash (Gemini API, Colab), PR-F1-001 v1.0, REQ-SF-03, max_tokens 400, top_p 0.95, reasoning_effort none, không dùng seed.

1. Ở temperature 0, 3 lần chạy cho 3 output khác nhau (3 hash khác nhau): cùng tập giá trị 0 / 5 / 11 nhưng khác thứ tự, định dạng và cách diễn đạt; run 2 còn ghi sai "11 (số lượng > 1)" - temperature 0 không bảo đảm deterministic.
2. Ở temperature 1, 3 lần chạy cũng khác nhau về diễn đạt nhưng tập condition không đổi (0 / 5 / 11); với prompt hẹp có SRS kèm theo, temperature ảnh hưởng tới câu chữ nhiều hơn tới nội dung.
3. Cả 6 lần E1 đều bỏ sót giá trị biên 1 và 10, nên output AI chưa đủ để thay thế phân tích giá trị biên của tester.
4. E2: có đoạn SRS thì trả lời đúng (tối đa 10, vượt thì không chấp nhận và hiển thị thông báo); không có SRS thì model trả lời "Không có trong tài liệu" - không có hallucination trong lần đo này, nhờ system prompt yêu cầu chỉ dựa trên tài liệu, nhưng cũng không trả lời được câu hỏi.
5. Hệ quả cho test oracle: không lấy expected result trực tiếp từ output AI; mọi expected phải đối chiếu SRS, cung cấp ngữ cảnh SRS trong prompt, và chấp nhận output thay đổi giữa các lần chạy.
