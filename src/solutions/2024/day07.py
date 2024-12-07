import logging
from typing import List

from utils.decorators import benchmark

log = logging.getLogger(__name__)


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def can_make_target(target: int, nums: List[int], part2: bool = False) -> bool:
    def dfs(index: int, current: int) -> bool:
        if index == len(nums):
            return current == target
        if dfs(index + 1, current + nums[index]):
            return True
        if dfs(index + 1, current * nums[index]):
            return True
        if part2 and dfs(index + 1, concat(current, nums[index])):
            return True
        return False

    if not nums:
        return False
    return dfs(1, nums[0])


@benchmark
def part_a[T](data: T) -> int:
    return sum([nums[0] for nums in data if can_make_target(nums[0], nums[1:])])


@benchmark
def part_b[T](data: T) -> int:
    return sum([nums[0] for nums in data if can_make_target(nums[0], nums[1:], True)])


def parse[T](data: str) -> T:
    return [list(map(int, line.replace(":", "").split())) for line in data.splitlines()]


test_data_a = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

test_data_b = test_data_a
