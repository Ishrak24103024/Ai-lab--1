link_map = {
    'A': ['B', 'D'],    
    'B': ['A', 'C', 'D'], 
    'C': ['B'],          
    'D': ['A', 'B', 'E'], 
    'E': ['D', 'F', 'G'], 
    'F': ['E', 'G'],      
    'G': ['E', 'F'] 
}

def limited_search(node, target, max_d, current_d, log):
    if node == target:
        return True
    
    if current_d == max_d:
        return False
        
    log.append(node)
    for next_one in link_map[node]:
        if next_one not in log:
            if limited_search(next_one, target, max_d, current_d + 1, log):
                return True
    return False

def run_iddfs(start, goal):
    level = 0
    while level <= 10:
        print("Checking level:", level)
        history = []
        if limited_search(start, goal, level, 0, history):
            print("Goal found at level:", level)
            break
        level = level + 1

run_iddfs('A', 'G')
