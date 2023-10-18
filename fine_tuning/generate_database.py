import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

sql_files_dir = os.environ.get('SQL_FILES_PATH')

# Create an SQLite database
conn = sqlite3.connect('EngFinDB.db')
cursor = conn.cursor()

# List of SQL files in the specified order
sql_files = [
    'ddl.sql',
    '1_jpk_header.sql',
    '2_jpk_entity.sql',
    '3_vat_sale.sql',
    '4_vat_purchase.sql',
]

# Execute each SQL file
for file_name in sql_files:
    with open(os.path.join(sql_files_dir, file_name), 'r', encoding='utf-8') as f:
        sql_script = f.read()
        try:
            cursor.executescript(sql_script)
            conn.commit()
            print(f"Executed {file_name} successfully.")
        except Exception as e:
            print(f"Error executing {file_name}: {e}")
            conn.rollback()

# Close the connection
conn.close()