from typing import TypeVar

from utils.decorators import benchmark
from utils.solver import Problem, solve_problem

# Define a TypeVar to represent the output type of `parse`
ParsedType = TypeVar("ParsedType")


@benchmark
def part_a(data: ParsedType) -> int:
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1
    return count


@benchmark
def part_b(data: ParsedType) -> int:
    count = 0
    for i in range(3, len(data)):
        if sum(data[i - 2 : i + 1]) > sum(data[i - 3 : i]):
            count += 1
    return count


def parse(data: str) -> ParsedType:
    return list(map(int, data.strip().splitlines()))


def solve(problem: Problem) -> None:
    solve_problem(
        problem,
        parse,
        part_a,
        part_b,
        test_data_a,
        test_data_b,
    )


test_data_a = """199
200
208
210
200
207
240
269
260
263
"""

test_data_b = """199
200
208
210
200
207
240
269
260
263
"""
