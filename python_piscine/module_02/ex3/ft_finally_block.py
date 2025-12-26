#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    """
    Waters a list of plants by name.

    Opens the watering system, attempts to water each plant in the provided
    list, and handles invalid plant names gracefully. Always closes the
    watering system after processing, regardless of errors.

    Args:
        plant_list (list): A list of plant names (strings) to be watered.

    Raises:
        None. Prints an error message if an invalid plant name is
        encountered.
    """

    plant_list_ok = {
        "tomato": "tomato",
        "lettuce": "lettuce",
        "carrots": "carrots",
        }

    print("Opening watering system")
    try:
        for plant in plant_list:
            _ = plant_list_ok[plant]
            print(f"Watering {plant}")
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing waterering system (cleanup)")


def test_watering_system() -> None:
    """
    Tests the garden watering system by simulating two scenarios:
    1. Normal operation with a valid list of plants.
    2. Error handling with an invalid list containing a None value.

    Prints the progress and results of each test, demonstrating that cleanup
    actions are performed regardless of errors during watering.
    """

    plant_list_ok = ["tomato", "lettuce", "carrots"]
    plant_list_nok = ["tomato", None, "carrots"]

    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(plant_list_ok)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(plant_list_nok)

    print("\nCleanup always happens, even with errors!")


test_watering_system()
