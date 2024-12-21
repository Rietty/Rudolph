from loguru import logger as log

from library.grid import Grid
from utils.decorators import benchmark


@benchmark
def part_a[T](data: Grid) -> int:
    count = 0

    for r in range(data.width):
        for c in range(data.height):
            neighbors = data.get_neighbour_ray_values(r, c, 3, True)
            for n in neighbors:
                n.insert(0, data[r][c])
                if "".join(n) == "XMAS":
                    count += 1

    return count


@benchmark
def part_b[T](data: Grid) -> int:
    count = 0
    opposites = {"S": "M", "M": "S"}

    for r in range(1, data.width - 1):
        for c in range(1, data.height - 1):
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
    return Grid([list(line) for line in data.splitlines()])


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
