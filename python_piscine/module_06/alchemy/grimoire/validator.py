#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    for word in ingredients.split():
        if word in ["fire", "water", "earth", "air"]:
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
