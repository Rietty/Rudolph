import re

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

from utils.decorators import benchmark

type Machine = dict[str, list]
type Machines = list[Machine]


def configure_lights(indicator, buttons):
    n, m = len(indicator), len(buttons)
    A = np.zeros((n, m), dtype=bool)
    target_state = np.array([i & 1 for i in indicator], dtype=bool)

    for btn_index, btn in enumerate(buttons):
        A[list(btn), btn_index] = True

    pivot_columns, row = [], 0

    for col in range(m):
        pivot_row = next((i for i in range(row, n) if A[i, col]), None)
        if pivot_row is None:
            continue

        if pivot_row != row:
            A[[row, pivot_row]], target_state[[row, pivot_row]] = (
                A[[pivot_row, row]],
                target_state[[pivot_row, row]],
            )

        pivot_columns.append(col)

        mask = A[:, col] & (np.arange(n) != row)
        A[mask] ^= A[row]
        target_state[mask] ^= target_state[row]

        row += 1
        if row == n:
            break

    if target_state[row:].any():
        return None

    solution = np.zeros(m, dtype=bool)
    solution[pivot_columns] = target_state[: len(pivot_columns)]

    free_columns = [c for c in range(m) if c not in pivot_columns]

    if len(free_columns) > 24:
        return int(solution.sum())

    basis_vectors = [np.zeros(m, dtype=bool) for _ in free_columns]

    for i, f_col in enumerate(free_columns):
        basis_vectors[i][f_col] = True
        basis_vectors[i][pivot_columns] = A[: len(pivot_columns), f_col]

    min_presses = solution.sum()
    for mask in range(1, 1 << len(free_columns)):
        candidate = solution.copy()
        for i in range(len(free_columns)):
            if mask >> i & 1:
                candidate ^= basis_vectors[i]
        min_presses = min(min_presses, candidate.sum())

    return int(min_presses)


def specify_joltages(buttons: list[int], target: list[int]):
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

    r = milp(c=cost, constraints=constraints, bounds=bounds, integrality=integrality)

    if not r.success:
        return None

    return int(round(r.fun))


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
    machines = []
    for line in data.splitlines():
        line = line.strip()

        i_m = re.search(r"\[(.*?)\]", line)

        i = [1 if c == "#" else 0 for c in i_m[1]]

        b = [
            [int(x) for x in b_m[1].strip().split(",") if x]
            for b_m in re.finditer(r"\((.*?)\)", line)
        ]

        j_m = re.search(r"\{(.*?)\}", line)
        j = [int(p) for p in j_m[1].split(",") if p.strip()]

        machines.append({"i": i, "b": b, "j": j})

    return machines


test_data_a = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

test_data_b = test_data_a
