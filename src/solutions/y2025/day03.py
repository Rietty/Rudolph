from utils.decorators import benchmark


def max_joltage(input: int, n: int) -> int:
    # Length of input number
    if input == 0:
        L = 1
    else:
        t = input
        L = 0
        while t > 0:
            t //= 10
            L += 1

    # If number of required digits is larger than number, we just return number.
    if n >= L:
        return input

    # Figure out how many digits to remove
    remove = L - n

    # Yay for monotonic stacks!
    stack = []

    # Go thru digits and basically we add whatever digit is bigger at the end.
    for i in range(L - 1, -1, -1):
        current_digit = input // (10**i) % 10

        while remove > 0 and stack and stack[-1] < current_digit:
            stack.pop()
            remove -= 1

        stack.append(current_digit)

    # Remove however many digits left in the stack
    final_digits = stack[:n]

    # Reconstruct number using power of 10
    result = 0
    for i in range(len(final_digits)):
        digit = final_digits[i]
        power = n - 1 - i
        result += digit * (10**power)

    return result


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
