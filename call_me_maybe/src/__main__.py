import sys
from typing import List
from src.enums.enums import Colors
from src.parser.parser import Parser
from src.prompt.prompt import Prompt
from src.validator.path_validator import PathValidator
from pydantic import ValidationError
from src.logic.logic import get_output_info

"""
ERROR CODES
1- Incorrect number of arguments
2- Issues with files (no files / corrupted files)
3- Incorrect fields in the json files
4- The vocab file couldn't be found
5- The vocab file cannot be read
6- Issues getting info from LLM
7- Permission issues with output file path
"""


def main(args: List[str]) -> int:
    """
    Main entry point for the call-me-maybe application.

    Args:
        args (List[str]): A list of command-line arguments.

    Returns:
        int: Exit code (0 for success, non-zero for errors).
    """

    try:
        path2jsons: PathValidator = Parser.start_parsing(args)
    except ValidationError as e:
        print(e)
        return 2
    try:
        initial_prompt = Prompt(input_paths=path2jsons).init_prompt()
    except (ValueError, ValidationError) as e:
        print(e)
        return 3

    ret = get_output_info(path2jsons, initial_prompt)
    if ret:
        return ret

    return 0


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args > 7:
        print(
            f"{Colors.RED.value}"
            f"Wrong number of input arguments."
            f"{Colors.RESET.value}")
        sys.exit(99)
    sys.exit(main(sys.argv))
