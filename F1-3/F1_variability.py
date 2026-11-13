"""Lab F1-3 – thí nghiệm biến thiên output và hallucination CÓ KIỂM SOÁT BIẾN (SM-WEB).

Chạy trên Google Colab (công cụ lab chính): !pip install openai ; đặt GEMINI_API_KEY, LLM_MODEL trong Colab Secrets.
Thiết kế (syllabus AAT v1.4, F1-3):
  - Giữ CỐ ĐỊNH: model/version, prompt (ID + version), input, max_tokens, top_p (và seed nếu provider hỗ trợ).
  - Mỗi thí nghiệm chỉ ĐỔI 1 BIẾN:
      E1: temperature 0 vs 1 – mỗi mức 3 lần (có ngữ cảnh SRS)           -> 6 lần
      E2: có / không có đoạn SRS làm ngữ cảnh (temperature 0) – câu hỏi dễ gây hallucination -> 2 lần
  - Tổng 8 lần chạy; ghi config + raw output vào f1_runs.csv và thư mục raw_ai_output/.
Lưu ý: temperature = 0 GIẢM biến thiên nhưng KHÔNG bảo đảm deterministic. Kết luận phải dựa trên kết quả đo.
Chỉ dùng dữ liệu hư cấu của SM-WEB (F3-1). Không in API key.
"""
import csv, datetime as dt, hashlib, os, pathlib
from llm_client import LLM

# ---- Biến cố định (ghi vào log mỗi lần chạy) ----
FIXED = {
    "model": os.getenv("LLM_MODEL", ""),             # ghi rõ tên + version model
    "prompt_id": "PR-F1-001 v1.0",
    "max_tokens": 400,
    "top_p": 0.95,
    # Gemini 3.x là model "thinking": token suy nghĩ tính vào max_tokens -> output bị cắt (finish=length).
    # Tắt thinking để 400 token dành cho câu trả lời; giữ cố định cho mọi lần chạy.
    "reasoning_effort": os.getenv("F1_REASONING_EFFORT", "none"),
    "seed": os.getenv("F1_SEED"),                    # tùy chọn: chỉ dùng nếu provider hỗ trợ tham số seed ; không hỗ trợ -> để trống
}

SRS_EXCERPT = (
    "REQ-SF-03: Số lượng mỗi sản phẩm trong giỏ từ 1 đến 10. "
    "Tiêu chí chấp nhận: nhập số lượng < 1 hoặc > 10 thì hệ thống không chấp nhận và hiển thị thông báo."
)
SYSTEM = "Bạn là tester. Chỉ dựa trên tài liệu được cung cấp; nếu tài liệu không có thông tin, trả lời 'Không có trong tài liệu'."
Q_E1 = "Sinh 3 test condition (mỗi dòng 1 condition, có giá trị cụ thể) cho yêu cầu dưới đây.\n<SRS>\n" + SRS_EXCERPT + "\n</SRS>"
Q_E2 = ("Theo SRS của website SM-WEB, khách được đặt tối đa bao nhiêu sản phẩm cùng loại trong giỏ "
        "và vượt giới hạn thì hệ thống làm gì?")

OUT_DIR = pathlib.Path("raw_ai_output"); OUT_DIR.mkdir(exist_ok=True)
LOG = "f1_runs.csv"
llm = LLM(log_file="f1_llm_calls.csv")   # log token theo từng lần gọi


def run(run_no, experiment, variable, temperature, with_ctx, user_msg):
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user_msg}]
    if experiment == "E2" and with_ctx:
        messages[1]["content"] = "<SRS>\n" + SRS_EXCERPT + "\n</SRS>\n" + Q_E2
    extra = {"top_p": FIXED["top_p"], "reasoning_effort": FIXED["reasoning_effort"]}
    if FIXED["seed"]:
        extra["seed"] = int(FIXED["seed"])
    text = llm.chat(messages, temperature=temperature, max_tokens=FIXED["max_tokens"], **extra)
    fname = OUT_DIR / f"run{run_no:02d}_{experiment}_t{temperature}_{'ctx' if with_ctx else 'noctx'}.txt"
    fname.write_text(text, encoding="utf-8")
    row = {"run": run_no, "experiment": experiment, "variable_changed": variable, **FIXED,
           "temperature": temperature, "with_srs_context": "Y" if with_ctx else "N",
           "datetime": dt.datetime.now().isoformat(timespec="seconds"),
           "raw_output_file": str(fname), "output_sha1": hashlib.sha1(text.encode()).hexdigest()[:10],
           "correct_vs_SRS": "", "hallucination": "", "observation": ""}   # 3 cột cuối: học viên tự điền
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(row)); new and w.writeheader(); w.writerow(row)
    print(f"[run {run_no}] {experiment} temp={temperature} ctx={with_ctx} sha1={row['output_sha1']} | {text[:150]!r}")


if __name__ == "__main__":
    n = 0
    for temp in (0.0, 1.0):            # E1: chỉ đổi temperature
        for _ in range(3):
            n += 1; run(n, "E1", "temperature", temp, True, Q_E1)
    for ctx in (True, False):          # E2: chỉ đổi có/không ngữ cảnh
        n += 1; run(n, "E2", "context", 0.0, ctx, Q_E2)
    print("\nĐáp án theo SRS (E2): tối đa 10; vượt giới hạn -> không chấp nhận và hiển thị thông báo.")
    print("So sánh cột output_sha1 giữa các lần cùng temperature: khác hash = output khác (kể cả ở temperature 0).")
    print("Điền correct_vs_SRS / hallucination / observation rồi chép sang 08_Templates/F1_Experiment_Log.csv.")
