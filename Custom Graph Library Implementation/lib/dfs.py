def dfs(graph, start):
    if not graph.has_node(start):
        raise KeyError(start)
        
    visited = set()
    order = []
    def visit(u):
        visited.add(u)
        order.append(u)
        
        for v in graph.neighbors(u):
            if v not in visited:
                visit(v)
    visit(start)
    
    return tuple(order)