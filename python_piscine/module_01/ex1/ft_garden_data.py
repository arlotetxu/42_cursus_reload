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

    def get_garden_data(self) -> None:
        """
        Prints the garden data for the current plant instance.

        Displays the plant's name, height in centimeters, and age in days
        in a formatted string to the standard output.

        Returns:
            None
        """

        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def __repr__(self) -> str:
        """
        Return a string representation of the Plant object.

        Returns:
            str: A formatted string containing the plant's name, height in
                centimeters, and age in days.
        """
        return f"Plant: {self.name} / Height: {self.height}cm " \
            f"/ Age: {self.age} days"


if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant_1.get_garden_data()
    plant_2.get_garden_data()
    plant_3.get_garden_data()
