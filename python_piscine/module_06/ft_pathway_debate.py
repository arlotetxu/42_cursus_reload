#!/usr/bin/env python3


def ft_absolute() -> None:
    """Demonstrates absolute imports."""

    print()
    print("Testing Absolute Imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")


def ft_relative() -> None:
    """Demonstrates relative imports."""

    print()
    print("Testing Relative Imports (from advanced.py):")
    from alchemy.transmutation.advanced import philosophers_stone, \
        elixir_of_life
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")


def ft_pack_access() -> None:
    """
    Demonstrates accessing functions within a subpackage using the
    fully qualified package name.

    This method shows how to call functions from 'transmutation'
    subpackage after importing the top-level 'alchemy' package."""

    print()
    print("Testing Package Access:")
    import alchemy
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold():}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")


def ft_main() -> None:
    """
    Main function to demonstrate absolute, relative, and package-level
    imports.

    It calls functions that showcase different import methods.
    """

    print("=== Pathway Debate Mastery ===")
    ft_absolute()
    ft_relative()
    ft_pack_access()
    print()
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_main()
