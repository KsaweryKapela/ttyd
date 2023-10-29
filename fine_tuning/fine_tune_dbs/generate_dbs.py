import os
import sqlite3

ddls_folder = '/home/ksaff/Desktop/ttyd/fine_tuning/fine_tune_dbs/ddls'

for ddl_file in os.listdir(ddls_folder):
    if ddl_file.endswith('.sql'):
        with open(os.path.join(ddls_folder, ddl_file), 'r') as f:
            ddl_statements = f.read()

        db_name = f"{ddl_file.split('.')[0]}.db"
        
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.executescript(ddl_statements)
        conn.commit()
        conn.close()