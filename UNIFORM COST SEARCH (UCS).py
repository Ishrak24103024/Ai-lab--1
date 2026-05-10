map_data = {
    'A': [('B', 4), ('D', 1)],     
    'B': [('A', 4), ('C', 4), ('D', 5)],
    'C': [('B', 2)],
    'D': [('A', 1), ('B', 5), ('E', 8)], 
    'E': [('D', 8), ('F', 2), ('G', 6)], 
    'F': [('E', 2), ('G', 1)],  
    'G': [('E', 6), ('F', 1)]
}

def start_ucs(begin, target):
    pending = [[0, begin, [begin]]]
    seen_costs = {}
    
    print("UCS search starting...")
    while pending:
        low_index = 0
        for i in range(1, len(pending)):
            if pending[i][0] < pending[low_index][0]:
                low_index = i
                
        price, node, steps = pending.pop(low_index)
        
        if node == target:
            print("Path found!")
            print("Steps:", steps)
            print("Cost:", price)
            return
        
        if node in seen_costs and seen_costs[node] < price:
            continue
            
        seen_costs[node] = price
        for neighbor, move_cost in map_data.get(node, []):
            total_price = price + move_cost
            new_steps = steps + [neighbor]
            pending.append([total_price, neighbor, new_steps])

start_ucs('A', 'C')
