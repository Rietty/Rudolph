from heapq import nsmallest
from itertools import combinations

from library.geometry import Point3D, euclidean_distance3D
from library.tree import DSU
from utils.decorators import benchmark


@benchmark
def part_a(data: list[Point3D]) -> int:
    max_unions = 1000 if len(data) > 20 else 10

    ds = [(euclidean_distance3D(a, b), a, b) for a, b in combinations(data, 2)]
    smallest_ds = nsmallest(max_unions, ds, key=lambda x: x[0])

    dsu = DSU(data)
    for _, a, b in smallest_ds:
        dsu.union(a, b)

    roots = [dsu.find(p) for p in data]
    root_set = set(roots)
    sizes = sorted((dsu.s[r] for r in root_set), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


@benchmark
def part_b(data: list[Point3D]) -> int:
    max_size = 1000 if len(data) > 20 else 10

    ds = [(euclidean_distance3D(a, b), a, b) for a, b in combinations(data, 2)]
    ds.sort(key=lambda x: x[0])

    u = DSU(data)

    for dt, a, b in ds:
        u.union(a, b)
        if u.s[u.find(data[0])] >= max_size:
            return a.x * b.x


@benchmark
def parse(data: str) -> list[Point3D]:
    return [Point3D(*map(int, line.split(","))) for line in data.splitlines() if line]


test_data_a = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

test_data_b = test_data_a
