#!/usr/bin/env python3


def check_temperature(temp_str: str) -> None:
    """
    Checks if the given temperature string represents a valid temperature
    for plants.

    Args:
        temp_str (str): The temperature value as a string.

    Returns:
        None

    Behavior:
        - Prints an error if the temperature is below 0°C or above 40°C.
        - Prints a success message if the temperature is within the
            acceptable range (0°C to 40°C inclusive).
        - Prints an error if the input string cannot be converted to an
            integer.
    """

    print(f"\nTesting temperature: {temp_str}")
    try:
        ret: int = int(temp_str)
        if ret < 0:
            print(f"Error: {ret}ºC is too cold for plants (min 0ºC)")
        elif ret > 40:
            print(f"Error: {ret}ºC is too hot for plants (max 40ºC)")
        else:
            print(f"Temperature {ret}ºC is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    """
    Runs a series of test cases for the check_temperature function using
    predefined arguments.

    This function prints a header, iterates over a set of test temperature
    inputs (including valid and invalid values), and calls the
    check_temperature function for each input. After all tests are run,
    it prints a completion message indicating that the program did not crash.

    Returns:
        None
    """
    print("=== Garden Temperature Checker ===")
    args: list = ["25", "abc", "100", "-50"]
    for arg in args:
        check_temperature(arg)
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
