#!/usr/bin/env python3

from alchemy.grimoire import validator


def ft_late_import() -> None:
    """
    Demonstrates late import technique to avoid circular imports.

    Imports spellbook at runtime instead of module load time to prevent
    circular dependency issues. Tests record_spell with various inputs.

    Returns:
        None: Prints test results to stdout.
    """

    from alchemy.grimoire import spellbook
    print("Testing spell recording with validation:")
    spell_1: str = "Fireball"
    ing_1: str = "fire air"
    check_spell_1: str = spellbook.record_spell(spell_1, ing_1)
    print(f"record_spell(\"{spell_1}\", \"{ing_1}\"): {check_spell_1}")
    spell_2: str = "Dark Magic"
    ing_2: str = "shadow"
    check_spell_2: str = spellbook.record_spell(spell_2, ing_2)
    print(f"record_spell(\"{spell_2}\", \"{ing_2}\"): {check_spell_2}")
    print()

    print("Testing late import technique:")
    from alchemy.grimoire.spellbook import record_spell
    spell_3: str = "Lightning"
    ing_3: str = "air"
    check_spell_3: str = record_spell(spell_3, ing_3)
    print(f"record_spell(\"{spell_3}\", \"{ing_3}\"): {check_spell_3}")
    print()


def ft_main() -> None:
    """
    Main function to demonstrate circular curse breaking.

    Validates two ingredient strings using the validator module and prints
    the results. Also calls ft_late_import to show late import usage.

    Returns:
        None
    """
    print()

    print("=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")
    ing_1: str = "fire air"
    check_ing_1: str = validator.validate_ingredients(ing_1)
    print(f"validate_ingredients(\"{ing_1}\"): {check_ing_1}")
    ing_2: str = "dragon scales"
    check_ing_2: str = validator.validate_ingredients(ing_2)
    print(f"validate_ingredients(\"{ing_2}\"): {check_ing_2}")
    print()

    ft_late_import()


if __name__ == "__main__":
    ft_main()
