from ex0.Card import Card, Card_Types
from random import shuffle as sf


class Deck:
    """
    Class representing a deck of cards in the game.
    """
    def __init__(self):
        """
        Initialize a new deck with an empty list of cards.
        """
        self.my_cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck and inject the deck reference into the card.

        Args:
            card (Card): The card to add.
        """
        if card not in self.my_cards:
            self.my_cards.append(card)
            card.deck = self  # (Dependency injection to the deck)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove a card from the deck by its name.

        Args:
            card_name (str): The name of the card to remove.
        """

        for card in self.my_cards:
            if card.name == card_name:
                self.my_cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """
        Shuffle the cards in the deck.
        """
        sf(self.my_cards)

    def draw_card(self) -> Card:
        """
        Draw cards from the deck one by one.

        Yields:
            Card: The next card in the deck.
        """
        if self.my_cards:
            for card in self.my_cards:
                print(
                    f"Drew: {card.name} "
                    f"({Card_Types[(type(card).__name__).upper()].value})")
                yield (card)

    def get_deck_stats(self) -> dict:
        """
        Calculate and return statistics about the cards in the deck.

        Returns:
            dict: A dictionary containing statistics about the deck.
        """
        deck_stats = {}

        deck_stats["total_cards"] = len(self.my_cards)
        deck_stats["creatures"] = sum(
            1 for card in self.my_cards
            if card.type.__class__.__name__ == "CreatureCard"
            )
        deck_stats["spells"] = sum(
            1 for card in self.my_cards
            if card.type.__class__.__name__ == "SpellCard"
            )
        deck_stats["artifacts"] = sum(
            1 for card in self.my_cards
            if card.type.__class__.__name__ == "ArtifactCard"
            )
        total_cost = sum(card.cost for card in self.my_cards)
        deck_stats["avg_cost"] = round(total_cost / len(self.my_cards), 1)

        return deck_stats
