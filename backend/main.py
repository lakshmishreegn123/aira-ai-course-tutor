import os
import time
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import (
    OpenAI,
    APITimeoutError,
    RateLimitError,
    APIConnectionError,
    InternalServerError,
)

from backend.database import init_db, ensure_session, log_message, get_history

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    timeout=25.0,
    max_retries=0,
)
MODEL = os.getenv("LLM_MODEL")
FALLBACK_MODEL = os.getenv("LLM_FALLBACK_MODEL")

ROOT = Path(__file__).resolve().parent.parent
NOTES = (ROOT / "knowledge" / "knowledge.md").read_text(encoding="utf-8")

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


def ask_llm(messages):
    models = [MODEL]
    if FALLBACK_MODEL and FALLBACK_MODEL != MODEL:
        models.append(FALLBACK_MODEL)

    for i, model_name in enumerate(models):
        try:
            return client.chat.completions.create(model=model_name, messages=messages)
        except (InternalServerError, RateLimitError, APITimeoutError) as e:
            print("Model problem with", model_name, "->", type(e).__name__)
            if i == len(models) - 1:
                raise


app = FastAPI()
init_db()
sessions = {}


class ChatRequest(BaseModel):
    session_id: str
    message: str


@app.get("/api/health")
def health():
    return {"status": "AIRA backend is running"}


@app.post("/api/chat")
def chat(req: ChatRequest):
    text = req.message.strip()
    if not text:
        return {"reply": "Please type a question first."}
    if len(text) > 1000:
        return {"reply": "That message is too long. Please keep it under 1000 characters."}

    ensure_session(req.session_id)
    history = sessions.setdefault(req.session_id, [])
    history.append({"role": "user", "content": text})
    log_message(req.session_id, "user", text)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history[-8:]

    start = time.time()
    try:
        r = ask_llm(messages)
        reply = r.choices[0].message.content
    except APITimeoutError:
        history.pop()
        return {"reply": "AIRA is taking too long to answer. Please try again in a moment."}
    except RateLimitError:
        history.pop()
        return {"reply": "Too many questions right now. Please wait a minute and try again."}
    except InternalServerError:
        history.pop()
        return {"reply": "The AI service is busy right now. Please try again in a minute."}
    except APIConnectionError:
        history.pop()
        return {"reply": "I can't reach the AI service. Please check your internet connection."}
    except Exception as e:
        print("LLM ERROR:", repr(e))
        history.pop()
        return {"reply": "Something went wrong on my side. Please try again."}

    latency_ms = int((time.time() - start) * 1000)
    tokens = r.usage.total_tokens if r.usage else None

    history.append({"role": "assistant", "content": reply})
    log_message(req.session_id, "assistant", reply, latency_ms, tokens)
    return {"reply": reply, "latency_ms": latency_ms}


@app.get("/api/history/{session_id}")
def get_chat_history(session_id: str):
    return {"session_id": session_id, "messages": get_history(session_id)}


@app.post("/api/reset/{session_id}")
def reset_chat(session_id: str):
    sessions.pop(session_id, None)
    return {"status": "Conversation memory cleared"}


app.mount("/", StaticFiles(directory=ROOT / "frontend", html=True), name="frontend")