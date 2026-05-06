from pydantic import BaseModel, Field
from typing import List, Dict


class ParameterDef(BaseModel):
    type: str


class ReturnDef(BaseModel):
    type: str


class FunctionDef(BaseModel):
    name: str
    description: str
    parameters: Dict[str, ParameterDef]
    returns: ReturnDef


class FuncDefVal(BaseModel):
    functions: List[FunctionDef]