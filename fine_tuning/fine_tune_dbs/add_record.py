import os
import sqlite3

dbs_folder = '/home/ksaff/Desktop/ttyd/fine_tuning/fine_tune_dbs/dbs'

def insert_dummy_record(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()

    column_names = []
    values = []

    for col in columns:
        col_name = col[1]
        col_type = col[2].upper()
        col_not_null = col[3]
        col_pk = col[5]  # Primary Key flag (1 if PK, 0 otherwise)

        column_names.append(col_name)

        if col_pk:
            # For primary keys, inserting a unique numeric value
            values.append("1")
        elif col_type == 'TEXT':
            values.append("'dummy'")
        elif col_type == 'NUMERIC':
            values.append("1")
        elif col_not_null:
            # If column has NOT NULL constraint but is not TEXT or NUMERIC
            values.append("'UNKNOWN'")
        else:
            values.append("NULL")

    try:
        cursor.execute(f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({','.join(values)});")
    except sqlite3.IntegrityError:
        # If primary key conflict happens, try a larger unique number
        values[0] = "2"
        cursor.execute(f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({','.join(values)});")
        
for db_file in os.listdir(dbs_folder):
    if db_file.endswith('.db'):
        db_path = os.path.join(dbs_folder, db_file)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            try:
                insert_dummy_record(cursor, table_name)
            except sqlite3.IntegrityError as e:
                print(f"Failed to insert into {table_name} in {db_file}: {e}")
        
        conn.commit()
        conn.close()
