from day_3_2 import compute_valid_sum


def test_aoc_example():
    _input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    assert compute_valid_sum(_input) == 467835
