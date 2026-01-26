from random import randint
from ex0.Card import Card_Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def ft_main() -> None:
    """
    Main function to demonstrate the deck builder system.

    It showcases the creation of different card types (Spell, Artifact,
    Creature), adding them to a deck, calculating deck statistics, and
    drawing/playing cards using a generator to demonstrate polymorphism.
    """
    print()
    print("=== DataDeck Deck Builder ===")
    print()

    my_deck = Deck()
    player_mana = 50
    card_list = []
    game_state = {}
    rarity_list = [rare.value for rare in Card_Rarity]

    # Creating the different Card types
    spell_1 = SpellCard(
        name="Lightning Bolt",
        cost=randint(1, 10),
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
        effect_type="Deal 3 damage to target",
    )
    card_list.append(spell_1)

    arti_1 = ArtifactCard(
        name="Mana Crystal",
        cost=randint(1, 10),
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
        durability=randint(1, 10),
        effect="Permanent: +1 mana per turn",
    )
    card_list.append(arti_1)

    creat_1 = CreatureCard(
        name="Fire Dragon",
        cost=2,
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
        attack=randint(1, 10),
        health=randint(1, 10),
    )
    card_list.append(creat_1)

    # Adding cards to the deck
    for card in card_list:
        my_deck.add_card(card)

    print("Building deck with different card types...")
    my_deck_stats = my_deck.get_deck_stats()
    print(f"Deck Stats: {my_deck_stats}")

    print()
    print("Drawing and playing cards:")

    # Getting the cards from the deck with a generator
    # draw_card() is executed
    # play() method is executed
    generator = my_deck.draw_card()
    for card in card_list:
        print()
        next(generator)
        if card.is_playable(player_mana):
            play_result = card.play(game_state)
            print(f"Play result: {play_result}")
            player_mana -= card.cost
        else:
            print(f"Not enought mana to play {card.name}")

    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    ft_main()
