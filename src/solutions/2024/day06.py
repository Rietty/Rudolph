from loguru import logger as log

from library.constants import Cardinals
from library.grid import Grid
from utils.decorators import benchmark


def traverse_route[
    T
](data: T, er: int = -1, ec: int = -1, detect_loops: bool = False) -> tuple[set, bool]:
    path = set()
    n, m = data.width, data.height
    r, c = data.find_value("^")

    if r == -1 or c == -1:
        return path, False

    dir = 0
    loop_detected = False

    while 0 <= r < n and 0 <= c < m:
        old_dir = dir
        dr, dc = Cardinals[dir]
        nr, nc = r + dr, c + dc

        while (
            0 <= nr < n
            and 0 <= nc < m
            and (data[nr][nc] == "#" or (nr == er and nc == ec))
        ):
            dir = (dir + 1) % 4
            dr, dc = Cardinals[dir]
            nr, nc = r + dr, c + dc

        path.add(((r, c), old_dir))

        if detect_loops and ((nr, nc), dir) in path:
            loop_detected = True
            break

        r, c = nr, nc

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

    for r, c in positions:
        if data[r][c] == ".":
            data[r][c] = "#"
            _, loop = traverse_route(data, r, c, detect_loops=True)
            if loop:
                ans += 1
            data[r][c] = "."

    return ans


@benchmark
def parse[T](data: str) -> T:
    return Grid([list(line) for line in data.splitlines()])


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
