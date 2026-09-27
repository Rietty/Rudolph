from copy import deepcopy

from library.grid import Grid
from utils.decorators import benchmark


@benchmark
def part_a(data: Grid[str]) -> int:
    old = data
    for _ in range(100):
        new = deepcopy(old)
        for x in range(old.width):
            for y in range(old.height):
                lit_neighbours = sum(
                    v == "#" for v in old.get_neighbour_values(x, y, diagonals=True)
                )
                if old[x][y] == "#" and (lit_neighbours == 2 or lit_neighbours == 3):
                    new[x][y] = "#"
                elif old[x][y] == "#":
                    new[x][y] = "."
                elif old[x][y] == "." and lit_neighbours == 3:
                    new[x][y] = "#"
                else:
                    new[x][y] = "."
        old = new
    return sum(old[x][y] == "#" for x in range(data.width) for y in range(data.height))


@benchmark
def part_b(data: Grid[str]) -> int:
    old = data
    for _ in range(100):
        new = deepcopy(old)
        for x in range(old.width):
            for y in range(old.height):
                lit_neighbours = sum(
                    v == "#" for v in old.get_neighbour_values(x, y, diagonals=True)
                )
                if old[x][y] == "#" and (lit_neighbours == 2 or lit_neighbours == 3):
                    new[x][y] = "#"
                elif old[x][y] == "#":
                    new[x][y] = "."
                elif old[x][y] == "." and lit_neighbours == 3:
                    new[x][y] = "#"
                else:
                    new[x][y] = "."

                # Force corners lit
                if x == 0 and y == 0:
                    new[x][y] = "#"
                if x == old.width - 1 and y == 0:
                    new[x][y] = "#"
                if x == 0 and y == old.height - 1:
                    new[x][y] = "#"
                if x == old.width - 1 and y == old.height - 1:
                    new[x][y] = "#"
        old = new
    return sum(old[x][y] == "#" for x in range(data.width) for y in range(data.height))


@benchmark
def parse(data: str) -> Grid[str]:
    return Grid([list(c) for c in data.splitlines()])


test_data_a = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

test_data_b = test_data_a
