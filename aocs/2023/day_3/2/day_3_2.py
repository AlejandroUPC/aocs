from typing import List, Tuple, Optional
from aocs.commons.input_reader import input_file_readlines
import re
from dataclasses import dataclass
from collections import defaultdict
from functools import reduce

@dataclass
class Part:
    y: int
    x_range: Tuple[int, int]
    value: int


@dataclass
class PartSurroundings:
    upper_range: List[Tuple[Optional[int], Optional[int]]]
    same_line: Tuple[Optional[int], Optional[int]]
    lower_range: List[Tuple[Optional[int], Optional[int]]]

    def _sanitize_surroundings(self, map_shape: Tuple[int, int]):
        """all ranges are set into one list and the values are cleaned if y is negative, or bigger than the edges on the map"""
        map_x, map_y = map_shape
        all_surroundings = [*self.upper_range, *self.lower_range, *self.same_line]
        filtered_surroundings = filter(
            lambda x: ((x[1] >= 0 and x[1] <= map_y))
            and ((x[0] >= 0 and x[0] < map_x)),
            all_surroundings,
        )
        return list(filtered_surroundings)


@dataclass
class Map:
    _map: List[List[str]]

    def _get_part_boundaries(self, part: Part) -> Tuple:
        """At the end we need +-1 of part.pos_y checking maxmin"""
        x_range_surround = (
            part.x_range[0] - 1,
            part.x_range[1] + 1,
        )  # range upper bound -.-
        upper_range = [
            (x_pos, part.y - 1)
            for x_pos in range(x_range_surround[0], x_range_surround[1] + 1)
        ]
        lower_range = [
            (x_pos, part.y + 1)
            for x_pos in range(x_range_surround[0], x_range_surround[1] + 1)
        ]
        same_line = [(x, part.y) for x in x_range_surround]
        return PartSurroundings(upper_range, same_line, lower_range)

    def is_asterisk_surrounded(self, part: Part) -> bool:
        boundaries = self._get_part_boundaries(part)
        boundaries = boundaries._sanitize_surroundings(
            (len(self._map[0]), len(self._map) - 1)
        )
        return [(part.value,x,y) for x, y in boundaries  if self._map[y][x] == "*" ]


def compute_valid_sum(
    engine_parts: List[str],
) -> Optional[List[Tuple[int, Tuple[int, int]]]]:
    asterisk_map = defaultdict(list)
    m = Map(engine_parts)
    for line, part in enumerate(engine_parts):
        parts = [
            Part(
                y=line,
                x_range=(
                    match.start(),
                    match.end() - 1,
                ),  # +1 because 0 index on list vs regex returning 1
                value=int(match.group()),
            )
            for match in re.finditer("(\d+)", part)
        ]
        for p in parts:
            for val,x,y  in m.is_asterisk_surrounded(p):
                asterisk_map[(x,y)].append(val)
        
    return sum([reduce(lambda x, y: x*y, v) for v in  asterisk_map.values() if len(v) > 1])


def main() -> None:
    print(compute_valid_sum(input_file_readlines("aocs/2023/day_3/2/input.txt")))


if __name__ == "__main__":
    main()
