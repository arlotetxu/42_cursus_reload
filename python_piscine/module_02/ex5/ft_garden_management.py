#!/usr/bin/env python3

class GardenError(Exception):

    def __init__(self, message: str = "Exception: Garden with issues") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):

    def __init__(self, message) -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):

    def __init__(self, plant_: Plant) -> None:
        message = ""
        if plant_.water > 10:
            message = f"Error checking {plant_.name}: Water level {plant_.water} is too high (max 10)"
        elif plant_.water < 1:
            message = f"Error checking {plant_.name}: Water level {plant_.water} is too low (min 1)"
        GardenError.__init__(self, message)


class SunError(GardenError):

    def __init__(self, plant_: Plant) -> None:
        if plant_.sun > 12:
            message = f"Error checking {plant_.name}: sun light {plant_.sun} is too high (max 12)"
        elif plant_.sun < 2:
            message = f"Error checking {plant_.name}: sun light {plant_.sun} is too low (min 2)"
        GardenError.__init__(self, message)


class GardenManager:
    def __init__(self):
        self.plants = []
        self.errors = []

    def add_plant(self, plant_):
        if not plant_.name:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        if plant_.water > 10 or plant_.water < 1:
            self.errors.append(WaterError(plant_))
            raise WaterError(plant_)
        if plant_.sun < 2 or plant_.sun > 12:
            self.errors.append(SunError(plant_))
            raise SunError(plant_)
        if plant_ not in self.plants:
            self.plants.append(plant_)
        print(f"Added {plant_.name} successfully")

    def watering(self):
        for plant_ in self.plants:
            print(f"Watering {plant_.name} -success")
            plant_.water += 1


    def checking(self):
        for plant_ in self.plants:
            try:
                if plant_.water > 10 or plant_.water < 1:
                    self.errors.append(WaterError(plant_))
                    raise WaterError(plant_)
                if plant_.sun < 2 or plant_.sun > 12:
                    self.errors.append(SunError(plant_))
                    raise SunError(plant_)
                print(f"{plant_.name}: healthy (water: {plant_.water}, sun: {plant_.sun})")
            except GardenError as e:
                print(e)

    def check_plants(self):
        for plant_ in self.plants:
            print(plant_.name)


class Plant:
    def __init__(self, name:str, water:int, sun:int):
        self.name = name
        self.water = water
        self.sun = sun

if __name__ == "__main__":
    print("=== Garden Management System ===")
    manager = GardenManager()

    plants = []
    plant_1 = Plant("tomato", 10, 2)
    plants.append(plant_1)
    plant_2 = Plant("lettuce", 1, 2)
    plants.append(plant_2)
    plant_3 = Plant("", 1, 2)
    plants.append(plant_3)


    print("\nAdding plants to garden...")
    try:
        for plant in plants:
            manager.add_plant(plant)
    except GardenError as e:
        print(e)


    print("\nWatering plants...")
    try:
        print("Opening watering system")
        manager.watering()
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


    print("\nChecking plant health...")
    try:
        manager.checking()
    except GardenError as e:
        print(e)
    print(manager.errors[0].__class__.__name__)
    print("\nAll error raising tests completed!")
    # finally:
    #     manager.check_plants()
