from src.enums.enums import Colors
import numpy as np
from icecream import ic

from llm_sdk import Small_LLM_Model

ic.configureOutput(includeContext=True)

my_model = Small_LLM_Model()
# my_prompt = "2, 4, 8, 16, 32, "
my_prompt = (
    "<|im_start|>system\n"
    "You are an expert assistant. You have access to the following functions:"
    "["
    "{'name': 'fn_add_numbers', 'description': 'Add two numbers together and return their sum.', "
    "'parameters': {'a': {'type': 'number'}, 'b': {'type': 'number'}}, 'returns': {'type': 'number'}}, "
    "{'name': 'fn_greet', 'description': 'Generate a greeting message for a person by name.', "
    "'parameters': {'name': {'type': 'string'}}, 'returns': {'type': 'string'}}, "
    "{'name': 'fn_reverse_string', 'description': 'Reverse a string and return the reversed result.', "
    "'parameters': {'s': {'type': 'string'}}, 'returns': {'type': 'string'}}, "
    "{'name': 'fn_get_square_root', 'description': 'Calculate the square root of a number.', "
    "'parameters': {'a': {'type': 'number'}}, 'returns': {'type': 'number'}}, "
    "{'name': 'fn_substitute_string_with_regex', "
    "'description': 'Replace all occurrences matching a regex pattern in a string.', "
    "'parameters': {'source_string': {'type': 'string'}, 'regex': {'type': 'string'}, "
    "'replacement': {'type': 'string'}}, 'returns': {'type': 'string'}}"
    "] "
    "According to the user_input, you must respond exclusively in JSON format:"
    "-user_input as a field named \"prompt\""
    "-name of corresponding function mentioned before as a field named \"name\""
    "-parameters as a field named \"parameters\""
    "Nothing else. Do not returning values\n"
    "<|im_end|>\n"
    "<|im_start|>user\n"
    "user_input: What is the sum of 2 and 3?<|im_end|>\n"
    "<|im_start|>assistant\n"
    "{\n"
)

model_output_idxs = []

# vocab_path = my_model.get_path_to_vocab_file()
# print(f"Ruta vocabulario: {vocab_path}\n")

# Getting the EOS (End of sequence) ID to stop the loop. For our model: 151645
# ic(my_model._tokenizer.eos_token_id)

func_def = ['fn_add_numbers', 'fn_greet', 'fn_reverse_string', 'fn_get_square_root',
            'fn_substitute_string_with_regex']


encoded_prompt_tensor = my_model.encode(my_prompt)  # Esto es un torch.Tensor
encoded_prompt_list = encoded_prompt_tensor[0].tolist()  # Extrae la lista de IDs del tensor
ic(type(encoded_prompt_list[0]))
for i in range (200):
    next_token_logits_list = my_model.get_logits_from_input_ids(encoded_prompt_list)  # Llama a la función con la lista de IDs
    logits_array_np = np.array(next_token_logits_list) # Convierte la lista de logits a un array de NumPy. Mayor velocidad
    token_idx = int(np.argmax(logits_array_np))

    if token_idx == 151645:
        break
    for func in func_def:
        if model_output_idxs
    # Getting the next token (index with the highest value)
    # max_logit = float('-inf')
    # token_idx = 0
    # for index, prob in enumerate(next_token_logits_list):
    #     if prob > max_logit:
    #         max_logit = prob
    #         token_idx = index

model_output = my_model.decode(model_output_idxs)
print(f"{Colors.GREEN.value}Initial prompt: \n{Colors.RESET.value}{my_prompt}")
print(f"{Colors.GREEN.value}Model Output: \n{Colors.RESET.value}{model_output}")
