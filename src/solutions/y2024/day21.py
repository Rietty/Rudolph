"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""

from utils.decorators import benchmark

numeric = dict(
    zip(
        "7894561230A",
        [
            [0, 0],
            [0, 1],
            [0, 2],
            [1, 0],
            [1, 1],
            [1, 2],
            [2, 0],
            [2, 1],
            [2, 2],
            [3, 1],
            [3, 2],
        ],
    )
)
directions = dict(zip("^A<v>", [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]))
keypads = {**numeric, **directions}


@benchmark
def part_a(data: list[str]) -> int:
    return 0


@benchmark
def part_b(data: list[str]) -> int:
    return 0


@benchmark
def parse(data: str) -> list[str]:
    return data.splitlines()


test_data_a = """029A
980A
179A
456A
379A
"""

test_data_b = test_data_a
