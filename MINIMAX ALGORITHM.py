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

def play_minimax(d, idx, max_turn, vals):
    if d == 3:
        return vals[idx]

    if max_turn == True:
        high_val = -1000
        L = idx * 2
        R = idx * 2 + 1
        
        v1 = play_minimax(d + 1, L, False, vals)
        v2 = play_minimax(d + 1, R, False, vals)
        
        if v1 > v2:
            high_val = v1
        else:
            high_val = v2
        return high_val

    else:
        low_val = 1000
        L = idx * 2
        R = idx * 2 + 1
        
        v1 = play_minimax(d + 1, L, True, vals)
        v2 = play_minimax(d + 1, R, True, vals)
        
        if v1 < v2:
            low_val = v1
        else:
            low_val = v2
        return low_val

leaf_scores = [3, 5, 2, 9, 12, 5, 23, 23]
print("Best Minimax Score:", play_minimax(0, 0, True, leaf_scores))
