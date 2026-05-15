from pydantic import BaseModel
from typing import List, Dict


class ParameterDef(BaseModel):
    """
    Defines the structure of a function parameter.

    Attributes:
        type (str): The expected data type of the parameter.
    """
    type: str


class ReturnDef(BaseModel):
    """
    Defines the structure of a function's return value.

    Attributes:
        type (str): The data type returned by the function.
    """
    type: str


class FunctionDef(BaseModel):
    """
    Represents the definition of a single function.

    Attributes:
        name (str): The name of the function.
        description (str): A brief explanation of what the function does.
        parameters (Dict[str, ParameterDef]): A mapping of parameter
            names to their definitions.
        returns (ReturnDef): The definition of the return value.
    """
    name: str
    description: str
    parameters: Dict[str, ParameterDef]
    returns: ReturnDef


class FuncDefVal(BaseModel):
    """
    Validator for a collection of function definitions.

    Attributes:
        functions (List[FunctionDef]): A list of validated function
            definition objects.
    """
    functions: List[FunctionDef]
