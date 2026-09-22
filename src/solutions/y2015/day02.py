from utils.decorators import benchmark

type Present = tuple[int, int, int]


@benchmark
def part_a(data: list[Present]) -> int:
    return sum(
        6
        + 2 * (length * width + length * height + width * height)
        + min(length * width, length * height, width * height)
        for length, width, height in data
    )


@benchmark
def part_b(data: list[Present]) -> int:
    return 0


@benchmark
def parse(data: str) -> list[Present]:
    def to_present(line: str) -> Present:
        length, width, height = map(int, line.split("x"))
        return length, width, height

    return [to_present(line) for line in data.splitlines() if line]


test_data_a = """2x3x4
1x1x10
"""

test_data_b = test_data_a
