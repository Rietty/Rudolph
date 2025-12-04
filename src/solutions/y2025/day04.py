from collections import Counter

from library.grid import Grid
from utils.decorators import benchmark


@benchmark
def part_a(data: Grid) -> int:
    n = data.width
    m = data.height
    sum = 0
    for r in range(n):
        for c in range(m):
            if data[r][c] == ".":
                continue
            counter = Counter(data.get_neighbour_values(r, c, True))
            if counter["@"] < 4:
                sum += 1
    return sum


@benchmark
def part_b(data: Grid) -> int:
    n = data.width
    m = data.height
    total_sum = 0

    while True:
        previous_sum = total_sum

        rolls_to_remove = []
        for r in range(n):
            for c in range(m):
                if data[r][c] == ".":
                    continue

                counter = Counter(data.get_neighbour_values(r, c, True))
                if counter["@"] < 4:
                    total_sum += 1
                    rolls_to_remove.append((r, c))

        if total_sum == previous_sum:
            break

        # Remove all the rolls
        for a, b in rolls_to_remove:
            current_string = data[a]
            new_string = current_string[:b] + "." + current_string[b + 1 :]
            data[a] = new_string

    return total_sum


@benchmark
def parse(data: str) -> Grid:
    return Grid([c for c in data.splitlines()])


test_data_a = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

test_data_b = test_data_a
