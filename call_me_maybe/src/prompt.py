import json

class Prompt:
    def __init__(
        self,
        func_call: str = "data/input/function_calling_tests.json",
        func_def: str = "data/input/function_definition.json",
        output: str = "data/output/"
        ) -> None:

        self.func_call = func_call
        self.func_def = func_def


