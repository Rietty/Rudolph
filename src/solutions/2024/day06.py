import logging
from typing import Tuple

from utils.decorators import benchmark

log = logging.getLogger(__name__)

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def calculate_route[T](data: T, ex: int, ey: int) -> Tuple[set, bool]:
    path = set()
    n = len(data)
    m = len(data[0])

    for x, row in enumerate(data):
        if "^" in row:
            y = row.index("^")
            break

    dir = 0

    while 0 <= x < n and 0 <= y < m:
        old_dir = dir

        dx, dy = DIRECTIONS[dir]
        nx, ny = x + dx, y + dy

        while (
            0 <= nx < n
            and 0 <= ny < m
            and (data[nx][ny] == "#" or (nx == ex and ny == ey))
        ):
            dir = (dir + 1) % 4
            dx, dy = DIRECTIONS[dir]
            nx, ny = x + dx, y + dy

        path.add(((x, y), old_dir))

        x, y = nx, ny

        if ((nx, ny), dir) in path:
            return path, True

    return path, False


@benchmark
def part_a[T](data: T) -> int:
    n = len(data)
    m = len(data[0])
    visited = set()

    for x, row in enumerate(data):
        if "^" in row:
            y = row.index("^")
            break

    dir = 0
    visited.add((x, y))

    while True:
        dx, dy = DIRECTIONS[dir]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        elif data[nx][ny] == "#":
            dir = (dir + 1) % 4
        else:
            x, y = nx, ny

        visited.add((x, y))

    return len(visited)


@benchmark
def part_b[T](data: T) -> int:
    n = len(data)
    m = len(data[0])
    ans = 0

    # For each `.` in the grid, replace it with `#` and calculate route. If the second value is True, then increment the answer.
    for x in range(n):
        for y in range(m):
            if data[x][y] == ".":
                _, is_loop = calculate_route(data, x, y)
                if is_loop:
                    ans += 1

    return ans


def parse[T](data: str) -> T:
    return [list(line) for line in data.splitlines()]


test_data_a = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

test_data_b = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
