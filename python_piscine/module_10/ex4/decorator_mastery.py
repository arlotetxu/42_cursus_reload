import time
from functools import wraps
from typing import Any


def spell_timer(func: callable) -> callable:
    """
    Decorator that measures and prints the execution time of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start: float = time.time()
        res: Any = func(*args, **kwargs)
        stop: float = time.time()
        print(f"Spell completed in {(stop - start):.6f}")
        return res

    return wrapper


def power_validator(min_power: int) -> callable:
    """Decorator that checks if the provided power level is sufficient for
    casting a spell."""
    def power_valid(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power: Any = kwargs.get("power")
            if not power and args:
                power: Any = args[-1]
            if isinstance(power, int) and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return power_valid


def retry_spell(max_attempts: int) -> callable:
    """Decorator that retries a spell casting function a specified number
    of times"""
    def spelling(func: callable) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {i + 1}"
                          f"/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts\n"

        return wrapper

    return spelling


class MageGuild:
    """Class representing a mage guild with spell casting capabilities."""
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate the mage's name to ensure it meets the criteria."""
        if len(name) < 3:
            return False
        for c in name:
            if not c.isalpha() and not c == 32:
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with the given name and power level."""
        return f"Successfully cast {spell_name} with {power} power"


# ===========================================================================


@spell_timer
def fireball() -> str:
    """Cast a fireball spell."""
    return f"Result: {fireball.__name__.capitalize()} cast!"


@power_validator(10)
def check_power(power: int) -> str:
    """Check if the power level is sufficient."""
    return f"Power level {power} is OK"


@retry_spell(2)
def cast_spell(spell: str):
    """Cast a spell with the given name."""
    print(f"Casting {spell}")
    spell_names: list = ["tornado", "flash", "meteor", "darkness"]
    if spell not in spell_names:
        raise ValueError
    return f"{spell} casted!\n"


# ===========================================================================


def ft_main() -> None:
    """Main function to test the decorators and MageGuild class."""

    test_powers: list[int] = [16, 17, 11, 9]

    print()
    print("Testing spell timer...")
    print(fireball())
    print()

    print("Testing power validation...")
    for power in test_powers:
        print(f"{check_power(power)}")
    print()

    print("Testing retry spell...")
    list_of_spells: list[str] = [
        "tornado",
        "flash",
        "perico",
        "meteor",
        "paquito",
        "pedrito",
    ]
    for spell in list_of_spells:
        print(cast_spell(spell))
    print()

    print("Testing MageGuild...")
    my_mage: MageGuild = MageGuild()
    print(my_mage.validate_mage_name("arlo"))
    print(my_mage.validate_mage_name("arlo3"))
    print(my_mage.cast_spell(spell_name="Lightning", power=15))
    print(my_mage.cast_spell(spell_name="Lightning", power=6))


if __name__ == "__main__":
    ft_main()
