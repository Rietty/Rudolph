from utils.decorators import benchmark


@benchmark
def part_a(data: str) -> int:
    floor = sum([1 if c == "(" else -1 for c in data])
    return floor


@benchmark
def part_b(data: str) -> int:
    while True:
        floor = 0
        for i, c in enumerate(data):
            floor += 1 if c == "(" else -1
            if floor == -1:
                return i + 1


@benchmark
def parse(data: str) -> str:
    return data


test_data_a = """(()(()("""

test_data_b = """()())"""
