#!/usr/bin/env python3
"""
Tu reto: Añade un último método de instancia a GardenManager llamado generate_report(self, gardener_name).

Este método debe:

Obtener la lista de plantas de ese jardinero (usando self.gardens).

Calcular la altura total llamando a self.GardenStats.calculate_total_height(...).

Calcular la puntuación llamando a self.GardenStats.calculate_score(...).

Imprimir un reporte similar al del ejemplo (Nombre, altura total, puntuación).
"""
from icecream import ic

class GardenManager:

    def __init__(self):

        self.gardens = {}

    def add_plant(self, gardener_name, plant):

        if gardener_name not in self.gardens:
            self.gardens[gardener_name] = []
        self.gardens[gardener_name].append(plant)
        print(f"Added {plant.name} to {gardener_name}'s garden")

    def generate_report(self, gardener_name):
        plants_list = self.gardens[gardener_name]
        total_height = self.GardenStats.calculate_total_height(plants_list)
        total_growth = self.GardenStats.calculate_total_grow(plants_list)
        total_regular = 0
        total_flowering = 0
        total_prize = 0

        print(f"\n=== {gardener_name}'s Garden Report ===")
        for plant in plants_list:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming), Prize points: {plant.points}")
                total_prize += 1
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")
                total_flowering += 1
            else:
                print(f"- {plant.name}: {plant.height}cm")
                total_regular += 1

        print(f"\nPlans added: {len(plants_list)}, Total growth: {total_growth}")
        print(f"Plant types: {total_regular} regular, {total_flowering} flowering, {total_prize} prize flowers")

        gardener_scores = {}
        for gardener, plants in self.gardens.items():
            gardener_scores[gardener] = self.GardenStats.calculate_score(plants)

        print("\nGarden scores -", end="")
        for gardener, score in gardener_scores.items():
            print(f" {gardener}: {score}", end=",")

        print(f"\nTotal gardens managed: {len(self.gardens.keys())}")

    @classmethod
    def create_garden_network(cls):

        print("=== Garden Management System Demo ===\n")
        return cls()


    class GardenStats:

        @staticmethod
        def calculate_total_height(plants: list) -> int:
            total_height = 0
            for plant in plants:
                total_height += plant.height
            return total_height

        @staticmethod
        def calculate_total_grow(plants: list) -> int:
            total_grow = 0
            for plant in plants:
                total_grow += plant._grow
            return total_grow

        @staticmethod
        def calculate_score(plants: list) -> int:
            total_points = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    total_points += plant.height + plant.points
                elif isinstance(plant, (Plant, FloweringPlant)):
                    total_points += plant.height
            return total_points



class Plant():

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self._grow = 0
        self.height_valid = False

    def grow(self, cms_grow: int):
        if cms_grow < 0:
            print(f"\nInvalid operation attempted: height {cms_grow}cm [REJECTED]")
        else:
            self._grow += cms_grow     # Sumamos al contador de crecimiento
            self.height += cms_grow    # ¡Y la planta crece de verdad!
            print(f"{self.name} grew {cms_grow}cm") # Feedback visual (opcional pero útil)
        self.height_valid = True


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int, age: int, color: str, points: int):
        super().__init__(name, height, age, color)
        self.points = points



if __name__ == "__main__":
    # 1. Crear el manager usando el método de clase
    manager = GardenManager.create_garden_network()

    # 2. Crear las plantas
    oak = Plant("Oak Tree", 100, 12)
    rose = FloweringPlant("Rose", 25, 13, "red")
    sunflower = PrizeFlower("Sunflower", 50, 14, "yellow", 10)

    # 3. Añadir plantas al jardín de Alice
    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)

    # 4. Simular crecimiento (manual para el ejemplo)
    # Nota: El PDF muestra crecimiento, pero como no implementamos grow()
    # en este ejercicio específico (venía del ex2), asumiremos que modificamos
    # la altura manualmente para el test o simplemente probamos el reporte actual.
    oak.grow(1)
    rose.grow(1)
    sunflower.grow(1)

    # 5. Añadir otro jardín para probar el score múltiple
    manager.add_plant("Bob", Plant("Cactus", 10, 15))

    # 6. Generar reporte
    manager.generate_report("Alice")
    #manager.generate_report("Bob")
