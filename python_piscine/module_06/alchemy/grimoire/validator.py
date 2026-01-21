#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    """
    Validates a string of ingredients.

    Checks if any of the essential elements (fire, water, earth, air)
    are present in the provided ingredients string.

    Args:
        ingredients (str): A space-separated string of ingredients.

    Returns:
        str: A string indicating whether the ingredients are "VALID" or
             "INVALID", along with the original ingredients.
    """
    for word in ingredients.split():
        if word in ["fire", "water", "earth", "air"]:
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
