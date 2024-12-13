from typing import Callable

from aocd import get_data, submit
from aocd.models import Puzzle
from loguru import logger as log


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
        log.info(f"Invalid part: {part}")
        return

    # Print the result.
    log.info(f"Solution: {result}")

    if publish:
        submit(result, part=part, year=year, day=day, quiet=True)
        puzzle = Puzzle(year=year, day=day)

        entry = next(
            (
                entry
                for entry in puzzle.submit_results
                if entry["part"] == part and entry["value"] == str(result)
            ),
            None,
        )

        if entry:
            log.info(" ".join(entry["message"].split()))


def test_problem[
    T
](
    part: str,
    parse: Callable[[str], T],
    part_a: Callable[[T], int],
    part_b: Callable[[T], int],
    test_data_a: str,
    test_data_b: str,
    file: str = None,
) -> None:
    # If filepath is provided, read full data from file.
    if file:
        with open(file, "r") as f:
            log.info(f"Reading from {file}...")
            data = f.read()
            test_data_a = data
            test_data_b = data

    if part == "a":
        data = parse(test_data_a)
        result = part_a(data)
    elif part == "b":
        data = parse(test_data_b)
        result = part_b(data)
    else:
        log.info(f"Invalid part: {part}")
        return

    # Print the result.
    log.info(f"Test Solution: {result}")
