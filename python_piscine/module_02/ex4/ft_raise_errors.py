#!/usr/bin/env python3


def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int
                       ) -> None:
    """
    Checks the health of a plant based on its name, water level, and sunlight
    hours.

    Parameters:
        plant_name (str): The name of the plant. Must not be empty.
        water_level (int): The water level of the plant. Must be between 1
            and 10 (inclusive).
        sunlight_hours (int): The number of sunlight hours the plant
            receives. Must be between 2 and 12 (inclusive).

    Raises:
        ValueError: If the plant name is empty.
        ValueError: If the water level is less than 1 or greater than 10.
        ValueError: If the sunlight hours are less than 2 or greater than 12.

    Prints:
        A message indicating that the plant is healthy if all checks pass.
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too low (min 1)")

    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         f"is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")

    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Runs a series of tests on the check_plant_health function to verify its
    error handling.

    The tests include:
    - Valid input values.
    - Empty plant name.
    - Invalid water level.
    - Invalid sunlight hours.

    Each test prints the result or the error message raised by
    check_plant_health.
    """
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        check_plant_health(plant_name="tomato",
                           water_level=5,
                           sunlight_hours=8)
    except ValueError as e:
        print(e)

    print("\nTesting empty plant name...")
    try:
        check_plant_health(plant_name="",
                           water_level=5,
                           sunlight_hours=8)
    except ValueError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        check_plant_health(plant_name="cactus",
                           water_level=15,
                           sunlight_hours=8)
    except ValueError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health(plant_name="fern",
                           water_level=5,
                           sunlight_hours=0)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


test_plant_checks()
