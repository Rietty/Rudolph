from utils.decorators import benchmark


def max_joltage(input: int, n: int) -> int:
    s = str(input)
    L = len(s)
    if n >= L:
        return input
    remove = L - n
    st = []
    for d in s:
        while remove and st and st[-1] < d:
            st.pop()
            remove -= 1
        st.append(d)
    if remove:
        st = st[:-remove]
    return int("".join(st))


@benchmark
def part_a(data: list[int]) -> int:
    return sum([max_joltage(n, 2) for n in data])


@benchmark
def part_b(data: list[int]) -> int:
    return sum([max_joltage(n, 12) for n in data])


@benchmark
def parse(data: str) -> list[int]:
    return [int(num) for num in data.splitlines()]


test_data_a = """987654321111111
811111111111119
234234234234278
818181911112111
"""

test_data_b = test_data_a
