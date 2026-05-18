from typing import List, Any
from src.validator.path_validator import PathValidator
from src.validator.func_def_validator import FuncDefVal
from src.validator.func_call_validator import FuncCallVal
from pydantic import BaseModel, ValidationError
from src.enums.enums import Colors
import json


class Prompt (BaseModel):
    """
    Handles the loading and preparation of prompts and function
    definitions for the function calling engine.
    """

    input_paths: PathValidator

    def get_func_def(self) -> FuncDefVal:
        """
        Loads and validates function definitions from a JSON file.

        Returns:
            FuncDefVal: Validated function definitions object.

        Raises:
            ValueError: If the file cannot be read or the JSON structure
                is invalid.
        """
        func_def_path: str = self.input_paths.func_def_path

        try:
            with open(func_def_path, mode='r') as fd:
                func_def_data: List[Any] = json.load(fd)
        except (FileExistsError, FileNotFoundError, ValueError,
                PermissionError, json.JSONDecodeError) as e:
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
        """
        Loads and validates function call prompts from a JSON file.

        Returns:
            FuncCallVal: Validated function calls object.

        Raises:
            ValueError: If the file cannot be read or the JSON structure
                is invalid.
        """
        func_call_path = self.input_paths.func_call_path
        try:
            with open(func_call_path, mode='r') as fd:
                content = fd.read().replace('\\"', "'")
                func_call_data = json.loads(content)
        except (
            FileExistsError, FileNotFoundError, ValueError,
                PermissionError, json.JSONDecodeError) as e:
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
        """
        Constructs the initial system prompt for the LLM.

        Returns:
            str: The formatted system instruction string.

        Raises:
            ValueError: If function definitions cannot be retrieved.
        """
        try:
            initial_prompt = (
                "You are the best function calling engine. "
                "You have access to the following functions list:\n"
                f"{str(self.get_func_def())}\n"
                "According to the prompt, you must return ONLY the right "
                "function. Put the focus on the verb or action in the prompt "
                "to return ONLY the function that matches the action. "
                "Do not consider other non importance words. "
                "If the function selected uses regex, choose a right "
                "validated  and proved regular expression. "
                "If the action is a substitution or replacement, check if "
                "the replacement value is codified (like asterisk meaning "
                "the symbol \"*\"). "
                "If a parameter has more than one value, separate them"
                "accordingly to the requested action. "
                "Check the sign of each number in the prompt to apply the"
                "right sign in the output. "
                "The output must be a valid JSON.\n")

        except (ValueError, ValidationError) as e:
            raise ValueError(e)
        return initial_prompt
