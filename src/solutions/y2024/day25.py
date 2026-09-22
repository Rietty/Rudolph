from enum import Enum
from typing import Any

from library.grid import Grid
from utils.decorators import benchmark


class Schematic(Enum):
    Key = 0
    Lock = 1


def key_or_lock(grid: Grid[str]) -> Schematic | None:
    if all(cell == "#" for cell in grid[0]):
        return Schematic.Lock
    if all(cell == "#" for cell in grid[-1]):
        return Schematic.Key
    return None


def get_columns(grid: Grid[Any]) -> list[str]:
    return ["".join(column) for column in zip(*grid)]


def get_scores(columns: list[str]) -> list[int]:
    return [column.count("#") - 1 for column in columns]


@benchmark
def part_a(data: list[Grid[str]]) -> int:
    keys = [d for d in data if key_or_lock(d) == Schematic.Key]
    locks = [d for d in data if key_or_lock(d) == Schematic.Lock]

    key_scores = [get_scores(get_columns(key)) for key in keys]
    lock_scores = [get_scores(get_columns(lock)) for lock in locks]

    valid_pairs = 0
    for key_score in key_scores:
        for lock_score in lock_scores:
            if any(key + lock > 5 for key, lock in zip(key_score, lock_score)):
                continue
            valid_pairs += 1

    return valid_pairs


@benchmark
def part_b(data: list[Grid[str]]) -> int:
    return 0  # Ta-da! No part B!


@benchmark
def parse(data: str) -> list[Grid[str]]:
    return [
        Grid([list(line) for line in grid.splitlines()]) for grid in data.split("\n\n")
    ]


test_data_a = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

test_data_b = test_data_a
