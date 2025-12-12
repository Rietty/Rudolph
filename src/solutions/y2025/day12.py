from utils.decorators import benchmark


@benchmark
def part_a(data: tuple[dict, list]) -> int:
    shape_tiles, regions = data
    total_fit = 0

    for region in regions:
        R, C, counts = region["R"], region["C"], region["c"]
        area_available = R * C
        area_needed = sum(shape_tiles[i] * cnt for i, cnt in enumerate(counts))
        if area_needed < area_available * 0.85:
            total_fit += 1

    return total_fit


@benchmark
def part_b(data: tuple[dict, list]) -> int:
    return 1


@benchmark
def parse(data: str) -> tuple[dict, list]:
    lines = [line.rstrip() for line in data.splitlines() if line.strip()]
    counts = {}
    regions = []

    current_shape = None
    shape_rows = []

    for ln in lines:
        if ln.endswith(":") and "x" not in ln:
            if current_shape is not None:
                counts[current_shape] = sum(
                    sum(1 for c in row if c == "#") for row in shape_rows
                )
            current_shape = int(ln[:-1])
            shape_rows = []
        elif "x" in ln and ":" in ln:
            size, cs = ln.split(":")
            R, C = map(int, size.split("x"))
            cs = list(map(int, cs.strip().split()))
            regions.append({"R": R, "C": C, "c": cs})
        else:
            shape_rows.append(ln)

    if current_shape is not None:
        counts[current_shape] = sum(
            sum(1 for c in row if c == "#") for row in shape_rows
        )

    return counts, regions


test_data_a = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

test_data_b = test_data_a
