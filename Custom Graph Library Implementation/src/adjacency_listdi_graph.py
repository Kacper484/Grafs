from base_graph import BaseGraph, Node, Edge


class AdjacencyListDiGraph(BaseGraph):
    def __init__(self, *, allow_loops: bool = False) -> None:
        super().__init__(is_directed=True, allow_loops=allow_loops)
        self._adj = {}

    def add_node(self, node: Node) -> None:
        if node not in self._adj:
            self._adj[node] = {}

    def add_edge(self, u: Node, v: Node, weight: float | None = None) -> None:
        if u == v and not self.allow_loops:
            raise ValueError("Loops are not allowed in this graph.")

        if not self.has_node(v)  or not self.has_node(u):
            raise KeyError("Both nodes must already exist.")
        
        self._adj[u][v] = weight

    def remove_node(self, node: Node) -> None:
        if not self.has_node(node):
            raise KeyError(f"Node need to exist {node}")

        del self._adj[node]

        for u in self._adj:
            if node in self._adj[u]:
                del self._adj[u][node]


    def remove_edge(self, u: Node, v: Node) -> None:
        if not self.has_node(v)  or not self.has_node(u):
            raise KeyError(f"Both nodes must already exist.{u, v}")
        
        if not self.has_edge(u, v):
            raise KeyError((u, v))

        del self._adj[u][v]

    def has_node(self, node: Node) -> bool:
        return node in self._adj

    def has_edge(self, u: Node, v: Node) -> bool:
        return self.has_node(u) and v in self._adj[u]

    def neighbors(self, node: Node):
        if not self.has_node(node):
            raise KeyError(node)

        return  tuple(self._adj[node].keys())

    def nodes(self):
        return tuple(self._adj.keys())

    def edges(self):
        for u in self._adj:
            for v, weight in self._adj[u].items():
                yield  (u, v, weight)

    def edge_weight(self, u: Node, v: Node):
        if not self.has_node(v)  or not self.has_node(u):
            raise KeyError((u, v)) 
        
        if not self.has_edge(u, v):
            raise KeyError((u, v))

        return self._adj[u][v]


from grader_helpers import assert_true, assert_false, assert_equal

if __name__ == "__main__":
    g = AdjacencyListDiGraph()
    for v in ["A", "B", "C"]:
        g.add_node(v)

    g.add_edge("A", "B", 4.0)
    g.add_edge("C", "A", 1.0)

    assert_true(g.has_edge("A", "B"))
    assert_false(g.has_edge("B", "A"))
    assert_equal(set(g.neighbors("A")), {"B"})
    assert_equal(g.edge_weight("A", "B"), 4.0)

    print("OK")


    g = AdjacencyListDiGraph()
    for v in ["A", "B", "C"]:
        g.add_node(v)

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")

    assert_equal(g.out_degree("A"), 2)
    assert_equal(g.in_degree("C"), 2)
    assert_equal(g.out_degree("C"), 0)
    assert_equal(g.in_degree("A"), 0)

    print("OK")