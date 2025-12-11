#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    """
    Water plants from a given list if they are valid.

    This function simulates a watering system that opens, waters valid plants,
    and closes regardless of whether an error occurs.

    Args:
        plant_list (list[str]): A list of plant names to water.

    Raises:
        ZeroDivisionError: Caught internally when an invalid plant is
            encountered.

    Note:
        The watering system cleanup (closing) always executes via the
        finally block.
    """

    plant_list_ok = ["tomato", "lettuce", "carrots"]
    print("Openning watering system")
    try:
        for plant in plant_list:
            if plant not in plant_list_ok:
                1/0
            print(f"Watering {plant}")
    except ZeroDivisionError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing waterering system (cleanup)")


def test_watering_system() -> None:
    """
    Test the garden watering system with different plant lists.

    This function demonstrates the behavior of the water_plants function
    with both valid and invalid plant lists. It shows how the finally
    block ensures cleanup operations are always executed, even when
    errors occur.

    The function tests two scenarios:
    1. Normal watering with a valid list of plants (tomato, lettuce, carrots)
    2. Error handling with an invalid list containing a None value

    Returns:
        None
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


# if __name__ == "__main__":
#     test_watering_system()
