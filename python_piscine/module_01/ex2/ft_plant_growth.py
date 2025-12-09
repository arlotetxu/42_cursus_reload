#!/usr/bin/env python3

class Plant:
    """
    A class to represent a plant and track its growth over time.

    This module provides a Plant class that allows tracking and simulating
    the growth of plants by monitoring their name, height, and age.

    Classes:
        Plant: Represents a plant with name, height, and age attributes.

    Example:
        >>> plant = Plant("Sunflower", 10.5, 30)
        >>> plant.get_info()
        Sunflower: 10.5cm, 30 days old
        >>> plant.grow(5.0)
        >>> plant.add_age(7)
        >>> print(plant)
        Plant: Sunflower / Height: 15.5cm / Age: 36 days
    """

    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initialize a Plant instance.

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

    def get_info(self) -> None:
        """
        Display information about the plant.

        Prints the plant's name, current height in centimeters, and age in days
        to the standard output.

        Returns:
            None
        """

        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, q_grow: float) -> None:
        """
        Increase the plant's height by a specified growth amount.

        Args:
            q_grow (float): The quantity of growth to add to the plant's
            height.

        Returns:
            None
        """

        self.height += q_grow

    def add_age(self, q_days: int) -> None:
        """
        Increment the plant's age by a specified number of days minus one.

        Args:
            q_days (int): The quantity of days to add to the plant's age.
                          The actual increment will be q_days - 1.

        Returns:
            None
        """

        self.age += q_days - 1

    def __repr__(self) -> str:
        """
        Return a string representation of the Plant object.

        Returns:
            str: A formatted string containing the plant's name, height in cm,
                 and age in days.
        """

        return f"Plant: {self.name} / Height: {self.height}cm " \
            f"/ Age: {self.age} days"


def ft_plant_growth(name: str, height: float, age: int) -> None:
    """
    Simulates the growth of a plant over a week and prints its progress.

    Args:
        name (str): The name of the plant (e.g., "Rose", "Sunflower",
        "Cactus").
        height (float): The initial height of the plant in cm.
        age (int): The initial age of the plant in days.

    Returns:
        None
    """
    q_grow = 0
    plant = Plant(name=name, height=height, age=age)

    print("=== Day 1 ===")
    plant.get_info()

    if name.lower() == "rose":
        q_grow = 6
    elif name.lower() == "sunflower":
        q_grow = 10
    elif name.lower() == "cactus":
        q_grow = 2
    else:
        q_grow = 0

    plant.grow(q_grow=q_grow)  # A growth of each plant
    plant.add_age(q_days=7)  # 7 days passed

    print(f"=== Day {plant.age - age + 1} ===")
    plant.get_info()

    print(f"Growth this week: {plant.height - height:+}cm\n")


if __name__ == "__main__":
    ft_plant_growth(name="Rose", height=25.0, age=30)
    ft_plant_growth(name="Sunflower", height=80.0, age=45)
    ft_plant_growth(name="Cactus", height=15, age=120)
