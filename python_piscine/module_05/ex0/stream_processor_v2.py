#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(result: str = "This is a std output"):
        print(f"{result}")


class NumericProcessor(DataProcessor):

    def __init__(self):
        self.numbers = []
        self.count = 0
        self.sum = 0
        self.output = False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return f"Processing data: {data}.\n Not numeric data found. " \
                "Exiting..."
        else:
            for x in data:
                self.numbers.append(x)
                self.count += 1
                self.sum += x
            self.output = True
        return f"Processing data: {data}.\n" \
            f"Validation: Numeric data verified\n" \
            f"Output: Processed {self.count} numeric values, " \
            f"sum={self.sum}, avg={self.sum / self.count}"

    def validate(self, data: Any) -> bool:
        for x in data:
            try:
                x = x / 1
            except TypeError:
                return False
        return True

    def format_output(self, result: str = "This is a std output"):
        if self.output:
            print(f"Processed {self.count} numeric values, "
                  f"sum={self.sum}, avg={self.sum / self.count}")


class TextProcessor(DataProcessor):
    def __init__(self):
        self.chars = 0
        self.words = []
        self.output = False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return f"Processing data: \"{data}\".\nNot text found. Exiting..."
        else:
            self.chars = 0
            for c in data:
                self.chars += 1
            self.words = data.split()
            self.output = True
            return f"Processing data: \"{data}\"\n" \
                "Validation: Text data verified\n" \
                f"Processed text: {self.chars} characters," \
                f"{len(self.words)} words"

    def validate(self, data: Any) -> bool:
        try:
            data = data + ""
            return True
        except TypeError:
            return False

    def format_output(self, result: str = "This is a std output"):
        if self.output:
            print(f"Processed text: {self.chars} characters, "
                  f"{len(self.words)} words")


class LogProcessor(DataProcessor):
    def __init__(self):
        self.output = False
        self.output_msg = ""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Processing data: "
            f"\"{data['level']}\": {data['message']}\nPassed data "
            "is not a valid log entry. Exiting..."
        else:
            self.output = True
            self.output_msg = f"[{data['type']}] " \
                f"{data['level']} level detected: {data['message']}"
            return f"Processing data: \"{data['level']}\": " \
                f"{data['message']}\nValidation: Log entry verified\n" \
                f"Output: {self.output_msg}"

    def validate(self, data: Any) -> bool:
        return ("type" in data and "level" in data and "message" in data)

    def format_output(self, result: str = "This is a std output"):
        if self.output:
            print(f"{self.output_msg}")


def ft_main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    num_data = [[1, 2, 3, 4, 5],]

    for item in num_data:
        num = NumericProcessor()
        msg = num.process(item)
        if num.validate(item):
            DataProcessor.format_output(msg)

    print("\nInitializing Text Processor..")
    text_data = ["Hello Nexus World", 12]

    for item in text_data:
        txt = TextProcessor()
        msg = txt.process(item)
        DataProcessor.format_output(msg)

    print("\nInitializing Log Processor...")
    log_data = {"type": "ALERT", "level": "ERROR",
                "message": "Connection timeout"}
    log = LogProcessor()
    msg = (log.process(log_data))
    DataProcessor.format_output(msg)

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")
    num_data = [1, 2, 3]
    num = NumericProcessor()
    num.process(num_data)
    print("Result 1: ", end="")
    num.format_output()

    my_str = "Hello World!"
    txt = TextProcessor()
    txt.process(my_str)
    print("Result 2: ", end="")
    txt.format_output()

    log_data = {"type": "INFO", "level": "INFO", "message": "System ready"}
    log = LogProcessor()
    log.process(log_data)
    print("Result 3: ", end="")
    log.format_output()

    print("\nFoundation systems online. Nexus ready for advanced streams.")


ft_main()
