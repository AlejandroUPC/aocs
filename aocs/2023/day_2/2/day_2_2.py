from typing import List
from aocs.commons.input_reader import input_file_readlines
from itertools import accumulate


def iter_games_power_set(all_games: List[str]) -> int:
    power_set_acc = 0
    for game in all_games:
        _, game_values = game.split(":")
        power_set_value = compute_power_set(game_values)
        power_set_acc += power_set_value
    return power_set_acc


def compute_power_set(game_shows: str) -> bool:
    cube_values_accumulator = {"red": [], "green": [], "blue": []}
    formated_game_shows = list(
        map(lambda x: x.strip().split(" "), game_shows.replace(";", ",").split(","))
    )
    for show in formated_game_shows:
        val, color = show
        try:
            cube_values_accumulator[color.strip()].append(int(val))
        except KeyError:
            continue
    return list(
        accumulate(
            [max(color_list) for color_list in cube_values_accumulator.values()],
            lambda x, y: x * y,
        )
    )[-1]


def main() -> None:
    print(iter_games_power_set(input_file_readlines("aocs/2023/day_2/2/input.txt")))


if __name__ == "__main__":
    main()
