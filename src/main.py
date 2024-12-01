import argparse
import importlib

if __name__ == "__main__":
    # Create an argument parser.
    parser = argparse.ArgumentParser(
        description="Solve a specific Advent of Code problem."
    )
    parser.add_argument(
        "--problem",
        type=str,
        required=True,
        help="The problem to solve in the format 'year/day/part', e.g., '2024/1/a'.",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Solve the test input instead of the puzzle input.",
    )
    parser.add_argument(
        "--submit", action="store_true", help="Run the code but do not submit it."
    )
    args = parser.parse_args()

    # Parse the --problem argument
    try:
        year, day, part = args.problem.split("/")
        year = int(year)
        day = int(day)
        part = part.lower()  # Normalize part to lowercase (e.g., 'a', 'b')
        if part not in ["a", "b"]:
            raise ValueError("Part must be 'a' or 'b'.")

        day_formatted = f"day{day:02d}"  # Format day as day01, day02, etc.
        module_name = f"solutions.{year}.{day_formatted}"

        # Dynamically import the module
        module = importlib.import_module(module_name)
        if hasattr(module, "solve"):
            print(
                f"Solving {year}/{day_formatted.capitalize()} - Part {part.upper()}..."
            )
            module.solve(
                year=year, day=day, part=part, test=args.test, submit_result=args.submit
            )
        else:
            print(
                f"The module '{day_formatted}' for year '{year}' does not have a solve() function."
            )
    except ValueError as e:
        print(
            f"Invalid problem format or input: {e}. Use 'year/day/part', e.g., '2024/1/a'."
        )
    except ModuleNotFoundError:
        print(f"Module for problem '{args.problem}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
