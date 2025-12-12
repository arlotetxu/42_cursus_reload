#!/usr/bin/env python3


def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> None:
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

    # Test 5: Low sunlight
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health(plant_name="fern",
                           water_level=5,
                           sunlight_hours=0)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


# if __name__ == "__main__":
#     test_plant_checks()
