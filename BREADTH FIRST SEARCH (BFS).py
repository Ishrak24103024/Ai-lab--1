ink_map = {
    'A': ['B', 'D'],    
    'B': ['A', 'C', 'D'], 
    'C': ['B'],          
    'D': ['A', 'B', 'E'], 
    'E': ['D', 'F', 'G'], 
    'F': ['E', 'G'],      
    'G': ['E', 'F']
}
def simple_bfs(start_point):
    done = []
    waiting = [start_point]
    done.append(start_point)
    
    while waiting:
        current = waiting.pop(0)
        print("At:", current)
        
        for buddy in link_map[current]:
            if buddy not in done:
                done.append(buddy)
                waiting.append(buddy)
    print("BFS Result:", done)

simple_bfs('A')
