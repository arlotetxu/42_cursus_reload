#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    
    def format_output(self, result: str = "This is a std output"):
        print(f"Output: {result}")


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if isinstance(data, (int, float)):
            return f"Processing data: {data}"
        if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
            return f"Processing list of numbers: {data}"
        return f"Error: {data} is not a valid number or list of numbers"
    
    def validate(self, data: Any) -> bool:
        pass


class TextProcessor(DataProcessor):
    super().__init__()
    def process(self, data: Any) -> str:
        pass
    
    def validate(self, data: Any) -> bool:
        pass


class LogProcessor(DataProcessor):
    super().__init__()
    def process(self, data: Any) -> str:
        pass
    
    def validate(self, data: Any) -> bool:
        pass