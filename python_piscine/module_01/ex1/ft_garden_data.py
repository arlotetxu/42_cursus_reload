#!/usr/bin/env python3

class Plant:
    """
    A class to represent a plant in a garden.

    Attributes
    ----------
    name : str
        The name of the plant.
    height : int
        The height of the plant in centimeters.
    age : int
        The age of the plant in days.

    Methods
    -------
    get_garden_data() -> None:
        Prints the plant's name, height, and age.
    __repr__() -> str:
        Returns a string representation of the plant.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new instance of the class.

        Args:
            name (str): The name of the object.
            height (int): The height of the object.
            age (int): The age of the object.

        Returns:
            None
        """
        self.name = name
        self.height = height
        self.age = age


# MAIN======================================================================
if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)

    plants = [plant_1, plant_2, plant_3]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
