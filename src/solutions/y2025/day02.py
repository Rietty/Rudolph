from utils.decorators import benchmark


def is_repeated(n: int, exact_twice=False) -> bool:
    s = str(n)
    L = len(s)
    if exact_twice:
        if L & 1:
            return False
        h = L // 2
        return s[:h] == s[h:]
    for d in range(1, L // 2 + 1):
        if L % d == 0 and s == s[:d] * (L // d):
            return True
    return False


@benchmark
def part_a(data: list[tuple[int, int]]) -> int:
    return sum(
        i for low, high in data for i in range(low, high + 1) if is_repeated(i, True)
    )


@benchmark
def part_b(data: list[tuple[int, int]]) -> int:
    return sum(
        i for low, high in data for i in range(low, high + 1) if is_repeated(i, False)
    )


@benchmark
def parse(data: str) -> list[tuple[int, int]]:
    return [tuple(map(int, seg.split("-"))) for seg in data.split(",")]


test_data_a = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

test_data_b = test_data_a
