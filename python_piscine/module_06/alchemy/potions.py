#!/usr/bin/env python3

# from elements import create_air, create_earth, create_fire, create_water

def healing_potion() -> str:
    from alchemy.elements import create_fire, create_water
    return (f"Healing potion brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    from alchemy.elements import create_earth, create_fire
    return (f"Strength potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    from alchemy.elements import create_air, create_water
    return (f"Invisibility potion brewed with {create_air()}"
            f" and {create_water()}")


def wisdom_potion() -> str:
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
