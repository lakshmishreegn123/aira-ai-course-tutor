import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print("Base URL:", os.getenv("LLM_BASE_URL"))
print("Model:", os.getenv("LLM_MODEL"))
print("Key loaded:", bool(os.getenv("LLM_API_KEY")))

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    timeout=15.0,
    max_retries=0,
)

start = time.time()
try:
    reply = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[{"role": "user", "content": "Say hello in one line."}],
    )
    print("REPLY:", reply.choices[0].message.content)
except Exception as e:
    print("ERROR TYPE:", type(e).__name__)
    print("ERROR:", e)
print("Took", round(time.time() - start, 1), "seconds")