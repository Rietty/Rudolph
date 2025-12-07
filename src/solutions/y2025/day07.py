from utils.decorators import benchmark


def emitter(data: list[str]) -> tuple[int, int]:
    width = len(data[0])
    counts = [0] * width
    counts[data[0].index("S")] = 1
    splits = 0

    for line in data[1:]:
        new = [0] * width
        for c, n in enumerate(counts):
            if n == 0:
                continue
            if line[c] == "^":
                splits += 1
                if c > 0:
                    new[c - 1] += n
                if c < width - 1:
                    new[c + 1] += n
            else:
                new[c] += n
        counts = new

    return splits, sum(counts)


@benchmark
def part_a(data: list[str]) -> int:
    splits, _ = emitter(data)
    return splits


@benchmark
def part_b(data: list[str]) -> int:
    _, quantum = emitter(data)
    return quantum


@benchmark
def parse(data: str) -> list[str]:
    return data.splitlines()


test_data_a = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


test_data_b = test_data_a
