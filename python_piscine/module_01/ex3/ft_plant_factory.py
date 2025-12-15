#!/usr/bin/env python3

class Plant:
    """
    A class representing a plant with basic growth tracking functionality.

    This module provides a Plant class that can be used to create and manage
    plant instances, tracking their name, height, and age over time.

    Attributes:
        num_plants (int): Class variable that tracks the total number of
            Plant instances created.

    Example:
        >>> plant = Plant("Rose", 10, 30)
        >>> plant.get_info()
        Created: Rose (10cm, 30 days)
        >>> plant.grow(2)
        >>> print(plant)
        Plant(name='Rose', height=12, age=30)
    """

    num_plants = 0

    def __init__(self, name: str, height: int, p_age: int) -> None:
        """
        Initialize a new Plant instance.
        Args:
            name (str): The name of the plant.
            height (int): The height of the plant.
            p_age (int): The age of the plant.
        Returns:
            None
        """

        self.name = name
        self.height = height
        self.p_age = p_age
        Plant.num_plants += 1
        print(f"Created: {self.name} ({self.height}cm, {self.p_age} days)")

    def get_info(self) -> None:
        """
        Display information about the plant.

        Prints the plant's name, current height in centimeters, and age in days
        to the standard output.

        Returns:
            None
        """

        print(f"{self.name}: {self.height}cm, {self.p_age} days old")

    def grow(self, q_grow: int) -> None:
        """
        Increases the plant's height by the specified growth amount.
        Args:
            q_grow (int): The quantity to add to the plant's current height.
        Returns:
            None
        """

        self.height += q_grow

    def age(self, q_days: int) -> None:
        """
        Increases the plant's age by the specified number of days minus one.
        Args:
            q_days (int): The quantity of days to add to the plant's age.
                          The actual age increase will be q_days - 1.
        Returns:
            None
        """

        self.p_age += q_days - 1


# MAIN=======================================================================
if __name__ == "__main__":
    # Define all plants to be created in one place
    plant_definitions = [
        {'name': "Rose", 'height': 25, 'age': 30},
        {'name': "Oak", 'height': 200, 'age': 365},
        {'name': "Cactus", 'height': 5, 'age': 90},
        {'name': "Sunflower", 'height': 80, 'age': 45},
        {'name': "Fern", 'height': 15, 'age': 120},
    ]

    created_plants = []

    # Display the created plants in an organized format
    print("=== Plant Factory Output ===")

    for data in plant_definitions:
        plant = Plant(name=data['name'], height=data['height'],
                      p_age=data['age'])
        created_plants.append(plant)

    print(f"\nTotal plants created: {Plant.num_plants}")
