from utils.decorators import benchmark

KEYPAD_ONE = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

KEYPAD_TWO = [
    ["0", "0", "1", "0", "0"],
    ["0", "2", "3", "4", "0"],
    ["5", "6", "7", "8", "9"],
    ["0", "A", "B", "C", "0"],
    ["0", "0", "D", "0", "0"],
]


@benchmark
def part_a(data: list[str]) -> str:
    x: int = 1
    y: int = 1
    res = ""
    for d in data:
        for c in d:
            match c:
                case "U":
                    y = max(0, y - 1)
                case "L":
                    x = max(0, x - 1)
                case "R":
                    x = min(2, x + 1)
                case "D":
                    y = min(2, y + 1)
                case _:
                    pass
        res += str(KEYPAD_ONE[y][x])
    return res


@benchmark
def part_b(data: list[str]) -> str:
    x: int = 0
    y: int = 2
    res = ""
    moves = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

    for d in data:
        for c in d:
            if c not in moves:
                continue
            dx, dy = moves[c]
            nx, ny = x + dx, y + dy
            if abs(nx - 2) + abs(ny - 2) <= 2:
                x, y = nx, ny
        res += KEYPAD_TWO[y][x]
    return res


@benchmark
def parse(data: str) -> list[str]:
    return data.splitlines()


test_data_a = """ULL
RRDDD
LURDL
UUUUD
"""

test_data_b = test_data_a
