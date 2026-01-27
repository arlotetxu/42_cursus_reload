from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def register_card(self, card: TournamentCard) -> str:
        ...

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        ...

    def get_leaderboard(self) -> list:
        ...

    def generate_tournament_report(self) -> dict:
        ...
