from collections import defaultdict

from loguru import logger as log

from utils.decorators import benchmark

type Coordinates = tuple[int, int]
type Region = list[Coordinates]
type Regions = list[Region]


def get_perimeter(region: Region) -> int:
    perimeter = 0
    for x, y in region:
        perimeter += 4 - sum((x + dx, y + dy) in region for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)))
    return perimeter


def get_area(region: Region) -> int:
    return len(region)


def get_corners(region: Region) -> int:
    corners = 0
    directions = [(-1, 0, 0, 1), (-1, 0, 0, -1), (1, 0, 0, 1), (1, 0, 0, -1)]
    diagonal_checks = [
        (-1, -1, -1, 0, 0, -1),
        (-1, 1, -1, 0, 0, 1),
        (1, -1, 1, 0, 0, -1),
        (1, 1, 1, 0, 0, 1),
    ]

    for x, y in region:
        for dx, dy, nx, ny in directions:
            if (x + dx, y + dy) not in region and (
                x + nx,
                y + ny,
            ) not in region:
                corners += 1

        for dx, dy, nx1, ny1, nx2, ny2 in diagonal_checks:
            if (x + dx, y + dy) not in region and (x + nx1, y + ny1) in region and (x + nx2, y + ny2) in region:
                corners += 1
    return corners


def get_regions(data: list[list[str]]) -> dict[str, Regions]:
    n = len(data)
    m = len(data[0])
    visited = [[False] * m for _ in range(n)]

    def flood_fill(r: int, c: int, char: str) -> Region:
        stack = [(r, c)]
        region = []
        while stack:
            x, y = stack.pop()
            if 0 <= x < n and 0 <= y < m and not visited[x][y] and data[x][y] == char:
                visited[x][y] = True
                region.append((x, y))
                stack.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
        return region

    regions = defaultdict(list)

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                char = data[i][j]
                region = flood_fill(i, j, char)
                if region:
                    regions[char].append(region)

    return regions


@benchmark
def part_a(data: list[list[str]]) -> int:
    regions = get_regions(data)
    return sum(get_perimeter(r) * get_area(r) for rlist in regions.values() for r in rlist)


@benchmark
def part_b(data: list[list[str]]) -> int:
    regions = get_regions(data)
    return sum(get_corners(r) * get_area(r) for rlist in regions.values() for r in rlist)


@benchmark
def parse(data: str) -> list[list[str]]:
    return [list(row) for row in data.splitlines()]


test_data_a = """AAAA
BBCD
BBCC
EEEC
"""

test_data_b = test_data_a
