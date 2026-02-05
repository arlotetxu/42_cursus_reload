

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sorts artifacts by power in descending order."""

    return list(sorted(artifacts, key=lambda x: x["power"], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filters mages by minimum power."""

    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wraps each spell string with asterisks."""

    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculates power statistics for a list of mages."""

    my_mages: dict = {
        "max_power": int(max(map(lambda x: x["power"], mages))),
        "min_power": int(min(map(lambda x: x["power"], mages))),
        "avg_power": sum(map(lambda x: x["power"], mages)) / len(mages)
    }
    return my_mages


def ft_main() -> None:
    """Main function to test spell functions."""

    artifacts = [
        {'name': 'Wind Cloak', 'power': 96, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 120, 'type': 'armor'},
        {'name': 'Lightning Rod', 'power': 111, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 63, 'type': 'focus'}
        ]

    mages = [
        {'name': 'Rowan', 'power': 59, 'element': 'fire'},
        {'name': 'Riley', 'power': 52, 'element': 'lightning'},
        {'name': 'Riley', 'power': 86, 'element': 'shadow'},
        {'name': 'Ember', 'power': 86, 'element': 'ice'},
        {'name': 'Rowan', 'power': 68, 'element': 'water'}
        ]

    spells = ['fireball', 'darkness', 'lightning', 'shield']

    print()
    result: list[dict] = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(f"{result[0].get('name')} ({result[0].get('power')}) "
          f"comes before {result[1].get('name')} ({result[1].get('power')})")
    print("="*42)
    result: list[dict] = power_filter(mages, 60)
    print("Testing filtering mages (power > 60)...")
    for mage in result:
        print(f"{mage['name']} - {mage['power']}")
    print("="*42)
    result: list[str] = spell_transformer(spells)
    print("Testing spell transformer...")
    for spell in result[:-1]:
        print(spell, end=" ")
    print(f"{result[-1]}")
    print("="*42)
    print("Printing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    ft_main()
