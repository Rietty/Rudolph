from utils.decorators import benchmark


@benchmark
def part_a(data: list[int]) -> int:
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1
    return count


@benchmark
def part_b(data: list[int]) -> int:
    count = 0
    for i in range(3, len(data)):
        if sum(data[i - 2 : i + 1]) > sum(data[i - 3 : i]):
            count += 1
    return count


@benchmark
def parse(data: str) -> list[int]:
    return list(map(int, data.strip().splitlines()))


test_data_a = """199
200
208
210
200
207
240
269
260
263
"""

test_data_b = test_data_a
