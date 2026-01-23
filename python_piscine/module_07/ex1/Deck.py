from ex0.Card import Card


class Deck:
    def __init__(self):
        self.my_cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if card not in self.my_cards:
            self.my_cards.append(card)
            card.deck = self # Inyeccion de dependencia del mazo (deck)

    def remove_card(self, card_name: str) -> bool:
        for card in self.my_cards:
            if card.name == card_name:
                self.my_cards.remove(card)
                return True
        return False

    def shuffle(self) -> None: ...

    def draw_card(self) -> Card:
        card_types = {
            "CreatureCard": "Creature",
            "SpellCard": "Spell",
            "ArtifactCard": "Artifact",
        }
        if self.my_cards:
            for card in self.my_cards:
                print(
                    f"Drew: {card.name} "
                    f"({card_types.get(card.__class__.__name__, 'Unknown')})")
                yield (card)

    def get_deck_stats(self) -> dict: ...
