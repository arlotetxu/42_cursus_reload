#!/usr/bin/env python3

def ft_main() -> None:
    """
    Analyzes and displays achievement statistics for a set of players.

    This function initializes a dictionary of players and their achievements
    (with possible duplicates), then performs set operations to:
    - Display each player's unique achievements.
    - Compute and display all unique achievements among selected players.
    - Find achievements common to all selected players.
    - Identify achievements unique to only one player (rare achievements).
    - Compare achievements between Alice and Bob, showing their common and
        unique achievements.

    No arguments or return values.
    """

    achieves: dict = {
        'alice': [
            'boss_hunter', 'first_blood', 'pixel_perfect', 'speed_runner',
            'first_blood', 'first_blood',
            ],
        'bob': [
            'first_blood', 'level_master', 'boss_hunter', 'treasure_seeker',
            'level_master', 'level_master',
            ],
        'charlie': [
            'treasure_seeker', 'boss_hunter', 'combo_king', 'first_blood',
            'boss_hunter', 'first_blood', 'boss_hunter', 'first_blood',

            ],
        'diana': [
            'first_blood', 'combo_king', 'level_master', 'treasure_seeker',
            'speed_runner', 'combo_king', 'combo_king', 'level_master',
            ],
        'eve': [
            'level_master', 'treasure_seeker', 'first_blood',
            'treasure_seeker', 'first_blood', 'treasure_seeker',
            ],
        'frank': [
            'explorer', 'boss_hunter', 'first_blood', 'explorer',
            'first_blood', 'boss_hunter',
            ]
            }

    alice: set = set(achieves['alice'])
    bob: set = set(achieves['bob'])
    charlie: set = set(achieves['charlie'])
    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_uniques: set = set.union(alice, bob, charlie)
    print(f"All unique achievements: {all_uniques}")
    print(f"Total unique achievements: {len(all_uniques)}")

    common: set = set.intersection(alice, bob, charlie)
    print(f"\nCommon to all players: {common}")

    alice_only: set = alice - bob - charlie
    bob_only: set = bob - alice - charlie
    charlie_only: set = charlie - alice - bob
    rares: set = set.union(alice_only, bob_only, charlie_only)
    print(f"Rare achievements (1 player): {rares}")

    print(f"\nAlice vs Bob common: {set.intersection(alice, bob)}")
    print(f"Alice unique: {set.difference(alice, bob)}")
    print(f"Bob unique: {set.difference(bob, alice)}")


ft_main()
