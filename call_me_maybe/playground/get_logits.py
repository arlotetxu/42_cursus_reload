import numpy as np
from icecream import ic

from llm_sdk import Small_LLM_Model

ic.configureOutput(includeContext=True)

my_model = Small_LLM_Model()
my_prompt = "Este es mi maravilloso prompt de test"

vocab_path = my_model.get_path_to_vocab_file()
print(f"Ruta vocabulario: {vocab_path}\n")

encoded_prompt_tensor = my_model.encode(my_prompt)  # Esto es un torch.Tensor
input_ids_list = encoded_prompt_tensor[0].tolist()  # Extrae la lista de IDs del tensor
next_token_logits_list = my_model.get_logits_from_input_ids(input_ids_list)  # Llama a la función con la lista de IDs
output_logits = np.array(next_token_logits_list)  # Convierte la lista de logits a un array de NumPy
ic(output_logits)
