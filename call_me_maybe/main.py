import sys
from typing import List, Dict
from src.enums.enums import Colors
from src.parser.parser import start_parsing
from src.prompt import Prompt
from src.validator.path_validator import PathValidator
from icecream import ic

ic.configureOutput(contextAbsPath=True)

def main(args: List[str]) -> None:
    print("Hello from call-me-maybe!")
    # if len(args) > 1:
    path_validator: PathValidator = start_parsing(args)
    ic(path_validator.func_call_path)
    ic(path_validator.func_def_path)

    # my_prompt = Prompt()
    # print(my_prompt.func_call)
    # print(my_prompt.func_def)


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args > 7:
        print(
            f"{Colors.RED.value}"
            f"Wrong number of input arguments."
            f"{Colors.RESET.value}")
        sys.exit(1)
    main(sys.argv)
