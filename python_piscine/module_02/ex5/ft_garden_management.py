#!/usr/bin/env python3

class Plant:
    """
    A class representing a plant with its basic care requirements.

    Attributes:
        name (str): The name of the plant.
        water (int): The water requirement level for the plant.
        sun (int): The sunlight requirement level for the plant.
    """

    def __init__(self, name: str, water: int, sun: int) -> None:
        """
        Initialize a new garden plant instance.

        Args:
            name (str): The name of the plant.
            water (int): The water requirement level for the plant.
            sun (int): The sun exposure requirement level for the plant.
        """

        self.name = name
        self.water = water
        self.sun = sun


# CUSTOM EXCEPTIONS==========================================================
class GardenError(Exception):
    """
    GardenError is a custom exception class for handling errors related to
    garden management.

    Attributes:
        message (str): The error message describing the garden issue.

        message (str, optional): The error message to be displayed. Defaults
            to "Exception: Garden with issues".

    Example:
        raise GardenError("Garden is overgrown")
    """

    def __init__(self, message: str = "Exception: Garden with issues") -> None:
        """
        Initialize a garden management exception.

        Args:
            message (str, optional): The error message describing the garden
            issue.
                Defaults to "Exception: Garden with issues".

        Returns:
            None
        """
        Exception.__init__(self, message)


class PlantError(GardenError):
    """
    Exception class for plant-related errors in the garden management system.

    This class extends GardenError to provide specific exception handling
    for errors that occur when working with plants.

    Attributes:
        message: A string describing the error that occurred.

    Args:
        message: A descriptive error message explaining the plant-related
        issue.

    Returns:
        None
    """

    def __init__(self, message) -> None:
        """
        Initialize a GardenError subclass instance.

        Args:
            message: The error message to be passed to the parent GardenError
            class.

        Returns:
            None
        """
        GardenError.__init__(self, message)


class WaterError(GardenError):
    """
    Exception raised for invalid water levels in a Plant instance.

    This exception is triggered when a plant's water level is outside the
    valid range (1-10). A water level above 10 is considered too high,
    and below 1 is considered too low.

    Raises:
        GardenError: If the plant's water level is not within the allowed
            range.

    Attributes:
        message (str): Explanation of the error, indicating whether the water
            level is too high or too low.
    """

    def __init__(self, plant_: Plant) -> None:
        """
        Initialize a WaterError exception for invalid water levels.

        Args:
            plant_ (Plant): The plant instance with an invalid water level.

        Raises:
            GardenError: When the plant's water level is outside the valid
            range (1-10).

        Note:
            A water level above 10 is considered too high.
            A water level below 1 is considered too low.
        """
        message = ""
        if plant_.water > 10:
            message = f"Error checking {plant_.name}: " \
                f"Water level {plant_.water} is too high (max 10)"
        elif plant_.water < 1:
            message = f"Error checking {plant_.name}: " \
                f"Water level {plant_.water} is too low (min 1)"
        GardenError.__init__(self, message)


class SunError(GardenError):
    """
    Exception raised for invalid sun light conditions for a plant.

    This error is triggered when a plant's sun light requirement is outside
    the valid range (2 to 12, inclusive).

        plant_ (Plant): The plant object whose sun light requirement is being
            validated.

        GardenError: If the plant's sun light requirement is above 12 or
            below 2.

    Attributes:
        message (str): Explanation of the error, specifying whether the sun
        light value is too high or too low.
    """

    def __init__(self, plant_: Plant) -> None:
        """
        Initialize a GardenError for invalid sun light conditions.

        Args:
            plant_ (Plant): The plant object to check for valid sun light
            requirements.

        Raises:
            GardenError: If the plant's sun light requirement is above 12 or
            below 2.

        Note:
            Valid sun light values are between 2 and 12 (inclusive).
        """
        message = ""
        if plant_.sun > 12:
            message = f"Error checking {plant_.name}: " \
                f"sun light {plant_.sun} is too high (max 12)"
        elif plant_.sun < 2:
            message = f"Error checking {plant_.name}: " \
                f"sun light {plant_.sun} is too low (min 2)"
        GardenError.__init__(self, message)


# GARDEN MANAGER CLASS=======================================================
class GardenManager:
    """
    GardenManager is a class responsible for managing a collection of plants
    within a garden.
    It provides functionality to add plants, water them, check their health
    status, and monitor the water tank level.

        Methods:
        __init__():
            Initializes a new GardenManager instance with an empty plant list
            and a water tank.
        add_plant(plant_: Plant):
            Adds a plant to the garden. Raises PlantError if the plant's name
            is empty. Prints a success message upon successful addition.
        watering():
            Waters all plants in the garden by incrementing each plant's
            water level and decrementing the water tank for each plant
            watered. Prints status messages.
        checking():
            Checks the health status of each plant based on their water and
            sun levels. Raises WaterError or SunError if a plant's attributes
            are out of acceptable ranges. Prints the health status or error
            messages for each plant.
        water_tank_check():
            Checks if the water tank has at least 2 units of water.
            Raises GardenError if the water tank level is below the
            threshold.
    """

    def __init__(self):
        """
        Initialize a new Garden instance.

        Attributes:
            plants (list): An empty list to store plants in the garden.
            water_tank (int): The initial water tank capacity, set to 2.
        """

        self.plants: list = []
        self.water_tank: int = 2

    def add_plant(self, plant_: Plant):
        """
        Add a plant to the garden.

        Args:
            plant_: The plant object to be added to the garden.

        Raises:
            PlantError: If the plant name is empty.

        Returns:
            None. Prints a success message upon adding the plant.
        """

        if not plant_.name:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        if plant_ not in self.plants:
            self.plants.append(plant_)
        print(f"Added {plant_.name} successfully")

    def watering(self):
        """
        Waters all plants in the garden by incrementing each plant's water
        level and decrementing the garden's water tank.

        For each plant in the garden, this method:
        - Prints a success message indicating the plant is being watered
        - Increases the plant's water attribute by 1
        - Decreases the garden's water_tank attribute by 1

        Returns:
            None
        """

        print("Opening watering system")
        for plant_ in self.plants:
            print(f"Watering {plant_.name} -success")
            plant_.water += 1
            self.water_tank -= 1

    def checking(self):
        """
        Checks the health status of each plant in the garden based on water
        and sun levels.

        Iterates through all plants in the `self.plants` list and evaluates
        their `water` and `sun` attributes.
        - Raises a `WaterError` if the plant's water level is greater than 10
            or less than 1.
        - Raises a `SunError` if the plant's sun exposure is less than 2 or
            greater than 12.
        - Prints the plant's name and its healthy status if both water and
            sun levels are within acceptable ranges.
        - Catches and prints any `GardenError` exceptions raised during the
            checks.

        Exceptions:
            WaterError: If the plant's water level is out of the acceptable
                range.
            SunError: If the plant's sun exposure is out of the acceptable
                range.
            GardenError: Base exception for garden-related errors.
        """

        for plant_ in self.plants:
            try:
                if plant_.water > 10 or plant_.water < 1:
                    raise WaterError(plant_)
                if plant_.sun < 2 or plant_.sun > 12:
                    raise SunError(plant_)
                print(f"{plant_.name}: healthy (water: {plant_.water}, "
                      f"sun: {plant_.sun})")
            except GardenError as e:
                print(e)

    def water_tank_check(self):
        """
        Check if there is enough water in the tank.

        Raises:
            GardenError: If the water tank level is below 2 units.
        """

        if self.water_tank < 2:
            raise GardenError("Caught GardenError: Not enough water in tank")


# MAIN=======================================================================
def ft_main() -> None:
    print("=== Garden Management System ===")
    manager: GardenManager = GardenManager()

    plants: list = []
    plant_1: Plant = Plant("tomato", 4, 8)
    plants.append(plant_1)
    plant_2: Plant = Plant("lettuce", 14, 2)
    plants.append(plant_2)
    plant_3: Plant = Plant("", 1, 2)
    plants.append(plant_3)

    print("\nAdding plants to garden...")
    try:
        for plant in plants:
            manager.add_plant(plant)
    except GardenError as e:
        print(e)

    print("\nWatering plants...")
    try:
        manager.watering()
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        manager.checking()
    except GardenError as e:
        print(e)

    print("\nTesting error recovery...")
    try:
        manager.water_tank_check()
    except GardenError as e:
        print(e)
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


ft_main()
