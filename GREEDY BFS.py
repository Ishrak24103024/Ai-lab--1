scores = {'A': 6, 'B': 5, 'C': 7, 'D': 3, 'E': 8, 'F': 9, 'G': 10}

map_data = {
    'A': ['B', 'D'],    
    'B': ['A', 'C', 'D'], 
    'C': ['B'],          
    'D': ['A', 'B', 'E'], 
    'E': ['D', 'F', 'G'], 
    'F': ['E', 'G'],      
    'G': ['E', 'F']
}

def simple_greedy(start, end):
    queue = [[scores[start], start, [start]]]
    done = []
    
    while queue:
        low = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[low][0]:
                low = i
        
        h_val, node, path = queue.pop(low)
        
        if node == end:
            print("Greedy Path:", path)
            return
        
        done.append(node)
        
        for nxt in map_data.get(node, []):
            if nxt not in done:
                queue.append([scores[nxt], nxt, path + [nxt]])

simple_greedy('A', 'E')
