from collections import deque

def bfs(graph, start):
    if not graph.has_node(start):
            raise KeyError(start)
        
    visited = {start}
    order = []
    
    queue = deque([start])
    
    while queue:
        u = queue.popleft()
        order.append(u)
        
        for v in graph.neighbors(u):
            if v not in visited:
                visited.add(v)
                queue.append(v)
                
    return tuple(order)
