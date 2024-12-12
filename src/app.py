import importlib
import logging
import logging.config
import os

import cloup
import yaml

from utils.solver import solve_problem, test_problem

log = logging.getLogger(__name__)


@cloup.command()
@cloup.option("--year", "-y", type=int, required=True, help="Problem year.")
@cloup.option("--day", "-d", type=int, required=True, help="Problem day.")
@cloup.option("--part", "-p", type=str, required=True, help="Problem part.")
@cloup.option_group(
    "Data",
    "Deciding on data source and destination.",
    cloup.option(
        "--test",
        "-t",
        is_flag=True,
        default=False,
        help="Solve the test input instead of the puzzle input.",
    ),
    cloup.option(
        "--submit",
        "-s",
        is_flag=True,
        default=False,
        help="Submit the solution after solving it.",
    ),
    cloup.option("--file", "-f", type=str, default=None, help="Path to an input file."),
    constraint=cloup.constraints.mutually_exclusive,
)
def main(**kwargs):
    """Solve a specific Advent of Code problem."""
    try:
        year = kwargs["year"]
        day = kwargs["day"]
        part = kwargs["part"].lower()

        if part not in ["a", "b"]:
            raise ValueError("Part must be 'a' or 'b'.")

        day_formatted = f"day{day:02d}"  # Format day as day01, day02, etc.
        module_name = f"solutions.{year}.{day_formatted}"

        # Check if the module exists
        module = importlib.import_module(module_name)

        if kwargs["test"] or kwargs["file"]:
            log.info(f"Testing Day {day}, {year}, Part {part.upper()}...")
            test_problem(
                part=part,
                parse=module.parse,
                part_a=module.part_a,
                part_b=module.part_b,
                test_data_a=module.test_data_a,
                test_data_b=module.test_data_b,
                file=kwargs["file"],
            )
        else:
            log.info(f"Solving Day {day}, {year}, Part {part.upper()}...")
            solve_problem(
                year=year,
                day=day,
                part=part,
                publish=kwargs["submit"],
                parse=module.parse,
                part_a=module.part_a,
                part_b=module.part_b,
            )

    except ValueError as e:
        log.error(f"{e}")
        raise e
    except ModuleNotFoundError as e:
        log.error(f"{e}")
        raise e
    except Exception as e:
        log.error(f"{e}")
        raise e


if __name__ == "__main__":
    # Load logging configuration.
    log_config_path = os.path.join(os.path.dirname(__file__), "config", "logger.yml")

    with open(log_config_path, "r") as f:
        log_config = yaml.safe_load(f.read())

    # Set up logging suppression of external loggers.
    logging.getLogger("aocd").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.getLogger("matplotlib").setLevel(logging.ERROR)
    logging.getLogger("PIL").setLevel(logging.ERROR)

    # Assign configuration to the logger.
    logging.config.dictConfig(log_config)

    # Start our application.
    main()
