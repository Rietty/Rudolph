import logging

from utils.decorators import benchmark

log = logging.getLogger(__name__)


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

test_data_b = """
"""
