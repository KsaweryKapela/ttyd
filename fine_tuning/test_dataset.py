import csv
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

conn = sqlite3.connect(os.environ.get('SQLITE_PATH'))
c = conn.cursor()

def execute_query(query):

    c.execute(query)
    result = c.fetchall()

    # Extract column names
    columns = [desc[0] for desc in c.description]
    
    # Prepare the response
    response = {"query": query, "headers": columns, "data": result}

    return response

filename = os.environ.get('FINETUNE_RAW_CSV_PATH')
data = []

with open(filename, 'r') as f:
    error = 0
    hit = 0
    i = 0
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        i += 1
        try:
            query = row[1]
        except IndexError:
            print(i)
            break
        try:
            result = execute_query(query)
            # print(query)
            # print(result)
            hit += 1
            data.append(row)
        except Exception as e:
            # print(row[1])
            # print(e)
            error += 1


print(f'Queries without error: {hit}, with error: {error}')

# OPTIONAL, CHANGES CSV TO ONE WITHOUT BUGS

filename = os.environ.get('FINETUNE_CSV_PATH')
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)