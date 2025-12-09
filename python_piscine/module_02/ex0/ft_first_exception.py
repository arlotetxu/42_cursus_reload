#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int:
    """
    Converts a temperature value from string to integer.

    Args:
        temp_str (str): The temperature value as a string.

    Returns:
        int: The temperature value as an integer if conversion is successful.

    Raises:
        ValueError: If the input string cannot be converted to an integer.
    """
    try:
        temp_int = int(temp_str)
        return temp_int
    except ValueError:
        pass


def test_temperature_input() -> None:
    """
    Test function to validate temperature input handling and error cases.

    This function tests the check_temperature function with various input
    values including valid temperatures, invalid strings, and out-of-range
    values.

    It prints a formatted report for each test case.

    Test cases include:
    - "25": Valid temperature within acceptable range
    - "abc": Invalid non-numeric input
    - "100": Valid number but too hot
    - "-50": Valid number but too cold

    Returns:
        None
    """
    args = ("25", "abc", "100", "-50")

    print("=== Garden Temperature Checker ===\n")
    for arg in args:
        ret = check_temperature(arg)
        print(f"Testing temperature: {arg}")
        if ret is None:
            print(f"Error: '{arg}' is not a valid number\n")
        elif ret >= 0 and ret <= 40:
            print(f"Temperature {ret}ºC is perfect for plants!\n")
        elif ret < 0:
            print(f"Error: {ret}ºC is too cold for plants (min 0ºC)\n")
        elif ret > 40:
            print(f"Error: {ret}ºC is too hot for plants (max 40ºC)\n")
    print("All tests completed - program didn't crash!")


# if __name__ == "__main__":
#     test_temperature_input()
