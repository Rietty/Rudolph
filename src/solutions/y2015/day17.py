from itertools import combinations

from utils.decorators import benchmark

TARGET = 150
TEST_TARGET = 25


@benchmark
def part_a(data: list[int]) -> int:
    return len(
        [
            combo
            for k in range(1, len(data) + 1)
            for combo in combinations(data, k)
            if sum(combo) == TARGET
        ]
    )


@benchmark
def part_b(data: list[int]) -> int:
    combos = [
        combo
        for k in range(1, len(data) + 1)
        for combo in combinations(data, k)
        if sum(combo) == TARGET
    ]
    min_len = len(min(combos, key=len))
    return len([t for t in combos if len(t) == min_len])


@benchmark
def parse(data: str) -> list[int]:
    return [int(d) for d in data.splitlines()]


test_data_a = """20
15
10
5
5
"""

test_data_b = test_data_a
