import sqlite3

def init_db():
    conn = sqlite3.connect("botdata.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS profit(user_id INTEGER, number INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS logs(user_id INTEGER, input TEXT, output TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    conn.close()

def set_profit_numbers(user_id, numbers):
    conn = sqlite3.connect("botdata.db")
    c = conn.cursor()
    c.execute("DELETE FROM profit WHERE user_id = ?", (user_id,))
    for n in numbers:
        c.execute("INSERT INTO profit(user_id, number) VALUES (?, ?)", (user_id, n))
    conn.commit()
    conn.close()

def get_profit_numbers(user_id):
    conn = sqlite3.connect("botdata.db")
    c = conn.cursor()
    c.execute("SELECT number FROM profit WHERE user_id = ?", (user_id,))
    rows = c.fetchall()
    conn.close()
    return [r[0] for r in rows] if rows else []

def log_prediction(user_id, input_nums, output_nums):
    conn = sqlite3.connect("botdata.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs(user_id, input, output) VALUES (?, ?, ?)",
              (user_id, str(input_nums), str(output_nums)))
    conn.commit()
    conn.close()
