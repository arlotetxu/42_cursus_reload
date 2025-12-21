#!/usr/bin/env python3


def ft_show_player_info(player: str, inventory: dict) -> None:
    """
        Display detailed inventory information for a specific player.

        This function retrieves and displays a player's complete inventory,
        including all items with their details, total inventory value, item
        count, and category breakdown.

        Args:
            player (str): The name of the player whose inventory should be
            displayed.
            inventory (dict): A dictionary containing all players' inventories.

        Returns:
            None: This function prints the inventory information to stdout
            and does not return a value.

        Note:
            If the player is not found in the inventory, an empty inventory
            will be displayed with zero values.
    """
    player_data: dict = inventory.get("players",{})\
        .get(player, {})
    player_items: dict = inventory.get("players", {})\
        .get(player, {}).get("items", {})
    catalog: dict = inventory.get("catalog", {})

    cat_items: dict = {}

    print(f"\n=== {player}'s Inventory ===")
    for name, quantity in player_items.items():
        for item, specific in catalog.items():
            if item == name:
                print(
                    f"{name} ({specific['type']}, {specific['rarity']}): "
                    f"{quantity}x @ {specific['value']} "
                    f"gold each = {quantity * specific['value']} "
                    f"gold"
                )
                if specific['type'] not in cat_items:
                    cat_items[specific['type']] = quantity
                else:
                    cat_items[specific['type']] += quantity

    print(f"\nInventory value: {player_data.get('total_value', 0)} gold")
    print(f"Item count: {player_data.get('item_count', 0)} items")
    print("Categories: ", end="")
    cat_list = [f"{k}({v})" for k, v in cat_items.items()]
    for cat in cat_list[:-1]:
        print(cat, end=", ")
    print(cat_list[-1])


def ft_donation(inventory: dict) -> None:
    """
    Transfer 2 quantum_rings from Alice's inventory to Bob's inventory.

    This function performs a donation transaction where Alice gives
    Bob 2 quantum_rings. It updates the quantity of quantum_rings in both Alice's and
    Bob's consumable inventories and prints the transaction details and
    updated quantum_rings counts.

    Returns:
        None: This function prints transaction information but does not return
        a value.

    Note:
        - Assumes Alice has at least 2 quantum_rings available for donation
        - The function only transfers quantum_rings, not other consumable items
    """
    alice_data: dict = inventory.get("players", {}).get("alice", {})
    bob_data: dict = inventory.get("players", {}).get("bob", {})
    alice_items: dict = inventory.get("players", {}).get("alice", {}).get("items", {})
    bob_items: dict = inventory.get("players", {}).get("bob", {}).get("items", {})
    catalog: dict = inventory.get("catalog", {})

    quantum_ring_value = 0
    for item, specific in catalog.items():
        if item == "quantum_ring":
            quantum_ring_value = specific["value"]

    print("\n=== Transaction: Alice gives Bob 2 quantum_rings ===")

    # Removing 2 quantum_ring from Alice's items
    alice_items['quantum_ring'] = alice_items['quantum_ring'] - 2
    alice_data["total_value"] = alice_data["total_value"] - (2 * quantum_ring_value)
    alice_data["item_count"] = alice_data["item_count"] - 2

    # Adding 2 quantum_rings to Bob's items
    if 'quantum_ring' in bob_items:
        bob_items['quantum_ring'] += 2
    else:
        bob_items['quantum_ring'] = 2
    bob_data["total_value"] = bob_data["total_value"] + (
            2 * quantum_ring_value)
    bob_data["item_count"] = bob_data["item_count"] + 2

    print("Transaction successful!")
    print("\n=== Updated Inventories ===")
    print(f"Alice quantum_rings: {alice_items['quantum_ring']}")
    print(f"Bob quantum_rings: {bob_items['quantum_ring']}")


def ft_analytics(inventory: dict) -> None:
    """
    Analyze and display inventory statistics across all players.

    This function processes a multi-level inventory dictionary to calculate
    and display three key analytics: the player with the most valuable
    inventory, the player with the most items, and a list of all unique rare
    items found across all players.

    Args:
        inventory (dict): A nested dictionary where:

    Returns:
        None: This function prints the analytics directly to stdout.

    Output:
        Prints three lines of analytics:
        - Most valuable player and their total inventory value in gold
        - Player with most items and their total item count
        - Comma-separated list of all unique rare items found
    """
    print("\n=== Inventory Analytics ===")
    players_data: dict = inventory.get("players", {})
    catalog: dict = inventory.get("catalog", {})

    most_valuable_player: str = ""
    most_value: int = 0
    most_items_player: str = ""
    most_items: int = 0
    rarest_catalog: list = []
    rarest_in_players: list = []

    for player, data in players_data.items():
        if data['total_value'] > most_value:
            most_value = data["total_value"]
            most_valuable_player = player
        if data['item_count'] > most_items:
            most_items = data["item_count"]
            most_items_player = player

    print(f"Most valuable player: {most_valuable_player} ({most_value} gold)")
    print(f"Most items: {most_items_player} ({most_items} items)")

    for item, specific in catalog.items():
        if specific["rarity"] == "rare":
            rarest_catalog.append(item)

    for player, data in players_data.items():
        player_items = data.get("items", {})
        for item in player_items:
            if item in rarest_catalog and item not in rarest_in_players:
                    rarest_in_players.append(item)
    print("Rarest items:", end=" ")
    for rare in rarest_in_players[:-1]:
        print(f"{rare}", end=", ")
    print(rarest_in_players[-1])


# MAIN=======================================================================
if __name__ == "__main__":
    print("=== Player Inventory System ===")

    inventory_2 = {
        'players':
            {'alice':
                 {'items': {'pixel_sword': 1, 'code_bow': 1, 'health_byte': 1,
                            'quantum_ring': 3},
                  'total_value': 1875,
                  'item_count': 6},
             'bob':
                 {'items': {'code_bow': 3, 'pixel_sword': 2},
                  'total_value': 900,
                  'item_count': 5},
             'charlie':
                 {'items': {'pixel_sword': 1, 'code_bow': 1},
                  'total_value': 350,
                  'item_count': 2},
             'diana':
                 {'items': {'code_bow': 3, 'pixel_sword': 3, 'health_byte': 3, 'data_crystal': 3},
                  'total_value': 4125,
                  'item_count': 12}},
        'catalog':
            {'pixel_sword':
                       {'type': 'weapon', 'value': 150, 'rarity': 'common'},
            'quantum_ring':
                        {'type': 'accessory', 'value': 500, 'rarity': 'rare'},
            'health_byte':
                       {'type': 'consumable', 'value': 25, 'rarity': 'common'},
            'data_crystal':
                       {'type': 'material', 'value': 1000, 'rarity': 'legendary'},
            'code_bow':
                       {'type': 'weapon', 'value': 200, 'rarity': 'uncommon'}}}


    ft_show_player_info("alice", inventory_2)
    ft_donation(inventory_2)
    ft_analytics(inventory_2)
