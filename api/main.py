from fastapi import FastAPI
from common import *
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

@app.get("/")
async def root():
    return {"message": f"Hello World{os.environ.get('SQLITE_PATH')}"}

@app.post("/query")
async def data(q: str):
    return c.execute(f"{q}").fetchall()
