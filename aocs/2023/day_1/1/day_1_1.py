import re
from typing import List

from aocs.commons.input_reader import input_file_readlines


def _two_or_one_digits(
    line: str,
) -> int:
    matches = re.findall("\d{1}", line)
    try:
        return int(matches[0] + matches[-1])
    except IndexError:
        if len(matches) > 0:
            return int(matches[0] * 2)
        return 0


def calibrator(lines: List[str]) -> int:
    return sum(map(_two_or_one_digits, lines))


def main() -> None:
    print(calibrator(input_file_readlines("aocs/2023/day_1/1/input.txt")))


if __name__ == "__main__":
    main()
