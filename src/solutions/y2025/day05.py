import re

from utils.decorators import benchmark


@benchmark
def part_a(data: tuple[list[tuple[int, int]], list[int]]) -> int:
    ranges, ingredients = data
    fresh = 0
    for x in ingredients:
        for a, b in ranges:
            if a <= x <= b:
                fresh += 1
                break
    return fresh


@benchmark
def part_b(data: tuple[list[tuple[int, int]], list[int]]) -> int:
    ranges, _ = data
    ranges = sorted(ranges, key=lambda x: x[0])
    merged: list[tuple[int, int]] = []

    # Basically going to merge overlapping ranges together as much as we can.
    i, j = ranges[0]

    for a, b in ranges[1:]:
        if a <= j + 1:
            j = max(j, b)
        else:
            merged.append((i, j))
            i, j = a, b

    merged.append((i, j))

    # Whatever is left over, we iterate and sum up all the differences between end and start of range.
    return sum(end - start + 1 for start, end in merged)


@benchmark
def parse(data: str) -> tuple[list[tuple[int, int]], list[int]]:
    a, b = re.split(r"\n\s*\n", data.strip())

    def pr(s):
        return tuple(map(int, s.split("-")))

    ranges = [pr(x) for x in a.splitlines() if x.strip()]
    available = [int(x) for x in b.splitlines() if x.strip()]
    return ranges, available


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
