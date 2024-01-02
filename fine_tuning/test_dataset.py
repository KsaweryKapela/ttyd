import pandas as pd
import csv
import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

i = 9
# conn = sqlite3.connect(os.environ.get('SQLITE_PATH'))
# conn = sqlite3.connect(f'/home/ksaff/Desktop/ttyd/fine_tuning/fine_tune_dbs/dbs/ddl{i}.db')
conn = sqlite3.connect(f'/home/ksaff/Desktop/sql/choosen_DB.sqlite')
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
# filename = f'/home/ksaff/Desktop/ttyd/fine_tuning/llama_finetuning/10_datasets/fine_tune_raw_{i}.csv'
filename = r'/home/ksaff/Desktop/sql/queries.xlsx'
data = []

# Read the Excel file
df = pd.read_excel(filename)

# Iterate through rows
error = 0
hit = 0
for i, row in df.iterrows():
    try:
        query = row[1]  # Assuming the query is in the second column


        # Execute your query and append results
        try:
            result = execute_query(query)  # Make sure execute_query is defined
            hit += 1
            data.append(row.tolist())
        except Exception as e:
            print(query)
            # print(e)
            # print(i)
            error += 1

    except IndexError:
        print(i)
        continue

print(f'Queries without error: {hit}, with error: {error}')

# OPTIONAL, CHANGES CSV TO ONE WITHOUT BUGS

# filename = f'/home/ksaff/Desktop/ttyd/fine_tuning/llama_finetuning/10_datasets/fine_tune_{i}.csv'
filename = r'/home/ksaff/Desktop/sql/no_err_queries.txt'

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)