import importlib
import logging

import click

from utils.solver import solve_problem, test_problem

log = logging.getLogger(__name__)


@click.command()
@click.option(
    "--problem",
    "-p",
    type=str,
    required=True,
    help="The problem to solve in the format 'year/day/part', e.g., '2024/1/a'.",
)
@click.option(
    "--test",
    "-t",
    is_flag=True,
    help="Solve the test input instead of the puzzle input.",
)
@click.option(
    "--submit", "-s", is_flag=True, help="Submit the solution after solving it."
)
def main(problem, test, submit):
    """Solve a specific Advent of Code problem."""
    try:
        # Parse the problem argument
        year, day, part = problem.split("/")
        year = int(year)
        day = int(day)
        part = part.lower()  # Normalize part to lowercase (e.g., 'a', 'b')

        if part not in ["a", "b"]:
            raise ValueError("Part must be 'a' or 'b'.")

        day_formatted = f"day{day:02d}"  # Format day as day01, day02, etc.
        module_name = f"solutions.{year}.{day_formatted}"

        # Check if the module exists
        module = importlib.import_module(module_name)

        if test:
            print(
                f"Testing {year}/{day_formatted.capitalize()} - Part {part.upper()}..."
            )
            test_problem(
                part=part,
                parse=module.parse,
                part_a=module.part_a,
                part_b=module.part_b,
                test_data_a=module.test_data_a,
                test_data_b=module.test_data_b,
            )
        else:
            print(
                f"Solving {year}/{day_formatted.capitalize()} - Part {part.upper()}..."
            )
            solve_problem(
                year=year,
                day=day,
                part=part,
                publish=submit,
                parse=module.parse,
                part_a=module.part_a,
                part_b=module.part_b,
            )

    except ValueError as e:
        print(f"Invalid format: {e}. Use 'year/day/part', e.g., '2024/1/a'.")
    except ModuleNotFoundError:
        print(f"Module for problem '{problem}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
