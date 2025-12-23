#!/usr/bin/env python3

if __name__ == "__main__":
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon", }
    bob = {"first_kill", "level_10", "boss_slayer", "collector", }
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_uniques = set.union(alice, bob, charlie)
    print(f"All unique achievements: {all_uniques}")
    print(f"Total unique achievements: {len(all_uniques)}")

    common = set.intersection(alice, bob, charlie)
    print(f"\nCommon to all players: {common}")

    alice_only = alice - bob - charlie
    bob_only = bob - alice - charlie
    charlie_only = charlie - alice - bob
    rares = set.union(alice_only, bob_only, charlie_only)
    print(f"Rare achievements (1 player): {rares}")

    print(f"\nAlice vs Bob common: {set.intersection(alice, bob)}")
    print(f"Alice unique: {set.difference(alice, bob)}")
    print(f"Bob unique: {set.difference(bob, alice)}")
