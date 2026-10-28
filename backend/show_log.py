from database import get_connection

conn = get_connection()
rows = conn.execute(
    "SELECT id, role, substr(content, 1, 40), latency_ms, tokens_used, timestamp "
    "FROM messages ORDER BY id DESC LIMIT 6"
).fetchall()
conn.close()

for row in rows:
    print(row)