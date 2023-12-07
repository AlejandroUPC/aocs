import pytest
from day_3_1 import compute_valid_sum, Map, Part, PartSurroundings
import re


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
    assert compute_valid_sum(_input) == 4361


def test_reddit_example():
    _input = [
        "12.......*..",
        "+.........34",
        ".......-12..",
        "..78........",
        "..*....60...",
        "78.........9",
        ".5.....23..$",
        "8...90*12...",
        "............",
        "2.2......12.",
        ".*.........*",
        "1.1..503+.56",
    ]
    assert compute_valid_sum(_input) == 925


def test_redit_example_idk():
    _input = ["...123", "456*.."]
    assert compute_valid_sum(_input) == 579


def test_reddit_example_2():
    _input = [
        "12.......*..",
        "+.........34",
        ".......-12..",
        "..78........",
        "..*....60...",
        "78..........",
        ".......23...",
        "....90*12...",
        "............",
        "2.2......12.",
        ".*.........*",
        "1.1.......56",
    ]
    assert compute_valid_sum(_input) == 413


def test_reddit_example_3():
    _input = ["....................", "..-52..52-..52..52..", "..................-."]
    assert compute_valid_sum(_input) == 156


def test_reddit_example_4():
    _input = [
        ".......................*......*",
        "...910*...............233..189.",
        "2......391.....789*............",
        "...................983.........",
        "0........106-...............226",
        ".%............................$",
        "...*......$812......812..851...",
        ".99.711.............+.....*....",
        "...........................113.",
        "28*.....411....%...............",
    ]
    assert compute_valid_sum(_input) == 7253


def test_edge_top_left_still_surroudned_should_ignore():
    _input = ["123.", "...."]
    assert compute_valid_sum(_input) == 0


def test_edge_top_right_still_surroudned_should_ignore():
    _input = [".123", "...."]
    assert compute_valid_sum(_input) == 0


def test__get_part_boundaries_self_thought_example():
    m = Map([".....", ".12...", "......"])
    p = Part(y=1, x_range=(1, 2), value=12)
    result = m._get_part_boundaries(p)
    assert result.upper_range == [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
    ], "failed computing upper_range"
    assert result.same_line == [(0, 1), (3, 1)], "failed computing same line range"
    assert result.lower_range == [
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
    ], "failed computing lower_bound"


def test__compute_horizontal_boundaries_top_right_corner():
    m = Map([".1234", "....."])
    p = Part(y=0, x_range=(1, 4), value=123)
    result = m._get_part_boundaries(p)
    assert result.upper_range == [
        (0, -1),
        (1, -1),
        (2, -1),
        (3, -1),
        (4, -1),
        (5, -1),
    ], "failed computing upper_range"
    assert result.same_line == [(0, 0), (5, 0)], "failed computing same line range"
    assert result.lower_range == [
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
    ], "failed computing lower_bound"


def test__compute_horizontal_boundaries_top_left_corner():
    m = Map(["1234.", "....."])
    p = Part(y=0, x_range=(0, 3), value=123)
    result = m._get_part_boundaries(p)
    assert result.upper_range == [
        (-1, -1),
        (0, -1),
        (1, -1),
        (2, -1),
        (3, -1),
        (4, -1),
    ], "failed computing upper_range"
    assert result.same_line == [(-1, 0), (4, 0)], "failed computing same line range"
    assert result.lower_range == [
        (-1, 1),
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
    ], "failed computing lower_bound"


def test__compute_horizontal_boundaries_bottom_left_corner():
    m = Map([".....", "1234."])
    p = Part(y=1, x_range=(0, 3), value=123)
    result = m._get_part_boundaries(p)
    assert result.upper_range == [
        (-1, 0),
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
    ], "failed computing upper_range"
    assert result.same_line == [(-1, 1), (4, 1)], "failed computing same line range"
    assert result.lower_range == [
        (-1, 2),
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (4, 2),
    ], "failed computing lower_bound"


def test__compute_horizontal_boundaries_bottom_right_corner():
    m = Map([".....", ".1234"])
    p = Part(y=1, x_range=(1, 4), value=123)
    result = m._get_part_boundaries(p)
    assert result.upper_range == [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
    ], "failed computing upper_range"
    assert result.same_line == [(0, 1), (5, 1)], "failed computing same line range"
    assert result.lower_range == [
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 2),
    ], "failed computing lower_bound"


def test_is_dot_or_number_surrounded_bottom_right_corner():
    m = Map([".....", ".1234"])
    p = Part(y=1, x_range=(1, 4), value=123)
    surrounded = m.is_dot_or_number_surrounded(p)
    assert surrounded == True


def test_is_dot_or_number_surrounded_bottom_left_corner():
    m = Map([".....", "1234."])
    p = Part(y=1, x_range=(0, 3), value=123)
    surrounded = m.is_dot_or_number_surrounded(p)
    assert surrounded == True


def test_is_dot_or_number_surrounded_top_left_corner():
    m = Map(["1234.", "....."])
    p = Part(y=0, x_range=(0, 3), value=123)
    surrounded = m.is_dot_or_number_surrounded(p)
    assert surrounded == True


def test_is_dot_or_number_surrounded_top_right_corner():
    m = Map([".1234", "....."])
    p = Part(y=0, x_range=(1, 4), value=123)
    surrounded = m.is_dot_or_number_surrounded(p)
    assert surrounded == True
