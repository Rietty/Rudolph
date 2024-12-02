from utils.decorators import benchmark
from utils.solver import Problem, solve_problem


@benchmark
def part_a[T](data: T) -> int:
    z_bits = list(zip(*data))

    most_common = [max(set(bits), key=bits.count) for bits in z_bits]
    least_common = [min(set(bits), key=bits.count) for bits in z_bits]

    gamma = int("".join(most_common), 2)
    epsilon = int("".join(least_common), 2)

    return gamma * epsilon


@benchmark
def part_b[T](data: T) -> int:
    pass


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


test_data_a = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

test_data_b = """
"""
