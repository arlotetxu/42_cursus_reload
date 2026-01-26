from abc import ABC, abstractmethod


class Magical(ABC):
    """
    Interface for cards that have magical abilities.
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Cast a spell on multiple targets.

        Args:
            spell_name (str): The name of the spell to cast.
            targets (list): A list of target cards.

        Returns:
            dict: A dictionary containing the results of the spell cast.
        """
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """
        Channel mana to increase the total mana pool.

        Args:
            amount (int): The amount of mana to channel.

        Returns:
            dict: A dictionary containing the results of the mana channeling.
        """
        ...

    @abstractmethod
    def get_magic_stats(self) -> dict:
        ...
