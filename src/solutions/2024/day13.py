import logging
import re

from z3 import Int, Optimize, Solver

from utils.decorators import benchmark

log = logging.getLogger(__name__)

type Machine = tuple[int, int, int, int, int, int]


def solve_with_z3(machine):
    ax, ay, bx, by, px, py = machine

    a = Int("a")
    b = Int("b")
    objective = a * 3 + b

    solver = Optimize()
    solver.add(ax * a + bx * b == px)
    solver.add(ay * a + by * b == py)
    solver.add(a >= 0)
    solver.add(b >= 0)

    solver.minimize(objective)

    if solver.check():
        model = solver.model()
        a_val, b_val = 0, 0
        if model[a] is not None:
            a_val = model[a].as_long()
        if model[b] is not None:
            b_val = model[b].as_long()

        return 3 * a_val + b_val
    return None


@benchmark
def part_a[T](data: T) -> int:
    total = 0
    for machine in data:
        if (ans := solve_with_z3(machine)) is not None:
            total += ans
    return total


@benchmark
def part_b[T](data: T) -> int:
    total = 0
    for machine in data:
        ax, ay, bx, by, px, py = machine
        machine = [ax, ay, bx, by, px + 10000000000000, py + 10000000000000]
        if (ans := solve_with_z3(machine)) is not None:
            total += ans
    return total


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
