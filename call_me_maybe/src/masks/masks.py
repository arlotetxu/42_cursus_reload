from typing import List, Dict
import numpy as np
from numpy.typing import NDArray
from icecream import ic

ic.configureOutput(includeContext=True)

def add_name_mask(
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

def add_numeric_mask(
    parameters: str,
    func_params: List,
    vocab_dict: Dict,
    prompt_logits_np: NDArray[np.float64]
) -> NDArray:
    valid_tokens = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-", ",", "}", ":", "\""]

    logits_np_copy = np.full_like(prompt_logits_np, -np.inf)

    for token, id in vocab_dict.items():
        if token in valid_tokens:
            logits_np_copy[id] = prompt_logits_np[id]
    return logits_np_copy