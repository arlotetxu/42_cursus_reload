#!/usr/bin/env python3

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """
    Transmutes lead into gold.

    Returns:
        str: A message indicating the successful transmutation.
    """
    return (f"Lead transmuted to gold using {create_fire()}")


def stone_to_gem() -> str:
    """
    Transmutes a stone into a gem.

    Returns:
        str: A message indicating the successful transmutation.
    """
    return (f"Stone transmuted to gem using {create_earth()}")


if __name__ == "__main__":
    lead_to_gold()
    stone_to_gem()
