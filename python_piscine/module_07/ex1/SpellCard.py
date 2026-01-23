from ex0.Card import Card
from icecream import ic


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = self

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = self.effect_type
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        for target in targets:
            target._health -= 3
        ic(self)
        self.deck.remove_card(card_name=self.name)
