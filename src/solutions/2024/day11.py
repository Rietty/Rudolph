import math
from collections import defaultdict
from functools import reduce

from loguru import logger as log

from utils.decorators import benchmark


def count_digits(n: int) -> int:
    return math.floor(math.log(n, 10) + 1)


def split_number(n: int, d: int) -> int:
    div = 10 ** (d // 2)
    right = n % div
    left = n // div
    return left, right


def apply_rules[T](data: T) -> T:
    new_stones = defaultdict(lambda: 0)

    for s, f in data.items():
        if s == 0:
            new_stones[1] += f
        elif (d := count_digits(s)) % 2 == 0:
            l, r = split_number(s, d)
            new_stones[l] += f
            new_stones[r] += f
        else:
            new_stones[s * 2024] += f

    return new_stones


@benchmark
def part_a[T](data: T) -> int:
    data = reduce(lambda data, _: apply_rules(data), range(25), data)
    return sum(data.values())


@benchmark
def part_b[T](data: T) -> int:
    data = reduce(lambda data, _: apply_rules(data), range(75), data)
    return sum(data.values())


@benchmark
def parse[T](data: str) -> T:
    return {int(item): 1 for item in data.split()}


test_data_a = """125 17"""

test_data_b = test_data_a
