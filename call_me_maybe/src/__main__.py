import sys
from typing import List
from src.enums.enums import Colors
from src.parser.parser import Parser
from src.prompt.prompt import Prompt
from src.validator.path_validator import PathValidator
from pydantic import ValidationError
from icecream import ic
ic.configureOutput(includeContext=True)

"""
ERROR CODES
1- Incorrect number of arguments
2- Issues with arguments (no files / corrupted files)
3- Incorrect fields in the json files
"""


def main(args: List[str]) -> int:
    print("Hello from call-me-maybe!")

    try:
        path_validator: PathValidator = Parser.start_parsing(args)
    except ValidationError as e:
        print(e)
        return 2
        # sys.exit(2)
    # ic(path_validator.func_call_path)
    # ic(path_validator.func_def_path)
    # ic(path_validator.output_path)
    try:
        Prompt(path_validator).get_func_def()
    except (ValueError, ValidationError):
        return 3
    return 0


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args > 7:
        print(
            f"{Colors.RED.value}"
            f"Wrong number of input arguments."
            f"{Colors.RESET.value}")
        sys.exit(1)
    # main(sys.argv)
    sys.exit(main(sys.argv))
