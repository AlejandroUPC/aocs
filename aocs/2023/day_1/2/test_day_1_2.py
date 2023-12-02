import pytest
from day_1_2 import (
    calibrator,
    _two_or_one_digits,
    _pick_right_type,
    STRING_TO_DIGIT_STRING_DICT,
)


@pytest.mark.parametrize(
    "_input,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("4jddtplseven", 47),
        ("4mrbkjvdz", 44),
        ("a", 0),
        ("rlvrxninethree4", 94),
        ("15", 15),
        ("nine6qpfzxhsdsfour9", 99),
        ("one", 11),
        ("2", 22),
        ("three", 33),
        ("four", 44),
        ("five", 55),
        ("six", 66),
        ("seven", 77),
        ("eight", 88),
        ("nine", 99),
        ("tbsxkhhv6twozrtczg6seven", 67),
        ("ccpeightbcvknglvcv81gcjnlnfnine9", 89),
        ("4twoscpht", 42),
        ("qdgdrtx9onefourdcvctldjnpcdjbc", 94),
        ("cjxkxsgmql4xxgjtpdcbmsixeight", 48),
        ("739", 79),
        ("twoone1threezdpmqthxf17oneightcj", 28),
    ],
)
def test__two_or_more_digits(_input, expected):
    assert _two_or_one_digits(_input) == expected


@pytest.mark.parametrize(
    "_input,expected",
    [
        (("two", "1"), "21"),
        (("three", "two"), "32"),
        (("nine", "1"), "91"),
        (("1", "1"), "11"),
    ],
)
def test__pick_right_type(_input, expected):
    assert _pick_right_type(*_input) == expected


def test_calibrator_aoc_sample():
    _input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert calibrator(_input) == 281
