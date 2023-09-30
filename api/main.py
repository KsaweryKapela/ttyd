from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
# from common import *
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": f"Hello World{os.environ.get('SQLITE_PATH')}"}

@app.post("/query")
async def data(q: str):
    return c.execute(f"{q}").fetchall()


class PromptBody(BaseModel):
    ddl: Union[str, None]
    prompt: str
    query: str

class QueryBody(BaseModel):
    query: str

def read_ddl_from_db():
    pass

def infere_model(ddl, prompt, query):
    pass

def execute_query(query):
    pass

@app.post("/mock_prompt")
async def prompt(body: PromptBody):
    ddl = body.ddl
    prompt = body.prompt
    query = body.query
    if ddl is None:
        ddl = read_ddl_from_db()
    print(body)
    result = infere_model(ddl, prompt, query)

    response = { 
        "query":
    """ SELECT AVG(P_96) AS
        SREDNIA_WARTOSC_FAKTURY
        FROM VAT_SPRZEDAZ
        WHERE DOWOD_SPRZEDAZY LIKE
        '%FV%' AND P_96 > 1000; """
    }
    return response

@app.post("/mock_query")
async def query(body: QueryBody):
    print(body)
    result = execute_query(body.query)
    response = {"headers": ["SREDNIA_WARTOSC_FAKTURY", "DRUGI HEADER"], "data": [[1234.56, 1234.56], [56, 56]]}
    return response

