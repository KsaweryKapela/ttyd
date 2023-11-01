from fastapi import HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
import gc
from transformers import AutoTokenizer, LlamaForCausalLM
from common import *
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Ignore if not installed, hope it's in the env already :P

app = FastAPI()

model_directory = "/home/ksaff/Desktop/ttyd/query_llama"
tokenizer = AutoTokenizer.from_pretrained(model_directory)
model = LlamaForCausalLM.from_pretrained(model_directory,
                                        load_in_8bit=True,
                                        device_map={'': 0})

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
    gc.collect()
    torch.cuda.empty_cache()
    prompt_2 = 'Make SQLite query based on DDL and instruction.'
    text = (
        prompt_2
        + '### Instruction:\n'
        + prompt
        + '### Input:\n'
        + ddl
        + '### Response:\n'
    )

    input_ids = tokenizer.encode(text, return_tensors='pt')
    input_ids = input_ids.to('cuda')
    output = model.generate(input_ids, max_length=1000, temperature=0.3, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    match = re.search(r'### Response:\s*(.*)', generated_text)
    response = match.group(1)
    return response

@app.post("/prompt")
async def prompt(body: PromptBody):
    ddl = body.ddl
    prompt = body.prompt
    query = body.query
    print(body)
    result = infere_model(ddl, prompt, query)
    return result

@app.get("/tables")
async def get_tables():
    return tables

@app.post('/ddl')
async def get_ddl(q: str):
    if not q in tables:
        raise HTTPException(status_code=404, detail="Table not found!", )

    c.execute(f"pragma table_info('{q}');")
    result = c.fetchall()
    result.insert(
        0,
        [
            "ID",
            "NAME",
            "TYPE",
            "REQUIRED",
            "UNIQ",
            "AUTO_INCREMENT"
        ]
    )

    return result
