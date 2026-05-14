from typing import List
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
                content = fd.read().replace('\\"', "'")
                # func_call_data = json.load(fd)
                func_call_data = json.loads(content)
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
                "to return ONLY the function that matches the action. "
                "Do not consider other non importance words. "
                "If the function selected uses regex, choose a right"
                "confirmed regular expression. "
                "If the action is a substitution or a replacement, check if"
                "the replacement value is codified (like asterisk meaning"
                "the symbol'*') or just a simple word. "
                "If a parameter has more than one value, separate them"
                "accordingly to the requested action. "
                "Check the sign of each number in the prompt to apply the"
                "right sign in the output. "
                "The output must be a valid JSON.\n")
        #     initial_prompt = (
        # "You are a strict function-calling assistant. "
        # "Your ONLY task is to extract the user's intent matching one of the provided functions.\n\n"

        # "<AVAILABLE_FUNCTIONS>\n"
        # f"{str(self.get_func_def())}\n"
        # "</AVAILABLE_FUNCTIONS>\n\n"

        # "RULES:\n"
        # "1. Focus strictly on the primary action/verb requested.\n"
        # "2. Output ONLY a valid JSON object. No explanations, no markdown "
        # "formatting outside the JSON, no conversational text.\n"
        # "3. Pay strict attention to EXACT parameter formats (e.g., regex, "
        # "codifications), SPECIALLY in regex parameters.\n"
        # # "4. CRITICAL: If the prompt contains negative numbers like -5, -66, "
        # # "-13,..., you MUST output the negative sign '-' before the digit token. "
        # # "I.e, Input: What is the sum of -5 and -6 → Output: {'a': '-5', 'b': '-6'}.\n"
        # # "5. Pay strict attention to the number of parameter and separate them to fulfill the action\n\n"
        # # "5. If a parameter has more than one value, separate them accordingly"
        # "5. One parameter could have more then one value. If so, separate them to fulfill the action requested"
        # "\n")
        except (ValueError, ValidationError) as e:
            raise ValueError(e)
        return initial_prompt
