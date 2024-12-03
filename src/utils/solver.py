import logging
from typing import Callable

from aocd import get_data, submit

log = logging.getLogger(__name__)


def solve_problem[
    T
](
    year: int,
    day: int,
    part: str,
    publish: bool,
    parse: Callable[[str], T],
    part_a: Callable[[T], int],
    part_b: Callable[[T], int],
) -> None:
    # Get the data for the problem and parse it.
    data = parse(get_data(year=year, day=day, block=True))

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
    if publish:
        submit(result, part=part, year=year, day=day)


def test_problem[
    T
](
    part: str,
    parse: Callable[[str], T],
    part_a: Callable[[T], int],
    part_b: Callable[[T], int],
    test_data_a: str,
    test_data_b: str,
) -> None:
    if part == "a":
        data = parse(test_data_a)
        result = part_a(data)
    elif part == "b":
        data = parse(test_data_b)
        result = part_b(data)
    else:
        print(f"Invalid part: {part}")
        return

    # Print the result.
    print(f"Test Solution: {result}")
