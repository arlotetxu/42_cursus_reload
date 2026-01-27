from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

class GameEngine:

    # TODO: implementar el metodo static para generar una mano (en main)
    # TODO: init de la clase para guardar datos que luego usaremos en get_engine_status


    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        player_cards = factory.create_themed_deck(size=5)
        self.strategy = strategy
        self.factory = factory
        print(f"Available types: {player_cards}")

    def simulate_turn(self) -> dict:
        # TODO lanzar el metodo para crear una mano y pasarlo como argumento a la funcion de abajo
        self.strategy.execute_turn()

        # TODO devolver el diccionario que obtengo de ejecutar execute_turn()

    def get_engine_status(self) -> dict:
        ...
        # TODO generar las estadisticas
