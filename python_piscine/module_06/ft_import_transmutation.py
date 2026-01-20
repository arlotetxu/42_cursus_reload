#!/usr/bin/env python3
import alchemy


def method_1() -> None:
    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def method_2() -> None:
    print("\nMethod 2 - Specific function import:")
    from alchemy import create_water
    print(f"create_water(): {create_water()}")


def method_3() -> None:
    print("\nMethod 3 - Aliased import:")
    from alchemy.potions import healing_potion as heal
    print(f"heal(): {heal()}")


def method_4() -> None:
    print("\nMethod 4 - Multiple imports:")
    from alchemy.elements import create_earth
    from alchemy import create_fire
    from alchemy.potions import strength_potion as strength
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength()}")


def ft_main() -> None:
    print("=== Import Transmutation Mastery ===")
    method_1()
    method_2()
    method_3()
    method_4()
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    ft_main()
