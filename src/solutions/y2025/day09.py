from math import fabs
from multiprocessing import Pool

from shapely.geometry import Polygon, box

from library.geometry import Point
from utils.decorators import benchmark


# Returns the size of the area if it is within the polygon.
def area_within_bounding_box(
    pair: tuple[int, int], data: list[Point], poly: Polygon
) -> int:
    i, j = pair
    a, b = data[i], data[j]

    x_min, x_max = min(a.x, b.x), max(a.x, b.x)
    y_min, y_max = min(a.y, b.y), max(a.y, b.y)

    region = box(x_min, y_min, x_max, y_max)

    if region.within(poly):
        return (fabs(b.x - a.x) + 1) * (fabs(b.y - a.y) + 1)

    return 0


@benchmark
def part_a(data: list[Point]) -> int:
    best = 0
    for i in range(len(data)):
        x1, y1 = data[i].x, data[i].y
        for j in range(i + 1, len(data)):
            x2, y2 = data[j].x, data[j].y
            a = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if a > best:
                best = a
    return best


@benchmark
def part_b(data: list[Point]) -> int:
    # Polygons will consist of all points in the list, it's basiclly a convex shape.
    poly = Polygon([(c.x, c.y) for c in data])

    pairs = [
        (i, j) for i in range(len(data) - 1) for j in range(len(data) - 1) if i != j
    ]

    with Pool() as pool:
        areas = pool.starmap(
            area_within_bounding_box, [(pair, data, poly) for pair in pairs]
        )

    return int(max(areas))


@benchmark
def parse(data: str) -> list[Point]:
    return [
        Point(tuple(map(int, line.split(",")))) for line in data.splitlines() if line
    ]


test_data_a = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

test_data_b = test_data_a
