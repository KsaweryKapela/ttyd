from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import get_connection
from model_handler import infere_model


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
    try:
        with get_connection() as connection:
            result_proxy = connection.execute(body.query)
            results = result_proxy.fetchall()
            columns = result_proxy.keys()  # Get column names
            response = {"headers": columns, "data": [dict(row) for row in results]}
            return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


class PromptBody(BaseModel):
    ddl: str
    prompt: str

@app.post("/prompt")
async def prompt(body: PromptBody):
    model_response = infere_model(body.ddl, body.prompt)
    response = {"query":model_response}
    return response
