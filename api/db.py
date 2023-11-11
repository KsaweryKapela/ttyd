from sqlalchemy import create_engine, text
import os

DB_PATH = os.environ.get('DB_PATH')
DATABASE_URL = f"sqlite:///{DB_PATH}"

def get_engine():
    engine = create_engine(DATABASE_URL)
    return engine

def get_connection():
    engine = get_engine()
    connection = engine.connect()
    return connection

def execute_query(query):
    with get_connection() as connection:
        result_proxy = connection.execute(text(query))
        results = result_proxy.fetchall()
        columns = result_proxy.keys()
        return columns, results