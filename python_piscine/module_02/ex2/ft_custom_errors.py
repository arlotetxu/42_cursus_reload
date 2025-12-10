#!/usr/bin/env python3

# class GardenError(Exception):
#     def __init__(self) -> None:
#         Exception.__init__(self)
#         self.message = f"Caught {self.__class__.__name__}: The garden has" \
#             f"issues."

#     def __str__(self) -> str:
#         return self.message


class GardenError(Exception):
    def __init__(self, message: str = "Exception: Garden with issues") -> None:
        Exception.__init__(self, message)


# class PlantError(GardenError):
#     def __init__(self, plant_name: str) -> None:
#         GardenError.__init__(self)
#         self.plant_name = plant_name
#         self.message = f"Caught {self.__class__.__name__}: " \
#             f"The {self.plant_name} pant is wilting!"

#     def __str__(self) -> str:
#         return self.message


class PlantError(GardenError):
    def __init__(self, plant_name: str) -> None:
        self.plant_name = plant_name
        message = f"The {self.plant_name} plant is wilting!"
        GardenError.__init__(self, message)


# class WaterError(GardenError):
#     def __init__(self) -> None:
#         GardenError.__init__(self)
#         self.message = f"Caught {self.__class__.__name__}: " \
#             f"Not enough water in the tank!"

#     def __str__(self) -> str:
#         return self.message


class WaterError(GardenError):
    def __init__(self) -> None:
        message = "Not enough water in the tank!"
        GardenError.__init__(self, message)


def test_plant_error(plant: str) -> None:
    try:
        raise PlantError(plant)
    except PlantError as pe:
        print(f"Caught {pe.__class__.__name__}: {pe}")


def test_water_error() -> None:
    try:
        raise WaterError()
    except WaterError as we:
        print(f"Caught {we.__class__.__name__}: {we}")


def test_all_errors(plant: str) -> None:
    errors = [PlantError(plant), WaterError()]

    for error in errors:
        try:
            raise error
        except GardenError as ge:
            print(f"Caught a garden error: {ge}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    test_plant_error("tomato")
    print("\nTesting WaterError...")
    test_water_error()
    print("\nTesting catching all garden errors...")
    test_all_errors("tomato")
    print("\nAll custom error types work correctly!")
