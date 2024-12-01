# Function to solve the problem
from dataclasses import dataclass
from typing import Callable, TypeVar

from aocd import get_data, submit

ParsedType = TypeVar("ParsedType")


@dataclass
class Problem:
    year: int
    day: int
    part: str
    test: bool
    publish: bool


def solve_problem(
    problem: Problem,
    parse: Callable[[str], ParsedType],
    part_a: Callable[[ParsedType], int],
    part_b: Callable[[ParsedType], int],
    test_data_a: str,
    test_data_b: str,
) -> None:
    # If we're testing, we need to load the test data instead of the real data.
    if problem.test:
        data = test_data_a if problem.part == "a" else test_data_b
    else:
        # Get the correct day's input data.
        data = get_data(year=problem.year, day=problem.day, block=True)

    data = parse(data)

    # Run the appropriate part of the solution.
    if problem.part == "a":
        result = part_a(data)
    elif problem.part == "b":
        result = part_b(data)
    else:
        print(f"Invalid part: {problem.part}")
        return

    # Print the result.
    print(f"Solution: {result}")

    # Submit if desired.
    if problem.publish:
        submit(result, part=problem.part, year=problem.year, day=problem.day)
