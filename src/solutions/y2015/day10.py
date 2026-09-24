from itertools import groupby

from utils.decorators import benchmark


def look_and_say(s: str) -> str:
    return "".join(f"{len(list(g))}{d}" for d, g in groupby(s))


@benchmark
def part_a(data: str) -> int:
    for _ in range(40):
        data = look_and_say(data)
    return len(data)


@benchmark
def part_b(data: str) -> int:
    for _ in range(50):
        data = look_and_say(data)
    return len(data)


@benchmark
def parse(data: str) -> str:
    return data.strip()


test_data_a = """1
"""

test_data_b = test_data_a
