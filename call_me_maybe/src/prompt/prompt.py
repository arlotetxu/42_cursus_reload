from typing import List, Dict, Any
from src.validator.path_validator import PathValidator
from src.validator.func_def_validator import FuncDefVal
from src.validator.func_call_validator import FuncCallVal
from pydantic import BaseModel, ValidationError
from src.enums.enums import Colors
import json
from icecream import ic

ic.configureOutput(includeContext=True)


class Prompt (BaseModel):
    
    input_paths: PathValidator

    def get_func_def(self) -> FuncDefVal:
        func_def_path: str = self.input_paths.func_def_path

        try:
            with open(func_def_path, mode='r') as fd:
                func_def_data: List = json.load(fd)
        except (FileExistsError, FileNotFoundError, AttributeError) as e:
            print(f"{Colors.RED.value}[ERROR] - "
                  f"There are issues while open {func_def_path}. "
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
        return validated_function

    def get_func_call(self) -> FuncCallVal:
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
            validated_prompts = FuncCallVal(prompts=func_call_data)
        except ValidationError as e:
            print(f"{Colors.RED.value}[ERROR] - "
                  f"JSON file: {func_call_data} has incorrect fields. "
                  f"Please, check it and try again."
                  f"{Colors.RESET.value}\n{e}")
            raise ValueError(e)
        return validated_prompts

    def init_prompt(self) -> str:
        try:
            initial_prompt = (
                "You are the best function calling engine. "
                "You have access to the following functions list:\n"
                f"{str(self.get_func_def())}\n"
                "According to the prompt, you must return ONLY the right "
                "function.Put the focus on the verb or action in the prompt "
                "to return ONLY the function that matches the action."
                "The output must be a valid JSON.\n")
        except (ValueError, ValidationError) as e:
            raise ValueError(e)
        return initial_prompt
