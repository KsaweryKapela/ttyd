import csv
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()
conn = sqlite3.connect(os.environ.get('SQLITE_PATH'))
c = conn.cursor()

def execute_query(query):
    print(query)

    c.execute(query)
    result = c.fetchall()

    # Extract column names
    columns = [desc[0] for desc in c.description]
    
    # Prepare the response
    response = {"query": query, "headers": columns, "data": result}

    return response

filename = ''
with open(filename, 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        query = row[1]
        result = execute_query(query)
        print(result)