from collections import Counter
from typing import TypeVar

from aocd import get_data, submit

from utils.decorators import benchmark

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


part1_testdata = """3   4
4   3
2   5
1   3
3   9
3   3
"""

part2_testdata = """3   4
4   3
2   5
1   3
3   9
3   3
"""
