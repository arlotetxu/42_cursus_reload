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
        default="data/output/function_calling_results.json"
    )

    @model_validator(mode="after")
    def check_func_def_path(self) -> Any:
        file_path = Path(self.func_def_path)
        if not file_path.is_file():
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - "
                f"The file specified as \"--functions_definition "
                f"{self.func_def_path}\" "
                f"is not valid. Please, check it and try again."
                f"{Colors.RESET.value}"
            )
        try:
            with open(self.func_def_path, 'r', encoding='utf-8') as fd:
                json.load(fd)
        except (json.JSONDecodeError):
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - "
                f"The json file specified as \"--functions_definition "
                f"{self.func_def_path}\" "
                f"is corrupted. Please, check it and try again."
                f"{Colors.RESET.value}"
            )
        return self

    @model_validator(mode="after")
    def check_func_call_path(self) -> Any:
        file_path = Path(self.func_call_path)
        if not file_path.is_file():
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - "
                f"The file specified as \"--input {self.func_call_path}\" "
                f"is not valid. Please, check it and try again."
                f"{Colors.RESET.value}"
            )
        try:
            with open(self.func_call_path, 'r', encoding='utf-8') as fd:
                json.load(fd)
        except (json.JSONDecodeError):
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - "
                f"The json file specified as \"--input {self.func_call_path}\""
                f" is corrupted. Please, check it and try again."
                f"{Colors.RESET.value}"
            )
        return self

    @model_validator(mode="after")
    def check_output_path(self) -> Any:
        file_path = Path(self.output_path)
        if file_path.is_file():
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - "
                f"The file specified as \"--output {self.output_path}\" "
                f"already exists. "
                f"Please, select a new output file and try again."
                f"{Colors.RESET.value}"
            )

        return self
