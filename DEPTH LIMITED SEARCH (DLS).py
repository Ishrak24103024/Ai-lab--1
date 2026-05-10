link_map = {
    'A': ['B', 'D'],    
    'B': ['A', 'C', 'D'], 
    'C': ['B'],          
    'D': ['A', 'B', 'E'], 
    'E': ['D', 'F', 'G'], 
    'F': ['E', 'G'],      
    'G': ['E', 'F']
}


def dls_runner(node, cap, depth, history):
    print("Visiting:", node, "at depth", depth)
    
    if depth > cap:
        return
    
    history.append(node)
    for adjacent in link_map[node]:
        if adjacent not in history:
            dls_runner(adjacent, cap, depth + 1, history)

track = []
dls_runner('A', 3, 0, track)
print("Visited List:", track)
