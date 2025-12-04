#!/usr/bin/env python3


class GardenManager:
    def __init__(self, owner: str):
        self.owner = owner
        """
			Instancia de la clase GardenStats. Le pasamos como argumento
			self para asi poder tener acceso desde la clase GardenStat a la
			info de la clase GardenManager:
		"""
        self.garden_stats = self.GardenStats(self)

    @classmethod
    def create_garden_network(cls):  # Para crear las instancias???
        pass

    class GardenStats:
        num_gardens = 0
        num_plants = 0

        def __init__(self, garden_manager):
            self.garden_manager = garden_manager
            GardenManager.GardenStats.num_gardens += 1


class Plant(GardenManager):


    def __init__(self, owner: str, name: str, height: int):
        super().__init__(owner)
        self.name = name
        self.height = height
        print(f"Added {self.name} to {owner}'s garden")
        GardenManager.GardenStats.num_plants += 1


class FloweringPlan(Plant):
    def __init__(self, owner: str, name: str, height: int):
        super().__init__(owner, name, height)


class PrizeFlower(FloweringPlan):
    total_points = 0

    def __init__(self, owner: str, name: str, height: int, points: int):
        super().__init__(owner, name, height)
        self.points = points
        PrizeFlower.total_points = points

    def give_points(self, extra):
        PrizeFlower.total_points += extra

    def get_status(self):
        print(f"Total Prize points: {PrizeFlower.total_points}")


if __name__ == "__main__":
    print("===============Plant_1================")
    plant_1 = PrizeFlower("Arlo", "clavel", 15, 10)
    print(plant_1.garden_stats.num_gardens)
    print(plant_1.owner)
    print(plant_1.__class__.__name__)
    print(plant_1.height)
    plant_1.get_status()
    plant_1.give_points(12)
    plant_1.get_status()
    print(plant_1.garden_stats.num_plants)
    print("===============Plant_2================")
    plant_2 = FloweringPlan("Arlo", "Rosa", 45)
    print(plant_2.garden_stats.num_gardens)
    print(plant_2.owner)
    print(plant_2.__class__.__name__)
    print(plant_2.height)
    # print("===============Plant_3================")
    # plant_3 = GardenManager("Eneko")
    # print(plant_3.garden_stats.num_gardens)
