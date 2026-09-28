from library.geometry import Point, manhattan_distance
from utils.decorators import benchmark

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W


def travel(movement: str, x: int, y: int, direction: int) -> list[tuple[int, int, int]]:
    dir: int = (direction + (1 if movement[0] == "R" else -1)) % 4

    dx, dy = DIRS[dir]
    dist = int(movement[1:])

    moves: list[tuple[int, int, int]] = []

    for i in range(1, dist + 1):
        moves.append((i * dx + x, i * dy + y, dir))

    return moves


@benchmark
def part_a(data: list[str]) -> float:
    x: int = 0
    y: int = 0
    dir: int = 0
    for d in data:
        x, y, dir = travel(d, x, y, dir)[-1]
    return manhattan_distance(Point(coords=(0, 0)), Point(coords=(x, y)))


@benchmark
def part_b(data: list[str]) -> float:
    x: int = 0
    y: int = 0
    dir: int = 0
    visited: set[tuple[int, int]] = {(0, 0)}

    for d in data:
        moves = travel(d, x, y, dir)
        for mx, my, _ in moves:
            if (mx, my) in visited:
                return manhattan_distance(Point(coords=(0, 0)), Point(coords=(mx, my)))
            visited.add((mx, my))
        x, y, dir = moves[-1]

    return manhattan_distance(Point(coords=(0, 0)), Point(coords=(x, y)))


@benchmark
def parse(data: str) -> list[str]:
    return [d.strip(",") for d in data.split()]


test_data_a = """R8, R4, R4, R8
"""

test_data_b = test_data_a
