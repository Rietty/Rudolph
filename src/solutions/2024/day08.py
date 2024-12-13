import itertools

from loguru import logger as log

from utils.decorators import benchmark

type Coordinates = tuple[int, int]


def generate_antinode_pair(
    a: Coordinates, b: Coordinates, n: int, m: int
) -> Coordinates:
    ax, ay = a
    bx, by = b
    nx = bx + (bx - ax)
    ny = by + (by - ay)

    if 0 <= nx < n and 0 <= ny < m:
        return nx, ny


def generate_antinode_line(
    a: Coordinates, b: Coordinates, n: int, m: int
) -> list[Coordinates]:
    res = []
    ax, ay = a
    bx, by = b

    nx = bx + (bx - ax)
    ny = by + (by - ay)
    res.append((bx, by))

    # Here we are essentially going down the line and offsetting the coordinates by the delta each time.
    # We only have to do this in one direction because the other direction will be covered when the function is called with opposite arguments.
    while 0 <= nx < n and 0 <= ny < m:
        res.append((nx, ny))
        nx += bx - ax
        ny += by - ay

    return res


@benchmark
def part_a[T](data: T) -> int:
    antennas, n, m = data
    antinodes = set()

    for _, coords in antennas.items():
        for a, b in itertools.combinations(coords, 2):
            if antinode := generate_antinode_pair(a, b, n, m):
                antinodes.add(antinode)
            if antinode := generate_antinode_pair(b, a, n, m):
                antinodes.add(antinode)

    return len(antinodes)


@benchmark
def part_b[T](data: T) -> int:
    antennas, n, m = data
    antinodes = set()

    for _, coords in antennas.items():
        for a, b in itertools.combinations(coords, 2):
            if antinode := generate_antinode_line(a, b, n, m):
                antinodes.update(antinode)
            if antinode := generate_antinode_line(b, a, n, m):
                antinodes.update(antinode)

    return len(antinodes)


def parse[T](data: str) -> T:
    data = data.splitlines()
    antennas = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char != ".":
                antennas.setdefault(char, []).append((x, y))
    return antennas, len(data), len(data[0])


test_data_a = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

test_data_b = test_data_a
