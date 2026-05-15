from pydantic import BaseModel
from typing import List, Dict, Any


class InfoVal(BaseModel):
    """
    Represents the structure of a single function call result.

    Attributes:
        prompt (str): The original input prompt.
        name (str): The name of the function to be called.
        parameters (Dict[str, Any]): The arguments extracted for the
            function call.
    """
    prompt: str
    name: str
    parameters: Dict[str, Any]


class OutputVal(BaseModel):
    """
    Validator for the collection of processed function call outputs.

    Attributes:
        items (List[InfoVal]): A list of validated function call
            information objects.
    """
    items: List[InfoVal]
