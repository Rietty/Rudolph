from loguru import logger as log

from utils.decorators import benchmark

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find_start[T](data: T) -> tuple[int, int]:
    for x, row in enumerate(data):
        if "^" in row:
            return x, row.index("^")
    return -1, -1


def traverse_route[
    T
](data: T, ex: int = -1, ey: int = -1, detect_loops: bool = False) -> tuple[set, bool]:
    path = set()
    n, m = len(data), len(data[0])
    x, y = find_start(data)
    if x == -1 or y == -1:
        return path, False

    dir = 0
    loop_detected = False

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

        if detect_loops and ((nx, ny), dir) in path:
            loop_detected = True
            break

        x, y = nx, ny

    return path, loop_detected


@benchmark
def part_a[T](data: T) -> int:
    visited, _ = traverse_route(data)
    return len({pos for pos, _ in visited})


@benchmark
def part_b[T](data: T) -> int:
    visited, _ = traverse_route(data)
    positions = {pos for pos, _ in visited}
    ans = 0

    for x, y in positions:
        if data[x][y] == ".":
            data[x][y] = "#"
            _, loop = traverse_route(data, x, y, detect_loops=True)
            if loop:
                ans += 1
            data[x][y] = "."

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

test_data_b = test_data_a
