from loguru import logger as log

from utils.decorators import benchmark


@benchmark
def part_a(data: list[str]) -> int:
    z_bits = list(zip(*data))

    most_common = [max(set(bits), key=bits.count) for bits in z_bits]
    least_common = [min(set(bits), key=bits.count) for bits in z_bits]

    gamma = int("".join(most_common), 2)
    epsilon = int("".join(least_common), 2)

    return gamma * epsilon


@benchmark
def part_b(data: list[str]) -> int:
    return 0


@benchmark
def parse(data: str) -> list[str]:
    return data.splitlines()


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

test_data_b = test_data_a
