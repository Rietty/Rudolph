import networkx as nx

from utils.decorators import benchmark


@benchmark
def part_a(data: nx.Graph) -> int:
    return len(
        [
            cycle
            for cycle in nx.simple_cycles(data, 3)
            if any(word[0] == "t" for word in cycle)
        ]
    )


@benchmark
def part_b(data: nx.Graph) -> str:
    cliques: list[list[str]] = list(nx.find_cliques(data))
    largest_clique = max(cliques, key=len)
    return ",".join(sorted(largest_clique))


@benchmark
def parse(data: str) -> nx.Graph:
    graph = nx.Graph()
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
