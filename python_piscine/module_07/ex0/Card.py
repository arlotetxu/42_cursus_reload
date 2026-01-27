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


class Creatures(Enum):

    FIRE_DRAGON = "Fire Dragon"
    GOBLIN_WARRIOR = "Goblin Warrior"
    FROST_WYRM = "Frost Wyrm"
    SHADOWBLADE_ASSASSIN = "Shadowblade Assassin"
    THUNDERCLAP_TITAN = "Thunderclap Titan"
    EMBERFANG_DRAKE = "Emberfang Drake"
    BLOODSWORN_BERSERKER = "Bloodsworn Berserker"
    ARCANE_NOVA = "Arcane Nova"
    VOIDCALLER_MAGE = "Voidcaller Mage"
    STONEHIDE_GOLEM = "Stonehide Golem"
    VENOMSTRIKE_RANGER = "Venomstrike Ranger"
    CELESTIAL_SMITE = "Celestial Smite"
    DREADBONE_NECROMANCER = "Dreadbone Necromancer"
    IRONJAW_BEHEMOTH = "Ironjaw Behemoth"
    SOULFIRE_RITUAL = "Soulfire Ritual"
    STORMWATCH_GRIFFIN = "Stormwatch Griffin"
    NIGHTVEIL_STALKER = "Nightveil Stalker"
    EARTHSHATTER_COLOSSUS = "Earthshatter Colossus"
    SUNFLARE_PALADIN = "Sunflare Paladin"
    MINDREND_HEX = "Mindrend Hex"
    ASHEN_WARLOCK = "Ashen Warlock"
    TEMPEST_BARRAGE = "Tempest Barrage"


class Spells(Enum):
    LIGHTNING_BOLT = "Lightning Bolt"
    ARCANE_NOVA = "Arcane Nova"
    CELESTIAL_SMITE = "Celestial Smite"
    SOULFIRE_RITUAL = "Soulfire Ritual"
    MINDREND_HEX = "Mindrend Hex"
    TEMPEST_BARRAGE = "Tempest Barrage"
    SHADOWFLAME = "Shadowflame"
    FROSTBIND = "Frostbind"
    VOID_SURGE = "Void Surge"
    EARTHSHATTER = "Earthshatter"
    FIRE = "Fire"
    ICE = "Ice"


class Artifacts(Enum):
    MANA_CRYSTAL = "Mana Crystal"
    SOULSTONE_AMULET = "Soulstone Amulet"
    DRAGONFIRE_RELIC = "Dragonfire Relic"
    VOID_COMPASS = "Void Compass"
    RUNIC_OBELISK = "Runic Obelisk"
    CHRONO_HOURGLASS = "Chrono Hourglass"
    BLOODBOUND_TALISMAN = "Bloodbound Talisman"
    STORMCORE_ENGINE = "Stormcore Engine"
    ETHEREAL_LENS = "Ethereal Lens"
    OBSIDIAN_IDOL = "Obsidian Idol"
    MAGICAL_RING = "Magical Ring"
    MAGICAL_STAFF = "Magical Staff"

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
