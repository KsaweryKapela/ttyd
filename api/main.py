from fastapi import FastAPI
from common import *

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hello World"}

@app.post("/query")
async def data(q: str):
    return c.execute(f"{q}").fetchall()
