import re

from intervaltree import IntervalTree

from utils.decorators import benchmark

type Ranges = IntervalTree
type Ingredients = list[int]


@benchmark
def part_a(data: tuple[Ranges, Ingredients]) -> int:
    ranges, ingredients = data
    return sum(1 for i in ingredients if ranges[i])


@benchmark
def part_b(data: tuple[Ranges, Ingredients]) -> int:
    ranges, _ = data
    ranges.merge_overlaps(strict=False)
    return sum(iv.end - iv.begin for iv in ranges)


@benchmark
def parse(data: str) -> tuple[IntervalTree, Ingredients]:
    r, i = re.split(r"\n\s*\n", data.strip())

    ranges = IntervalTree()
    for line in r.splitlines():
        if not line.strip():
            continue
        begin, end = map(int, line.split("-"))
        ranges[begin : end + 1] = (begin, end + 1)

    ingredients = [int(v) for v in i.splitlines() if v.strip()]

    return ranges, ingredients


test_data_a = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

test_data_b = test_data_a
