#!/usr/bin/env python3
from abc import ABC, abstractmethod
from enum import Enum


class Card_Types(Enum):
    """
    Enum representing the different types of cards.
    """
    CARD = "Card"
    CREATURECARD = "Creature"
    SPELLCARD = "Spell"
    ARTIFACTCARD = "Artifact"
    ELITECARD = "Elite"


class Card_Rarity(Enum):
    """
    Enum representing the rarity of cards.
    """
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    LEGENDARY = "Legendary"


class Card(ABC):
    """
    Abstract base class representing a generic card in the game.
    """
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Initialize a card with a name, mana cost, and rarity.
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Abstract method to play the card and update the game state.
        """
        ...

    def get_card_info(self) -> dict:
        """
        Get information about the card.

        Returns:
            dict: A dictionary containing card details.
        """
        from ex0.CreatureCard import CreatureCard

        if isinstance(self, CreatureCard):
            self.card_info = {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": Card_Types[type(self).__name__.upper()].value,
                "attack": self._attack,
                "health": self._health,
            }
        return self.card_info

    def is_playable(self, available_mana: int) -> bool:
        """
        Check if the card is playable given the available mana.

        Args:
            available_mana (int): The amount of mana available to the player.

        Returns:
            bool: True if the card is playable, False otherwise.
        """
        from ex0.CreatureCard import CreatureCard
        if isinstance(self, CreatureCard):
            if self._health <= 0 or available_mana < self.cost:
                return False
        else:
            if available_mana < self.cost:
                return False
        return True
