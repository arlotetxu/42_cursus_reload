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
    A custom exception class for garden-related errors.

    This exception is raised when issues occur in garden management operations.

    Attributes:
        message (str): The error message describing the garden issue.
            Defaults to "Exception: Garden with issues".

    Example:
        >>> raise GardenError("Invalid plant type")
        GardenError: Invalid plant type

        >>> raise GardenError()
        GardenError: Exception: Garden with issues
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
    Exception raised when a plant's water level is outside acceptable bounds.

    This exception is raised when a plant has a water level that is either
    too high (greater than 10) or too low (less than 1).

    Attributes:
        Inherits from GardenError.

    Args:
        plant_ (Plant): The plant object with an invalid water level.

    Raises:
        WaterError: When plant_.water > 10 or plant_.water < 1.

    Example:
        >>> plant = Plant(name="Rose", water=15)
        >>> raise WaterError(plant)
        WaterError: Error checking Rose: Water level 15 is too high (max 10)
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
    Exception raised when a plant has invalid sun light requirements.

    This exception is a subclass of GardenError and is raised when a plant's
    sun light requirement falls outside the acceptable range of 2 to 12 hours.

    Attributes:
        Inherits all attributes from GardenError.

        plant_ (Plant): The plant object with invalid sun light requirements.

        GardenError: When sun light is above 12 (too high) or below 2
        (too low).

    Example:
        >>> plant = Plant(name="Sunflower", sun=15)
        >>> raise SunError(plant)
        GardenError: Error checking Sunflower: sun light 15 is too high
        (max 12)
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
    A class to manage a garden with plants and water resources.

    This class provides functionality to add plants, water them,
    check their health status, and monitor water tank levels.

    Attributes:
        plants (list): A list of plant objects in the garden.
        water_tank (int): The current water level in the tank, initialized
        to 2.

    Methods:
        add_plant(plant_):
            Adds a plant to the garden if it has a valid name and is not
            already present.

        watering():
            Waters all plants in the garden, incrementing each plant's water
            level by 1 and decrementing the water tank by 1 for each plant.

        checking():
            Checks the health status of all plants based on water and sun
            levels.
            Prints health status for healthy plants or catches and prints
            errors for plants with invalid water (not between 1-10) or sun
            (not between 2-12) levels.

            Raises:
                WaterError: If a plant's water level is outside the valid
                range.
                SunError: If a plant's sun level is outside the valid range.

        water_tank_check():
            Verifies if there is sufficient water in the tank.

            Raises:
                GardenError: If the water tank level is below 2.
    """

    def __init__(self):
        """
        Initialize a new Garden instance.

        Attributes:
            plants (list): An empty list to store plants in the garden.
            water_tank (int): The initial water tank capacity, set to 2.
        """

        self.plants = []
        self.water_tank = 2

    def add_plant(self, plant_):
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

        for plant_ in self.plants:
            print(f"Watering {plant_.name} -success")
            plant_.water += 1
            self.water_tank -= 1

    def checking(self):
        """
        Check the health status of all plants in the garden.

        Iterates through all plants and validates their water and sun levels.
        Plants with water levels outside the range 1-10 will raise a
        WaterError.
        Plants with sun levels outside the range 2-12 will raise a SunError.
        Healthy plants will have their status printed with current water and
        sun values.

        Raises:
            WaterError: If a plant's water level is less than 1 or greater
            than 10.
            SunError: If a plant's sun level is less than 2 or greater
            than 12.

        Note:
            Exceptions are caught and printed rather than propagated.
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
if __name__ == "__main__":
    print("=== Garden Management System ===")
    manager = GardenManager()

    plants = []
    plant_1 = Plant("tomato", 4, 8)
    plants.append(plant_1)
    plant_2 = Plant("lettuce", 14, 2)
    plants.append(plant_2)
    plant_3 = Plant("", 1, 2)
    plants.append(plant_3)

    print("\nAdding plants to garden...")
    try:
        for plant in plants:
            manager.add_plant(plant)
    except GardenError as e:
        print(e)

    print("\nWatering plants...")
    try:
        print("Opening watering system")
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
