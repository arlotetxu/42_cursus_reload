#!/usr/bin/env python3

def garden_operations(error_type: int):
    """
    Demonstrate different types of Python errors based on error type.

    Args:
        error_type (int): An integer specifying which error to raise:
            - 1: ValueError - Raises when converting non-numeric string to int
            - 2: ZeroDivisionError - Raises when dividing by zero
            - 3: FileNotFoundError - Raises when opening a non-existent file
            - 4: KeyError - Raises when accessing a non-existent dictionary key

    Raises:
        ValueError: If error_type is 1
        ZeroDivisionError: If error_type is 2
        FileNotFoundError: If error_type is 3
        KeyError: If error_type is 4
    """

    if error_type == 1:
        int("abc")
    elif error_type == 2:
        1 / 0
    elif error_type == 3:
        with open("missing.txt", "r") as fd:
            fd.readlines()
    elif error_type == 4:
        my_dict = {"0": 0}
        my_dict["_plant"]


def test_error_types():
    """
    This function tests the garden_operations function with various inputs that
    trigger different types of exceptions: ValueError, ZeroDivisionError,
    FileNotFoundError, and KeyError. Each exception is caught and handled
    individually, with informative messages printed to the console.

    The function also demonstrates catching multiple exception types together
    in a single try-except block.

    Raises:
        No exceptions are raised; all exceptions are caught and handled
        internally.

    Returns:
        None
    """
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations(1)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations(2)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations(3)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_operations(4)
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")

    print("\nTesting multiple errors together...")
    try:
        for test in range(1, 5):
            garden_operations(test)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


test_error_types()
