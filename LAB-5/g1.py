# Lab 5: River Crossing Problem
# 3 Boys, 3 Girls, 1 Boat
# Constraint: Girls never outnumbered by boys on either side

initial_state = [3, 3, 1] # 3 girls, 3 boys, boat on left (1)
goal_state = [0, 0, 0]
ids_limit=0

# Counters
dls_explored = 0
ids_explored = 0

def is_valid(state):
    g = state[0]    #NO. OF GIRLS
    b = state[1]    #NO. OF BOYS
    
    # checking bounds
    if g < 0 or g > 3 or b < 0 or b > 3:
        return False
        
    #checkoing constraints
    #left side
    if g > 0 and b > g:
        return False
    #the condition for failure given in question
    
    #right side
    g_right = 3 - g
    b_right = 3 - b
    if g_right > 0 and b_right > g_right:
        return False
    #the condition for failure given in question
    
    #no.of boys should not outnumber no. of girls on a side
        
    return True

def get_successors(state):
    successors = []
    g = state[0]
    b = state[1]
    boat = state[2]
    
    # Possible moves: (g, b)
    moves = [[1, 0], [2, 0], [0, 1], [0, 2], [1, 1]]
    
    #i have defined status of boat as
    #1 means boat is at left, so it moves from left to right
    if boat == 1:
        for m in moves:
            new_state = [g - m[0], b - m[1], 0]
            if is_valid(new_state):
                successors.append(new_state)
    else: # right to left
        for m in moves:
            new_state = [g + m[0], b + m[1], 1]
            if is_valid(new_state):
                successors.append(new_state)
                
    return successors

# Depth Limited Search
def dls(current_state, depth, limit, path):
    global dls_explored
    dls_explored += 1
    
    if current_state == goal_state:
        return path
        
    if depth >= limit:
        return None
        
    for succ in get_successors(current_state):
        if succ not in path:
            res = dls(succ, depth + 1, limit, path + [succ])
            if res is not None:
                return res
    return None

# Iterative Deepening Search
def dls_for_ids(current_state, depth, limit, path):
    global ids_explored
    ids_explored += 1
    
    if current_state == goal_state:
        return path
        
    if depth >= limit:
        return None
        
    for succ in get_successors(current_state):
        if succ not in path:
            res = dls_for_ids(succ, depth + 1, limit, path + [succ])
            if res is not None:
                return res
    return None

def ids():
    global ids_limit
    limit = 0
    while True:
        # print("Trying limit:", limit)
        res = dls_for_ids(initial_state, 0, limit, [initial_state])
        if res is not None:
            ids_limit=limit
            return res
        limit += 1
        if limit > 20: # Safety break
            return None

print("1. Implement and solve the problem optimally")
print("------------------------------------------")

print("a) Depth Limited Search (limit=3)")
path_dls = dls(initial_state, 0, 3, [initial_state])
if path_dls:
    print("Solution Found:")
    for p in path_dls:
        print(p)
else:
    
    print("No solution found within depth limit 3")

print("\n------------------------------------------")
print("b) Iterative Deepening Search")
path_ids = ids()
if path_ids:
    print("Solution Found:")
    print("Steps:", len(path_ids) - 1)
    for p in path_ids:
        print(p)
else:
    print("No solution found")



total_successors = 0
total_states = 0

# All possible states (g, b, boat)
for g in range(4):
    for b in range(4):
        for boat in [0, 1]:
            state = [g, b, boat]
            if is_valid(state):
                total_states += 1
                total_successors += len(get_successors(state))


branching_factor = total_successors / total_states
print("branching factor = average amount of child nodes per parent node=", branching_factor)


print("\n2. Comparison")
print("-------------")
print("Algorithm                | Explored States | Approx Time Complexity")
print("-------------------------|-----------------|-----------------------")
print("Depth Limited Search (3) | " + str(dls_explored) + "               | O(",branching_factor,"^ 3)")
print("Iterative Deepening      | " + str(ids_explored) + "              | O(", branching_factor,"^", ids_limit,")")

print("\nAnalysis:")
print("DLS with limit 3 explores very few states because the solution requires more steps (minimum 11 moves).")
print("IDS explores many more states because it re-generates the tree for each depth limit iteration.")
print("However, IDS guarantees finding the optimal (shortest) solution.")