from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        pass

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        # TODO Añadir los diferentes tipos de cartas al diccionario
        creature_types = {
            "CreatureCard": "Creature",
        }

        self.card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": creature_types.get(self.__class__.__name__, "Unknown"),
            "attack": self._attack,
            "health": self._health
        }
        return self.card_info


    def is_playable(self, available_mana: int) -> bool:
        if self._attack > 0 and self._health > 0 and available_mana > self.cost:
            return True
        return False

