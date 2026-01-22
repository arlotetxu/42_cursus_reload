#!/usr/bin/env python3
from random import randint
from ex0.CreatureCard import CreatureCard


def ft_main() -> None:
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    rarity_list: list[str] = ["Legendary", "Common"]

    try:
        fire_dragon = CreatureCard(
            name="Fire Dragon",
            cost=randint(4, 10),
            rarity=rarity_list[randint(0, len(rarity_list) - 1)],
            attack=randint(1, 10),
            health=randint(1, 10)
        )
    except ValueError as v_e:
        print(v_e)
        return

    try:
        goblin_warrior = CreatureCard(
            name="Goblin Warrior",
            cost=randint(1, 5),
            rarity=rarity_list[randint(0, len(rarity_list) - 1)],
            attack=randint(1, 10),
            health=randint(1, 10)
        )
    except ValueError as v_e:
        print(v_e)
        return

    game_state: dict = {}
    print("CreatureCard Info:")
    fire_dragon_info: dict = fire_dragon.get_card_info()
    print(fire_dragon_info)
    print()
    # goblin_warrior_info: dict = goblin_warrior.get_card_info()
    # print(goblin_warrior_info)
    # print()

    try:
        fire_dragon.play(game_state=game_state)
        fire_dragon.attack_target(goblin_warrior)
    except ValueError as v_e:
        print(v_e)
        return
    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    ft_main()
