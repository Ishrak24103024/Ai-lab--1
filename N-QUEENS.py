def check_place(grid, r, c):
    for i in range(r):
        if grid[i] == c:
            return False
        
        r_gap = r - i
        if c > grid[i]:
            c_gap = c - grid[i]
        else:
            c_gap = grid[i] - c
            
        if r_gap == c_gap:
            return False
    return True

def find_queens(grid, r, total):
    if r == total:
        print("Solution Found")
        for i in range(total):
            row_text = ""
            for j in range(total):
                if grid[i] == j:
                    row_text += " Q "
                else:
                    row_text += " . "
            print(row_text)
        return True
    
    for c in range(total):
        if check_place(grid, r, c):
            grid[r] = c
            if find_queens(grid, r + 1, total):
                return True
            grid[r] = -1
    return False

find_queens([-1, -1, -1, -1], 0, 4)
