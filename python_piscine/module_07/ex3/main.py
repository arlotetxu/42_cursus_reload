from random import choice, sample

from ex0.CreatureCard import CreatureCard
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
from icecream import ic


def ft_create_hand(factory: CardFactory) -> list:
    my_hand_size = 3
    deck_cards = factory.deck.my_cards

    if len(deck_cards) <= my_hand_size:
        return deck_cards.copy()

    my_hand = []

    creatures = [c for c in deck_cards if isinstance(c, CreatureCard)]

    if creatures:
        chosen_creature = choice(creatures)
        my_hand.append(chosen_creature)

        other_cards = [card for card in deck_cards if card is not chosen_creature]

        num_remaining_cards = my_hand_size - 1
        my_hand.extend(sample(other_cards, k=num_remaining_cards))
    else:
        my_hand = sample(deck_cards, k=my_hand_size)

    return my_hand

def ft_cards_2_play(cards: list):
    ...


def ft_main():
    p1_mana = 50

    print()
    print("=== DataDeck Game Engine ===")
    print()

    print("Configuring Fantasy Card Game...")
    p1_factory = FantasyCardFactory()
    print(f"Factory: {type(p1_factory).__name__}")
    p1_strategy = AggressiveStrategy()
    print(f"Strategy: {p1_strategy.get_strategy_name()}")
    my_game = GameEngine()
    my_game.configure_engine(factory=p1_factory, strategy=p1_strategy)

    p1_hand = ft_create_hand(p1_factory)
    p1_hand_print = [card.name + " (" + str(card.cost) + ")" for card in p1_hand]
    print()

    print("Simulating aggressive turn...")
    print(f"Hand: {p1_hand_print}")
    print()

    print("Turn execution:")
    print(f"Strategy: {p1_strategy.get_strategy_name()}")




if __name__ == "__main__":
    ft_main()
