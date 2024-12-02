from utils.decorators import benchmark
from utils.solver import Problem, solve_problem


@benchmark
def part_a[T](data: T) -> int:
    return 0


@benchmark
def part_b[T](data: T) -> int:
    return 0


def parse[T](data: str) -> T:
    return data.splitlines()


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
