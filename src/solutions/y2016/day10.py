from collections import deque
from math import prod

import networkx as nx

from utils.decorators import benchmark

type Node = tuple[str, int]


def simulate(
    g: nx.MultiDiGraph, low_target: int, high_target: int
) -> tuple[int | None, dict[int, list[int]]]:
    chips = {n: list(d.get("values", [])) for n, d in g.nodes(data=True)}
    ready = deque(n for n, v in chips.items() if n[0] == "bot" and len(v) == 2)
    comparer: int | None = None

    while ready:
        bot = ready.popleft()
        lo, hi = sorted(chips[bot])

        if (lo, hi) == (low_target, high_target):
            comparer = bot[1]

        chips[bot] = []
        for _, dest, d in g.out_edges(bot, data=True):
            chips[dest].append(lo if d["kind"] == "low" else hi)
            if dest[0] == "bot" and len(chips[dest]) == 2:
                ready.append(dest)

    outputs = {n[1]: v for n, v in chips.items() if n[0] == "output"}
    return comparer, outputs


@benchmark
def part_a(data: nx.MultiDiGraph) -> int:
    return simulate(data, 17, 61)[0] or -1


@benchmark
def part_b(data: nx.MultiDiGraph) -> int:
    return prod(simulate(data, 17, 61)[1][i][0] for i in (0, 1, 2))


@benchmark
def parse(data: str) -> nx.MultiDiGraph:
    g: nx.MultiDiGraph = nx.MultiDiGraph()

    for line in data.strip().splitlines():
        match line.split():
            case ["value", val, "goes", "to", "bot", bot]:
                node: Node = ("bot", int(bot))
                g.add_node(node)
                g.nodes[node].setdefault("values", []).append(int(val))

            case [
                "bot",
                bot,
                "gives",
                "low",
                "to",
                low_kind,
                low_id,
                "and",
                "high",
                "to",
                high_kind,
                high_id,
            ]:
                src: Node = ("bot", int(bot))
                g.add_node(src)
                g.nodes[src].setdefault("values", [])
                g.add_edge(src, (low_kind, int(low_id)), kind="low")
                g.add_edge(src, (high_kind, int(high_id)), kind="high")

            case _:
                raise ValueError(f"Invalid line: {line!r}")

    return g


test_data_a = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

test_data_b = test_data_a
