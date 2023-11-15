from transformers import AutoTokenizer
import re
from peft import AutoPeftModelForCausalLM

model_directory = '/opt/api/model'
model = AutoPeftModelForCausalLM.from_pretrained(model_directory,
                                        load_in_8bit=True,
                                        device_map={'': 0})
tokenizer = AutoTokenizer.from_pretrained(model_directory)

def clean_DDL(DDL):
    lines = DDL.split('\n')
    modified_text = "DDL: "
    for line in lines:
        if len(line) < 2:
            pass
        elif '/*' in line:
            pass
        elif 'DROP TABLE' in line:
            pass

        else:
            line = re.sub(r'(?<!NOT )\bNULL\b', '', line)
            modified_text += f'{line}\n'
            
    return modified_text

def infere_model(ddl, prompt):
    # ddl = clean_DDL(ddl)
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
    inputs = {
    'input_ids': input_ids,
    'max_length': 1000
    }
    output = model.generate(**inputs)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    match = re.search(r"### Response:\s*(.+?);", generated_text)
    response = match.group(1)
    print(response)
    return response