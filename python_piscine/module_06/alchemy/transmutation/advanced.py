#!/usr/bin/env python3

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """
    Creates the legendary Philosopher's Stone.

    Returns:
        str: A message indicating the creation of the Philosopher's Stone.
    """
    return (f"Philosopher’s stone created using {lead_to_gold()} "
            f"and {healing_potion()}")


def elixir_of_life() -> str:
    """
    Creates the mythical Elixir of Life.

    Returns:
        str: A message indicating the creation of the Elixir of Life."""
    return ("Elixir of life: eternal youth achieved!")


if __name__ == "__main__":
    philosophers_stone()
    elixir_of_life()
