#!/usr/bin/env python3

from icecream import ic

if __name__ == "__main__":
    print("=== Player Inventory System ===")

    # weapon = {"sword":
    #           {"type": "rare", "quantity": 1, "prize": 500}
    # }
    # consumable = {"potion":
    #               {"type": "common", "quantity": 5, "prize": 50}
    #               }
    # armor = {"shield":
    #          {"type": "uncommon", "quantity": 1, "prize": 200}
    #          }

    alice_inv = {
        "weapon": [
            {"name": "sword", "type": "rare", "quantity": 1, "prize": 500},
        ],
        "consumable": [
            {"name": "potion", "type": "common", "quantity": 5, "prize": 50},
        ],
        "armor": [
            {"name": "shield", "type": "uncommon", "quantity": 1, "prize": 200},
        ],
    }

    bob_inv = {
        "weapon": [
            {"name": "sword", "type": "rare", "quantity": 0, "prize": 500},
        ],
        "consumable": [
            {"name": "potion", "type": "common", "quantity": 0, "prize": 50},
        ],
        "armor": [
            {"name": "shield", "type": "uncommon", "quantity": 0, "prize": 200},
        ],
    }


    print("\n=== Alice's Inventory ===")
    inv_value = 0
    item_count = 0
    weapon_count = 0
    consumable_count = 0
    armor_count = 0
    for cat, cat_list in alice_inv.items():
        for item in cat_list:
            print(f"{item["name"]} ({cat}, {item["type"]}): "
                    f"{item["quantity"]}x @ {item["prize"]} gold each = "
                    f"{item["quantity"] * item["prize"]}")
            inv_value += item["quantity"] * item["prize"]
            item_count += item["quantity"]
            if cat == "weapon":
                weapon_count += item["quantity"]
            elif cat == "consumable":
                consumable_count += item["quantity"]
            elif cat == "armor":
                armor_count += item["quantity"]

    print(f"\nInventory value: {inv_value} gold")
    print(f"Item count: {item_count} items")
    print(f"Categories: weapon({weapon_count}, consumable({consumable_count}), armor({armor_count})")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    