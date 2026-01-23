#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict: ...

    def get_card_info(self) -> dict:
        from ex0.CreatureCard import CreatureCard

        # TODO Añadir los diferentes tipos de cartas al diccionario
        card_types = {
            "CreatureCard": "Creature",
            "SpellCard": "Spell",
            "ArtifactCard": "Artifact",
        }

        if isinstance(self, CreatureCard):
            self.card_info = {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": card_types.get(self.__class__.__name__, "Unknown"),
                "attack": self._attack,
                "health": self._health,
            }
        return self.card_info

    def is_playable(self, available_mana: int) -> bool:
        from ex0.CreatureCard import CreatureCard
        if isinstance(self, CreatureCard):
            if self._health <= 0 or available_mana < self.cost:
                return False
        else:
            if available_mana < self.cost:
                return False
        return True
