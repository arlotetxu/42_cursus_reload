# from ex0.Card import Card
from random import randint

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from icecream import ic

# effect_type_list = ["damage", "heal", "buff", "debuff"]
# effect = choice(effect_type_list)
# print(effect)


def ft_main() -> None:
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")

    my_deck = Deck()
    player_mana = 50
    card_list = []
    game_state = {}

    spell_1 = SpellCard(
        name="Lightning Bolt",
        cost=randint(1, 10),
        rarity="Common",
        effect_type="Deal 3 damage to target",
    )
    card_list.append(spell_1)

    arti_1 = ArtifactCard(
        name="Mana Crystal",
        cost=randint(1, 10),
        rarity="Common",
        durability=randint(1, 10),
        effect="Permanent: +1 mana per turn",
    )
    card_list.append(arti_1)

    creat_1 = CreatureCard(
        name="Fire Dragon",
        cost=2,
        rarity="Legendary",
        attack=randint(1, 10),
        health=randint(1, 10),
    )
    card_list.append(creat_1)

    for card in card_list:
        my_deck.add_card(card)

    # Vamos sacando cada carta de mazo con un generador.
    # Se ejecuta el metodo draw_card con cada next
    # Se ejecuta el metodo play
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
    ic(my_deck.my_cards)
    ic(creat_1._health)
    spell_1.resolve_effect([creat_1,])
    ic(creat_1._health)
    ic(my_deck.my_cards)

    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    ft_main()
