#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joflorid <joflorid@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/03 09:24:10 by joflorid          #+#    #+#              #
#    Updated: 2025/12/03 09:24:15 by joflorid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """
    Represents a single plant with properties like name, height, and age.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initializes a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (float): The initial height of the plant in cm.
            age (int): The initial age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """
        Prints the current information about the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, q_grow: float) -> None:
        """
        Increases the plant's height by a given amount.
        """
        self.height += q_grow

    def add_age(self, q_days: int) -> None:
        """
        Increases the plant's age by a given amount.
        """
        self.age += q_days - 1

    def __repr__(self) -> str:
        """
        Provides a developer-friendly string representation of the plant.
        """
        return f"Plant: {self.name} / Height: {self.height}cm " \
            f"/ Age: {self.age} days"


def ft_plant_growth(name: str, height: float, age: int) -> None:
    """
    Simulates the growth of a plant over a week and prints its progress.

    Args:
        name (str): The name of the plant (e.g., "Rose", "Sunflower",
        "Cactus").
        height (float): The initial height of the plant in cm.
        age (int): The initial age of the plant in days.

    Returns:
        None
    """
    q_grow = 0
    plant = Plant(name=name, height=height, age=age)
    print("=== Day 1 ===")
    plant.get_info()

    if name == "Rose":
        q_grow = 6
    elif name == "Sunflower":
        q_grow = 10
    elif name == "Cactus":
        q_grow = 2
    else:
        q_grow = 0
    plant.grow(q_grow=q_grow)  # A growth of each plant
    plant.add_age(q_days=7)  # 7 days passed
    print(f"=== Day {plant.age - age + 1} ===")
    plant.get_info()

    print(f"Growth this week: {plant.height - height:+}cm\n")


if __name__ == "__main__":
    ft_plant_growth(name="Rose", height=25.0, age=30)
    ft_plant_growth(name="Sunflower", height=80.0, age=45)
    ft_plant_growth(name="Cactus", height=15, age=120)
