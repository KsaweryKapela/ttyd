from fastapi import FastAPI
from common import *

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hello World"}

@app.post("/query")
async def data(q: str):
    return c.execute(f"{q}").fetchall()

@app.get("/translate")
async def translate(q: str):
    src_path=os.environ.get('TRANS_PATH')
    return os.popen(f"bash {src_path} {q}").read().replace("\n", "")
