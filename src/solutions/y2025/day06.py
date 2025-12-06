import operator as op
from functools import reduce

from utils.decorators import benchmark

type Worksheet = tuple[list[list[str]]]


def do_homework(worksheet: Worksheet) -> int:
    operators = {"+": op.add, "*": op.mul}
    return sum(reduce(operators[sym], map(int, nums)) for *nums, sym in worksheet)


@benchmark
def part_a(data: tuple[Worksheet, Worksheet]) -> int:
    fake, _ = data
    return do_homework(fake)


@benchmark
def part_b(data: tuple[Worksheet, Worksheet]) -> int:
    _, real = data
    return do_homework(real)


@benchmark
def parse(data: str) -> tuple[Worksheet, Worksheet]:
    rows = data.splitlines()
    width = max(len(r) for r in rows)
    rows = [r.ljust(width) for r in rows]

    blocks = []

    c = 0
    while c < width:
        if all(r[c] == " " for r in rows):
            c += 1
            continue
        s = c
        while c < width and any(r[c] != " " for r in rows):
            c += 1
        blocks.append([r[s:c] for r in rows])

    fake = [[x.strip() for x in b] for b in blocks]

    real = []
    for b in blocks:
        op = b[-1].strip()
        cols = zip(*b[:-1])
        nums = ["".join(col).strip() for col in reversed(list(cols))]
        real.append([x for x in nums if x] + [op])

    return fake, real


test_data_a = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""

test_data_b = test_data_a
