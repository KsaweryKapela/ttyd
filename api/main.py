from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from common import *
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Ignore if not installed, hope it's in the env already :P

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:5004"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryBody(BaseModel):
    query: str

@app.post("/query")
async def data(body: QueryBody):
    print(body)

    c.execute(body.query)
    result = c.fetchall()

    # Extract column names
    columns = [desc[0] for desc in c.description]
    
    # Prepare the response
    response = {"headers": columns, "data": result}

    return response

@app.get("/translate")
async def translate(q: str):
    src_path=os.environ.get('TRANS_PATH')
    return os.popen(f"bash {src_path} {q}").read().replace("\n", "")


class PromptBody(BaseModel):
    ddl: str
    prompt: str
    query: str

def infere_model(ddl, prompt, query):
    pass

@app.post("/mock_prompt")
async def prompt(body: PromptBody):
    ddl = body.ddl
    prompt = body.prompt
    query = body.query
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

@app.get("/tables")
async def get_tables():
    return tables

