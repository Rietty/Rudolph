from utils.decorators import benchmark


def rotate(current: int, rotation: int) -> int:
    return (current + rotation) % 100


@benchmark
def part_a(data: list[tuple[str, int]]) -> int:
    dial = 50
    zeros = 0
    for d, n in data:
        res = rotate(dial, n if d == "R" else -n)
        if res == 0:
            zeros += 1
        dial = res
    return zeros


@benchmark
def part_b(data: list[tuple[str, int]]) -> int:
    dial = 50
    zeros = 0
    for d, n in data:
        step = n if d == "R" else -n
        s = 1 if step > 0 else -1
        for _ in range(abs(step)):
            dial = rotate(dial, s)
            if dial == 0:
                zeros += 1
    return zeros


@benchmark
def parse(data: str) -> list[tuple[str, int]]:
    return [(line[0], int(line[1:])) for line in data.splitlines() if line]


test_data_a = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

test_data_b = test_data_a
