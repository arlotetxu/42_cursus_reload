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
        _height (int): The protected height of the plant in centimeters.
        _age (int): The protected age of the plant in days.

    Example:
        >>> plant = SecurePlant("Rose", 15, 30)
        Plant created: Rose
        >>> plant.get_height()
        15.5
        >>> plant.set_height(20)
        Height updated: 20cm [OK]
        >>> plant.set_height(-5)
        Invalid operation attempted: height -5cm [REJECTED]
        Security: Negative height rejected
    """

    num_plants = 0

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
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

        SecurePlant.num_plants += 1

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

    def get_height(self) -> int:
        """
        Get the height of the object.

        Returns:
            int: The height value of the object.
        """

        return self._height

    def set_height(self, value: int) -> None:
        """
        Set the height of the object with security validation. If the value
        is negative, the operation is rejected and an error message is
        printed. Otherwise, the height is updated.

        Args:
            value (int): The height value in centimeters to be set.

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


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = SecurePlant(name="Rose", height=15, age=20)
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    # rose.set_age(-15)

    rose.get_info()
