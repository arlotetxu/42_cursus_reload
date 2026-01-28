from random import choice, randint
from ex0.Card import CardRarity, Creatures
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def ft_main() -> None:
    """
    Main function to demonstrate the Tournament Platform functionality.
    Registers cards, creates a match, and displays the leaderboard and report.
    """
    print()
    print("=== DataDeck Tournament Platform ===")
    print()
    print("Registering Tournament Cards...")
    print()
    # Creating Tournament cards and registering
    my_tournament = TournamentPlatform()
    card_1 = TournamentCard(
        name=choice([card.value for card in Creatures]),
        cost=randint(1, 5),
        rarity=choice([card.value for card in CardRarity]),
        rating=1200,
    )
    print(my_tournament.register_card(card=card_1))

    card_2 = TournamentCard(
        name=choice([card.value for card in Creatures]),
        cost=randint(1, 5),
        rarity=choice([card.value for card in CardRarity]),
        rating=1150,
    )
    print(my_tournament.register_card(card=card_2))

    print("Creating tournament match...")
    match_result: dict = my_tournament.create_match(
        card1_id=card_1.id, card2_id=card_2.id
        )
    print(f"Match result: {match_result}")
    print()

    print("Tournament Leaderboard:")
    leader_resul: list = my_tournament.get_leaderboard()
    for i, card in enumerate(leader_resul, start=1):
        print(f"{i}. {card['card_name']} - Rating: {card['rating']} "
              f"({card['wins']}-{card['loses']})")
    print()

    print("Platform Report:")
    platform_result: dict = my_tournament.generate_tournament_report()
    print(f"{platform_result}")
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    ft_main()
