from random import randint, choice, sample
from ex0.CreatureCard import CreatureCard
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    The main engine for simulating card game turns.
    """

    def __init__(self):
        """
        Initializes the GameEngine.
        """
        self.turns_simulated: int = 0

    @staticmethod
    def ft_create_hand(factory: CardFactory) -> list:
        """
        Creates a hand of cards for the player from the factory's deck.

        Args:
            factory (CardFactory): The factory containing the deck.

        Returns:
            list: A list of cards representing the player's hand.
        """
        my_hand_size: int = 3
        deck_cards: list = factory.deck.my_cards

        if len(deck_cards) <= my_hand_size:
            return deck_cards.copy()

        my_hand: list = []

        creatures: list = [
            c for c in deck_cards if isinstance(c, CreatureCard)
            ]

        if creatures:
            chosen_creature: CreatureCard = choice(creatures)
            my_hand.append(chosen_creature)

            other_cards: list = [
                card for card in deck_cards if card is not chosen_creature
                ]

            num_remaining_cards: int = my_hand_size - 1
            my_hand.extend(sample(other_cards, k=num_remaining_cards))
        else:
            my_hand = sample(deck_cards, k=my_hand_size)

        return my_hand

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        Configures the game engine with a factory and a strategy.

        Args:
            factory (CardFactory): The card factory to use.
            strategy (GameStrategy): The game strategy to use.
        """
        self.strategy: GameStrategy = strategy
        self.factory: CardFactory = factory

        self.player_cards: dict = factory.create_themed_deck(size=5)
        self.strategy_name: str = type(self.strategy).__name__
        self.player_hand: list = self.ft_create_hand(factory)

    def simulate_turn(self) -> dict:
        """
        Simulates a single turn of the game.

        Returns:
            dict: A dictionary containing the results of the turn.
        """
        # Generating an Enemy Player creature
        enemy_player: CreatureCard = CreatureCard(
            name="Enemy Player",
            cost=randint(1, 3),
            rarity="Common",
            attack=randint(1, 3),
            health=randint(1, 5)
        )
        self.factory.deck.add_card(enemy_player)
        self.my_turn: dict = self.strategy.execute_turn(
            hand=self.player_hand, battlefield=[enemy_player]
            )
        self.turns_simulated += 1

        return self.my_turn

    def get_engine_status(self) -> dict:
        """
        Gets the current status and statistics of the game engine.

        Returns:
            dict: A dictionary containing game statistics.
        """
        game_report: dict = {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy_name,
            "total_damage": self.my_turn["damage_dealt"],
            "cards_created": len(self.factory.deck.my_cards)
        }

        return game_report
