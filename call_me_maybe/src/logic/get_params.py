import numpy as np
from typing import List, Dict, Any, Tuple
from llm_sdk import Small_LLM_Model
from src.masks.masks import add_numeric_mask


def get_number_params(
    llm: Small_LLM_Model,
    prompt: str,
    func_params: List[Any],
    vocab_dict: Dict[str, int],
    param_type: str,
) -> Tuple[str, int | float]:
    """
    Predicts a numeric parameter from the LLM using logit masking.

    Args:
        llm (Small_LLM_Model): The LLM instance.
        prompt (str): The current prompt string.
        func_params (List[Any]): List of function parameter definitions.
        vocab_dict (Dict[str, int]): The vocabulary dictionary.
        param_type (str): The expected type ('number' or 'integer').

    Returns:
        Tuple[str, int | float]: A tuple containing the updated prompt and
        the predicted numeric value.
    """

    parameters = ""

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
    if param_type == "number":
        nb_parameters = float(parameters)
    else:
        nb_parameters = int(parameters)
    return prompt, nb_parameters


def get_str_params(
    llm: Small_LLM_Model,
    prompt: str,
    func_params: List[Any],
    vocab_dict: Dict[str, int]
) -> Tuple[str, str]:
    """
    Predicts a string parameter from the LLM.

    Args:
        llm (Small_LLM_Model): The LLM instance.
        prompt (str): The current prompt string.
        func_params (List[Any]): List of function parameter definitions.
        vocab_dict (Dict[str, int]): The vocabulary dictionary.

    Returns:
        Tuple[str, str]: A tuple containing the updated prompt and the
        predicted
        string.
    """

    parameters = ""
    while True:
        prompt_ids = llm.encode(prompt)
        prompt_logits = llm.get_logits_from_input_ids(
            prompt_ids[0].tolist())
        prompt_logits_np = np.array(prompt_logits)
        next_token_id = int(np.argmax(prompt_logits_np))
        next_token_str = llm.decode([next_token_id])
        if "\"" in next_token_str:
            clean_token = next_token_str.split("\"")[0]
            parameters += clean_token
            prompt += clean_token + "\""
            break
        parameters += next_token_str
        prompt += next_token_str
    return prompt, parameters
