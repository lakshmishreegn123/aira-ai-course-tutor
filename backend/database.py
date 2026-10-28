import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "aira.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS sessions (
        session_id TEXT PRIMARY KEY,
        created_at TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        latency_ms INTEGER,
        tokens_used INTEGER
    );

    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        message_id INTEGER,
        rating TEXT NOT NULL,
        timestamp TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS test_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        category TEXT,
        expected TEXT,
        actual TEXT,
        correct INTEGER,
        latency_ms INTEGER,
        run_at TEXT
    );
    """)
    conn.commit()
    conn.close()


def now():
    return datetime.now().isoformat(timespec="seconds")


def ensure_session(session_id):
    conn = get_connection()
    conn.execute(
        "INSERT OR IGNORE INTO sessions (session_id, created_at) VALUES (?, ?)",
        (session_id, now()),
    )
    conn.commit()
    conn.close()


def log_message(session_id, role, content, latency_ms=None, tokens_used=None):
    conn = get_connection()
    conn.execute(
        "INSERT INTO messages (session_id, role, content, timestamp, latency_ms, tokens_used) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (session_id, role, content, now(), latency_ms, tokens_used),
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    conn = get_connection()
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    conn.close()
    print("Database ready at", DB_PATH)
    print("Tables:", [r[0] for r in rows])