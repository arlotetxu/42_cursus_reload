from icecream import ic
from llm_sdk import Small_LLM_Model
from src.validator.path_validator import PathValidator
from src.prompt.prompt import Prompt
import numpy as np


ic.configureOutput(includeContext=True)


def get_fn_name(path2jsons: PathValidator, init_prompt: str):
    my_model = Small_LLM_Model()
    full_func_def = Prompt(path2jsons).get_func_def()
    full_func_call = Prompt(path2jsons).get_func_call()
    func_names = [func.get("name", "") for func in full_func_def]
    func_call = [prompt.get("prompt", "") for prompt in full_func_call]
    ic(func_names)
    ic(func_call)
    output = ""


    init_prompt += f" {func_call[0]}\n"
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


