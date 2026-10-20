import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   # reads your .env file

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)

reply = client.chat.completions.create(
    model=os.getenv("LLM_MODEL"),
    messages=[{"role": "user", "content": "Say hello in one line."}],
)
print(reply.choices[0].message.content)