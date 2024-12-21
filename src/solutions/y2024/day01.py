from collections import Counter

from loguru import logger as log

from utils.decorators import benchmark


@benchmark
def part_a(data: list[list[int]]) -> int:
    left, right = sorted(data[0]), sorted(data[1])
    return sum(abs(a - b) for a, b in zip(left, right))


@benchmark
def part_b(data: list[list[int]]) -> int:
    left, right = data
    c: Counter = Counter(right)
    return sum(num * c[num] for num in left)


@benchmark
def parse(data: str) -> list[list[int]]:
    # For each line, split it into 2 numbers, put first in list 1, second in list 2.
    # Return a list of the two lists.
    left: list[int] = []
    right: list[int] = []
    for line in data.split("\n"):
        if not line:
            continue
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)
    return [left, right]


test_data_a = """3   4
4   3
2   5
1   3
3   9
3   3
"""

test_data_b = test_data_a
