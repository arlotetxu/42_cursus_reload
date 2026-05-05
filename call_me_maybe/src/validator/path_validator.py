from pydantic import BaseModel, Field, model_validator
from typing import Any
from pathlib import Path
from src.enums.enums import Colors
import json

from icecream import ic
ic.configureOutput(contextAbsPath=True)

class PathValidator(BaseModel):

    func_def_path: str = Field(
        default="data/input/functions_definition.json"
        )
    func_call_path: str = Field(
        default="data/input/function_calling_tests.json"
    )
    output_path: str = Field(
        default="data/output/"
    )


    @model_validator(mode="after")
    def check_func_def_path(self) -> Any:
        file_path = Path(self.func_def_path)
        if not file_path.is_file():
            raise ValueError(
                f"{Colors.RED.value}[ERROR] -"
                f"The file specified as --functions_definition "
                f"is not valid. Please, check it and try again."
                f"{Colors.RESET.value}"
            )
        try:
            with open(self.func_def_path, 'r', encoding='utf-8') as fd:
                json.load(fd)
        except (json.JSONDecodeError):
            raise ValueError(
                f"{Colors.RED.value}[ERROR] -"
                f"The json file specified as --functions_definition "
                f"is corrupted. Please, check it and try again."
                f"{Colors.RESET.value}"
            )
        return self

    @model_validator(mode="after")
    def check_func_call_path(self) -> Any:
        file_path = Path(self.func_call_path)
        if not file_path.is_file():
            raise ValueError(
                f"{Colors.RED.value}[ERROR] -"
                f"The file specified as --input "
                f"is not valid. Please, check it and try again."
                f"{Colors.RESET.value}"
            )
        try:
            with open(self.func_call_path, 'r', encoding='utf-8') as fd:
                json.load(fd)
        except (json.JSONDecodeError):
            raise ValueError(
                f"{Colors.RED.value}[ERROR] -"
                f"The json file specified as --input "
                f"is corrupted. Please, check it and try again."
                # f"\n{e}"  #TODO --> Eliminar linea
                f"{Colors.RESET.value}"
            )
        return self

    #TODO Analizar como gestionar el fichero de salida para no comprometer a
    #TODO ficheros existentes
