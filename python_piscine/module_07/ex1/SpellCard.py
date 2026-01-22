from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = self

    def play(self, game_state: dict) -> dict:
        print("Estoy en play de SpellCard")

    def resolve_effect(self, targets: list) -> dict:
        ...
