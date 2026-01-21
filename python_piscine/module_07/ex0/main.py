from random import randint
from CreatureCard import CreatureCard
from icecream import ic

# my_random = randint(0, 100)
# ic(my_random)


def ft_main() -> None:
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    rarity_list: list[str] = ["Legendary", "Common"]

    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=randint(1, 5),
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
        attack=randint(1, 10),
        health=randint(0, 10)
    )

    print("CreatureCard Info:")
    fire_dragon_info: dict =fire_dragon.get_card_info()
    print(fire_dragon_info)
    print()
    fire_dragon.play(fire_dragon_info)


if __name__ == "__main__":
    ft_main()
