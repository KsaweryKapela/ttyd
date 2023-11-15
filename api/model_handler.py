from transformers import AutoTokenizer
import re
from peft import AutoPeftModelForCausalLM


model_directory = '/opt/api/model'
model = AutoPeftModelForCausalLM.from_pretrained(model_directory,
                                        load_in_8bit=True,
                                        device_map={'': 0})
tokenizer = AutoTokenizer.from_pretrained(model_directory)

def infere_model(ddl, prompt):
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