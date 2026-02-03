

def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    return list(sorted(artifacts, key=lambda x: x["power"], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:

    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:

    my_mages = {
        "max_power": int(max(map(lambda x: x["power"], mages))),
        "min_power": int(min(map(lambda x: x["power"], mages))),
        "avg_power": sum(map(lambda x: x["power"], mages)) / len(mages)
    }
    return my_mages


def ft_main() -> None:

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

    print(artifact_sorter(artifacts))
    print("="*42)
    print(power_filter(mages, 60))
    print("="*42)
    print(spell_transformer(spells))
    print("="*42)
    print(mage_stats(mages))




if __name__ == "__main__":
    ft_main()
