from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        turn_result = {
            "cards_played": hand,
            "mana_used": sum(card.cost for card in hand),
            "targets_attacked": [card.name for card in battlefield],
            "damage_dealt": sum(card.attack for card in hand)
        }

        return turn_result


    def get_strategy_name(self) -> str:

        return type(self).__name__

    def prioritize_targets(self, available_targets: list) -> list:
        ...
        # TODO ordenar los targets de menor a mayor coste
