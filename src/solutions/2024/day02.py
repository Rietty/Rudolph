from typing import TypeVar

from aocd import get_data, submit

from utils.decorators import time_function

# Define a TypeVar to represent the output type of `parse`
ParsedType = TypeVar("ParsedType")


@time_function
def part_a(data: ParsedType) -> int:
    return 0


@time_function
def part_b(data: ParsedType) -> int:
    return 0


def parse(data: str) -> ParsedType:
    return data  # Replace with actual parsing logic.


def solve(year: int, day: int, part: str, test: bool, submit_result: bool) -> None:

    # If we're testing, we need to load the test data instead of the real data.
    # Those are defined as triple quotes strings at the bottom of the file.
    if test:
        data = part1_testdata if part == "a" else part2_testdata
    else:
        # Get the correct day's input data, waiting for it to be released if necessary.
        data = get_data(year=year, day=day, block=True)

    data = parse(data)

    # Run the appropriate part of the solution.
    if part == "a":
        result = part_a(data)
    elif part == "b":
        result = part_b(data)
    else:
        print(f"Invalid part: {part}")
        return

    # Print the result.
    print(f"Solution: {result}")

    # Submit if desired.
    if submit_result:
        submit(result, part=part, year=year, day=day)


part1_testdata = """
"""

part2_testdata = """
"""
