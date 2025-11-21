import typing

import networkx as netx

from utils.decorators import benchmark

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

BYTES: typing.Final[int] = 1024
MX: typing.Final[int] = 70
MY: typing.Final[int] = 70


@benchmark
def part_a(data: list[tuple[int, int]]) -> int:
    graph = netx.Graph()

    for x in range(MX + 1):
        for y in range(MY + 1):
            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= MX and 0 <= ny <= MY:
                    graph.add_edge((x, y), (nx, ny))

    graph.remove_nodes_from(data[:BYTES])

    return netx.shortest_path_length(graph, (0, 0), (MX, MY))


@benchmark
def part_b(data: list[tuple[int, int]]) -> str:
    byte = 0
    graph = netx.Graph()

    for x in range(MX + 1):
        for y in range(MY + 1):
            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= MX and 0 <= ny <= MY:
                    graph.add_edge((x, y), (nx, ny))

    while True:
        graph.remove_node(data[byte])
        try:
            netx.shortest_path_length(graph, (0, 0), (MX, MY))
        except Exception:
            return ",".join(map(str, data[byte]))
        finally:
            byte += 1


@benchmark
def parse(data: str) -> list[tuple[int, int]]:
    return [
        (int(x), int(y)) for x, y in (line.split(",") for line in data.splitlines())
    ]


test_data_a = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

test_data_b = test_data_a
