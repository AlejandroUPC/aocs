import pytest
from day_1_1 import calibrator, _two_or_one_digits


@pytest.mark.parametrize(
    "_input,expected",
    [
        ("2", 22),
        ("1aaaa1", 11),
        ("aaaaaa", 0),
        ("33a", 33),
        ("a44", 44),
        ("aaaa5", 55),
        ("6aaaaa", 66),
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("two76", 76),
    ],
)
def test__two_or_more_digits(_input, expected):
    assert _two_or_one_digits(_input) == expected


def test_calibrator_aoc_sample():
    _input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert calibrator(_input) == 142
