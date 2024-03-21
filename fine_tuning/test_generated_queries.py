import pandas as pd
import csv
import sqlite3
import pandas as pd

def execute_query(query):

    c.execute(query)
    result = c.fetchall()
    columns = [desc[0] for desc in c.description]
    response = {"query": query, "headers": columns, "data": result}

    return response

if __name__ == '__main__':

    i = 1

    conn = sqlite3.connect(f'/home/ksaff/Desktop/ttyd/fine_tuning/fine_tune_dbs/dbs/ddl{i}.db')
    c = conn.cursor()
    filename = f'/home/ksaff/Desktop/ttyd/fine_tuning/fine_tune_dbs/raw_query_pairs/fine_tune_raw_{i}.csv'
    data = []

    df = pd.read_csv(filename)

    error = 0
    hit = 0
    for i, row in df.iterrows():
        try:
            query = row[1]
            try:
                result = execute_query(query)
                hit += 1
                data.append(row.tolist())
            except Exception as e:
                print(query)
                error += 1

        except IndexError:
            print(i)
            continue

    print(f'Queries without error: {hit}, with error: {error}')

    filename = f'/home/ksaff/Desktop/ttyd/fine_tuning/fine_tune_dbs/final_query_pairs/fine_tune_raw_{i}.txt'

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)