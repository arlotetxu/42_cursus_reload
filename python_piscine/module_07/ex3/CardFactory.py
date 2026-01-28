from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """
    Abstract base class for a card factory.
    """

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """
        Creates a creature card.

        Args:
            name_or_power (str | int | None): The name or power of the
            creature.

        Returns:
            Card: The created creature card.
        """
        ...

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        Creates a spell card.

        Args:
            name_or_power (str | int | None): The name or power of the spell.

        Returns:
            Card: The created spell card.
        """
        ...

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        Creates an artifact card.

        Args:
            name_or_power (str | int | None): The name or power of the
            artifact.

        Returns:
            Card: The created artifact card.
        """
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """
        Creates a themed deck of a given size.

        Args:
            size (int): The number of cards in the deck.

        Returns:
            dict: A dictionary representing the themed deck.
        """
        ...

    @abstractmethod
    def get_supported_types(self) -> dict:
        """
        Gets the supported card types.

        Returns:
            dict: A dictionary of supported card types.
        """
        ...
