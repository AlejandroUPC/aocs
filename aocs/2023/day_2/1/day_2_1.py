from typing import List
from aocs.commons.input_reader import input_file_readlines

CUBES_AVAILABLE = {"red": 12, "green": 13, "blue": 14}


def is_game_possible(game_shows: str) -> bool:
    for shows in game_shows.split(";"):
        for show in shows.split(","):
            amount, color = show.strip().split(" ")
            try:
                if CUBES_AVAILABLE[color.strip()] < int(amount):
                    return False
            except KeyError:
                continue
    return True


def iter_games_sum_id_possible(all_games: List[str]) -> int:
    id_acc = 0
    for game in all_games:
        game_metadata, game = game.split(":")
        if is_game_possible(game):
            id_acc += int(game_metadata.split(" ")[-1])
    return id_acc


def main() -> None:
    print(
        iter_games_sum_id_possible(input_file_readlines("aocs/2023/day_2/1/input.txt"))
    )


if __name__ == "__main__":
    main()
