#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Abstract base class for data processing operations.

    This class defines the interface for data processors that validate,
    process, and format data outputs. Subclasses must implement the
    abstract methods to provide specific processing logic.

    Methods
    -------
    process(data: Any) -> str
        Abstract method that processes the input data and returns
        a string result. Must be implemented by subclasses.

    validate(data: Any) -> bool
        Abstract method that validates the input data.
        Must be implemented by subclasses.
        Returns True if data is valid, False otherwise.

    format_output(result: str = "This is a std output")
        Prints the formatted result string to standard output.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the input data and return a string result.

        Args:
            data (Any): The input data to be processed.

        Returns:
            str: The processed result as a string.
        """
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate the provided data.

        Args:
            data (Any): The data to be validated. Can be of any type.

        Returns:
            bool: True if the data is valid, False otherwise.
        """
        ...

    def format_output(result: str = "This is a std output"):
        """
        Prints a formatted output message to standard output.

        Args:
            result (str, optional): The message to be printed.
                Defaults to "This is a std output".

        Returns:
            None
        """
        print(f"{result}")


class NumericProcessor(DataProcessor):
    """
    A processor class for handling numeric data.

    This class extends DataProcessor to provide specialized processing
    for numeric data collections. It maintains running statistics including
    count, sum, and average of processed numeric values.

    Attributes:
        numbers (list): A list storing all processed numeric values.
        count (int): The count of numeric values processed.
        sum (int/float): The running sum of all processed numeric values.
        output (bool): Flag indicating whether valid data has been processed.

    Methods:
        process(data: Any) -> str:
            Processes the input data if it contains valid numeric values.
            Updates internal statistics and returns a formatted result string.

        validate(data: Any) -> bool:
            Validates that all elements in the data are numeric by attempting
            division operation on each element.

        format_output(result: str) -> None:
            Prints formatted output with statistics if valid data has been
            processed.
    """

    def __init__(self):
        """
        Initialize a new StreamProcessor instance.

        Attributes:
            numbers (list): Empty list to store numbers for processing.
            count (int): Counter initialized to 0 to track the number of
                elements.
            sum (int): Accumulator initialized to 0 to store the sum of
                numbers.
            output (bool): Flag initialized to False to control output
                behavior.
        """
        self.numbers: list = []
        self.count: int = 0
        self.sum: int = 0
        self.output: bool = False

    def process(self, data: Any) -> str:
        """
        Process input data by validating and accumulating numeric values.

        This method validates the input data, and if valid, appends each
        element to the numbers list while updating count and sum statistics.

        Args:
            data (Any): The input data to process. Expected to be an
            iterable containing numeric values.

        Returns:
            str: A formatted string describing the processing result.
            If validation fails, returns an error message.
            If successful, returns statistics including the count
            of processed values, their sum, and average.
        """

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
        """
        Validate that all elements in the data are numeric (divisible by 1).

        Args:
            data: An iterable containing elements to validate.

        Returns:
            bool: True if all elements in data are numeric types that support
                  division, False if any element raises a TypeError when
                  divided by 1.
        """
        for x in data:
            try:
                x = x / 1
            except TypeError:
                return False
        return True

    def format_output(self, result: str = "This is a std output"):
        """
        Format and print the output of the stream processing.

        If output is enabled, prints the count of processed numeric
        values, their sum, and their average.

        Args:
            result (str, optional): A default output message.
            Defaults to "This is a std output".

        Returns:
            None
        """

        if self.output:
            print(f"Processed {self.count} numeric values, "
                  f"sum={self.sum}, avg={self.sum / self.count}")


class TextProcessor(DataProcessor):
    """
    A text processor class that extends DataProcessor to handle text data.

    This class provides functionality to process text data by counting
    characters and words, validating that the input is text, and
    formatting the output.

    Attributes:
        chars (int): The number of characters in the processed text.
        words (list): A list of words extracted from the processed text.
        output (bool): Flag indicating whether text has been successfully
            processed.

    Methods:
        process(data: Any) -> str:
            Processes the input data by counting characters and words.
            Returns a formatted string with processing results or an
            error message if validation fails.

        validate(data: Any) -> bool:
            Validates that the input data is a string by attempting
            string concatenation. Returns True if data is text,
            False otherwise.

        format_output(result: str = "This is a std output"):
            Prints the processed text statistics (character and word
            count) if text has been successfully processed.
    """

    def __init__(self):
        """
        Initialize a new TextProcessor instance.

        Attributes:
            chars (int): Counter for the number of characters
                processed, initialized to 0.
            words (list): List to store words encountered during
                processing, initialized as empty.
            output (bool): Flag indicating whether output should
                be generated, initialized to False.
        """

        self.chars: int = 0
        self.words: list = []
        self.output: bool = False

    def process(self, data: Any) -> str:
        """
        Process input data and return a formatted result string.

        Validates input data and if valid, counts characters and words
        in the text. Updates instance attributes with processing results.

        Args:
            data: Any input data to process. Expected to be text for
                successful validation.

        Returns:
            str: A formatted string containing:
            - If validation fails: Message indicating no text found
            - If validation succeeds: Processing summary with
              character and word counts
        """

        if not self.validate(data):
            return f"Processing data: \"{data}\".\n" \
                "Not text found. Exiting..."
        else:
            self.chars = 0
            for c in data:
                self.chars += 1
            self.words = data.split()
            self.output = True
            return f"Processing data: \"{data}\"\n" \
                "Validation: Text data verified\n" \
                f"Processed text: {self.chars} characters, " \
                f"{len(self.words)} words"

    def validate(self, data: Any) -> bool:
        """
        Validate if the given data is a string type.

        This method attempts to concatenate the data with an empty
        string to check if it's a string or string-compatible type.

        Args:
            data (Any): The data to validate.

        Returns:
            bool: True if the data is a string or can be concatenated
            with a string, False otherwise.
        """

        try:
            data = data + ""
            return True
        except TypeError:
            return False

    def format_output(self, result: str = "This is a std output"):
        """
        Format and print the output of the processed text.

        Args:
            result (str, optional): The result string to be formatted.
                Defaults to "This is a std output".

        Returns:
            None: This method prints the output if self.output is
                True, displaying the character count and word count
                of the processed text.
        """

        if self.output:
            print(f"Processed text: {self.chars} characters, "
                  f"{len(self.words)} words")


class LogProcessor(DataProcessor):
    """
    A processor class for handling log entries.

    This class extends DataProcessor to provide specialized handling
    for log data, including validation, processing, and formatted
    output of log entries.

    Attributes:
        output (bool): Flag indicating whether valid output has been
            generated.
        output_msg (str): The formatted output message from the last
            processed log entry.

    Methods:
        process(data: Any) -> str:
            Processes a log entry dictionary and returns a formatted
            result string. Validates the data and sets output
            attributes if valid.

        validate(data: Any) -> bool:
            Validates that the provided data contains required log
            entry fields.

        format_output(result: str = "This is a std output"):
            Prints the stored output message if valid output was
            generated.
    """

    def __init__(self):
        """
        Initialize a new LogProcessor instance.

        Attributes:
            output (bool): Flag indicating whether output should be
                generated, initialized to False.
            output_msg (str): The output message string, initialized
                as empty.
        """
        self.output: bool = False
        self.output_msg: str = ""

    def process(self, data: Any) -> str:
        """
        Process a log entry dictionary and return a formatted result.

        Args:
            data (Any): A dictionary expected to contain 'type',
                'level', and 'message' keys.

        Returns:
            str: A formatted string containing processing status
                and log information.
        """
        if not self.validate(data):
            return "Processing data: " \
                f"\"{data['level']}\": {data['message']}\nPassed data " \
                "is not a valid log entry. Exiting..."
        else:
            self.output = True
            self.output_msg = f"[{data['type']}] " \
                f"{data['level']} level detected: {data['message']}"
            return f"Processing data: \"{data['level']}\": " \
                f"{data['message']}\nValidation: Log entry verified\n" \
                f"Output: {self.output_msg}"

    def validate(self, data: Any) -> bool:
        """
        Validate that data contains required log entry fields.

        Args:
            data (Any): A dictionary to validate.

        Returns:
            bool: True if data contains 'type', 'level', and
                'message' keys, False otherwise.
        """
        return ("type" in data and "level" in data and "message" in data)

    def format_output(self, result: str = "This is a std output"):
        """
        Print the stored output message if valid output was generated.

        Args:
            result (str, optional): Default output string.
                Defaults to "This is a std output".

        Returns:
            None
        """
        if self.output:
            print(f"{self.output_msg}")


def ft_main():
    """
    Main function demonstrating the Data Processor Foundation system.

    This function showcases polymorphic processing capabilities by:
    - Initializing and testing NumericProcessor with numeric list data
    - Initializing and testing TextProcessor with string and mixed data types
    - Initializing and testing LogProcessor with dictionary log entries
    - Demonstrating polymorphic processing through a unified interface

    The function processes various data types (lists, strings, dictionaries)
    through specialized processor classes that inherit from a common
    DataProcessor interface, illustrating object-oriented design patterns.

    Returns:
        None: This function prints output directly to stdout.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    num_data: list = [[1, 2, 3, 4, 5],]

    num: NumericProcessor = NumericProcessor()
    for item in num_data:
        # num: NumericProcessor = NumericProcessor()
        msg: str = num.process(item)
        if num.validate(item):
            DataProcessor.format_output(msg)

    print("\nInitializing Text Processor..")
    text_data: list = ["Hello Nexus World", 12]

    txt: TextProcessor = TextProcessor()
    for item in text_data:
        # txt: TextProcessor = TextProcessor()
        msg: str = txt.process(item)
        DataProcessor.format_output(msg)

    print("\nInitializing Log Processor...")
    log_data: dict = {
        "type": "ALERT", "level": "ERROR", "message": "Connection timeout"}
    log: LogProcessor = LogProcessor()
    msg: str = (log.process(log_data))
    DataProcessor.format_output(msg)

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")
    num_data: list = [1, 2, 3]
    num: NumericProcessor = NumericProcessor()
    num.process(num_data)
    print("Result 1: ", end="")
    num.format_output()

    my_str: str = "Hello World!"
    txt: TextProcessor = TextProcessor()
    txt.process(my_str)
    print("Result 2: ", end="")
    txt.format_output()

    log_data: dict = {
        "type": "INFO", "level": "INFO", "message": "System ready"}
    log: LogProcessor = LogProcessor()
    log.process(log_data)
    print("Result 3: ", end="")
    log.format_output()

    print("\nFoundation systems online. Nexus ready for advanced streams.")


ft_main()
