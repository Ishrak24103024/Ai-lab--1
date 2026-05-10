def solve_ab(d, pos, my_go, data, low_limit, high_limit):
    if d == 3:
        return data[pos]

    if my_go == True:
        best_v = -1000
        for i in range(2):
            move = pos * 2 + i
            res = solve_ab(d + 1, move, False, data, low_limit, high_limit)
            
            if res > best_v:
                best_v = res
            if best_v > low_limit:
                low_limit = best_v
            if high_limit <= low_limit:
                print("Skipping branch at depth", d)
                break
        return best_v

    else:
        best_v = 1000
        for i in range(2):
            move = pos * 2 + i
            res = solve_ab(d + 1, move, True, data, low_limit, high_limit)
            
            if res < best_v:
                best_v = res
            if best_v < high_limit:
                high_limit = best_v
            if high_limit <= low_limit:
                print("Skipping branch at depth", d)
                break
        return best_v

game_points = [3, 5, 6, 9, 1, 2, 0, -1]
print("Alpha-Beta Result:", solve_ab(0, 0, True, game_points, -1000, 1000))
