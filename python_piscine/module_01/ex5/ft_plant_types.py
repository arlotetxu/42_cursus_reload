#!/usr/bin/env python3

class Plant:
    """
    A class representing a plant with basic attributes and behaviors.
    This module defines a Plant class that tracks plant information including
    name, height, and age. It includes validation to prevent negative values
    for height and age.

    Attributes:
        num_plants (int): Class variable that tracks the total number of Plant
            instances created.
    Example:
        >>> plant = Plant("Rose", 30, 60)
        >>> plant.get_info()
        Rose (Plant): 30cm, 60 days,
        >>> plant.set_height(35)
        Height updated: 35cm [OK]
        >>> plant.get_height()
        35
    """

    num_plants = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
        """
        self.name = name
        self._height = height
        self._age = age
        Plant.num_plants += 1

    def get_info(self) -> None:
        """
        Display information about the plant.

        Prints the plant's name, class type, height in centimeters,
        and age in days to the standard output.

        Returns:
            None
        """

        print(f"\n{self.name} ({self.__class__.__name__}): {self._height}cm, "
              f"{self._age} days", end=", ")

    def get_height(self) -> int:
        """
        Get the height of the plant. GETTER

        Returns:
            int: The height of the plant.
        """

        return self._height

    def set_height(self, value: int) -> None:
        """
        Changes the plant's height by a given value. This value must be psitive
        otherwise the change is not executed. SETTER

        Args:
            value (int): The new value to update the plant's height
        """
        if value < 0:
            print("\nInvalid operation attempted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm [OK]")

    def get_age(self) -> int:
        """
        Get the age of the plant. GETTER

        Returns:
            int: The age of the plant.
        """
        return self._age

    def set_age(self, value: int) -> None:
        """
        Changes the plant's age by a given value. This value must be psitive
        otherwise the change is not executed. SETTER

        Args:
            value (int): The new value to update the plant's age
        """
        if value < 0:
            print(f"\nInvalid operation attempted: age {value}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days [OK]")


class Flower(Plant):
    """
    A class representing a Flower, which is a type of Plant.

    Flower extends the Plant class and adds color as an additional attribute.
    It also provides functionality to simulate blooming.

    Attributes:
        name (str): The name of the flower.
        height (int): The height of the flower in cm.
        age (int): The age of the flower in days.
        color (str): The color of the flower.

    Methods:
        __init__(name, height, age, color): Initializes a new Flower instance.
        bloom(): Displays a message indicating that the flower is blooming.
    """

    def __init__(self, name, height, age, color: str) -> None:
        """
        Initializes a new Flower instance. Prints basics & specific features

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
            color (str): The flower's color
        """
        super().__init__(name, height, age)
        self.color = color
        self.get_info()
        print(f"{self.color} color")

    def bloom(self) -> None:
        """
        Display a message indicating that the plant is blooming.

        Returns:
            None
        """

        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    A class representing a Tree, which is a type of Plant.

    Tree extends the Plant class and adds tree-specific attributes and
    behaviors, such as trunk diameter and shade production.

    Attributes:
        name (str): The name of the tree.
        height (int): The height of the tree in cm.
        age (int): The age of the tree in days.
        trunk_diameter (int): The diameter of the tree's trunk in cm.

    Methods:
        produce_shade(): Calculates and displays the shade area produced by
        the tree.
    """

    def __init__(self, name, height, age, trunk_diameter: int) -> None:
        """
        Initializes a new Tree instance. Prints basics & specific features

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
            trunk_diameter (int): The tree's trunk diameter
            shade (int): The shade the tree generates
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.get_info()
        print(f"{self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """
        Calculate and display the shade produced by the tree.
        The shade area is calculated by multiplying the trunk diameter by 4.
        Returns:
            None: Prints the shade area in square meters to stdout.
        """

        shade = self.trunk_diameter * 4
        print(f"{self.name} provides {shade} square meters of "
              f"shade")


class Vegetable(Plant):
    """
    A class representing a vegetable, which is a type of Plant.

    The Vegetable class extends the Plant class and adds specific attributes
    related to vegetables such as harvest season and nutritional value.

    Attributes:
        name (str): The name of the vegetable.
        height (int): The height of the vegetable in cm.
        age (int): The age of the vegetable in days.
        harvest_season (str): The season when the vegetable should be
            harvested.
        nutritional_value (str): The nutritional benefits of the vegetable.

    Methods:
        __init__(name, height, age, harvest_season, nutritional_value):
            Initializes a new vegetable instance with the given attributes.
        nutritional_info():
            Displays the nutritional information of the vegetable.
    """

    def __init__(self, name, height, age, harvest_season: str,
                 nutritional_value: str):
        """Initializes a new vegetable instance. Prints basics & specific
        features

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
            harvest_season (str): The season to harvest the vegetable
            nutritional_value (str): The specific nutrition vegetable feature
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.get_info()
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":

    plant_data = {
        "Flower": [
            {"name": "Rose", "height": 25.0, "age": 30, "color": "red"},
            {"name": "Sunflower", "height": 80.0, "age": 45,
             "color": "yellow"},
            {"name": "Violet", "height": 15.0, "age": 15, "color": "purple"},
        ],
        "Tree": [
            {"name": "Oak", "height": 500.0, "age": 100,
             "trunk_diameter": 25, },
            {"name": "Pine", "height": 700.0, "age": 30,
             "trunk_diameter": 5, },
            {"name": "Beech", "height": 500.0, "age": 80,
             "trunk_diameter": 15, },
        ],
        "Vegetable": [
            {"name": "Tomato", "height": 80.0, "age": 91,
             "harvest_season": "summer", "nutritional_value": "vitamin C"},
            {"name": "Pepper", "height": 20.0, "age": 90,
             "harvest_season": "summer", "nutritional_value": "vitamin C"},
            {"name": "Eggplant", "height": 25.0, "age": 100,
             "harvest_season": "autumn", "nutritional_value": "vitamin A"},
        ]
    }

    print("=== Garden Plant Types ===")
    for plant_type, plants in plant_data.items():
        for plant_details in plants:
            if plant_type == "Flower":
                f_instance = Flower(name=plant_details["name"],
                                    height=plant_details["height"],
                                    age=plant_details["age"],
                                    color=plant_details["color"])
                f_instance.bloom()
            elif plant_type == "Tree":
                t_instance = Tree(name=plant_details["name"],
                                  height=plant_details["height"],
                                  age=plant_details["age"],
                                  trunk_diameter=plant_details["trunk_"
                                                               "diameter"],)
                t_instance.produce_shade()
            elif plant_type == "Vegetable":
                v_instance = Vegetable(name=plant_details["name"],
                                       height=plant_details["height"],
                                       age=plant_details["age"],
                                       harvest_season=plant_details["harvest_"
                                                                    "season"],
                                       nutritional_value=plant_details["nutr"
                                                                       "itio"
                                                                       "nal_"
                                                                       "valu"
                                                                       "e"])
