#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joflorid <joflorid@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/03 09:23:37 by joflorid          #+#    #+#              #
#    Updated: 2025/12/03 09:23:42 by joflorid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
        self.height = height
        self.age = age
        Plant.num_plants += 1

    def get_info(self) -> None:
        """
        Prints the current information about the plant.
        """
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def grow(self, q_grow: float) -> None:
        """
        Increases the plant's height by a given amount.
        """
        self.height += q_grow

    def age(self, q_days: int) -> None:
        """
        Increases the plant's age by a given amount.
        """
        self.age += q_days - 1

    def __repr__(self) -> str:
        """
        Provides a developer-friendly string representation of the plant.
        """
        return f"Plant(name='{self.name}', height={self.height}, " \
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
        plant = Plant(name=data['name'], height=data['height'],
                      age=data['age'])
        created_plants.append(plant)
    return created_plants


if __name__ == "__main__":
    # Define all plants to be created in one place
    plant_definitions = [
        {'name': "Rose", 'height': 25.0, 'age': 30},
        {'name': "Oak", 'height': 200.0, 'age': 365},
        {'name': "Cactus", 'height': 5.0, 'age': 90},
        {'name': "Sunflower", 'height': 80.0, 'age': 45},
        {'name': "Fern", 'height': 15.0, 'age': 120},
    ]

    # Use the factory to create all plants at once
    garden = ft_plant_factory(plant_definitions)

    # Display the created plants in an organized format
    print("=== Plants Created in the Garden ===")
    for plant in garden:
        plant.get_info()

    print(f"\nTotal plants created: {Plant.num_plants}")
