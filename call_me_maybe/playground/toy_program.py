from src.enums.enums import Colors
import numpy as np
from icecream import ic

from llm_sdk import Small_LLM_Model

ic.configureOutput(includeContext=True)

my_model = Small_LLM_Model()
# my_prompt = "2, 4, 8, 16, 32, "
my_prompt = "What is your n"
# my_prompt = "{\"name\": \"fn_add_numbers\",\"description\": \"Add two numbers tog"
model_output = ""

vocab_path = my_model.get_path_to_vocab_file()
print(f"Ruta vocabulario: {vocab_path}\n")

# Getting the EOS (End of sequence) ID to stop the loop. For our model: 151645
ic(my_model._tokenizer.eos_token_id)

encoded_prompt_tensor = my_model.encode(my_prompt)  # Esto es un torch.Tensor
encoded_prompt_list = encoded_prompt_tensor[0].tolist()  # Extrae la lista de IDs del tensor
for i in range (100):
    next_token_logits_list = my_model.get_logits_from_input_ids(encoded_prompt_list)  # Llama a la función con la lista de IDs
    # output_logits = np.array(next_token_logits_list)  # Convierte la lista de logits a un array de NumPy

    # Getting the next token (index with the highest value)
    max_logit = 0
    token_idx = 0
    for index, prob in enumerate(next_token_logits_list):
        if prob > max_logit:
            max_logit = prob
            token_idx = index
    if token_idx == 151645:
        break
    encoded_prompt_list.append(token_idx)
    model_output += my_model.decode([token_idx])
print(f"{Colors.GREEN.value}Initial prompt: \n{Colors.RESET.value}{my_prompt}")
print(f"{Colors.GREEN.value}Model Output: \n{Colors.RESET.value}{model_output}")
