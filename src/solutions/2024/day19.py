from loguru import logger as log

from utils.decorators import benchmark


def count_designs(target: str, patterns: list[str]) -> int:
    cache = {}

    def combos(target: str) -> bool:
        if target == "":
            return 1

        if target in cache:
            return cache[target]

        counter = 0

        for p in patterns:
            if target.startswith(p):
                counter += combos(target[len(p) :])

        cache[target] = counter
        return cache[target]

    return combos(target)


@benchmark
def part_a[T](data: T) -> int:
    targets, patterns = data
    return sum(count_designs(t, patterns) > 0 for t in targets)


@benchmark
def part_b[T](data: T) -> int:
    targets, patterns = data
    return sum(count_designs(t, patterns) for t in targets)


@benchmark
def parse[T](data: str) -> T:
    towels, targets = data.split("\n\n")
    towels = [towel.strip() for towel in towels.split(",")]
    targets = [target.strip() for target in targets.splitlines()]
    return targets, towels


test_data_a = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

test_data_b = test_data_a
