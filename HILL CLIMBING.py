mountain_map = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'E'],
    'D': ['A', 'B', 'E'],
    'E': ['C', 'D', 'F', 'G'],
    'F': ['E', 'G'],
    'G': ['E', 'F']
}
scores = {'A': 6, 'B': 5, 'C': 7, 'D': 3, 'E': 8, 'F': 9, 'G': 10}

def climb(start_node):
    now = start_node
    val_now = scores[start_node]
    route = [start_node]
    
    while True:
        options = mountain_map.get(now, [])
        top_neighbor = None
        top_val = val_now
        
        for n in options:
            if scores[n] > top_val:
                top_val = scores[n]
                top_neighbor = n
        
        if top_neighbor is None:
            print("Peak reached at", now)
            break
        else:
            now = top_neighbor
            val_now = top_val
            route.append(now)
    print("Final Route:", route)

climb('B')
