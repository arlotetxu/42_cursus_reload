from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Interface for objects that can be ranked in a tournament.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate the current rating of the object.

        Returns:
            int: The calculated rating.
        """
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the number of wins and adjust the rating.

        Args:
            wins (int): The number of wins to add.
        """
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the number of losses and adjust the rating.

        Args:
            losses (int): The number of losses to add.
        """
        ...

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Get ranking information for the object.

        Returns:
            dict: A dictionary containing ranking details.
        """
        ...
