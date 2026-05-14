from icecream import ic
from llm_sdk import Small_LLM_Model
from src.enums.enums import Colors
from src.validator.path_validator import PathValidator
from src.prompt.prompt import Prompt
from src.masks.masks import add_name_mask, add_numeric_mask
from typing import List, Dict
import numpy as np
import json
from pathlib import Path

ic.configureOutput(includeContext=True)


def get_func_name(
    prompt: str,
    llm: Small_LLM_Model,
    func_names: List,
    vocab_dict: Dict) -> str:

    selected_func_name = ""
    try:
        while True:
            prompt_ids = llm.encode(prompt)
            prompt_logits = llm.get_logits_from_input_ids(
                prompt_ids[0].tolist()
                )
            prompt_logits_np = np.array(prompt_logits)

            masked_logits_np = add_name_mask(
                selected_func_name,
                func_names,
                vocab_dict,
                prompt_logits_np
            )
            next_token_id = int(np.argmax(masked_logits_np))
            next_token = llm.decode([next_token_id])
            if selected_func_name in func_names:
                break
            selected_func_name += next_token
            prompt += next_token
    except Exception as e:
        raise ValueError(e)

    return selected_func_name

def get_func_parameters(
    prompt:str,
    llm:Small_LLM_Model,
    full_func_def: List,
    selected_func_name: str,
    vocab_dict: Dict) -> Dict:

    func_params = [
        func_obj.parameters for func_obj in full_func_def
        if func_obj.name == selected_func_name]

    parameters = ""
    parameters_dict = {}

    prompt += "\"parameters\": {"
    try:
        for param in func_params:
            for param_name, param_type in param.items():
                prompt += f"\"{param_name}\": "
                if param_type.type == "number":
                    while True:
                        prompt_ids = llm.encode(prompt)
                        prompt_logits = llm.get_logits_from_input_ids(
                            prompt_ids[0].tolist())
                        prompt_logits_np = np.array(prompt_logits)
                        masked_logit_np = add_numeric_mask(
                            parameters,
                            func_params,
                            vocab_dict,
                            prompt_logits_np
                        )
                        next_token_id = int(np.argmax(masked_logit_np))
                        next_token_str = llm.decode([next_token_id])
                        if next_token_str in ['}', ',']:
                            # prompt += ', '
                            break
                        parameters += next_token_str
                        prompt += next_token_str
                    parameters_dict[param_name] = parameters

                if param_type.type == "string":
                    prompt += "\""
                    while True:
                        prompt_ids = llm.encode(prompt)
                        prompt_logits = llm.get_logits_from_input_ids(
                            prompt_ids[0].tolist())
                        prompt_logits_np = np.array(prompt_logits)
                        next_token_id = int(np.argmax([prompt_logits_np]))
                        next_token_str = llm.decode([next_token_id])
                        if next_token_str[0] in ["\"}", "\"", "}"]:
                            break
                        parameters += next_token_str
                        prompt += next_token_str
                    parameters_dict[param_name] = parameters
                parameters = ""
    except Exception as e:
        raise ValueError(e)
    return parameters_dict


def get_output_info(path2jsons: PathValidator, init_prompt: str) -> int:

    output_info = []
    llm = Small_LLM_Model()
    full_func_def = Prompt(input_paths=path2jsons).get_func_def().functions
    full_func_call = Prompt(input_paths=path2jsons).get_func_call().prompts
    func_names = [func.name for func in full_func_def]
    func_call = [prompt.get("prompt", None) for prompt in full_func_call]

    vocab_json_path = llm.get_path_to_vocab_file()
    try:
        with open(vocab_json_path, mode='r') as vj:
            vocab_dict = json.load(vj)
    except FileNotFoundError:
        print(f"{Colors.RED.value}[ERROR] - "
              "The vocab.json file couldn't be found. "
              f"Please, check it and try again.{Colors.RESET.value}")
        return 4
    except PermissionError:
        print(f"{Colors.RED.value}[ERROR] - "
              "The vocab.json file couldn't be open. "
              "Please, check the file permissions and try it again."
              f"{Colors.RESET.value}")
        return 5

    try:
        for i in range(len(func_call) - 1):
            prompt = (init_prompt +
                      "[\n" + "{\n\t\"prompt\":" + f"\"{func_call[i]}\",\n")
            prompt += "\"name\": \""

            selected_func_name = get_func_name(
                prompt, llm, func_names, vocab_dict
                )
            prompt += selected_func_name + "\",\n"

            selected_func_params = get_func_parameters(
                prompt, llm, full_func_def, selected_func_name, vocab_dict)

            output_info.append(dict(
                prompt=func_call[i],
                name=selected_func_name,
                parameters=selected_func_params
            ))
    except ValueError:
        print(f"{Colors.RED.value}[ERROR] - "
              "There was an issue while geeting the output information "
              "with the LLM. "
              f"{Colors.RESET.value}")
        return 6

    # TODO: Crea nueva funcion para salvar el JSON y comprobarlo
    output_path = Path(path2jsons.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(output_path, mode='x') as fd:
            json.dump(output_info, fd, indent=4)
    except PermissionError:
        print(f"{Colors.RED.value}[ERROR] - "
              f"The output file ({path2jsons.output_path}) couldn't be saved. "
              "Check the folder/file permissions and try it again."
              f"{Colors.RESET.value}")
        return 7

    return (0)