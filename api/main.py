from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import execute_query
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

@app.get("/health")
async def healthcheck():
    return {"status": "ok"}

class QueryBody(BaseModel):
    query: str

@app.post("/query")
async def data(body: QueryBody):
    # try:
    columns, results = execute_query(body.query)
    response = {"headers": columns, "data": results}
    return response
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail=str(e))


class PromptBody(BaseModel):
    ddl: str
    prompt: str

@app.post("/prompt")
async def prompt(body: PromptBody):
    model_response = infere_model(body.ddl, body.prompt)
    response = {"query":model_response}
    return response
