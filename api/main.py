from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
from model_handler import setup_conversation_buff, do_query, load_llm
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session, sessionmaker
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
import os

if not os.environ.get("DOCKERIZED"):
    from dotenv import load_dotenv
    load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

DB_PATH = os.environ.get("DB_PATH")
API_PATH = os.environ.get("API_PATH")

DATABASE_URL = f"sqlite:////{DB_PATH}"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

templates = Jinja2Templates(directory=f"{API_PATH}templates")
app.mount("/static", StaticFiles(directory=f"{API_PATH}static"), name="static")

llm = load_llm()

class QueryRequest(BaseModel):
    user_query: str

class SQLQuery(BaseModel):
    sql_query: str

class ConversationManager:
    _instance = None
    _is_initialized = False

    def __init__(self, llm):
        if not ConversationManager._is_initialized:
            self.conversation_chain = setup_conversation_buff(llm)
            ConversationManager._is_initialized = True

    @classmethod
    def get_conversation_chain(cls, llm=None):
        if cls._instance is None:
            if llm is None:
                raise ValueError("LLM must be provided for the first initialization of ConversationManager.")
            cls._instance = cls(llm)
        return cls._instance.conversation_chain

    @classmethod
    def reset_instance(cls):
        if cls._is_initialized:
            cls._instance = None
            cls._is_initialized = False
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    ConversationManager.reset_instance()
    return templates.TemplateResponse(request, "index.html")

@app.post("/convert-query")
async def convert_query(query_request: QueryRequest, request: Request):
    user_query = query_request.user_query

    conversation_buff = ConversationManager.get_conversation_chain(llm)

    sql_query = do_query(question=user_query, conversation=conversation_buff)
    return JSONResponse(content={"sql_query": sql_query})

@app.post("/execute-query")
async def execute_query(sql_query: SQLQuery, db: Session = Depends(get_db)):
    try:
        result = db.execute(text(sql_query.sql_query))
        rows = result.fetchall()

        if len(rows) > 1001:
            rows = rows[:1000]
            
        columns = result.keys()
        results = [dict(zip(columns, row)) for row in rows]
        print(results)
        return JSONResponse(content={"query_result": results})
    
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

if not os.environ.get("DOCKERIZED"):
    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info", reload=False)