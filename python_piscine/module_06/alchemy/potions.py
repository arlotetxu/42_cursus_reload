#!/usr/bin/env python3

def healing_potion() -> str:
    """
    Brew a healing potion.

    Returns:
        str: A message indicating the successful brewing of a healing potion
             with the elements used.
    """
    from alchemy.elements import create_fire, create_water
    return (f"Healing potion brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    """
    Brew a strength potion.

    Returns:
        str: A message indicating the successful brewing of a strength potion
             with the elements used.
    """

    from alchemy.elements import create_earth, create_fire
    return (f"Strength potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    """
    Brew an invisibility potion.

    Returns:
        str: A message indicating the successful brewing of an invisibility
             potion with the elements used.
    """

    from alchemy.elements import create_air, create_water
    return (f"Invisibility potion brewed with {create_air()}"
            f" and {create_water()}")


def wisdom_potion() -> str:
    """
    Brew a wisdom potion.

    Returns:
        str: A message indicating the successful brewing of a wisdom potion
             with all elements used.
    """

    from alchemy.elements import \
        create_fire, create_water, create_earth, create_air
    return (f"Wisdom potion brewed with all elements: "
            f"\n{create_fire()}, {create_water()}, {create_earth()}, "
            f"{create_air()}")


if __name__ == "__main__":
    print(f"{healing_potion()}")
    print(f"\n{strength_potion()}")
    print(f"\n{invisibility_potion()}")
    print(f"\n{wisdom_potion()}")
