from base_graph import BaseGraph, Node, Edge

class AdjacencyListGraph(BaseGraph):
    def __init__(self, *, allow_loops: bool = False) -> None:
        super().__init__(is_directed=False, allow_loops=allow_loops)
        self._adj = {}

    def add_node(self, node: Node) -> None:
        if node not in self._adj:
            self._adj[node] = {}

    def add_edge(self, u: Node, v: Node, weight: float | None = None) -> None:
        if u == v and not self.allow_loops:
            raise ValueError("Loops are not allowed in this graph.")

        if not self.has_node(v)  or not self.has_node(u):
            raise KeyError("Both nodes must already exist.")
        
        self._adj[v][u] = weight
        self._adj[u][v] = weight


    def remove_node(self, node: Node) -> None:
        if not self.has_node(node):
            raise KeyError(f"Node need to exist {node}")
        neighbors_tab = list(self.neighbors(node))

        for d in neighbors_tab:
            del self._adj[d][node]

        del self._adj[node]


    def remove_edge(self, u: Node, v: Node) -> None:
        if not self.has_node(v)  or not self.has_node(u):
            raise KeyError(f"Both nodes must already exist.{u, v}")
        
        if not self.has_edge(u, v):
            raise KeyError((u, v))

        del self._adj[u][v]
        if v == u:
            return None
        else:
            del self._adj[v][u]

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
        seen_edges = set()
        for u in self._adj:
            for v, weight in self._adj[u].items():
                edge_pair = frozenset([u, v])
                if edge_pair not in seen_edges:
                    seen_edges.add(edge_pair)
                    yield (u, v, weight)


    def edge_weight(self, u: Node, v: Node):
        if not self.has_node(v)  or not self.has_node(u):
            raise KeyError((u, v)) 
        
        if not self.has_edge(u, v):
            raise KeyError((u, v))

        return self._adj[u][v]

from grader_helpers import assert_equal, assert_true, assert_false
if __name__ == "__main__":

    g = AdjacencyListGraph()
    for v in ["A", "B", "C"]:
        g.add_node(v)

    g.add_edge("A", "B")
    g.add_edge("B", "C")

    g.remove_edge("A", "B")

    assert_false(g.has_edge("A", "B"))
    assert_false(g.has_edge("B", "A"))
    assert_true(g.has_edge("B", "C"))

    print("OK")

    g = AdjacencyListGraph()
    for v in ["A", "B", "C", "D"]:
        g.add_node(v)

    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("B", "D")

    g.remove_node("B")

    assert_false(g.has_node("B"))
    assert_false(g.has_edge("A", "B"))
    assert_false(g.has_edge("C", "B"))
    assert_false(g.has_edge("D", "B"))
    assert_equal(set(g.nodes()), {"A", "C", "D"})

    print("OK")

