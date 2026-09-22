from typing import TypedDict

import cvxpy as cp
import numpy as np
from cvxpy.atoms.affine.sum import sum as cp_sum
from scipy.optimize import Bounds, LinearConstraint, milp

from utils.decorators import benchmark


class Machine(TypedDict):
    i: list[int]
    b: list[list[int]]
    j: list[int]


type Machines = list[Machine]


def configure_lights(indicator: list[int], buttons: list[list[int]]) -> int:
    n, m = len(indicator), len(buttons)
    A = np.zeros((n, m), dtype=int)
    b = np.array([i & 1 for i in indicator], dtype=int)

    for j, btn in enumerate(buttons):
        A[list(btn), j] = 1

    x = cp.Variable(m, boolean=True)
    y = cp.Variable(n, integer=True)

    constraints = [A[i] @ x - 2 * y[i] == b[i] for i in range(n)]

    cp.Problem(cp.Minimize(cp_sum(x)), constraints).solve(solver=cp.GLPK_MI)
    assert x.value is not None

    return int(np.round(x.value).sum())


def specify_joltages(buttons: list[list[int]], target: list[int]) -> int:
    n = len(target)
    m = len(buttons)

    A = np.zeros((n, m))

    for index, btn in enumerate(buttons):
        for joltage in btn:
            A[joltage, index] = 1

    cost = np.ones(m)
    integrality = np.ones(m, dtype=int)
    bounds = Bounds(np.zeros(m), np.full(m, np.inf))
    constraints = LinearConstraint(A, np.array(target), np.array(target))
    res = milp(c=cost, constraints=constraints, bounds=bounds, integrality=integrality)
    assert res.fun is not None
    return round(float(res.fun))


@benchmark
def part_a(data: Machines) -> int:
    total = 0
    for _, m in enumerate(data, 1):
        if (w := configure_lights(m["i"], m["b"])) is not None:
            total += w
    return total


@benchmark
def part_b(data: Machines) -> int:
    total = 0
    for m in data:
        if w := specify_joltages(m["b"], m["j"]):
            total += w
    return total


@benchmark
def parse(data: str) -> Machines:
    machines: Machines = []

    for line in data.splitlines():
        parts = line.split()
        i = [int(ch == "#") for ch in parts[0][1:-1]]
        b = [[int(x) for x in part[1:-1].split(",")] for part in parts[1:-1]]
        j = [int(x) for x in parts[-1][1:-1].split(",")]

        machines.append({"i": i, "b": b, "j": j})

    return machines


test_data_a = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

test_data_b = test_data_a
