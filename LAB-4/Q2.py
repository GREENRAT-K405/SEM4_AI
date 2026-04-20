#NON HEU. BEFS

def best_first_no_heuristic(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

# [cost,node,path]
    open_list = []     
    reached = []

    open_list.append([0, start, [start]])
    reached.append(start)

    explored = 0

    while len(open_list) > 0:

        # choose lowest cost node
        open_list.sort()
        cost, current, path = open_list.pop(0)
        explored += 1

        if current == goal:
            return path, explored

        r, c = current

        moves = [[0,1],[1,0],[0,-1],[-1,0]]

        for m in moves:
            nr = r + m[0]
            nc = c + m[1]

            if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                if grid[nr][nc] == 0:

                    nxt = (nr, nc)

                    if nxt not in reached:
                        reached.append(nxt)
                        open_list.append(
                            [cost + 1, nxt, path + [nxt]]
                        )

    return None, explored


#making the map
building = [
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,1,0,0,0,0,1],
[1,0,1,0,1,0,1,1,0,1],
[1,0,1,0,0,0,0,1,0,1],
[1,0,1,1,1,1,0,1,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
]
#1 is for the wall
#0 if for path

start = (1,1)
exit = (5,8)

path, explored = best_first_no_heuristic(building, start, exit)

print("Evacuation Path:", path)
print("Nodes Explored:", explored)