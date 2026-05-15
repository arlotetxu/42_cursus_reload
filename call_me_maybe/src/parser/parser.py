import sys
from typing import List, Dict
from pydantic import ValidationError
from src.validator.path_validator import PathValidator


class Parser:
    """
    Handles command-line argument parsing for file paths.
    """

    @classmethod
    def get_func_def_path(cls, args: List[str]) -> str:
        """
        Extracts the function definitions file path from arguments.

        Args:
            args: List of command-line arguments.

        Returns:
            The path to the function definitions JSON file.
        """
        if "--functions_definition" not in args:
            return ("data/input/functions_definition.json")
        for index, value in enumerate(args):
            if value == "--functions_definition":
                return (args[index + 1])
        return ""

    @classmethod
    def get_func_call_path(cls, args: List[str]) -> str:
        """
        Extracts the function calls file path from arguments.

        Args:
            args: List of command-line arguments.

        Returns:
            The path to the input function calls JSON file.
        """
        if "--input" not in args:
            return ("data/input/function_calling_tests.json")
        for index, value in enumerate(args):
            if value == "--input":
                return (args[index + 1])
        return ""

    @classmethod
    def get_output_path(cls, args: List[str]) -> str:
        """
        Extracts the output file path from arguments.

        Args:
            args: List of command-line arguments.

        Returns:
            The path where results will be saved.
        """
        if "--output" not in args:
            return ("data/output/function_calling_results.json")
        for index, value in enumerate(args):
            if value == "--output":
                return (args[index + 1])
        return ""

    @classmethod
    def path_validator(cls, input_paths: Dict[str, str]) -> PathValidator:
        """
        Validates the existence and format of provided paths.

        Args:
            input_paths: Dictionary containing the three required paths.

        Returns:
            A validated PathValidator instance.
        """
        try:
            validator = PathValidator(**input_paths)
        except ValidationError as e:
            print(e)
            sys.exit(1)
        return validator

    @classmethod
    def start_parsing(cls, args: List[str]) -> PathValidator:
        """
        Orchestrates the parsing and validation of all input arguments.

        Args:
            args: List of command-line arguments.

        Returns:
            A validated PathValidator object containing all paths.
        """
        input_paths = {}
        input_paths["func_def_path"] = cls.get_func_def_path(args)
        input_paths["func_call_path"] = cls.get_func_call_path(args)
        input_paths["output_path"] = cls.get_output_path(args)
        validator = cls.path_validator(input_paths)
        return validator
