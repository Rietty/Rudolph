from utils.decorators import benchmark


# Instead of a graph easier to model this problem row by row instead and just.. count?
# Why the fuck didn't I think of this ages ago???
def emitter(data: list[str]) -> tuple[int, int]:
    counts = {data[0].index("S"): 1}
    splits = 0

    for line in data[1:]:
        nc = {}
        for c, n in counts.items():
            hit = 0 <= c < len(data[0]) and line[c] == "^"
            if hit:
                splits += 1
                for nc2 in (c - 1, c + 1):
                    if 0 <= nc2 < len(data[0]):
                        nc[nc2] = nc.get(nc2, 0) + n
            else:
                if 0 <= c < len(data[0]):
                    nc[c] = nc.get(c, 0) + n
        counts = nc

    return splits, sum(counts.values())


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
