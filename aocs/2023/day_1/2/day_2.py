import re
from typing import List

from aocs.commons.input_reader import input_file_readlines

STRING_TO_DIGIT_STRING_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
}


def _pick_right_type(*digits):
    return "".join(
        STRING_TO_DIGIT_STRING_DICT[d] if d in STRING_TO_DIGIT_STRING_DICT else d
        for d in digits
    )


def _two_or_one_digits(
    line: str,
) -> int:
    matches = re.findall(
        rf"\d{{1}}|{'|'.join(list(STRING_TO_DIGIT_STRING_DICT.keys()))}", line
    )
    try:
        return int(_pick_right_type(matches[0], matches[-1]))
    except IndexError:
        if len(matches) > 0:
            return int(_pick_right_type(matches[0], matches[0]))
        return 0


def calibrator(lines: List[str]) -> int:
    return sum(map(_two_or_one_digits, lines))


def main() -> None:
    print(calibrator(input_file_readlines("aocs/2023/day_1/2/input.txt")))


if __name__ == "__main__":
    main()
