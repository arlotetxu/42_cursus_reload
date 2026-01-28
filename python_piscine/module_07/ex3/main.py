from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def ft_main():
    p1_mana = 50

    print()
    print("=== DataDeck Game Engine ===")
    print()

    print("Configuring Fantasy Card Game...")
    p1_factory = FantasyCardFactory()
    print(f"Factory: {type(p1_factory).__name__}")
    p1_strategy = AggressiveStrategy()
    print(f"Strategy: {p1_strategy.get_strategy_name()}")
    my_game = GameEngine()
    my_game.configure_engine(factory=p1_factory, strategy=p1_strategy)
    print(f"Available types: {my_game.player_cards}")
    print()
    print("Simulating aggressive turn...")
    p1_hand = my_game.player_hand
    p1_hand_print = [f"{card.name} ({card.cost})"for card in p1_hand]
    print(f"Hand: {p1_hand_print}")
    print()
    print("Turn execution:")
    print(f"Strategy: {my_game.strategy_name}")
    p1_turn = my_game.simulate_turn()
    print(f"Actions: {p1_turn}")
    p1_mana -= p1_turn["mana_used"]
    print()
    print("Game Report:")
    print(f"{my_game.get_engine_status()}")
    print()
    print("Abstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    ft_main()
