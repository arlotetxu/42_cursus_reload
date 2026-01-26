#!/usr/bin/env python3
from ex0.Card import Card


class CreatureCard(Card):
    """
    Class representing a creature card in the game.
    """
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        """
        Initialize a creature card with a name, mana cost, rarity, attack,
        and health.
        """
        super().__init__(name, cost, rarity)
        self._attack = 0
        self._health = 0
        self.type = self

        self.set_attack(attack)
        self.set_health(health)

    def get_attack(self):
        """
        Get the attack value of the creature.
        """
        return self._attack

    def set_attack(self, value):
        """
        Set the attack value of the creature.
        """
        if value > 0:
            self._attack = value
        else:
            print()
            raise (
                ValueError(
                    f"\033[31mERROR. {self.name}'s attack value "
                    f"cannot be less than 1. Please, check...\033[0m"
                )
            )

    def get_health(self):
        """
        Get the health value of the creature.
        """
        return self._health

    def set_health(self, value):
        """
        Set the health value of the creature.
        """
        if value > 0:
            self._health = value
        else:
            print()
            raise (
                ValueError(
                    f"\033[31mERROR. {self.name}'s health "
                    f"cannot be less than 1. Please, check...\033[0m"
                )
            )

    def play(self, game_state: dict) -> dict:
        """
        Play the creature card and update the game state.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: The updated game state.
        """
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = "Creature summoned to battlefield"
        return game_state

    def attack_target(self, target: Card) -> dict:
        """
        Attack a target card and return the result of the combat.

        Args:
            target (Card): The card to attack.

        Returns:
            dict: A dictionary containing the results of the attack.
        """
        print()
        attack_result: dict = {}
        print(f"{self.name} attacks {target.name}:")
        target._health -= self._attack
        combat_resolved: bool = True if target._health <= 0 else False
        attack_result["attacker"] = self.name
        attack_result["target"] = target.name
        attack_result["damage_dealt"] = self._attack
        attack_result["combat_resolved"] = combat_resolved

        return attack_result
