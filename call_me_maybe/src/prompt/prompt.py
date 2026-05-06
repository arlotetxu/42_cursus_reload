import sys
from typing import List, Dict, Any
from src.validator.path_validator import PathValidator
from src.validator.func_def_validator import FuncDefVal
from src.validator.func_call_validator import FuncCallVal
from pydantic import ValidationError
from src.enums.enums import Colors
import json
from icecream import ic

ic.configureOutput(includeContext=True)


class Prompt:
    def __init__(
        self,
        input_paths: PathValidator
    ) -> None:

        self.input_paths = input_paths

    def get_func_def(self) -> int | str:
        func_def_path = self.input_paths.func_def_path

        try:
            with open(func_def_path, mode='r') as fd:
                func_def_data = json.load(fd)
        except (FileExistsError, FileNotFoundError, AttributeError) as e:
            print(f"{Colors.RED.value}[ERROR] - "
                  f"There are issue while open {func_def_data}. "
                  f"Please, check the file and permissions and try again."
                  f"{Colors.RESET.value}\n{e}")
            raise ValueError(e)

        # CHECKING THE FILE STRUCTURE
        try:
            validated_function = FuncDefVal(functions=func_def_data)
        except ValidationError as e:
            print(f"{Colors.RED.value}[ERROR] - "
                  f"JSON file: {func_def_path} has incorrect fields. "
                  f"Please, check it and try again."
                  f"{Colors.RESET.value}\n{e}")
            raise ValueError(e)
        ic(func_def_data)
        return (str(func_def_data))

    def get_func_call(self) -> Any:
        func_call_path = self.input_paths.func_call_path

        try:
            with open(func_call_path, mode='r') as fd:
                func_call_data = json.load(fd)
        except (FileExistsError, FileNotFoundError, AttributeError) as e:
            print(f"{Colors.RED.value}[ERROR] - "
                  f"There are issue while open {func_call_path}. "
                  f"Please, check the file and permissions and try again."
                  f"{Colors.RESET.value}\n{e}")
            raise ValueError(e)

        # CHECKING THE FILE STRUCTURE
        try:
            validated_prompts = FuncCallVal(func_call_data)
        except ValidationError as e:
            print(f"{Colors.RED.value}[ERROR] - "
                  f"JSON file: {func_call_data} has incorrect fields. "
                  f"Please, check it and try again."
                  f"{Colors.RESET.value}\n{e}")
            raise ValueError(e)
        return func_call_data

    def init_prompt(self) -> int | str:
        try:
            initial_prompt = f"You are an expert assistant. "\
                "You have access to the following functions:\n"\
                f"{self.get_func_def()}\n"\
                "According to the user_input, you must respond exclusively "\
                "with a string formatted as a JSON with the following"\
                "information: "\
                "{\"prompt\": user_input, "\
                "\"name\": corresponding function name, "\
                "\"parameters\": "\
                "{function parameter name: \"parameter value\"}...}\n"\
                "user_input: "
        except (ValueError, ValidationError) as e:
            raise ValueError(e)
        return initial_prompt
