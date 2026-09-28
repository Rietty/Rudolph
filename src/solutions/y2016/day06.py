from collections import Counter

from utils.decorators import benchmark


@benchmark
def part_a(data: list[str]) -> str:
    return "".join(Counter(col).most_common(1)[0][0] for col in data)


@benchmark
def part_b(data: list[str]) -> str:
    return "".join(Counter(col).most_common()[-1][0] for col in data)


@benchmark
def parse(data: str) -> list[str]:
    return ["".join(col) for col in zip(*data.splitlines())]


test_data_a = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""

test_data_b = test_data_a
