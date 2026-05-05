import sys
from typing import List, Dict
from pydantic import ValidationError
from src.validator.path_validator import PathValidator
from icecream import ic

def get_func_def_path(args: List[str]) -> str | None:
    if "--functions_definition" not in args:
        return ("data/input/functions_definition.json")
    for index, value in enumerate(args):
        if value == "--functions_definition":
            # ic(args[index + 1])
            return (args[index + 1])

def get_func_call_path(args: List[str]) -> str | None:
    if "--input" not in args:
        return ("data/input/function_calling_tests.json")
    for index, value in enumerate(args):
        if value == "--input":
            return (args[index + 1])

def get_output_path(args: List[str]) -> str | None:
    if "--output" not in args:
        return ("data/output/")
    for index, value in enumerate(args):
        if value == "--output":
            return (args[index + 1])

def path_validator(input_paths: Dict[str, str]) -> PathValidator:
    try:
        validator = PathValidator(**input_paths)
    except ValidationError as e:
        print(e)
        # for error in e.errors():
        #     msg = error.get("msg", "")
        #     print(msg)
        sys.exit(1)
    return validator


def start_parsing(args: List[str]):
    input_paths = {}
    # func_def_path = get_func_def_path(args)
    # if func_def_path:
    input_paths["func_def_path"] = get_func_def_path(args)
    # func_call_path = get_func_call_path(args)
    # if func_call_path:
    input_paths["func_call_path"] = get_func_call_path(args)
    # output_path = get_output_path(args)
    # if output_path:
    input_paths["output_path"] = get_output_path(args)
    validator = path_validator(input_paths)
    return validator
