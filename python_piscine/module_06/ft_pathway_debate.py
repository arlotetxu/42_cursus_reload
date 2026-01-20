#!/usr/bin/env python3


def ft_absolute() -> None:
    print()
    print("Testing Absolute Imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")


def ft_relative() -> None:
    print()
    print("Testing Relative Imports (from advanced.py):")
    from alchemy.transmutation.advanced import philosophers_stone, \
        elixir_of_life
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")


def ft_pack_access() -> None:
    print()
    print("Testing Package Access:")
    import alchemy
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold():}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")


def ft_main() -> None:
    print("=== Pathway Debate Mastery ===")
    ft_absolute()
    ft_relative()
    ft_pack_access()
    print()
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_main()
