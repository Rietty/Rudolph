from utils.decorators import benchmark
from utils.solver import Problem, solve_problem


@benchmark
def part_a[T](data: T) -> int:
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1
    return count


@benchmark
def part_b[T](data: T) -> int:
    count = 0
    for i in range(3, len(data)):
        if sum(data[i - 2 : i + 1]) > sum(data[i - 3 : i]):
            count += 1
    return count


def parse[T](data: str) -> T:
    return list(map(int, data.strip().splitlines()))


def solve(problem: Problem) -> None:
    solve_problem(
        problem,
        parse,
        part_a,
        part_b,
        test_data_a,
        test_data_b,
    )


test_data_a = """199
200
208
210
200
207
240
269
260
263
"""

test_data_b = """199
200
208
210
200
207
240
269
260
263
"""
