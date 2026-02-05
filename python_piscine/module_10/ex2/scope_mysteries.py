from typing import Any


def mage_counter() -> callable:
    """
    Returns a closure that increments and returns a counter.
    """
    n: int = 0

    def counter(*args, **kwargs) -> int:
        nonlocal n
        n += 1
        return n
    return counter


def spell_accumulator(initial_power: int) -> callable:
    """
    Returns a closure that accumulates power values starting from
    an initial value.
    """
    power: int = initial_power

    def adding_power(extra_power: int) -> int:
        nonlocal power
        power += extra_power
        return power
    return adding_power


def enchantment_factory(enchantment_type: str) -> callable:
    """
    Returns a closure that prepends a type to an item name.
    """
    e_type: str = enchantment_type

    def enchantment_type(item_name: str):
        return f"{e_type} {item_name}"
    return enchantment_type


def memory_vault() -> dict[str, callable]:
    """
    Returns a dictionary with 'store' and 'recall' closures to
    manage a private memory vault.
    """
    my_memory_vault: dict = {}

    def store(key: str, value: Any) -> None:
        my_memory_vault[key] = value

    def recall(key: str) -> Any:
        return my_memory_vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


# ===========================================================================

def ft_main() -> None:
    """
    Main function to demonstrate and test the various closure
    factories defined in the script.
    """
    print()
    print("Testing mage counter...")
    res = mage_counter()
    print(f"Call 1: {res()}")
    print(f"Call 2: {res()}")
    print(f"Call 3: {res()}")
    print()

    print("Testing spell acumulator...")
    initial_power: int = 0
    add_power = spell_accumulator(initial_power)
    print(f"Initial power: {initial_power}")
    print(f"Adding 5 -> New power value: {add_power(5)}")
    print(f"Adding 10 -> New power value: {add_power(10)}")
    print(f"Adding 2 -> New power value: {add_power(2)}")
    print()

    print("Testing enchantment factory...")
    res = enchantment_factory("Flaming")
    enchant1 = res("Sword")
    print(enchant1)
    res = enchantment_factory("Frozen")
    enchant2 = res("Shield")
    print(enchant2)
    print()

    print("Testing memory vault...")
    res = memory_vault()
    print("Storing: {'one': 1}")
    res["store"]("one", 1)
    print("Storing: {'two': 2}")
    res["store"]("two", 2)
    print("Recalling 'two'")
    print(res["recall"]("two"))
    print("Recalling a non valid key ('three'):")
    print(res["recall"]("three"))


if __name__ == "__main__":
    ft_main()
