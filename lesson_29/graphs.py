from typing import List

graph = {
    "A": [
        ["B", 3],
    ],
    "B": [
        ["C", 300],
        ["E", 30],
    ],
    "C": [
        ["D", 15],
    ],
    "D": [],
    "E": [
        ["F", 70],
    ],
    "F": [],
}


routes = [
    ["A", "B", "C", "D"],
    ["A", "B", "C", "E", "G"],
    ["A", "B", "C", "E", "F"],
    ["A", "B", "E", "G"],
    ["A", "B", "E", "F"],
]


def find_route(start, end, routes=None) -> List[str]:
    routes = []

    edges = graph[start]
    for node, length in edges:
        print(start, node)
        find_route(node, end, ...)

    # print(start, routes)

    return routes


result_route = find_route("A", "F")
assert (
    result_route == ["A", "B", "E", "F"]
), (
    f"Result route is: {result_route}"
)






class Node:
    pass


class Edge:
    pass
