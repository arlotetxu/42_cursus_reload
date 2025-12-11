#!/usr/bin/env python3


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low (min 1)")

    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")

    print(f"Plant '{plant_name}' is healthy!")

    #print("\nAll error raising tests completed!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    # Test 1: Good values
    print("\nTesting good values...")
    try:
        check_plant_health(plant_name="tomato", water_level=5, sunlight_hours=8)
    except ValueError as e:
        print(e)

    # Test 2: Empty plant name
    print("\nTesting empty plant name...")
    try:
        check_plant_health(plant_name="", water_level=5, sunlight_hours=8)
    except ValueError as e:
        print(e)

    # Test 3: Low water
    print("\nTesting low water...")
    try:
        check_plant_health(plant_name="rose", water_level=0, sunlight_hours=8)
    except ValueError as e:
        print(e)

    # Test 4: High water
    print("\nTesting high water...")
    try:
        check_plant_health(plant_name="cactus", water_level=15, sunlight_hours=8)
    except ValueError as e:
        print(e)

    # Test 5: Low sunlight
    print("\nTesting low sunlight...")
    try:
        check_plant_health(plant_name="fern", water_level=5, sunlight_hours=1)
    except ValueError as e:
        print(e)

    # Test 6: High sunlight
    print("\nTesting high sunlight...")
    try:
        check_plant_health(plant_name="lettuce", water_level=5, sunlight_hours=15)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
