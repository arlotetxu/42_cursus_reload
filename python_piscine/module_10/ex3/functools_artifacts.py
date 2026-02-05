import operator
from functools import lru_cache, partial, reduce, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduces a list of spell powers based on the specified operation."""

    if spells:
        if operation == "add":
            return reduce(operator.add, spells)
        elif operation == "multiply":
            return reduce(operator.mul, spells)
        elif operation == "max":
            return reduce(max, spells)
        elif operation == "min":
            return reduce(min, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Creates a dictionary of partially applied enchantment functions."""

    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number using memoization."""

    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """Creates a single-dispatch function for processing different spell
    types."""

    @singledispatch
    def dispatcher(arg1) -> str:
        return "generic return"

    @dispatcher.register
    def is_int(arg1: int):
        return "Damage spell"

    @dispatcher.register
    def is_str(arg1: str):
        return "Enchantment"

    @dispatcher.register
    def is_list(arg1: list):
        return " | ".join(dispatcher(item) for item in arg1)

    return dispatcher

# ===========================================================================


def base_enchantment_test(power: int, element: str, target: str) -> str:
    """Returns a formatted string describing an elemental attack."""
    return f"{element} attacks {target} with {power} power"


def ft_main() -> None:
    """Main function to demonstrate and test functools-based spell
    utilities."""

    print()
    print("Testing spell reducer...")
    spells: list = [1, 2, 3, 4]
    res: int = spell_reducer(spells, "add")
    print(f"Sum: {res}")
    res: int = spell_reducer(spells, "multiply")
    print(f"Product: {res}")
    res: int = spell_reducer(spells, "max")
    print(f"Max: {res}")
    print()

    print("Testing partial enchanter...")
    res: dict[str, callable] = partial_enchanter(base_enchantment_test)
    print(res["fire_enchant"]("Enemy_of_fire"))
    print(res["ice_enchant"]("Enemy_of_ice"))
    print(res["lightning_enchant"]("Enemy_of_light"))
    print()

    print("Testing memoized fibonnacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()

    print("Testing spell dispatcher...")
    res:callable = spell_dispatcher()
    print(f"With int: {res(1)}")
    print(f"With str: {res('string')}")
    print(f"With list: {res(['fireball', 15 , 'amazing ice'])}")


if __name__ == "__main__":
    ft_main()
