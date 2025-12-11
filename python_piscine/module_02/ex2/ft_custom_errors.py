#!/usr/bin/env python3


class GardenError(Exception):
    """
    A custom exception class for garden-related errors.

    This exception is raised when there are issues related to garden operations
    or garden-related functionality.

    Attributes:
        message (str): The error message describing the garden issue.
            Defaults to "Exception: Garden with issues".

    Example:
        >>> raise GardenError("Invalid plant type")
        Traceback (most recent call last):
            ...
        GardenError: Invalid plant type

        >>> raise GardenError()
        Traceback (most recent call last):
            ...
        GardenError: Exception: Garden with issues
    """
    def __init__(self, message: str = "Exception: Garden with issues") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    """
    Exception raised when a plant encounters an error in the garden.

    This exception is a subclass of GardenError and is specifically used
    to indicate issues with individual plants.

    Attributes:
        plant_name (str): The name of the plant that encountered the error.

    Example:
        >>> raise PlantError("Rose")
        PlantError: The Rose plant is wilting!
    """
    def __init__(self, plant_name: str) -> None:
        self.plant_name = plant_name
        message = f"The {self.plant_name} plant is wilting!"
        GardenError.__init__(self, message)


class WaterError(GardenError):
    """
    Exception raised when there is insufficient water in the tank.

    This exception is a subclass of GardenError and is raised when
    water-related operations.

    Attributes:
        message (str): Explanation of the error, defaults to "Not enough water
        in the tank!"

    Example:
        >>> raise WaterError()
        GardenError: Not enough water in the tank!
    """
    def __init__(self) -> None:
        message = "Not enough water in the tank!"
        GardenError.__init__(self, message)


def test_plant_error(plant: str) -> None:
    """
    Test function to demonstrate the PlantError exception.

    This function raises a PlantError with the given plant name and then
    catches it, printing the error information.

    Args:
        plant (str): The name of the plant to include in the error.

    Returns:
        None

    Raises:
        PlantError: Always raised internally but caught within the function.
    """
    try:
        raise PlantError(plant)
    except PlantError as pe:
        print(f"Caught {pe.__class__.__name__}: {pe}")


def test_water_error() -> None:
    """
    Test function for the WaterError exception.

    This function demonstrates the raising and catching of a WaterError
    exception. It raises a WaterError within a try block and catches it
    in the except block, then prints the exception class name and message.

    Returns:
        None

    Raises:
        WaterError: Raised intentionally to test exception handling.
    """
    try:
        raise WaterError()
    except WaterError as we:
        print(f"Caught {we.__class__.__name__}: {we}")


def test_all_errors(plant: str) -> None:
    """
    Test function that demonstrates custom error handling in a garden context.

    This function creates instances of PlantError and WaterError, raises each
    one, and catches them as their parent GardenError type to demonstrate
    polymorphic exception handling.

    Args:
        plant (str): The name of the plant to be used when creating a
        PlantError.

    Returns:
        None

    Raises:
        No exceptions escape this function as all GardenError instances are
        caught and handled internally.

    Example:
        >>> test_all_errors("rose")
        Caught a garden error: PlantError: rose
        Caught a garden error: WaterError
    """
    errors = [PlantError(plant), WaterError()]

    for error in errors:
        try:
            raise error
        except GardenError as ge:
            print(f"Caught a garden error: {ge}")


# if __name__ == "__main__":
#     print("=== Custom Garden Errors Demo ===")
#     print("\nTesting PlantError...")
#     test_plant_error("tomato")
#     print("\nTesting WaterError...")
#     test_water_error()
#     print("\nTesting catching all garden errors...")
#     test_all_errors("tomato")
#     print("\nAll custom error types work correctly!")
