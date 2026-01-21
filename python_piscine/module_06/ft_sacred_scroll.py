#!/usr/bin/env python3
import alchemy


def ft_main() -> None:
    """
    Main function to demonstrate package structure and access.

    It showcases direct module access within a package and package-level
    access controlled by __init__.py. It also prints package metadata.
    """

    print("\n=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")

    print(f"alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError as a_e:
        print(f"alchemy.create_fire(): {a_e.__class__.__name__} "
              f"- not exposed")
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError as a_e:
        print(f"alchemy.create_water(): {a_e.__class__.__name__} "
              f"- not exposed")
    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError as a_e:
        print(f"alchemy.create_earth(): {a_e.__class__.__name__} "
              f"- not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError as a_e:
        print(f"alchemy.create_air(): {a_e.__class__.__name__} "
              f"- not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    ft_main()
