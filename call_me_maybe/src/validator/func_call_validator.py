from pydantic import BaseModel
from typing import List, Dict


class FuncCallVal(BaseModel):
    """
    Validator for a collection of function call prompts.

    Attributes:
        prompts (List[Dict[str, str]]): A list of dictionaries where
            each dictionary represents a prompt and its associated
            metadata.
    """

    prompts: List[Dict[str, str]]
