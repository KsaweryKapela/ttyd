import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
conn = sqlite3.connect(os.environ.get('SQLITE_PATH'))
c = conn.cursor()
