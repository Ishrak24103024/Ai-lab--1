map_data = {
    'A': [('B', 4), ('D', 2)],
    'B': [('A', 4), ('C', 3), ('D', 5)],
    'C': [('B', 3)],
    'D': [('A', 2), ('B', 5), ('E', 6)],
    'E': [('D', 6), ('F', 2), ('G', 8)],
    'F': [('E', 2), ('G', 3)],
    'G': []
}

scores = {
    'A': 6,
    'B': 5,
    'C': 7,
    'D': 3,
    'E': 1,
    'F': 1,
    'G': 0
}

def run_astar(start, goal):
    open_list = [[scores[start], 0, start, [start]]]
    closed_list = {}
    
    while open_list:
        best_idx = 0
        for i in range(1, len(open_list)):
            if open_list[i][0] < open_list[best_idx][0]:
                best_idx = i
                
        f, g, node, path = open_list.pop(best_idx)
        
        if node == goal:
            print("A* Path:", " >> ".join(path))
            print("Total Cost:", g)
            return
        
        closed_list[node] = g
        
        for buddy, edge in map_data.get(node, []):
            new_g = g + edge
            
            if buddy in closed_list and closed_list[buddy] <= new_g:
                continue
            
            new_f = new_g + scores[buddy]
            open_list.append([new_f, new_g, buddy, path + [buddy]])

run_astar('A', 'G')
