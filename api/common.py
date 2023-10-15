import sqlite3
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Ignore if not installed, hope it's in the env already :P

try:
    conn = sqlite3.connect(os.environ.get('SQLITE_PATH'))
    c = conn.cursor()
except Exception as e:
    print("So there probablt is actually not set ENV variable SQLITE_PATH, or the path is wrong.")
    print(f"Error: {e}")

tables = [item for sublist in c.execute(
    "SELECT name FROM sqlite_master WHERE type='table';").fetchall() for item in sublist]
