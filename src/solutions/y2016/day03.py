from itertools import batched, chain

from utils.decorators import benchmark


@benchmark
def part_a(data: list[list[int]]) -> int:
    return sum(x + y > z and x + z > y and y + z > x for x, y, z in data)


@benchmark
def part_b(data: list[list[int]]) -> int:
    flat = chain.from_iterable(zip(*data))
    data = [list(b) for b in batched(flat, 3)]
    return sum(x + y > z and x + z > y and y + z > x for x, y, z in data)


@benchmark
def parse(data: str) -> list[list[int]]:
    return [[int(n) for n in line.split()] for line in data.splitlines()]


test_data_a = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
"""

test_data_b = test_data_a
