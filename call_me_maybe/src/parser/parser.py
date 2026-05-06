import sys
from typing import List, Dict
from pydantic import ValidationError
from src.validator.path_validator import PathValidator
from icecream import ic

ic.configureOutput(includeContext=True)


class Parser:

    @classmethod
    def get_func_def_path(cls, args: List[str]) -> str:
        if "--functions_definition" not in args:
            return ("data/input/functions_definition.json")
        for index, value in enumerate(args):
            if value == "--functions_definition":
                # ic(args[index + 1])
                return (args[index + 1])
        return ""

    @classmethod
    def get_func_call_path(cls, args: List[str]) -> str:
        if "--input" not in args:
            return ("data/input/function_calling_tests.json")
        for index, value in enumerate(args):
            if value == "--input":
                return (args[index + 1])
        return ""

    @classmethod
    def get_output_path(cls, args: List[str]) -> str:
        if "--output" not in args:
            return ("data/output/function_calls.json")
        for index, value in enumerate(args):
            if value == "--output":
                return (args[index + 1])
        return ""

    @classmethod
    def path_validator(cls, input_paths: Dict[str, str]) -> PathValidator:
        try:
            validator = PathValidator(**input_paths)
        except ValidationError as e:
            print(e)
            # for error in e.errors():
            #     msg = error.get("msg", "")
            #     print(msg)
            sys.exit(1)
        return validator

    @classmethod
    def start_parsing(cls, args: List[str]) -> PathValidator:
        input_paths = {}
        input_paths["func_def_path"] = cls.get_func_def_path(args)
        input_paths["func_call_path"] = cls.get_func_call_path(args)
        input_paths["output_path"] = cls.get_output_path(args)
        validator = cls.path_validator(input_paths)
        return validator
