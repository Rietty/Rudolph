from typing import Iterable


class DSU[T]:
    def __init__(self, elements: Iterable[T]):
        self.p: dict[T, T] = {v: v for v in elements}
        self.s: dict[T, int] = {v: 1 for v in elements}

    def find(self, i: T) -> T:
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, i: T, j: T) -> bool:
        r_i = self.find(i)
        r_j = self.find(j)
        if r_i != r_j:
            if self.s[r_i] < self.s[r_j]:
                r_i, r_j = r_j, r_i
            self.p[r_j] = r_i
            self.s[r_i] += self.s[r_j]
            return True
        return False
