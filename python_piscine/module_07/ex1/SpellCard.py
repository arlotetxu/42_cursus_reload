from ex0.Card import Card


class SpellCard(Card):
    """
    Class representing a spell card in the game.
    """
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """
        Initialize a spell card with a name, mana cost, rarity, and effect
        type.
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = self

    def play(self, game_state: dict) -> dict:
        """
        Play the spell card and update the game state.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: The updated game state.
        """
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = self.effect_type
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        """
        Resolve the spell's effect on the given targets.

        Args:
            targets (list): A list of target cards.

        Returns:
            dict: A dictionary containing the results of the spell resolution.
        """
        spell_info = {}
        if self.effect_type == "Deal 3 damage to target":
            for target in targets:
                target.set_health = target.get_health() - 3
                if target.get_health() <= 0:
                    self.deck.remove_card(card_name=target.name)
        self.deck.remove_card(card_name=self.name)

        return spell_info
