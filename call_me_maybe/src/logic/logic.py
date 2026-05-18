from llm_sdk import Small_LLM_Model
from src.enums.enums import Colors
from src.validator.path_validator import PathValidator
from src.validator.output_json_validator import OutputVal
from src.prompt.prompt import Prompt
from src.masks.masks import add_name_mask, add_numeric_mask
from src.logic.print_result import print_result
from src.logic.param_adaptor import str_param_adaptor
from pydantic import ValidationError
from typing import List, Dict, Any
import numpy as np
import json
from pathlib import Path


def get_func_name(
    prompt: str,
    llm: Small_LLM_Model,
    func_names: List[str],
    vocab_dict: Dict[str, int]
) -> str:
    """
    Predicts the function name from the LLM using logit masking.

    Args:
        prompt (str): The current prompt string.
        llm (Small_LLM_Model): The LLM instance.
        func_names (List): List of available function names.
        vocab_dict (Dict): The vocabulary dictionary.

    Returns:
        str: The predicted function name.

    Raises:
        ValueError: If an error occurs during LLM inference.
    """
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
    prompt: str,
    llm: Small_LLM_Model,
    full_func_def: List[Any],
    selected_func_name: str,
    vocab_dict: Dict[str, int]
) -> Dict[str, Any]:
    """
    Predicts function parameters from the LLM using logit masking.

    Args:
        prompt (str): The current prompt string.
        llm (Small_LLM_Model): The LLM instance.
        full_func_def (List): List of function definitions.
        selected_func_name (str): The name of the selected function.
        vocab_dict (Dict): The vocabulary dictionary.

    Returns:
        Dict: A dictionary containing the predicted parameters.

    Raises:
        ValueError: If an error occurs during LLM inference.
    """

    func_params = [
        func_obj.parameters for func_obj in full_func_def
        if func_obj.name == selected_func_name]

    parameters = ""
    parameters_dict: Dict[str, str | float] = {}

    prompt += "\"parameters\": {"
    try:
        for param in func_params:
            for param_name, param_type in param.items():
                prompt += f"\"{param_name}\": "
                if param_type.type in ["number", "integer"]:
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
                        if ',' in next_token_str or '}' in next_token_str:
                            prompt += ', '
                            break
                        parameters += next_token_str
                        prompt += next_token_str
                    if param_type.type == "number":
                        parameters_dict[param_name] = float(parameters)
                    else:
                        parameters_dict[param_name] = int(parameters)

                if param_type.type == "string":
                    prompt += "\""
                    while True:
                        prompt_ids = llm.encode(prompt)
                        prompt_logits = llm.get_logits_from_input_ids(
                            prompt_ids[0].tolist())
                        prompt_logits_np = np.array(prompt_logits)
                        next_token_id = int(np.argmax(prompt_logits_np))
                        next_token_str = llm.decode([next_token_id])
                        if "\"" in next_token_str:
                            parameters += next_token_str.split("\"")[0]
                            prompt += parameters + "\""
                            break
                        parameters += next_token_str
                        prompt += next_token_str
                    parameters_dict[param_name] = str_param_adaptor(parameters)
                parameters = ""
    except Exception as e:
        raise ValueError(e)
    return parameters_dict


def create_output_file(
    path2jsons: PathValidator,
    output_info: List[Dict[str, Any]]
) -> int:
    """
    Validates and writes the LLM output to a JSON file.

    Args:
        path2jsons (PathValidator): Validated input paths.
        output_info (List[Dict[str, Any]]): The data to be saved.

    Returns:
        int: 0 on success, error code otherwise.
    """

    output_path = Path(path2jsons.output_path)
    try:
        out_validator = OutputVal(items=output_info)
        validated_data = out_validator.model_dump()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, mode='x') as fd:
            json.dump(validated_data.get("items", ""), fd, indent=4)
    except (ValidationError, TypeError):
        print(f"{Colors.RED.value}[ERROR] - "
              f"The output file ({output_path}) has a wrong structure "
              f"or your are trying to create a JSOn file from a wrong source. "
              "Exiting..."
              f"{Colors.RESET.value}")
        return 8
    except PermissionError:
        print(f"{Colors.RED.value}[ERROR] - "
              f"The output file ({output_path}) couldn't be saved. "
              "Check the folder path permissions and try it again."
              f"{Colors.RESET.value}")
        return 7
    return 0


def get_output_info(path2jsons: PathValidator, init_prompt: str) -> int:
    """
    Orchestrates the LLM inference process for all prompts.

    Args:
        path2jsons (PathValidator): Validated input paths.
        init_prompt (str): The base system prompt.

    Returns:
        int: 0 on success, error code otherwise.
    """
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
        for i in range(len(func_call)):
            prompt = (init_prompt +
                      "[\n" + "{\n\t\"prompt\":" + f"\"{func_call[i]}\",\n")
            prompt += "\"name\": \""

            selected_func_name = get_func_name(
                prompt, llm, func_names, vocab_dict
                )
            prompt += selected_func_name + "\",\n"

            selected_func_params = get_func_parameters(
                prompt, llm, full_func_def, selected_func_name, vocab_dict)

            print_result(
                func_call[i], selected_func_name, selected_func_params
                )
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
    ret = create_output_file(path2jsons, output_info)
    if ret:
        return ret
    return 0
