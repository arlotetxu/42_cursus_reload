from pydantic import BaseModel
from typing import List, Dict


# class PromptDef(BaseModel):
#     prompt: str


class FuncCallVal(BaseModel):
    prompts: List[Dict[str, str]]