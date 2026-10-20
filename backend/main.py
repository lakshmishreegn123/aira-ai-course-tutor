import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url=os.getenv("LLM_BASE_URL"), api_key=os.getenv("LLM_API_KEY"))
MODEL = os.getenv("LLM_MODEL")

# Read the notes file (the "recipe book")
ROOT = Path(__file__).resolve().parent.parent
NOTES = (ROOT / "knowledge" / "knowledge.md").read_text(encoding="utf-8")

# AIRA's "job description"
SYSTEM_PROMPT = f"""You are AIRA, a friendly senior-student tutor for BCS515B
(Artificial Intelligence). Explain briefly and clearly, give one simple example,
and end by offering a practice question.

SCOPE: Answer only BCS515B and AI-fundamentals topics covered in the notes below.
If asked anything else, politely decline and say what you can help with.

HONESTY: If the answer is not in the notes, say "I don't have that in my notes."
Do not guess.

SAFETY: For assignment questions, give the concept and a hint, never the final
answer. For marks, attendance or grades, tell the student to ask the faculty.

NOTES:
{NOTES}
"""

app = FastAPI()
sessions = {}   # remembers each chat's messages

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/api/chat")
def chat(req: ChatRequest):
    text = req.message.strip()
    if not text:
        return {"reply": "Please type a question first."}

    history = sessions.setdefault(req.session_id, [])
    history.append({"role": "user", "content": text})

    # Job description + only the last 8 messages = "memory"
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history[-8:]
    try:
        r = client.chat.completions.create(model=MODEL, messages=messages)
        reply = r.choices[0].message.content
    except Exception:
        history.pop()
        return {"reply": "Sorry, I couldn't reach the AI service. Please try again."}

    history.append({"role": "assistant", "content": reply})
    return {"reply": reply}

# Show the chat page from the frontend folder (we create it in Stage 6)
app.mount("/", StaticFiles(directory=ROOT / "frontend", html=True), name="frontend")