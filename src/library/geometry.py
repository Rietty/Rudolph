# Common geometry functions and calculations for various problems.
import math
from dataclasses import dataclass
from typing import Callable, Iterator

_SHORTHAND = "xyzwvutsrqponmlkjihgfedcba"  # 26 possible indices


@dataclass(frozen=True)
class Point:
    coords: tuple[float, ...]

    def __hash__(self) -> int:
        h = 0
        for c in self.coords:
            h = (h * 1315423911) ^ hash(c)
        return h

    def _binop(self, other: "Point", op: Callable[[float, float], float]) -> "Point":
        return Point(tuple(op(a, b) for a, b in zip(self.coords, other.coords)))

    def __add__(self, o: "Point") -> "Point":
        return self._binop(o, lambda a, b: a + b)

    def __sub__(self, o: "Point") -> "Point":
        return self._binop(o, lambda a, b: a - b)

    def __mul__(self, o: "Point") -> "Point":
        return self._binop(o, lambda a, b: a * b)

    def __truediv__(self, o: "Point") -> "Point":
        return self._binop(o, lambda a, b: a / b)

    def __floordiv__(self, o: "Point") -> "Point":
        return self._binop(o, lambda a, b: a // b)

    def __mod__(self, o: "Point") -> "Point":
        return self._binop(o, lambda a, b: a % b)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Point):
            return NotImplemented
        return self.coords == o.coords

    def __ne__(self, o: object) -> bool:
        result = self.__eq__(o)
        if result is NotImplemented:
            return result
        return not result

    # Lexicographic order (fast, supports sorting)
    def __lt__(self, o: "Point") -> bool:
        return self.coords < o.coords

    def __le__(self, o: "Point") -> bool:
        return self.coords <= o.coords

    def __gt__(self, o: "Point") -> bool:
        return self.coords > o.coords

    def __ge__(self, o: "Point") -> bool:
        return self.coords >= o.coords

    def __getattr__(self, name: str) -> float:
        if name in _SHORTHAND:
            i = _SHORTHAND.index(name)
            if i < len(self.coords):
                return self.coords[i]
        raise AttributeError(name)

    def __str__(self) -> str:
        return f"{self.coords}"

    def __repr__(self) -> str:
        return f"PointN{self.coords}"

    def __iter__(self) -> Iterator[float]:
        return iter(self.coords)


def manhattan_distance(a: Point, b: Point) -> float:
    return sum(abs(x - y) for x, y in zip(a.coords, b.coords))


def euclidean_distance(a: Point, b: Point) -> float:
    return math.dist(a.coords, b.coords)


def chebyshev_distance(a: Point, b: Point) -> float:
    return max(abs(x - y) for x, y in zip(a.coords, b.coords))
