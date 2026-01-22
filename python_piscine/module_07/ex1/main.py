# from ex0.Card import Card
from random import randint
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard

# effect_type_list = ["damage", "heal", "buff", "debuff"]
# effect = choice(effect_type_list)
# print(effect)


def ft_main() -> None:
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")

    my_deck = Deck()
    card_list = []

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
    generator = my_deck.draw_card()
    for _ in range(len(card_list)):
        next(generator)


if __name__ == "__main__":
    ft_main()
