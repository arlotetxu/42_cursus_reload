#!/usr/bin/env python3

class Plant:
    """
    Represents a single plant with properties like name, height, and age.
    """

    num_plants = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initializes a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (float): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
        """
        self.name = name
        self._height = height
        self._age = age
        Plant.num_plants += 1

    def get_info(self) -> None:
        """
        Prints the current information about the plant.
        """
        print(f"{self.name} ({self.__class__.__name__}): {self._height}cm, "
              f"{self._age} days", end=", ")

    @property
    def height(self) -> float:
        """
        Prints the plant's height. GETTER

        Returns:
            float: self._height
        """
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """
        Changes the plant's height by a given value. This value must be psitive
        otherwise the change is not executed.

        Args:
            value (float): The new value to update the plant's height
        """
        if value < 0:
            print("\nInvalid operation attempted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm [OK]")

    @property
    def age(self) -> int:
        """
        Prints the plant's age. GETTER

        Returns:
            float: self._age
        """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """_summary_
        Changes the plant's age by a given value. This value must be psitive
        otherwise the change is not executed.

        Args:
            value (int): The new value to update the plant's age
        """
        if value < 0:
            print(f"\nInvalid operation attempted: age {value}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days [OK]")

    def __repr__(self) -> str:
        """
        Provides a developer-friendly string representation of the plant.
        """
        return f"Plant(name='{self.name}', height={self.height}," \
            f"age={self.age})"


class Flower(Plant):

    def __init__(self, name, height, age, color: str):
        """
        Initializes a new Flower instance. Prints basics & specific features

        Args:
            name (str): The name of the plant.
            height (float): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
            color (str): The flower's color
        """
        super().__init__(name, height, age)
        self.color = color
        self.get_info()
        print(f"{self.color} color")

    def bloom(self):
        """
        Prints specific message about flowers
        """
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):

    def __init__(self, name, height, age, trunk_diameter: int, shade: int):
        """
        Initializes a new Tree instance. Prints basics & specific features

        Args:
            name (str): The name of the plant.
            height (float): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
            trunk_diameter (int): The tree's trunk diameter
            shade (int): The shade the tree generates
        """
        super().__init__(name, height, age)
        self.shade = shade
        self.trunk_diameter = trunk_diameter
        self.get_info()
        print(f"{self.trunk_diameter}cm diameter")

    def produce_shade(self):
        """
        Prints specific message about trees
        """
        print(f"{self.name} provides {self.shade} square meters of "
              f"shade\n")


class Vegetable(Plant):

    def __init__(self, name, height, age, harvest_season: str,
                 nutritional_value: str):
        """Initializes a new vegetable instance. Prints basics & specific
        features

        Args:
            name (str): The name of the plant.
            height (float): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
            harvest_season (str): The season to harvest the vegetable
            nutritional_value (str): The specific nutrition vegetable feature
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.get_info()
        print(f"{self.harvest_season} harvest")

    def nutritional_info(self):
        """
        Prints specific message about vegetables
        """
        print(f"{self.name} is rich in {self.nutritional_value}\n")


if __name__ == "__main__":

    plant_data = {
        "Flower": [
            {"name": "Rose", "height": 25.0, "age": 30,
             "color": "red"},
            {"name": "Sunflower", "height": 80.0, "age": 45,
             "color": "yellow"},
            {"name": "Violet", "height": 15.0, "age": 15,
             "color": "purple"},
        ],
        "Tree": [
            {"name": "Oak", "height": 500.0, "age": 100,
             "trunk_diameter": 25, "shade": 78},
            {"name": "Pine", "height": 700.0, "age": 30,
             "trunk_diameter": 5, "shade": 22},
            {"name": "Beech", "height": 500.0, "age": 80,
             "trunk_diameter": 15, "shade": 45},
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

    print("=== Garden Plant Types ===\n")
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
                                                               "diameter"],
                                  shade=plant_details["shade"])
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
                v_instance.nutritional_info()
