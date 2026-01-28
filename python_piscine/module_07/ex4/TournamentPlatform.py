from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """
    A platform to manage tournament matches between cards.
    """

    def __init__(self):
        """
        Initialize the TournamentPlatform.
        """
        self.cards_playing: list = []
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a card for the tournament.

        Args:
            card (TournamentCard): The card to register.

        Returns:
            str: A string confirming registration with card details.
        """
        self.cards_playing.append(card)
        interfaces = [base.__name__ for base in card.__class__.__bases__]
        return (f"{card.name} (ID: {card.id}):\n"
                f"- Interfaces: {interfaces}"
                f"\n- Rating: {card.rating}"
                f"\n- Record: {card.wins}-{card.loses}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        Create and resolve a match between two cards.

        Args:
            card1_id (str): The ID of the first card.
            card2_id (str): The ID of the second card.

        Returns:
            dict: A dictionary containing the match results.
        """
        match_result: dict = {}
        defense_result: dict = self.cards_playing[0].defend(incoming_damage=3)
        attack_result: dict = (
            self.cards_playing[0].attack(self.cards_playing[1])
            )
        match_result = defense_result | attack_result
        self.cards_playing[0].update_wins(wins=1)
        self.cards_playing[1].update_losses(losses=1)
        match_result["winner_rating"] = self.cards_playing[0].rating
        match_result["loser_rating"] = self.cards_playing[1].rating
        self.matches += 1

        return match_result

    def get_leaderboard(self) -> list:
        """
        Get the current tournament leaderboard.

        Returns:
            list: A list of dictionaries containing card ranking info.
        """
        leaderb_result = []
        for card in self.cards_playing:
            card_info = {
                "card_name": card.name,
                "rating": card.rating,
                "wins": card.wins,
                "loses": card.loses
                }
            leaderb_result.append(card_info)

        return leaderb_result

    def generate_tournament_report(self) -> dict:
        """
        Generate a report of the tournament platform status.

        Returns:
            dict: A dictionary containing tournament statistics.
        """
        return {
            "total_cards": len(self.cards_playing),
            "matches_played": self.matches,
            "avg_rating": int(
                sum(card.rating for card in self.cards_playing)
                / len(self.cards_playing)
            ),
            "platform_status": "active",
        }
