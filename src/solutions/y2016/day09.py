import re
from collections import deque

from utils.decorators import benchmark

TOKEN_RE = re.compile(r"\(\d+[xX]\d+\)|\S")
MARKER_RE = re.compile(r"\((\d+)[xX](\d+)\)")


def decompress(tokens: deque[str]) -> str:
    """Consume the deque and return the decompressed string."""
    out: list[str] = []

    while tokens:
        token = tokens.popleft()
        m = MARKER_RE.fullmatch(token)

        if m is None:
            out.append(token)
            continue

        length, times = int(m[1]), int(m[2])

        # Grab the next `length` *characters* (not tokens).
        chunk: list[str] = []
        remaining = length
        while remaining > 0 and tokens:
            tok = tokens.popleft()
            if len(tok) > remaining:
                # Marker straddles the boundary: split it, push the rest back.
                tokens.appendleft(tok[remaining:])
                tok = tok[:remaining]
            chunk.append(tok)
            remaining -= len(tok)

        out.append("".join(chunk) * times)

    return "".join(out)


def decompressed_length(tokens: deque[str]) -> int:
    total = 0
    pos = 0
    stack: list[tuple[int, int]] = []

    while tokens:
        while stack and pos >= stack[-1][0]:
            stack.pop()

        mult = stack[-1][1] if stack else 1
        token = tokens.popleft()

        if stack:
            room = stack[-1][0] - pos
            if len(token) > room:
                tokens.appendleft(token[room:])
                token = token[:room]

        m = MARKER_RE.fullmatch(token)
        pos += len(token)

        if m is None:
            total += len(token) * mult
        else:
            length, times = int(m[1]), int(m[2])
            end = pos + length
            if stack:
                end = min(end, stack[-1][0])
            stack.append((end, mult * times))

    return total


@benchmark
def part_a(data: deque[str]) -> int:
    return len(decompress(data))


@benchmark
def part_b(data: deque[str]) -> int:
    return decompressed_length(data)


@benchmark
def parse(data: str) -> deque[str]:
    return deque(TOKEN_RE.findall(data))


test_data_a = """X(8x2)(3x3)ABCY
"""

test_data_b = test_data_a
