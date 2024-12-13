from loguru import logger as log

from utils.decorators import benchmark


@benchmark
def part_a[T](data: T) -> int:
    return 0


@benchmark
def part_b[T](data: T) -> int:
    return 0


def parse[T](data: str) -> T:
    return data.splitlines()


test_data_a = """
"""

test_data_b = test_data_a
