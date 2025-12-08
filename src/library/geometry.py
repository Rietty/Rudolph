# Common geometry functions and calculations for various problems.
from dataclasses import dataclass

_SHORTHAND = "xyzwvutsrqponmlkjihgfedcba"  # 26 possible indices


@dataclass(frozen=True)
class Point:
    coords: tuple

    def __hash__(self):
        h = 0
        for c in self.coords:
            h = (h * 1315423911) ^ c
        return h

    def _binop(self, other, op):
        return Point(tuple(op(a, b) for a, b in zip(self.coords, other.coords)))

    def __add__(self, o):
        return self._binop(o, lambda a, b: a + b)

    def __sub__(self, o):
        return self._binop(o, lambda a, b: a - b)

    def __mul__(self, o):
        return self._binop(o, lambda a, b: a * b)

    def __truediv__(self, o):
        return self._binop(o, lambda a, b: a / b)

    def __floordiv__(self, o):
        return self._binop(o, lambda a, b: a // b)

    def __mod__(self, o):
        return self._binop(o, lambda a, b: a % b)

    def __eq__(self, o):
        return self.coords == o.coords

    def __ne__(self, o):
        return self.coords != o.coords

    # Lexicographic order (fast, supports sorting)
    def __lt__(self, o):
        return self.coords < o.coords

    def __le__(self, o):
        return self.coords <= o.coords

    def __gt__(self, o):
        return self.coords > o.coords

    def __ge__(self, o):
        return self.coords >= o.coords

    def __getattr__(self, name):
        if name in _SHORTHAND:
            i = _SHORTHAND.index(name)
            if i < len(self.coords):
                return self.coords[i]
        raise AttributeError(name)

    def __str__(self):
        return f"{self.coords}"

    def __repr__(self):
        return f"PointN{self.coords}"


def manhattan_distance(a: Point, b: Point):
    return sum(abs(x - y) for x, y in zip(a.coords, b.coords))


def euclidean_distance(a: Point, b: Point):
    return sum((x - y) * (x - y) for x, y in zip(a.coords, b.coords)) ** 0.5


def chebyshev_distance(a: Point, b: Point):
    return max(abs(x - y) for x, y in zip(a.coords, b.coords))
