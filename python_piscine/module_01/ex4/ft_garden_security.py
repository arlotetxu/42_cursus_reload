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
        print(f"Plant created: {self.name}")

    def get_info(self) -> None:
        """
        Prints the current information about the plant.
        """
        print(f"\nCurrent plant: {self.name} ({self._height}cm,"
              f"{self._age} days)")

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
        plant = Plant(name=data["name"], height=data["height"],
                      age=data["age"])
        created_plants.append(plant)
    return created_plants


if __name__ == "__main__":
    print("=== Garden Security System ===")
    # Define all plants to be created in one place
    plant_definitions = [
        {"name": "Rose", "height": 30.0, "age": 60},
        # {'name': "Oak", 'height': 200.0, 'age': 365},
        # {'name': "Cactus", 'height': 5.0, 'age': 90},
        # {'name': "Sunflower", 'height': 80.0, 'age': 45},
        # {'name': "Fern", 'height': 15.0, 'age': 120},
    ]

    # Use the ft_plant_factory to create all plants at once
    garden = ft_plant_factory(plant_definitions)

    rose = next((p for p in garden if p.name == "Rose"), None)
    rose.height = 25
    rose.age = 30

    rose.height = -5
    rose.age = -15

    rose.get_info()
