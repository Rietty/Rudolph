from utils.decorators import benchmark


def value(row: int, col: int) -> int:
    a = row + col - 2
    b = row + col - 1
    n = ((a * b) // 2) + col
    return (20151125 * pow(252533, n - 1, 33554393)) % 33554393


@benchmark
def part_a(data: tuple[int, int]) -> int:
    return value(data[0], data[1])


@benchmark
def part_b(data: tuple[int, int]) -> int:
    return 0


@benchmark
def parse(data: str) -> tuple[int, int]:
    line = data.strip().split()
    return (int(line[-3].strip(",")), int(line[-1].strip(".")))


test_data_a = """To continue, please consult the code grid in the manual.  Enter the code at row 5, column 5.
"""

test_data_b = test_data_a
