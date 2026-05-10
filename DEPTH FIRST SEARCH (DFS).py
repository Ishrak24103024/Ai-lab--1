link_map = {
    'A': ['B', 'D'],    
    'B': ['A', 'C', 'D'], 
    'C': ['B'],          
    'D': ['A', 'B', 'E'], 
    'E': ['D', 'F', 'G'], 
    'F': ['E', 'G'],      
    'G': ['E', 'F']
}


def simple_dfs(node, history):
    history.append(node)
    print("Saw:", node)
    
    for neighbor in link_map[node]:
        if neighbor not in history:
            simple_dfs(neighbor, history)

order = []
simple_dfs('A', order)
