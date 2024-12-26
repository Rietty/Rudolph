from loguru import logger as log

from utils.decorators import benchmark


@benchmark
def part_a(data: list[int, int, int]) -> int:
    return sum(
        2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l) for l, w, h in data
    )


@benchmark
def part_b(data: list[int, int, int]) -> int:
    return sum(2 * min(l + w, l + h, w + h) + l * w * h for l, w, h in data)


@benchmark
def parse(data: str) -> list[int, int, int]:
    return [tuple(map(int, line.split("x"))) for line in data.strip().split("\n")]


test_data_a = """2x3x4
1x1x10
"""

test_data_b = test_data_a
