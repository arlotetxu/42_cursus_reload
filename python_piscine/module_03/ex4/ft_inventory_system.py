#!/usr/bin/env python3
# TODO añadir docstrings


def ft_show_player_info(player: str, inventory: dict) -> None:
    player_data: dict = inventory.get(player, {})
    inv_value_player: int = 0
    items_player: int = 0
    cat_items: list = []

    print(f"\n=== {player}'s Inventory ===")
    for categs, items in player_data.items():
        for item in items:
            print(
                f"{item['name']} ({categs}, {item['type']}): "
                f"{item['quantity']}x @ {item['prize']} "
                f"gold each = {item['quantity'] * item['prize']} "
                f"gold"
            )
            inv_value_player += item["quantity"] * item["prize"]
            items_player += item["quantity"]
            cat_items.append(f"{categs}({item['quantity']})")

    print(f"\nInventory value: {inv_value_player} gold")
    print(f"Item count: {items_player}")
    print("Categories: ", end="")
    for item in cat_items[:-1]:
        print(f"{item}", end=", ")
    print(f"{cat_items[-1]}")


def ft_donation(inventory: dict) -> None:
    alice_consumables: list = inventory.get("Alice", {}).get("consumable", [])
    bob_consumables: list = inventory.get("Bob", {}).get("consumable", [])

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    for items in alice_consumables:
        if items["name"] == "potion":
            items["quantity"] -= 2
            break

    for items in (
        bob_consumables
    ):  # TODO chequear si Bob tiene el item. Si no, habria que copiarlo?
        if items["name"] == "potion":
            items["quantity"] += 2
            break
    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    for item in alice_consumables:
        if item["name"] == "potion":
            print(f"Alice potions: {item['quantity']}")
            break
    for item in bob_consumables:
        if item["name"] == "potion":
            print(f"Bob potions: {item['quantity']}")
            break


def ft_analytics(inventory: dict) -> None:
    print("\n=== Inventory Analytics ===")
    most_valued: dict = {}
    more_items: dict = {}
    rare_items: list = []

    for player, player_data in inventory.items():
        total_value = 0
        total_items = 0
        for cats, items in player_data.items():
            for item in items:
                total_value += item["quantity"] * item["prize"]
                total_items += item["quantity"]
                if item["type"] == "rare" and item["name"] not in rare_items:
                    rare_items.append(item["name"])
        most_valued[player] = total_value
        more_items[player] = total_items

    max_player: str = None
    max_value: int = 0
    for player, value in most_valued.items():
        if value > max_value:
            max_value = value
            max_player = player
    print(f"Most valuable player: {max_player} ({max_value} gold)")

    max_item_player: str = None
    max_items: int = 0
    for player, value in more_items.items():
        if value > max_items:
            max_items = value
            max_item_player = player
    print(f"Most items: {max_item_player} ({max_items} items)")
    print("Rarest items: ", end="")
    for rare in rare_items[:-1]:
        print(f"{rare}", end=", ")
    print(f"{rare_items[-1]}")


# MAIN=======================================================================
if __name__ == "__main__":
    print("=== Player Inventory System ===")
    inventory: dict = {
        "Alice": {
            "weapon": [
                {"name": "sword", "type": "rare", "quantity": 1, "prize": 500},
            ],
            "consumable": [
                {"name": "potion", "type": "common", "quantity": 5, "prize": 50},
            ],
            "armor": [
                {"name": "shield", "type": "uncommon", "quantity": 1, "prize": 200},
            ],
        },
        "Bob": {
            "weapon": [],
            "consumable": [
                {"name": "potion", "type": "common", "quantity": 0, "prize": 50},
            ],
            "armor": [
                {"name": "magic_ring", "type": "rare", "quantity": 1, "prize": 200},
            ],
        },
    }
    ft_show_player_info("Alice", inventory)
    ft_donation(inventory)
    ft_analytics(inventory)
