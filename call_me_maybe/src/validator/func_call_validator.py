from pydantic import BaseModel
from typing import List, Dict


class FuncCallVal(BaseModel):
    prompts: List[Dict[str, str]]