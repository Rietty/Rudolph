from loguru import logger as log

from utils.decorators import benchmark


# Get the valid possible directions a word can appear in.
def valid_dirs(
    rows: int, cols: int, r: int, c: int, directions: list[list[list[int]]]
) -> list[list[list[int]]]:
    return [
        dir
        for dir in directions
        if 0 <= dir[-1][0] + r < rows and 0 <= dir[-1][1] + c < cols
    ]


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
            possible_directions = valid_dirs(n, m, r, c, directions)
            for dir in possible_directions:
                res = [data[r + offset[0]][c + offset[1]] for offset in dir]
                if "".join(res) == "XMAS":
                    count += 1

    return count


@benchmark
def part_b[T](data: T) -> int:
    n = len(data)
    m = len(data[0])
    count = 0
    opposites = {"S": "M", "M": "S"}

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
                    and d3 == opposites[d1]
                    and d4 == opposites[d2]
                ):
                    count += 1

    return count


@benchmark
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

test_data_b = test_data_a
