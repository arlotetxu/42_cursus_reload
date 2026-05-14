from pydantic import BaseModel
from typing import List, Dict


class ParameterInfo(BaseModel):
    source_string: str
    regex: str
    replacement: str


class OutputInfo(BaseModel):
    prompt: str
    name: str
    parameters: Dict[str, ParameterInfo]


class OutputVal(BaseModel):
    item: List[OutputInfo]