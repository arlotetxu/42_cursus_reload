from random import randint
from ex0.Card import Card, CardRarity, CardTypes
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical


def ft_main() -> None:
    """
    Main function to demonstrate the ability system and multiple inheritance.

    It showcases the EliteCard class, which implements both Combatable and
    Magical interfaces, demonstrating its ability to perform combat actions
    and cast spells while inheriting from the base Card class.
    """
    print()
    print("=== DataDeck Ability System ===")
    print()

    # Getting the different class methods names
    print("EliteCard capabilities:")

    card_methods: list = [
        method for method in dir(Card) if not method.startswith("_")
        ]
    print(f"- Card: {card_methods}")

    combat_methods: list = [
        method for method in dir(Combatable) if not method.startswith("_")
        ]
    print(f"- Combatable: {combat_methods}")

    magic_methods: list = [
        method for method in dir(Magical) if not method.startswith("_")
        ]
    print(f"- Magical: {magic_methods}")

    # === General Variables ===
    rarity_list: list = [rare.value for rare in CardRarity]
    player_mana: int = 10

    # === Creating the EliteCard instance ===
    arcane_warrior: EliteCard = EliteCard(
        name="Arcane Warrior",
        cost=randint(1, 10),
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
    )
    arcane_warrior._attack: int = 5  # Attribute injection
    arcane_warrior._health: int = 10  # Attribute injection
    arcane_warrior.combat_type: str = "melee"  # Attribute injection
    arcane_warrior.block: str = 3  # Attribute injection

    print()
    print(
        f"Playing {arcane_warrior.name} "
        f"({CardTypes[type(arcane_warrior).__name__.upper()].value})"
    )

    # === Creating Enemy ===
    enemy: CreatureCard = CreatureCard(
        name="Enemy",
        cost=randint(1, 10),
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
        attack=randint(1, 10),
        health=randint(1, 10),
    )

    # ============ Combat phase ============
    print()
    print("Combat phase:")
    combat_result: dict = arcane_warrior.attack(target=enemy)
    print(f"Attack result: {combat_result}")
    # Defense
    defense_result: dict = arcane_warrior.defend(incoming_damage=5)
    print(f"Defense result: {defense_result}")

    # ============ Magic phase ============
    print()
    print("Magic phase:")

    # === Creating Enemies ===
    enemy_1: CreatureCard = CreatureCard(
        name="Enemy1",
        cost=randint(1, 10),
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
        attack=randint(1, 10),
        health=randint(1, 10),
    )

    enemy_2: CreatureCard = CreatureCard(
        name="Enemy2",
        cost=randint(1, 10),
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
        attack=randint(1, 10),
        health=randint(1, 10),
    )

    # === Creating a spell ===
    spell_1 = SpellCard(
        name="Fireball",
        cost=randint(1, 3),
        rarity=rarity_list[randint(0, len(rarity_list) - 1)],
        effect_type="??"
    )

    magic_result: dict = arcane_warrior.cast_spell(
        spell_name=spell_1.name, targets=[enemy_1, enemy_2]
        )
    player_mana -= magic_result["mana_used"]
    print(f"Spell cast: {magic_result}")
    arcane_warrior.mana = player_mana  # Attribute injection
    mana_result: dict = arcane_warrior.channel_mana(amount=3)
    print(f"Mana channel: {mana_result}")
    player_mana += mana_result["channeled"]

    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    ft_main()
