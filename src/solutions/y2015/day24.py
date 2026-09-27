from math import prod
from typing import Sequence

from utils.decorators import benchmark


def get_group_one(nums: Sequence[int], groups: int) -> list[list[int]]:
    target = sum(nums) // groups

    n = len(nums)

    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + nums[i]

    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            results.append(path.copy())
            return
        if start >= n or suffix_sum[start] < remaining:
            return

        prev = None
        for i in range(start, n):
            v = nums[i]
            if v == prev:
                continue
            if v > remaining:
                break
            path.append(v)
            backtrack(i + 1, remaining - v)
            path.pop()
            prev = v

    backtrack(0, target)
    return results


@benchmark
def part_a(data: list[int]) -> int:
    partitions = get_group_one(data, 3)
    smallest = min(partitions, key=len)
    return prod(smallest)


@benchmark
def part_b(data: list[int]) -> int:
    partitions = get_group_one(data, 4)
    smallest = min(partitions, key=len)
    return prod(smallest)


@benchmark
def parse(data: str) -> list[int]:
    return [int(d) for d in data.splitlines()]


test_data_a = """1
2
3
4
5
7
8
9
10
11
"""

test_data_b = test_data_a
