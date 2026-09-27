from utils.decorators import benchmark

LIMIT = 1_000_000  # We have one million houses and 1 million elves!


@benchmark
def part_a(data: int) -> int:
    totals = [0] * LIMIT
    for elf in range(1, LIMIT):
        for house in range(elf, LIMIT, elf):
            totals[house] += elf * 10
    return next((i for i, x in enumerate(totals) if x >= data))


@benchmark
def part_b(data: int) -> int:
    totals = [0] * LIMIT
    for elf in range(1, LIMIT):
        for house in range(elf, min(LIMIT, elf * 50 + 1), elf):
            totals[house] += elf * 11
    return next((i for i, x in enumerate(totals) if x >= data))


@benchmark
def parse(data: str) -> int:
    return int(data.strip())


test_data_a = """100
"""

test_data_b = test_data_a
