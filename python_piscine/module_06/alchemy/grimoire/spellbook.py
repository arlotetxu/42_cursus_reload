#!/usr/bin/env python3


def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Records a spell after validating its ingredients.

    This function takes a spell name and a string of ingredients,
    validates the ingredients using `validate_ingredients` from the
    `validator` module, and returns a string indicating whether the
    spell was recorded or rejected.

    Args:
        spell_name (str): The name of the spell to record.
        ingredients (str): A string containing the ingredients for the spell.
    """

    from alchemy.grimoire.validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    if "INVALID" in validation:
        return (f"Spell rejected: {spell_name} ({validation})")
    return (f"Spell recorded: {spell_name} ({validation})")
