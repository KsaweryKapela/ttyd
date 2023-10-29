import pandas as pd
import csv
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

i = 7
# conn = sqlite3.connect(os.environ.get('SQLITE_PATH'))
conn = sqlite3.connect(f'/home/ksaff/Desktop/ttyd/fine_tuning/fine_tune_dbs/dbs/ddl{i}.db')
c = conn.cursor()

def execute_query(query):

    c.execute(query)
    result = c.fetchall()

    # Extract column names
    columns = [desc[0] for desc in c.description]
    
    # Prepare the response
    response = {"query": query, "headers": columns, "data": result}

    return response



# filename = os.environ.get('FINETUNE_RAW_CSV_PATH')
filename = f'/home/ksaff/Desktop/ttyd/fine_tuning/llama_finetuning/10_datasets/fine_tune_raw_{i}.csv'

data = []

with open(filename, 'r') as f:
    error = 0
    hit = 0
    i2 = 0
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        i2 += 1
        try:
            query = row[1]
        except IndexError:
            print(i2)
            continue
        try:
            result = execute_query(query)
            hit += 1
            data.append(row)
        except Exception as e:
            print(query)
            print(e)
            error += 1


print(f'Queries without error: {hit}, with error: {error}')

# OPTIONAL, CHANGES CSV TO ONE WITHOUT BUGS

filename = f'/home/ksaff/Desktop/ttyd/fine_tuning/llama_finetuning/10_datasets/fine_tune_{i}.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)