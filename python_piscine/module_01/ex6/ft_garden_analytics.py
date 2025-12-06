#!/usr/bin/env python3

class GardenManager:
    """A class to manage gardens and their plants for multiple gardeners.
    This class provides functionality to add plants to gardeners' gardens,
    simulate plant growth, and generate detailed reports about garden status.

    Attributes:
        gardens (dict): A dictionary mapping gardener names to their list
        of plants.
    """

    def __init__(self):
        """Initialize a new GardenManager instance with an empty gardens
        dictionary.
        """
        self.gardens = {}

    def add_plant(self, gardener_name, plant) -> None:
        """ Add a plant to a gardener's garden.

            Args:
                - gardener_name: The name of the gardener.
                - plant: The plant object to add to the garden.

            Returns:
                None
            """
        if gardener_name not in self.gardens:
            self.gardens[gardener_name] = []
        self.gardens[gardener_name].append(plant)
        print(f"\nAdded {plant.name} to {gardener_name}'s garden")

    def simulate_growth(self, gardener_name: str, cms: int) -> None:
        """Simulates growth for all plants in a specified gardener's garden.

        Args:
            - gardener_name (str): The name of the gardener whose plants
            will grow.
            - cms (int): The amount in centimeters by which each plant
            will grow.

        Returns:
            None
        """
        plant_list = []
        if gardener_name in self.gardens:
            plant_list = self.gardens[gardener_name]
        else:
            print("Gardener not found")
            return
        print(f"\n{gardener_name} is helping all plants grow...")
        for plant in plant_list:
            plant.grow(cms)

    def generate_report(self, gardener_name) -> None:
        """Generates a detailed report for a specific gardener's garden.

        The report includes plant details, total growth, plant type counts,
        a height validation test, and garden scores for all gardeners.

        Args:
            gardener_name (str): The name of the gardener for whom to generate
                                 the report.
        """
        plants_list = self.gardens[gardener_name]
        total_growth = self.GardenStats.calculate_total_grow(plants_list)
        total_regular = 0
        total_flowering = 0
        total_prize = 0

        print(f"\n=== {gardener_name}'s Garden Report ===")
        for plant in plants_list:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming), "
                      f"Prize points: {plant.points}")
                total_prize += 1
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming)")
                total_flowering += 1
            else:
                print(f"- {plant.name}: {plant.height}cm")
                total_regular += 1

        print(f"\nPlants added: {len(plants_list)}, "
              f"Total growth: {total_growth}")
        print(f"Plant types: {total_regular} regular, "
              f"{total_flowering} flowering, {total_prize} prize flowers")

        validation_status = all(plant.height >= 0 for plant in plants_list)
        print(f"\nHeight validation test: {validation_status}")

        gardener_scores = {}
        for gardener, plants in self.gardens.items():
            gardener_scores[gardener] = \
                self.GardenStats.calculate_score(plants)
        print("Garden scores -", end="")
        for gardener, score in gardener_scores.items():
            print(f" {gardener}: {score}", end=",")

        print(f"\nTotal gardens managed: {len(self.gardens.keys())}")

    @classmethod
    def create_garden_network(cls):
        """
        Class method to create and initialize a GardenManager instance.
        It prints a welcome message for the Garden Management System Demo.

        Returns:
            cls: An instance of the GardenManager class."""

        print("=== Garden Management System Demo ===")
        return cls()

    class GardenStats:
        """
        A nested class within GardenManager to provide static methods for
        calculating various garden statistics.
        """

        @staticmethod
        def calculate_total_height(plants: list) -> int:
            """
            Calculates the total height of a list of plants.

            Args:
                plants (list): A list of plant objects.

            Returns:
                int: The sum of the heights of all plants in the list.
            """

            total_height = 0
            for plant in plants:
                total_height += plant.height
            return total_height

        @staticmethod
        def calculate_total_grow(plants: list) -> int:
            """
            Calculates the total growth (sum of _grow attribute) of a list of plants.

            Args:
                plants (list): A list of plant objects.

            Returns:
                int: The sum of the _grow attribute for all plants in the list.
            """
            total_grow = 0
            for plant in plants:
                total_grow += plant._grow
            return total_grow

        @staticmethod
        def calculate_score(plants: list) -> int:
            """
            Calculates a score for a list of plants based on their height and
            additional points for PrizeFlower instances.

            Args:
                plants (list): A list of plant objects.

            Returns:
                int: The total score.
            """
            total_points = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    total_points += plant.height + plant.points
                elif isinstance(plant, (Plant, FloweringPlant)):
                    total_points += plant.height
            return total_points


class Plant():
    """
    Represents a generic plant with a name, height, and age.
    """

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        """
        Initializes a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
            age (int): The age of the plant in years.
        """
        self.height = height
        self.age = age
        self._grow = 0

    def grow(self, cms_grow: int):
        """
        Simulates the growth of the plant by increasing its height.
        If cms_grow is negative, it prints an error message and rejects the operation.

        Args:
            cms_grow (int): The amount in centimeters by which the plant will grow.
        Returns:
            None
        """
        if cms_grow < 0:
            print(f"\nInvalid operation attempted: height "
                  f"{cms_grow}cm [REJECTED]")
        else:
            self._grow += cms_grow
            self.height += cms_grow
            print(f"{self.name} grew {cms_grow}cm")


class FloweringPlant(Plant):
    """
    Represents a flowering plant, inheriting from Plant and adding a color attribute.
    """

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        """
        Initializes a new FloweringPlant instance.

        Args:
            name (str): The name of the flowering plant.
            height (int): The initial height of the flowering plant in centimeters.
            age (int): The age of the flowering plant in years.
            color (str): The color of the flowers.
        """
        self.color = color


class PrizeFlower(FloweringPlant):

    """
    Represents a prize-winning flowering plant, inheriting from FloweringPlant
    and adding a points attribute.
    """

    def __init__(self, name: str, height: int, age: int,
                 color: str, points: int):
        """
        Initializes a new PrizeFlower instance.

        Args:
            name (str): The name of the prize-winning flowering plant.
            height (int): The initial height of the prize-winning flowering plant in centimeters.
            age (int): The age of the prize-winning flowering plant in years.
            color (str): The color of the flowers.
            points (int): The prize points awarded to the plant.
        """
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
    manager.simulate_growth("Alice", 1)

    # 5. Añadir otro jardín para probar el score múltiple
    manager.add_plant("Bob", Plant("Cactus", 10, 15))

    # 6. Generar reporte
    manager.generate_report("Alice")
