from loguru import logger as log
from library.graph import Graph
import networkx as nx

from utils.decorators import benchmark


@benchmark
def part_a(data: Graph) -> int:
    return len(
        [
            cycle
            for cycle in nx.simple_cycles(data.get(), 3)
            if any(word[0] == "t" for word in cycle)
        ]
    )


@benchmark
def part_b(data: Graph) -> str:
    return ",".join(sorted(max(nx.find_cliques(data.get()), key=len)))


@benchmark
def parse(data: str) -> Graph:
    graph = Graph()
    for line in data.splitlines():
        u, v = line.split("-")
        graph.add_edge(u, v)
    return graph


test_data_a = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

test_data_b = test_data_a
