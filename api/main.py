from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
from model_handler import setup_conversation_buff, do_query, load_llm
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session, sessionmaker
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

DATABASE_URL = "sqlite:///./choosen_DB.sqlite"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

templates = Jinja2Templates(directory="api/templates")
app.mount("/static", StaticFiles(directory="api/static"), name="static")

class QueryRequest(BaseModel):
    user_query: str

class SQLQuery(BaseModel):
    sql_query: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert-query")
async def convert_query(query_request: QueryRequest, request: Request):
    user_query = query_request.user_query
    context = request.session.get("context", [])
    
    if len(context) >= 3:
        context = [user_query]
    else:
        context.append(user_query)
    
    request.session["context"] = context

    conversation_buff = setup_conversation_buff(llm)
    sql_query = do_query(question=user_query, conversation=conversation_buff)

    return JSONResponse(content={"sql_query": sql_query})

@app.post("/execute-query")
async def execute_query(sql_query: SQLQuery, db: Session = Depends(get_db)):
    try:
        result = db.execute(text(sql_query.sql_query))
        rows = result.fetchall()
        columns = result.keys()
        results = [dict(zip(columns, row)) for row in rows]
        return JSONResponse(content=results)
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    llm = load_llm()
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
