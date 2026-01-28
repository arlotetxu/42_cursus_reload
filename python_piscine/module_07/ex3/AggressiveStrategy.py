from ex0.CreatureCard import CreatureCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    A game strategy that focuses on playing all cards in hand and
    attacking all available targets.
    """
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Executes a turn by playing all cards in hand and attacking
        all targets on the battlefield.

        Args:
            hand (list): The list of cards currently in the player's hand.
            battlefield (list): The list of cards currently on the battlefield.

        Returns:
            dict: A dictionary containing the results of the turn, including
                  cards played, mana used, targets attacked, and damage dealt.
        """
        turn_result: dict = {
            "cards_played": [card.name for card in hand],
            "mana_used": sum(card.cost for card in hand),
            "targets_attacked": [card.name for card in battlefield],
            "damage_dealt": sum(
                card._attack for card in hand if isinstance(
                    card, CreatureCard
                    )
            ),
        }

        return turn_result

    def get_strategy_name(self) -> str:
        """
        Returns the name of the strategy.

        Returns:
            str: The name of the strategy class.
        """

        return type(self).__name__

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Prioritizes targets based on their cost
        """

        return sorted(available_targets, key=lambda target: target.cost)
