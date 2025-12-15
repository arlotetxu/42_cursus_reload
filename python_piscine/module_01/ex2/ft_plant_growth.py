#!/usr/bin/env python3

class Plant:
    """
    A class to represent a plant and track its growth over time.

    This module provides a Plant class that allows tracking and simulating
    the growth of plants by monitoring their name, height, and age.

    Classes:
        Plant: Represents a plant with name, height, and age attributes.

    Example:
        >>> plant = Plant("Sunflower", 10, 30)
        >>> plant.get_info()
        Sunflower: 10cm, 30 days old
        >>> plant.grow(5)
        >>> plant.age(7)
    """

    def __init__(self, name: str, height: int, p_age: int) -> None:
        """
        Initialize a Plant instance.

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
        Increase the plant's height by a specified growth amount.

        Args:
            q_grow (int): The quantity of growth to add to the plant's
            height.

        Returns:
            None
        """

        self.height += q_grow

    def age(self, q_days: int) -> None:
        """
        Increment the plant's age by a specified number of days minus one.

        Args:
            q_days (int): The quantity of days to add to the plant's age.
                          The actual increment will be q_days - 1.

        Returns:
            None
        """

        self.p_age += q_days - 1


# MAIN=======================================================================
if __name__ == "__main__":

    q_grow = 0

    plant_1 = Plant(name="Rose", height=25, p_age=30)
    plant_2 = Plant(name="Sunflower", height=80, p_age=45)
    plant_3 = Plant(name="Cactus", height=15, p_age=120)

    plants = [plant_1, plant_2, plant_3]

    for plant in plants:
        plant_height = plant.height
        plant_age = plant.p_age

        print("=== Day 1 ===")
        plant.get_info()

        if plant.name.lower() == "rose":
            q_grow = 6
        elif plant.name.lower() == "sunflower":
            q_grow = 10
        elif plant.name.lower() == "cactus":
            q_grow = 2
        else:
            q_grow = 0

        plant.grow(q_grow=q_grow)  # A growth of each plant
        plant.age(q_days=7)  # 7 days passed

        print(f"=== Day {plant.p_age - plant_age + 1} ===")
        plant.get_info()
        print(f"Growth this week: {plant.height - plant_height:+}cm\n")
