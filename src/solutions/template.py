from typing import TypeVar

from utils.decorators import benchmark
from utils.solver import Problem, solve_problem

# Define a TypeVar to represent the output type of `parse`
ParsedType = TypeVar("ParsedType")


@benchmark
def part_a(data: ParsedType) -> int:
    return 0


@benchmark
def part_b(data: ParsedType) -> int:
    return 0


def parse(data: str) -> ParsedType:
    return data.splitlines()  # Replace with actual parsing logic.


def solve(problem: Problem) -> None:
    solve_problem(
        problem,
        parse,
        part_a,
        part_b,
        test_data_a,
        test_data_b,
    )


test_data_a = """
"""

test_data_b = """
"""
