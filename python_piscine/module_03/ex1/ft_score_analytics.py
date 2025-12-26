#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:
    """
    Analyzes player scores provided as command-line arguments and prints
    statistics.

    This function reads integer scores from the command-line arguments,
    processes them, and displays analytics including the total number of
    players, total score, average score, highest and lowest scores, and the
    score range. If no scores are provided, or if any argument is not a
    valid integer, an appropriate message is displayed.

    Usage:
        python3 ft_score_analytics.py <score1> <score2> ...

    Returns:
        None
    """

    num_args = len(sys.argv)
    scores = []

    print("=== Player Score Analytics ===")
    if num_args == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")
    elif num_args > 1:
        try:
            for score in sys.argv[1:]:
                scores.append(int(score))
        except ValueError:
            print(f"oops, I typed '{score}' instead of ... 🤷")
            return

        print(f"Scores processed: {scores}")
        print(f"Total players: {num_args - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / (num_args - 1):.2f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


ft_score_analytics()
