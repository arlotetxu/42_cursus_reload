from ex0.Card import Card


class ArtifactCard(Card):
    """
    Class representing an artifact card in the game.
    """
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        """
        Initialize an artifact card with a name, mana cost, rarity,
        durability, and effect.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = self

    def play(self, game_state: dict) -> dict:
        """
        Play the artifact card and update the game state.

        Args:
            game_state (dict): The current state of the game.
        """
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = self.effect
        return game_state

    def activate_ability(self) -> dict:
        """
        Activate the artifact's special ability and update its durability.

        Returns:
            dict: A dictionary containing the results of the activation.
        """
        arti_info = {}

        if self.effect == "Permanent: +1 mana per turn":
            arti_info["input_mana"] = 1
        self.durability -= 1
        if self.durability == 0:
            self.deck.remove_card(card_name=self.name)
        return arti_info
