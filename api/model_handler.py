import torch
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from langchain import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, pipeline
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def load_llm():
    model_id = "codellama/CodeLlama-34b-hf"

    peft_model_id = "/home/ksaff/Desktop/ttyd/fine_tuning/2nd_try"
    config = PeftConfig.from_pretrained(peft_model_id)

    bnb_config = BitsAndBytesConfig(
                                    load_in_4bit=True,
                                    bnb_4bit_use_double_quant=True,
                                    bnb_4bit_quant_type="nf4",
                                    bnb_4bit_compute_dtype=torch.bfloat16
                                    )

    model = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path,
        return_dict=True,
        quantization_config=bnb_config, device_map={'': 0}
    )
    tokenizer = AutoTokenizer.from_pretrained(
                                            config.base_model_name_or_path,
                                            )

    generation_config = GenerationConfig.from_pretrained(model_id)
    generation_config.max_new_tokens = 1024
    generation_config.max_time = 3
    generation_config.pad_token_id = 2
    
    text_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        generation_config=generation_config,
    )
    
    llm = HuggingFacePipeline(pipeline=text_pipeline)
    return llm

def create_prompt(question):
    database_scheme = """
                         CREATE TABLE Salaries
                         Id INTEGER PRIMARY KEY, -- Unique ID for each employee
                         EmployeeName VARCHAR, -- Name of the employee
                         JobTitle VARCHAR, -- Name of employees proffesion
                         BasePay NUMERIC, -- Base pay of employee
                         OvertimePay NUMERIC, -- Overtime pay of employee
                         OtherPay NUMERIC, -- Other pays of employee
                         Benefits NUMERIC, -- Benefits of employee
                         TotalPay NUMERIC, -- Total pay of employee
                         TotalPayBenefits NUMERIC, -- Sum of pay benefits of employee
                         Year INTEGER, -- Year data from row reffers to
                      """
    text = (
            f"""
            ### Task
            Generate a SQL query to answer the following question:
            {question}
            ### Database Schema
            This query will run on a database whose schema is represented in this string:""" 
            +
            database_scheme
            +
            f"""
            ### SQL
            Given the database schema, here is the SQL query that answers `{question}`:
            ```sql
            """
    )
    return text

def setup_conversation_buff(llm):
    memory = ConversationBufferMemory()
    conversation_buf = ConversationChain(
        llm=llm,
        memory=memory)
    return conversation_buf

def do_query(question, conversation):
    text = create_prompt(question)
    response = conversation(text)
    print(f'question - {question}')
    print(response)
    raw_query = response['response'].split("```")[-2].replace('sql', '')
    return response['response']