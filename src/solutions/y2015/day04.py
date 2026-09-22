import hashlib

from utils.decorators import benchmark


def find_adventcoin(secret_key: str, zeroes: int) -> int:
    prefix = "0" * zeroes
    number = 0
    while True:
        number += 1
        digest = hashlib.md5(f"{secret_key}{number}".encode()).hexdigest()
        if digest.startswith(prefix):
            return number


@benchmark
def part_a(data: str) -> int:
    return find_adventcoin(data, 5)


@benchmark
def part_b(data: str) -> int:
    return find_adventcoin(data, 6)


@benchmark
def parse(data: str) -> str:
    return data


test_data_a = """abcdef
"""

test_data_b = test_data_a
