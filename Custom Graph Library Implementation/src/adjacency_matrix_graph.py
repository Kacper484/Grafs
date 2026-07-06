from base_graph import BaseGraph, Node, Edge


_NO_EDGE = object()


class AdjacencyMatrixGraph(BaseGraph):
    def __init__(self, *, allow_loops: bool = False) -> None:
        super().__init__(is_directed=False, allow_loops=allow_loops)
        self._nodes = []
        self._index = {}
        self._matrix = []

    def add_node(self, node: Node) -> None:
        if node in self._index:
            return

        self._index[node] = len(self._nodes)
        self._nodes.append(node)

        for row in self._matrix:
            row.append(_NO_EDGE)

        self._matrix.append([_NO_EDGE] * len(self._nodes))

    def add_edge(self, u: Node, v: Node, weight: float | None = None) -> None:
        # 1. Sprawdź istnienie obu wierzchołków.
        # 2. Obsłuż pętle zgodnie z allow_loops.
        # 3. Wyznacz indeksy i, j.
        # 4. Zapisz wagę symetrycznie w macierzy.
        if not self.has_node(u):
            raise KeyError(u)
        if not self.has_node(v):
            raise KeyError(v)
        if u == v and not self._allow_loops:
            raise ValueError
        
        i = self._index[u]
        j = self._index[v]

        self._matrix[i][j] = weight
        self._matrix[j][i] = weight


    def remove_node(self, node: Node) -> None:
        # 1. Sprawdź, czy node istnieje.
        # 2. Usuń odpowiedni element z _nodes.
        # 3. Usuń wiersz i kolumnę z macierzy.
        # 4. Przebuduj _index.
        if not self.has_node(node):
            raise KeyError(node)
            
        idx = self._index[node]
        
        self._nodes.pop(idx)
        
        self._matrix.pop(idx)
        
        for row in self._matrix:
            row.pop(idx)
            
        self._index.clear()
        for i, n in enumerate(self._nodes):
            self._index[n] = i

    def remove_edge(self, u: Node, v: Node) -> None:
        # Ustaw oba pola macierzy na _NO_EDGE.
        if not self.has_node(u):
            raise KeyError(u)
        if not self.has_node(v): 
            raise KeyError(v)
        if not self.has_edge(u, v):
            raise KeyError((u, v))
        
        i = self._index[u]
        j = self._index[v]
        
        self._matrix[i][j] = _NO_EDGE
        self._matrix[j][i] = _NO_EDGE

    def has_node(self, node: Node) -> bool:
        return node in self._index

    def has_edge(self, u: Node, v: Node) -> bool:
        # Krawędź istnieje wtedy i tylko wtedy,
        # gdy komórka macierzy nie jest _NO_EDGE.
        if not self.has_node(u) or not self.has_node(v):
            return False
            
        i = self._index[u]
        j = self._index[v]
        
        return self._matrix[i][j] is not _NO_EDGE

    def neighbors(self, node: Node):
        # Zwróć te wierzchołki, których komórki w wierszu
        # nie są równe _NO_EDGE.

        if not self.has_node(node): 
            raise KeyError(node)
            
        i = self._index[node]
        row = self._matrix[i]
    
        return tuple(self._nodes[j] for j, weight in enumerate(row) if weight is not _NO_EDGE)

    def nodes(self):
        return tuple(self._nodes)

    def edges(self):
        # Ponieważ graf jest nieskierowany, każdą krawędź
        # zwracaj tylko raz.
        for i in range(len(self._nodes)):
            for j in range(i, len(self._nodes)):
                weight = self._matrix[i][j]
                if weight is not _NO_EDGE:
                    yield (self._nodes[i], self._nodes[j], weight)

    def edge_weight(self, u: Node, v: Node):
        # Jeśli krawędź nie istnieje, zgłoś KeyError.
        # W przeciwnym razie zwróć wagę, nawet jeśli jest nią None.
        if not self.has_node(u): raise KeyError(u)
        if not self.has_node(v): raise KeyError(v)
        if not self.has_edge(u, v): raise KeyError((u, v))
        
        i = self._index[u]
        j = self._index[v]
        return self._matrix[i][j]
