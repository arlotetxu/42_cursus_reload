#!/usr/bin/env python3

def ft_with_list(data: dict) -> None:
    """
    Processes player data using list comprehensions and prints analytics.
    Args:
        data (dict): Dictionary containing player information under the
            "players" key. Each player entry should be a dictionary with at
            least a "total_score" field.
    Prints:
        - List of players with a total score greater than 2000.
        - List of all players' scores doubled.
        - List of all active player names.
    """

    print("\n=== List Comprehension Examples ===")
    player_data: dict = data.get("players", {})
    high_score_players: list = [
        player
        for player, player_info in player_data.items()
        if player_info["total_score"] > 2000
    ]
    print(f"High scorers (>2000): {high_score_players}")
    scores_doubled: list = [
        int(data["total_score"]) * 2 for player, data in player_data.items()
    ]
    print(f"Scores doubled: {scores_doubled}")
    active_players: list = [player for player in player_data.keys()]
    print(f"Active players: {active_players}")


def ft_with_dict(data: dict) -> None:
    """
    Processes player data from a dictionary and prints analytics using dict
    comprehensions.
    Args:
        data (dict): A dictionary containing player information and game modes.
    Prints:
        - Player scores as a dictionary mapping player names to their total
            scores.
        - Counts of players preferring each game mode.
        - Achievement counts for each player.
    """

    print("\n=== Dict Comprehension Examples ===")
    player_data: dict = data.get("players", {})
    player_scores: dict = {
        player: player_info["total_score"]
        for player, player_info in player_data.items()
    }
    print(f"Player scores: {player_scores}")

    mode_counts: dict = {
        mode: sum(1 for p in player_data.values()
                  if p["favorite_mode"] == mode)
        for mode in data["game_modes"]
    }
    print(f"Favorite mode counts: {mode_counts}")
    player_achievement: dict = {
        player: player_info["achievements_count"]
        for player, player_info in player_data.items()
    }
    print(f"Achievement counts: {player_achievement}")


def ft_with_set(data: dict) -> None:
    """
    Displays examples of set comprehensions using player and session data.
    Args:
        data (dict): A dictionary containing 'players' and 'sessions' data.
            - 'players': A dictionary where keys are player identifiers and
                values are dictionaries with player info.
            - 'sessions': A list of dictionaries, each representing a session
                with 'player' and 'region' keys.
    Prints:
        - Unique players from session data.
        - Unique achievements from player data.
        - Active regions from session data.
    """

    print("\n=== Set Comprehension Examples ===")
    player_data: dict = data.get("players", {})
    session_data: list = data.get("sessions", [])
    unique_players: set = {session["player"] for session in session_data}
    print(f"Unique players: {unique_players}")
    unique_achievements: set = {player_info["achievement"]
                                for player, player_info in player_data.items()}
    print(f"Unique achievements: {unique_achievements}")
    active_regions: set = {sesion["region"] for sesion in session_data}
    print(f"Active regions: {active_regions}")


def ft_combined(data: dict) -> None:
    """
    Performs a combined analysis on player data and prints summary statistics.
    Args:
        data (dict): A dictionary containing player information under the
        "players" key. Each player entry should include "achievement",
        "total_score", and "achievements_count".
    Prints:
        - Total number of players.
        - Total number of unique achievements.
        - Average score across all players.
        - Top performer with their score and achievement count.
    """

    player_data: dict = data.get("players", {})
    unique_achievements: set = {
        player_info["achievement"]
        for player, player_info in player_data.items()}
    player_scores: dict = {
        player: player_info["total_score"]
        for player, player_info in player_data.items()
        }

    print("\n=== Combined Analysis ===")
    total_players: int = len({player for player in player_data.keys()})
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    average_score: int = sum(
        player_info['total_score']
        for player, player_info in player_data.items()) / total_players
    print(f"Average score: {average_score:.1f}")
    top_perf_player: str = max(player_scores, key=player_scores.get)
    top_perf_points: int = player_scores[top_perf_player]
    top_perf_achiev: int = [player_info['achievements_count']
                            for player, player_info in player_data.items()
                            if player == top_perf_player][0]
    print(f"Top performer: {top_perf_player} ({top_perf_points} points, "
          f"{top_perf_achiev} achievements)")


def ft_main() -> None:
    """
    Displays a game analytics dashboard using the provided player, session,
    game mode, and achievement data.
    The function initializes a data dictionary containing information about
    players, their game sessions, available game modes, and achievements.
    It then prints a dashboard header and calls four functions:
    ft_with_list, ft_with_dict, ft_with_set, and ft_combined, each of which
    performs analytics or displays information using different data
    structures and approaches.

    No arguments are required, and the function does not return any value.
    """

    data: dict = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
                "achievement": "first_blood",
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
                "achievement": "level_master",
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
                "achievement": "first_blood",
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
                "achievement": "treasure_seeker",
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
                "achievement": "first_blood",
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
                "achievement": "speed_runner",
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
                "region": "NA",
            },
            {
                "player": "bob",
                "duration_minutes": 32,
                "score": 1478,
                "mode": "casual",
                "completed": True,
                "region": "EU",
            },
            {
                "player": "diana",
                "duration_minutes": 17,
                "score": 1570,
                "mode": "competitive",
                "completed": False,
                "region": "ASIA",
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
                "region": "SA",
            },
            {
                "player": "diana",
                "duration_minutes": 15,
                "score": 2361,
                "mode": "competitive",
                "completed": False,
                "region": "OCE",
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
                "region": "NA",
            },
            {
                "player": "frank",
                "duration_minutes": 34,
                "score": 1285,
                "mode": "casual",
                "completed": True,
                "region": "EU",
            },
            {
                "player": "alice",
                "duration_minutes": 53,
                "score": 1238,
                "mode": "competitive",
                "completed": False,
                "region": "ASIA",
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 1555,
                "mode": "casual",
                "completed": False,
                "region": "SA",
            },
            {
                "player": "frank",
                "duration_minutes": 92,
                "score": 2754,
                "mode": "casual",
                "completed": True,
                "region": "OCE",
            },
            {
                "player": "eve",
                "duration_minutes": 98,
                "score": 1102,
                "mode": "casual",
                "completed": False,
                "region": "NA",
            },
            {
                "player": "diana",
                "duration_minutes": 39,
                "score": 2721,
                "mode": "ranked",
                "completed": True,
                "region": "EU",
            },
            {
                "player": "frank",
                "duration_minutes": 46,
                "score": 329,
                "mode": "casual",
                "completed": True,
                "region": "ASIA",
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
                "region": "SA",
            },
            {
                "player": "eve",
                "duration_minutes": 117,
                "score": 1388,
                "mode": "casual",
                "completed": False,
                "region": "OCE",
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
                "region": "NA",
            },
            {
                "player": "charlie",
                "duration_minutes": 22,
                "score": 1110,
                "mode": "ranked",
                "completed": False,
                "region": "EU",
            },
            {
                "player": "frank",
                "duration_minutes": 79,
                "score": 1854,
                "mode": "ranked",
                "completed": False,
                "region": "ASIA",
            },
            {
                "player": "charlie",
                "duration_minutes": 33,
                "score": 666,
                "mode": "ranked",
                "completed": False,
                "region": "SA",
            },
            {
                "player": "alice",
                "duration_minutes": 101,
                "score": 292,
                "mode": "casual",
                "completed": True,
                "region": "OCE",
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
                "region": "NA",
            },
            {
                "player": "diana",
                "duration_minutes": 53,
                "score": 2540,
                "mode": "competitive",
                "completed": False,
                "region": "EU",
            },
            {
                "player": "eve",
                "duration_minutes": 115,
                "score": 147,
                "mode": "ranked",
                "completed": True,
                "region": "ASIA",
            },
            {
                "player": "frank",
                "duration_minutes": 118,
                "score": 2299,
                "mode": "competitive",
                "completed": False,
                "region": "SA",
            },
            {
                "player": "alice",
                "duration_minutes": 42,
                "score": 1880,
                "mode": "casual",
                "completed": False,
                "region": "OCE",
            },
            {
                "player": "alice",
                "duration_minutes": 97,
                "score": 1178,
                "mode": "ranked",
                "completed": True,
                "region": "NA",
            },
            {
                "player": "eve",
                "duration_minutes": 18,
                "score": 2661,
                "mode": "competitive",
                "completed": True,
                "region": "EU",
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
                "region": "ASIA",
            },
            {
                "player": "eve",
                "duration_minutes": 46,
                "score": 2101,
                "mode": "casual",
                "completed": True,
                "region": "SA",
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
                "region": "OCE",
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
        ],
    }

    print("=== Game Analytics Dashboard ===")
    ft_with_list(data)
    ft_with_dict(data)
    ft_with_set(data)
    ft_combined(data)


ft_main()
