from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Interface for cards that can engage in combat.
    """

    @abstractmethod
    def attack(self, target) -> dict:
        """
        Perform an attack on a target.

        Args:
            target: The target to attack.

        Returns:
            dict: A dictionary containing the results of the attack.
        """
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage (int): The amount of damage to defend against.

        Returns:
            dict: A dictionary containing the results of the defense.
        """
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """
        Get the combat-related statistics.

        Returns:
            dict: A dictionary containing combat statistics.
        """
        ...
