from collections import Counter

from loguru import logger as log

from utils.decorators import benchmark


@benchmark
def part_a[T](data: T) -> int:
    left, right = sorted(data[0]), sorted(data[1])
    return sum(abs(a - b) for a, b in zip(left, right))


@benchmark
def part_b[T](data: T) -> int:
    left, right = data
    c = Counter(right)
    return sum(num * c[num] for num in left)


def parse[T](data: str) -> T:
    # For each line, split it into 2 numbers, put first in list 1, second in list 2.
    # Return a list of the two lists.
    left = []
    right = []
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
