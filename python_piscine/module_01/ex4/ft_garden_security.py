#!/usr/bin/env python3

class SecurePlant:
    """
    A class representing a secure plant with protected attributes.
    This class implements a plant with name, height, and age attributes,
    where height and age are protected and can only be modified through
    setter methods that validate the input values to prevent negative values.

    Attributes:
        num_plants (int): Class variable tracking the total number of plant
                          instances created.
        _height (float): The protected height of the plant in centimeters.
        _age (int): The protected age of the plant in days.

    Example:
        >>> plant = SecurePlant("Rose", 15.5, 30)
        Plant created: Rose
        >>> plant.get_height()
        15.5
        >>> plant.set_height(20.0)
        Height updated: 20.0cm [OK]
        >>> plant.set_height(-5.0)
        Invalid operation attempted: height -5.0cm [REJECTED]
        Security: Negative height rejected
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
        SecurePlant.num_plants += 1
        print(f"Plant created: {self.name}")

    def get_info(self) -> None:
        """
        Display information about the current plant.
        Prints the plant's name, height in centimeters, and age in days
        to the standard output.

        Returns:
            None
        """

        print(f"\nCurrent plant: {self.name} ({self._height}cm,"
              f"{self._age} days)")

    def get_height(self) -> float:
        """
        Get the height of the object.

        Returns:
            float: The height value of the object.
        """

        return self._height

    def set_height(self, value: float) -> None:
        """
        Set the height of the object with security validation. If the value
        is negative, the operation is rejected and an error message is
        printed. Otherwise, the height is updated.

        Args:
            value (float): The height value in centimeters to be set.

        Returns:
            None
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
        Get the age of the object.

        Returns:
            int: The age value stored in the private _age attribute.
        """

        return self._age

    def set_age(self, value: int) -> None:
        """
        Set the age of the garden element. If the provided value is negative,
        the operation is rejected and an error message is printed. Otherwise,
        the age is updated

        Args:
            value (int): The age value in days to set.

        Returns:
            None
        """

        if value < 0:
            print(f"\nInvalid operation attempted: age {value}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days [OK]")

    def __repr__(self) -> str:
        """
        Return a string representation of the Plant object.

        Returns:
            str: A string representation of the Plant object in the format
                 "Plant(name='<name>', height=<height>, age=<age>)".
        """

        return f"Plant(name='{self.name}', height={self.height}," \
            f"age={self.age})"


def ft_plant_factory(plants_data: list[dict]) -> list[SecurePlant]:
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
        plant = SecurePlant(name=data["name"], height=data["height"],
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
    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-15)

    rose.get_info()
