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
        >>> plant = Plant("Rose", 10.5, 30)
        >>> plant.get_info()
        Created: Rose (10.5cm, 30 days)
        >>> plant.grow(2.5)
        >>> print(plant)
        Plant(name='Rose', height=13.0, age=30)

    Note:
        There is a naming conflict between the `age` attribute and the `age`
        method. Consider renaming the method to `add_age` or `increase_age`
        to avoid this issue.
    """

    num_plants = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initialize a new Plant instance.
        Args:
            name (str): The name of the plant.
            height (float): The height of the plant.
            age (int): The age of the plant.
        Returns:
            None
        """

        self.name = name
        self.height = height
        self.age = age
        Plant.num_plants += 1

    def get_info(self) -> None:
        """
        Print information about the plant.

        Displays the plant's name, height in centimeters, and age in days
        to the standard output.
        Returns:
            None
        """

        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def grow(self, q_grow: float) -> None:
        """
        Increases the plant's height by the specified growth amount.
        Args:
            q_grow (float): The quantity to add to the plant's current height.
        Returns:
            None
        """

        self.height += q_grow

    def aging(self, q_days: int) -> None:
        """
        Increases the plant's age by the specified number of days minus one.
        Args:
            q_days (int): The quantity of days to add to the plant's age.
                          The actual age increase will be q_days - 1.
        Returns:
            None
        """

        self.age += q_days - 1

    def __repr__(self) -> str:
        """Return a string representation of the Plant object.
        Returns:
            str: A formatted string containing the plant's name, height, and
                age in the format "Plant(name='...', height=..., age=...)".
        """

        return f"Plant(name='{self.name}', height={self.height}, " \
               f"age={self.age})"


def ft_plant_factory(plants_data: list[dict]) -> list[Plant]:
    """
    Creates multiple Plant instances from a list of data.

    This function acts as a factory, taking a list of dictionaries where each
    dictionary contains the data for one plant, and returns a list of
    created Plant objects.

    Args:
        plants_data (list[dict]): A list where each item is a dictionary
                                  with 'name', 'height', and 'age' keys.

    Returns:
        list[Plant]: A list containing all the created Plant instances.
    """
    created_plants = []
    for data in plants_data:
        plant = Plant(name=data['name'], height=data['height'],
                      age=data['age'])
        created_plants.append(plant)
    return created_plants


if __name__ == "__main__":
    # Define all plants to be created in one place
    plant_definitions = [
        {'name': "Rose", 'height': 25.0, 'age': 30},
        {'name': "Oak", 'height': 200.0, 'age': 365},
        {'name': "Cactus", 'height': 5.0, 'age': 90},
        {'name': "Sunflower", 'height': 80.0, 'age': 45},
        {'name': "Fern", 'height': 15.0, 'age': 120},
    ]

    # Use the factory to create all plants at once
    garden = ft_plant_factory(plant_definitions)

    # Display the created plants in an organized format
    print("=== Plant Factory Output ===")
    for plant in garden:
        plant.get_info()

    print(f"\nTotal plants created: {Plant.num_plants}")
