"""Client LLM dùng chung cho khóa học (Gemini hoặc Groq qua endpoint tương thích OpenAI).

Cài đặt:  pip install openai
Biến môi trường (Colab: dùng Secrets; máy cá nhân: file .env – KHÔNG commit):
  LLM_PROVIDER = gemini | groq      (mặc định gemini)
  GEMINI_API_KEY / GROQ_API_KEY
  LLM_MODEL    = tên model (xem trang models của nhà cung cấp; ví dụ bản Flash của Gemini)
Chỉ gửi dữ liệu công khai / hư cấu (SM-WEB) / giả. Gemini free tier (https://ai.google.dev/gemini-api/terms): nội dung gửi và phản hồi có thể được Google dùng để cải thiện sản phẩm và người review có thể đọc -> không gửi thông tin nhạy cảm, bí mật, cá nhân.
"""
import os, time, random, csv, datetime as dt
from openai import OpenAI

BASES = {"gemini": "https://generativelanguage.googleapis.com/v1beta/openai/",
         "groq": "https://api.groq.com/openai/v1"}
KEYS = {"gemini": "GEMINI_API_KEY", "groq": "GROQ_API_KEY"}

class BudgetExceeded(Exception):
    pass

class Budget:
    """Guardrail ngân sách token cho một phiên làm việc."""
    def __init__(self, max_tokens=200_000, warn_ratio=0.8):
        self.max, self.used, self.warn_ratio, self.warned = max_tokens, 0, warn_ratio, False
    def add(self, n):
        self.used += n
        if not self.warned and self.used >= self.max * self.warn_ratio:
            print(f"[CẢNH BÁO] đã dùng {self.used}/{self.max} token"); self.warned = True
        if self.used > self.max:
            raise BudgetExceeded(f"Vượt ngân sách: {self.used} > {self.max} token")

class LLM:
    def __init__(self, provider=None, model=None, budget=None, log_file="llm_calls.csv",
                 price_in_per_m=0.0, price_out_per_m=0.0, min_interval_s=4.0):
        self.provider = provider or os.getenv("LLM_PROVIDER", "gemini")
        self.model = model or os.getenv("LLM_MODEL")
        if not self.model:
            raise ValueError("Đặt LLM_MODEL (tên model của nhà cung cấp)")
        self.client = OpenAI(api_key=os.environ[KEYS[self.provider]], base_url=BASES[self.provider])
        self.budget = budget or Budget()
        self.log_file, self.pin, self.pout = log_file, price_in_per_m, price_out_per_m
        self.min_interval, self._last = min_interval_s, 0.0   # giới hạn tốc độ gọi (RPM)

    def chat(self, messages, temperature=0.0, max_tokens=1024, tries=5, **kw):
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        for i in range(tries):
            wait = self.min_interval - (time.time() - self._last)
            if wait > 0: time.sleep(wait)
            self._last = time.time()
            try:
                r = self.client.chat.completions.create(model=self.model, messages=messages,
                        temperature=temperature, max_tokens=max_tokens, **kw)
                u = r.usage
                tin, tout = (u.prompt_tokens, u.completion_tokens) if u else (0, 0)
                self.budget.add(tin + tout)
                self._log(tin, tout)
                return r.choices[0].message.content
            except BudgetExceeded:
                raise
            except Exception as e:  # 429/5xx: backoff có giới hạn
                msg = str(e)
                retryable = any(c in msg for c in ("429", "500", "502", "503", "504", "timeout", "Timeout"))
                if not retryable or i == tries - 1:
                    raise
                time.sleep(2 ** i + random.random())

    def _log(self, tin, tout):
        new = not os.path.exists(self.log_file)
        with open(self.log_file, "a", newline="") as f:
            w = csv.writer(f)
            if new: w.writerow(["time", "provider", "model", "tokens_in", "tokens_out", "cost_usd_equiv"])
            w.writerow([dt.datetime.now().isoformat(timespec="seconds"), self.provider, self.model, tin, tout,
                        round(tin / 1e6 * self.pin + tout / 1e6 * self.pout, 6)])
