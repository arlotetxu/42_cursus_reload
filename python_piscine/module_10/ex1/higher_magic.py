def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Combines two spells into one returning a tuple."""

    def combination(*args, **kwargs) -> tuple:
        """Executes both spells with the same arguments."""
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combination


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Amplifies the result of a spell by a multiplier."""

    def amplification(*args, **kwargs) -> int:
        """Executes spell and multiplies result."""
        return base_spell(*args, **kwargs) * multiplier
    return amplification


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Casts a spell only if a condition is met."""

    def casting_spell(*args, **kwargs):
        """Checks condition before casting."""
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return casting_spell


def spell_sequence(spells: list[callable]) -> callable:
    """Executes a list of spells in order."""

    def spelling(*args, **kwargs):
        """Returns a list of results from spells."""
        ret_list = []
        for spell in spells:
            ret_list.append(spell(*args, **kwargs))
        return ret_list
    return spelling


# ===============================================================================
def spell_fireball(name: str, target: str) -> str:
    """Returns a fireball hit message."""
    return f"{name} hits {target}"


def spell_heal(name: str, target: str) -> str:
    """Returns a healing message."""
    return f"Heals {target}"


def base_sp(value: int) -> int:
    """Returns the base power value."""
    return value * 1


def condition_to_spell(t_f: bool, name: str) -> bool:
    """Returns the boolean condition."""
    return t_f


def launch_spell(t_f: bool, name: str) -> str:
    """Returns a spell cast message."""
    return f"{name} casted"


def cast_spell1() -> str:
    """Casts the first spell."""
    return "Spell_1 casted"


def cast_spell2() -> str:
    """Casts the second spell."""
    return "Spell_2 casted"


def cast_spell3() -> str:
    """Casts the third spell."""
    return "Spell_3 casted"


# ===============================================================================

def ft_main() -> None:
    """Tests higher-order magic functions."""

    print()
    print("Testing spell combiner...")
    spell_combi = spell_combiner(spell_fireball, spell_heal)
    res = spell_combi("Fireball", "Dragon")
    print(f"{res[0]}, {res[1]}")

    print()
    print("Testing power amplifier...")
    power_amp = power_amplifier(base_sp, 3)
    print(f"Original: {base_sp(10)}, Amplified: {power_amp(10)}")

    print()
    print("Testing conditional casting...")
    conditional_c = conditional_caster(condition_to_spell, launch_spell)
    res = conditional_c(True, "Fireball")
    print(res)

    print()
    print("Testing sequence spell cast...")
    spell_list = [cast_spell1, cast_spell2, cast_spell3]
    spell_seq = spell_sequence(spell_list)
    res = spell_seq()
    print(res)


if __name__ == "__main__":
    ft_main()
