import argparse
import importlib

if __name__ == "__main__":
    # Create an argument parser.
    parser = argparse.ArgumentParser(description="Solve a specific Advent of Code problem.")
    parser.add_argument("--year", type=int, required=True, help="The year of the module, e.g., 2024.")
    parser.add_argument("--day", type=int, required=True, help="The day module to run, e.g., 1.")
    parser.add_argument("--part", type=int, required=True, help="The part of the day to run, e.g., 1 or 2.")
    parser.add_argument("--test", action="store_true", help="Solve the test input instead of the puzzle input.")
    parser.add_argument("--submit", action="store_true", help="Run the code but do not submit it.")
    args = parser.parse_args()

    # Construct the module name dynamically based on year and day
    day_formatted = f"day{args.day:02d}"  # Format day as day01, day02, etc.
    module_name = f"solutions.{args.year}.{day_formatted}"

    try:
        # Dynamically import the specified module
        module = importlib.import_module(module_name)
        if hasattr(module, "solve"):
            module.solve(test=args.test, part=args.part)
        else:
            print(f"The module '{day_formatted}' in year '{args.year}' does not have a solve() function.")
    except ModuleNotFoundError:
        print(f"Module '{day_formatted}' for year '{args.year}' not found. Please check the input.")