from icecream import ic
from llm_sdk import Small_LLM_Model
from src.validator.path_validator import PathValidator
from src.prompt.prompt import Prompt
from typing import List, Dict
import numpy as np
from numpy.typing import NDArray
import json


ic.configureOutput(includeContext=True)


def put_name_mask(
    selected_func_name: str,
    func_names: List[str],
    vocab_dict: Dict,
    prompt_logits_np: NDArray[np.float64]
) -> NDArray:

    logits_np_copy = np.full_like(prompt_logits_np, -np.inf)

    for token, id in vocab_dict.items():
        posible_next_token = selected_func_name + token
        for func_name in func_names:
            if func_name.startswith(posible_next_token):
                logits_np_copy[id] = prompt_logits_np[id]
                break
    return logits_np_copy

def get_fn_name(path2jsons: PathValidator, init_prompt: str):

    my_model = Small_LLM_Model()
    # GETTING FUNCTION NAMES LIST AND PROMPTS LIST AS FUNC_CALL
    full_func_def = Prompt(input_paths=path2jsons).get_func_def().functions
    full_func_call = Prompt(input_paths=path2jsons).get_func_call().prompts
    func_names = [func.name for func in full_func_def]
    func_call = [prompt.get("prompt", None) for prompt in full_func_call]
    # ic(func_names)
    # ic(func_call)
    # func_params = [func.parameters for func in full_func_def]
    # ic(func_params)
    selected_func_name = ""

    # GETTING ALL THE INFO TO CREATE THE NAME MASK
    vocab_json_path = my_model.get_path_to_vocab_file()
    try:
        with open(vocab_json_path, mode='r') as vj:
            vocab_dict = json.load(vj)
    except (FileNotFoundError, AttributeError) as e:
        raise ValueError(e)
    i = 1
    ic(func_call[i])
    prompt = init_prompt + "[\n" + "{\n\tprompt:" + f"\"{func_call[i]}\",\n"
    prompt += "\"name\": \""
    
    while True:
        prompt_ids = my_model.encode(prompt)
        prompt_logits = my_model.get_logits_from_input_ids(prompt_ids[0].tolist())
        prompt_logits_np = np.array(prompt_logits)
        
        masked_logits_np = put_name_mask(
            selected_func_name, 
            func_names,
            vocab_dict,
            prompt_logits_np
        )
        next_token_id = int(np.argmax(masked_logits_np))
        next_token = my_model.decode([next_token_id])
        if selected_func_name in func_names:
            break
        selected_func_name += next_token
        prompt += next_token
        
    prompt += "\",\n"

    print(selected_func_name)
    ic(prompt)

    """
    Propuesta de logica

    for prompt in func_call:
        OBTENER NOMBRE FUNCION
            # tokenizar prompt
            # convertir a lista
            # obtener logits
            # convertir logits a np.array
            # Llamar funcion para actualizar logits disponibles (mask)
                # crear copia de logits np y poner valores a -inf
                # Recorrer vocab.json (a dict) y comprobar si alguna funcion
                    comienza con los caracteres de vocab_dict
                    # SI -> Guardar en cadena de chequeo
                    # NO -> Siguiente token de vocab_dict
                # Devolver copia del array
            # Seleccionar el max de la copia de logits np devuelta
            # Guardar en el output general
            # Adjuntar token seleccionado a prompt

        OBTENER PARAMETROS
            #
            #
            #

        CADENA FINAL A JSON
    """

    # while True:
    #     tokenized_prompt_tensor = my_model.encode(init_prompt)
    #     tokenized_prompt_list = tokenized_prompt_tensor[0].tolist()
    #     array_logits = my_model.get_logits_from_input_ids(tokenized_prompt_list)
    #     array_logits_np = np.array(array_logits)


