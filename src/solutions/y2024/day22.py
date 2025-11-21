from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from typing import Final

from utils.decorators import benchmark

Iterations: Final[int] = 2000


def evolve(s: int) -> int:
    s = s ^ (s << 6) & ((1 << 24) - 1)
    s = s ^ (s >> 5) & ((1 << 24) - 1)
    s = s ^ (s << 11) & ((1 << 24) - 1)
    return s


def prices(s: int) -> list[int]:
    digits = []
    for _ in range(Iterations):
        digits.append(s % 10)
        s = evolve(s)
    return digits


def changes(s: list[int]) -> list[int]:
    return [s[i + 1] - s[i] for i in range(len(s) - 1)]


def map_changes_to_prices(s: int) -> dict[tuple[int, int, int, int], int]:
    price_list = prices(s)
    change_list = changes(price_list)
    result: dict[tuple[int, int, int, int], int] = {}
    n = len(change_list)

    if n < 4:
        return result

    # Explicitly construct the initial window
    window: tuple[int, int, int, int] = (
        change_list[0],
        change_list[1],
        change_list[2],
        change_list[3],
    )
    for i in range(n - 4):
        if window not in result:
            result[window] = price_list[i + 4]
        # Explicitly construct the next window
        window = (window[1], window[2], window[3], change_list[i + 4])

    return result


@benchmark
def part_a(data: list[int]) -> int:
    ans = 0
    for s in data:
        for _ in range(Iterations):
            s = evolve(s)
        ans += s
    return ans


@benchmark
def part_b(data: list[int]) -> int:
    def compute_price_map(s):
        return s, map_changes_to_prices(s)

    with ThreadPoolExecutor() as executor:
        price_map = dict(executor.map(compute_price_map, data))

    change_sums: defaultdict[tuple[int, int, int, int], int] = defaultdict(int)
    for _, price in price_map.items():
        for change, value in price.items():
            change_sums[change] += value

    max_sum = max(change_sums.values(), default=0)
    return max_sum


@benchmark
def parse(data: str) -> list[int]:
    return list(map(int, data.splitlines()))


test_data_a = """1
2
3
2024"""

test_data_b = test_data_a
