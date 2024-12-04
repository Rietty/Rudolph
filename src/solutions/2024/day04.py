import logging
from typing import List

from utils.decorators import benchmark

log = logging.getLogger(__name__)


# Get the valid possible directions a word can appear in.
def valid_dirs(
    rows: int, cols: int, r: int, c: int, directions: List[List[List[int]]]
) -> List[List[List[int]]]:
    valid = []
    for dir in directions:
        lx, ly = dir[-1]
        if 0 <= lx + r < rows and 0 <= ly + c < cols:
            valid.append(dir)
    return valid


def get_opposite_letter(letter: str):
    return "M" if letter == "S" else "S"


@benchmark
def part_a[T](data: T) -> int:
    n = len(data)
    m = len(data[0])
    count = 0

    directions = [
        [[0, 0], [-1, 0], [-2, 0], [-3, 0]],
        [[0, 0], [-1, 1], [-2, 2], [-3, 3]],
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 1], [2, 2], [3, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[0, 0], [1, -1], [2, -2], [3, -3]],
        [[0, 0], [0, -1], [0, -2], [0, -3]],
        [[0, 0], [-1, -1], [-2, -2], [-3, -3]],
    ]

    for r in range(n):
        for c in range(m):
            # We grab possible ways our word can be on this part of the grid.
            possible_directions = valid_dirs(n, m, r, c, directions)
            for dir in possible_directions:
                coords = []
                for offset in dir:
                    coords.append([r + offset[0], c + offset[1]])

                res = ""
                for cx, cy in coords:
                    res += data[cx][cy]

                if res == "XMAS":
                    count += 1

    return count


@benchmark
def part_b[T](data: T) -> int:
    n = len(data)
    m = len(data[0])
    count = 0

    for r in range(1, n - 1):
        for c in range(1, m - 1):
            if data[r][c] == "A":
                d1 = data[r + 1][c + 1]
                d2 = data[r + 1][c - 1]
                d3 = data[r - 1][c - 1]
                d4 = data[r - 1][c + 1]
                if (
                    d1 in "SM"
                    and d2 in "SM"
                    and d3 == get_opposite_letter(d1)
                    and d4 == get_opposite_letter(d2)
                ):
                    count += 1

    return count


def parse[T](data: str) -> T:
    return [list(line) for line in data.splitlines()]


test_data_a = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

test_data_b = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
