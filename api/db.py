from sqlalchemy import create_engine
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
