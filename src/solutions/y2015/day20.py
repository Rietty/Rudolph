from utils.decorators import benchmark


@benchmark
def part_a(data: list[str]) -> int:
    return 0


@benchmark
def part_b(data: list[str]) -> int:
    return 0


@benchmark
def parse(data: str) -> list[str]:
    return data.splitlines()


test_data_a = """
"""

test_data_b = test_data_a
