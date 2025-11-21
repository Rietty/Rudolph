from utils.decorators import benchmark


def is_safe(row: list[int]) -> bool:
    # Check to see if it is strictly decreasing or strictly increasing
    if sorted(row) == row or sorted(row, reverse=True) == row:
        # Check to see the difference between any 2 adjacent numbers is at most 3 and at least 1
        if all(abs(a - b) <= 3 for a, b in zip(row, row[1:])) and all(
            abs(a - b) >= 1 for a, b in zip(row, row[1:])
        ):
            return True
    return False


@benchmark
def part_a(data: list[list[int]]) -> int:
    return sum(is_safe(row) for row in data)


@benchmark
def part_b(data: list[list[int]]) -> int:
    # For each row of data, check if it is safe or not.
    # If it is not safe, then check if removing any 1 element makes it safe.
    safe = 0
    for row in data:
        if is_safe(row):
            safe += 1
        else:
            for i in range(len(row)):
                if is_safe(row[:i] + row[i + 1 :]):
                    safe += 1
                    break

    return safe


@benchmark
def parse(data: str) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in data.strip().splitlines()]


test_data_a = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

test_data_b = test_data_a
