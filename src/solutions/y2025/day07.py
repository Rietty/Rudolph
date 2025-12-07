from utils.decorators import benchmark


# Instead of a graph easier to model this problem row by row instead and just.. count?
# Why the fuck didn't I think of this ages ago???
def emitter(data: list[str]) -> tuple[int, int]:
    W = len(data[0])
    start = data[0].index("S")

    beams = {start}
    counts = {start: 1}
    splits = 0

    for row in range(1, len(data)):
        line = data[row]

        new_beams = set()
        new_counts = {}

        for c in beams:
            if 0 <= c < W and line[c] == "^":
                splits += 1
                if c - 1 >= 0:
                    new_beams.add(c - 1)
                if c + 1 < W:
                    new_beams.add(c + 1)
            else:
                if 0 <= c < W:
                    new_beams.add(c)

        for c, n in counts.items():
            if 0 <= c < W and line[c] == "^":
                for nc in (c - 1, c + 1):
                    if 0 <= nc < W:
                        new_counts[nc] = new_counts.get(nc, 0) + n
            else:
                if 0 <= c < W:
                    new_counts[c] = new_counts.get(c, 0) + n

        beams = new_beams
        counts = new_counts

    return splits, sum(counts.values())


@benchmark
def part_a(data: list[str]) -> int:
    splits, _ = emitter(data)
    return splits


@benchmark
def part_b(data: list[str]) -> int:
    _, quantam = emitter(data)
    return quantam


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
