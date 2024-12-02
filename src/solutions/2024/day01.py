from collections import Counter
from typing import TypeVar

from utils.decorators import benchmark
from utils.solver import Problem, solve_problem

# Define a TypeVar to represent the output type of `parse`
ParsedType = TypeVar("ParsedType")


@benchmark
def part_a(data: ParsedType) -> int:
    left, right = sorted(data[0]), sorted(data[1])
    return sum(abs(a - b) for a, b in zip(left, right))


@benchmark
def part_b(data: ParsedType) -> int:
    left, right = data
    c = Counter(right)
    return sum(num * c[num] for num in left)


def parse(data: str) -> ParsedType:
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


def solve(problem: Problem) -> None:
    solve_problem(
        problem,
        parse,
        part_a,
        part_b,
        test_data_a,
        test_data_b,
    )


test_data_a = """3   4
4   3
2   5
1   3
3   9
3   3
"""

test_data_b = """3   4
4   3
2   5
1   3
3   9
3   3
"""
