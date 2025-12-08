#!/usr/bin/env python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    str_final = ""
    if unit == "packets":
        str_final = (f"{seed_type.capitalize()} seeds: {quantity} "
                     f"packets available")
    elif unit == "grams":
        str_final = f"{seed_type.capitalize()} seeds: {quantity} grams total"
    elif unit == "area":
        str_final = (f"{seed_type.capitalize()} seeds: covers {quantity} "
                     f"square meters")
    else:
        str_final = (f"{seed_type.capitalize()} seeds: {quantity} "
                     f"Unknown unit type")
    print(str_final)


# if __name__ == "__main__":
#     ft_seed_inventory("tomato", 15, "packets")
#     ft_seed_inventory("carrot", 8, "grams")
#     ft_seed_inventory("lettuce", 12, "area")
