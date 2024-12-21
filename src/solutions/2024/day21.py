import networkx as nx
from loguru import logger as log

from utils.decorators import benchmark

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
numeric_keypad = nx.DiGraph()
navigation_keypad = nx.DiGraph()

# Add edges for the numeric keypad. This also adds the nodes automatically.
# region
numeric_keypad.add_edge(" ", "1", label="^")
numeric_keypad.add_edge(" ", "0", label=">")
numeric_keypad.add_edge("0", " ", label="<")
numeric_keypad.add_edge("0", "A", label=">")
numeric_keypad.add_edge("0", "2", label="^")
numeric_keypad.add_edge("A", "0", label="<")
numeric_keypad.add_edge("A", "3", label="^")
numeric_keypad.add_edge("1", "4", label="^")
numeric_keypad.add_edge("1", "2", label=">")
numeric_keypad.add_edge("1", " ", label="v")
numeric_keypad.add_edge("2", "1", label="<")
numeric_keypad.add_edge("2", "3", label=">")
numeric_keypad.add_edge("2", "5", label="^")
numeric_keypad.add_edge("2", "0", label="v")
numeric_keypad.add_edge("3", "2", label="<")
numeric_keypad.add_edge("3", "6", label="^")
numeric_keypad.add_edge("3", "A", label="v")
numeric_keypad.add_edge("4", "1", label="v")
numeric_keypad.add_edge("4", "5", label=">")
numeric_keypad.add_edge("4", "7", label="^")
numeric_keypad.add_edge("5", "2", label="v")
numeric_keypad.add_edge("5", "4", label="<")
numeric_keypad.add_edge("5", "6", label=">")
numeric_keypad.add_edge("5", "8", label="^")
numeric_keypad.add_edge("6", "3", label="v")
numeric_keypad.add_edge("6", "5", label="<")
numeric_keypad.add_edge("6", "9", label="^")
numeric_keypad.add_edge("7", "4", label="v")
numeric_keypad.add_edge("7", "8", label=">")
numeric_keypad.add_edge("8", "5", label="v")
numeric_keypad.add_edge("8", "7", label="<")
numeric_keypad.add_edge("8", "9", label=">")
numeric_keypad.add_edge("9", "6", label="v")
numeric_keypad.add_edge("9", "8", label="<")
# endregion

# Add edges for the navigation keypad. This also adds the nodes automatically.
# region
navigation_keypad.add_edge(" ", "^", label=">")
navigation_keypad.add_edge(" ", "<", label="v")
navigation_keypad.add_edge("^", " ", label="<")
navigation_keypad.add_edge("^", "A", label=">")
navigation_keypad.add_edge("^", "v", label="v")
navigation_keypad.add_edge("A", "^", label="<")
navigation_keypad.add_edge("A", ">", label="v")
navigation_keypad.add_edge("<", " ", label="^")
navigation_keypad.add_edge("<", "v", label=">")
navigation_keypad.add_edge("v", "<", label="<")
navigation_keypad.add_edge("v", "^", label="^")
navigation_keypad.add_edge("v", ">", label=">")
navigation_keypad.add_edge(">", "v", label="<")
navigation_keypad.add_edge(">", "A", label="^")
# endregion


def generate_numeric_sequence(code: str, graph: nx.DiGraph) -> list[str]:
    try:
        res = []
        code = "A" + code
        for i in range(len(code)):
            if i < len(code) - 1:
                path = nx.shortest_path(graph, code[i], code[i + 1])
                res.append(
                    "".join(
                        graph.get_edge_data(u, v)["label"]
                        for u, v in zip(path, path[1:])
                    )
                )

        # Append the letter 'A' at the end of each path
        for i in range(len(res)):
            res[i] += "A"

        return res
    except nx.NetworkXNoPath:
        return ""  # Or handle the case appropriately for your application


def generate_directional_sequence(
    directions: list[str], graph: nx.DiGraph
) -> list[str]:
    try:
        # We start off at the 'A' key. So for the very first direction set, we need to first prepend a 'A' to it.
        res = []
        # For each direction set, we need to go back to 'A' first.
        directions = ["A" + d for d in directions]
        # Add going back to 'A' at the end of final direction set.
        directions[-1] += "A"

        # Go through each set of directions and do similiar to the generate_numeric_sequence function, except we have to go back to 'A' after each set of directions.
        for i in range(len(directions)):
            for j in range(len(directions[i])):
                if j < len(directions[i]) - 1:
                    path = nx.shortest_path(
                        graph, directions[i][j], directions[i][j + 1]
                    )
                    res.append(
                        "".join(
                            graph.get_edge_data(u, v)["label"]
                            for u, v in zip(path, path[1:])
                        )
                    )

        # Append the letter 'A' at the end of each path
        for i in range(len(res)):
            res[i] += "A"

        return res
    except nx.NetworkXNoPath:
        return ""


@benchmark
def part_a[T](data: T) -> int:
    res = generate_numeric_sequence("029A", numeric_keypad)
    log.debug("".join(res))
    res2 = generate_directional_sequence(res, navigation_keypad)
    log.debug("".join(res2))
    res3 = generate_directional_sequence(res2, navigation_keypad)
    log.debug("".join(res3))
    res4 = generate_directional_sequence(res3, navigation_keypad)
    log.debug("".join(res4))
    return 0


@benchmark
def part_b[T](data: T) -> int:
    return 0


@benchmark
def parse[T](data: str) -> T:
    return data.splitlines()


test_data_a = """029A
"""

test_data_b = test_data_a
