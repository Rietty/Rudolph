import re
import typing

from loguru import logger as log

from utils.decorators import benchmark

type Machine = tuple[int, int, int, int, int, int]
OFFSET: typing.Final[int] = 10_000_000_000_000


def solve(machine: Machine, limit: int) -> int:
    ax, ay, bx, by, px, py = machine

    x = (ax * py - ay * px) / (ax * by - ay * bx)
    y = (bx * py - by * px) / (bx * ay - by * ax)

    if x.is_integer() and y.is_integer() and 0 <= x <= limit and 0 <= y <= limit:
        return int(x) + 3 * int(y)

    return None


@benchmark
def part_a[T](data: T) -> int:
    total = 0
    for machine in data:
        if (ans := solve(machine, 100)) is not None:
            total += ans
    return total


@benchmark
def part_b[T](data: T) -> int:
    total = 0
    for machine in data:
        ax, ay, bx, by, px, py = machine
        machine = [ax, ay, bx, by, px + OFFSET, py + OFFSET]
        if (ans := solve(machine, OFFSET)) is not None:
            total += ans
    return total


@benchmark
def parse[T](data: str) -> T:
    machines = []
    for block in data.split("\n\n"):
        lines = block.split("\n")
        values = []
        for line in lines:
            match = re.search(r"X[+=](\d+), Y[+=](\d+)", line)
            if match:
                values.extend([int(match.group(1)), int(match.group(2))])
        machines.append(values)
    return machines


test_data_a = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

test_data_b = test_data_a
