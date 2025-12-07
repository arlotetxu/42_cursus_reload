#!/usr/bin/env python3

class Plant:
    """
    DOCSTRING
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_garden_data(self) -> None:
        """
        docstring
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def __repr__(self) -> str:
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
