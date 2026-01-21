from Card import Card
from icecream import ic

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self._attack = 0
        self._health = 0
        self.type = self
        # ic("Inicializacion de CreatureCard completada!!")  # TODO Eliminar

        self.set_attack(attack)
        self.set_health(health)

    def get_attack(self):
        return self._attack

    def set_attack(self, value):
        if value > 0:
            self._attack = value
        else:
            print("\033[31mERROR. Attack value cannot be less than 1. Please, check...\033[0m")
            print()

    def get_health(self):
        return self._health

    def set_health(self, value):
        if value > 0:
            self._health = value
        else:
            print("\033[31mERROR. Health value cannot be less than 1. Please, check...\033[0m")
            print()

    def play(self, game_state: dict) -> dict:
        if self.is_playable(available_mana=6):
            ic("El jugable. Continua aqui JMF - CreatureCard.play()")

    def attack_target(self, target: Card) -> dict:
        target.health -= self.attack  # TODO Esto es asi?
        self.attack -= 1
