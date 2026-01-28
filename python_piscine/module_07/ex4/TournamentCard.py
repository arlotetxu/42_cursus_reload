from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    A card class that combines basic card properties with combat and
    ranking functionality.
    """

    def __init__(self, name: str, cost: int, rarity: str, rating: int):
        """
        Initialize a TournamentCard instance.

        Args:
            name (str): The name of the card.
            cost (int): The cost of the card.
            rarity (str): The rarity of the card.
            rating (int): The initial rating of the card.
        """
        super().__init__(name, cost, rarity)
        self.id = name.split()[1].lower() + "_001"
        self.rating = rating
        self.wins = 0
        self.loses = 0

    def play(self, game_state: dict) -> dict:
        """
        Play the tournament card and update the game state.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: A dictionary containing the results of playing the card.
        """
        return {"card_played:": self.name}

    def attack(self, target) -> dict:
        """
        Perform an attack on a target.

        Args:
            target: The target to attack.

        Returns:
            dict: A dictionary containing the result of the attack.
        """
        return {"loser": target.id}

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage (int): The amount of damage received.

        Returns:
            dict: A dictionary containing the result of the defense.
        """
        return {"winner": self.id}

    def get_combat_stats(self) -> dict:
        """
        Get the combat statistics of the card.

        Returns:
            dict: A dictionary containing wins and losses.
        """
        return {
            "wins": self.wins,
            "losses": self.loses
        }

    def calculate_rating(self) -> int:
        """
        Calculate the current rating of the object.

        Returns:
            int: The calculated rating.
        """
        return self.rating

    def update_wins(self, wins: int) -> None:
        """
        Update the number of wins and adjust the rating.

        Args:
            wins (int): The number of wins to add.
        """
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        """
        Update the number of losses and adjust the rating.

        Args:
            losses (int): The number of losses to add.
        """
        self.loses += losses
        self.rating -= 16

    def get_rank_info(self) -> dict:
        """
        Get ranking information for the object.

        Returns:
            dict: A dictionary containing ranking details.
        """
        return {self.name: self.rating}
