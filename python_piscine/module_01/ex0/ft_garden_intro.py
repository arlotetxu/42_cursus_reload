#!/usr/bin/env python3

def ft_garden_intro() -> None:
    """
    Display information about a garden plant.

    This function prints a formatted welcome message for a garden program,
    displaying details about a plant including its name, height, and age.

    Returns:
        None
    """

    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == '__main__':
    ft_garden_intro()
