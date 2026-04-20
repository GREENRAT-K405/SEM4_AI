import random
import matplotlib.pyplot as plt

def calc(arr):
    h = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if arr[i] == arr[j]:        #for same row
                h = h + 1
            elif abs(arr[i] - arr[j]) == abs(i - j):      #for same diagonal
                h = h + 1
    return h

def get_nxt(b): #input is state of the board configuration
    min_h = calc(b)     # minimum heuristic
    best = list(b)      # best board state
    
    for i in range(8):  #each queen
        for j in range(8):  #movement in row
            if b[i] != j:
                temp = list(b)
                temp[i] = j
                th = calc(temp)     #total heuristic
                if th < min_h:
                    min_h = th
                    best = list(temp)
    return best, min_h

def run_hc(b):
    cur = b
    h1 = calc(cur)
    count = 0
    
    while 1:
        next_board, next_heuristic = get_nxt(cur)
        if next_heuristic >= h1:
            break
        cur = next_board
        h1 = next_heuristic
        count = count + 1
        
    return cur, h1, count

def show_b(arr):
    fig, ax = plt.subplots()
    for i in range(9):
        ax.axhline(i - 0.5, color='black', lw=1)
        ax.axvline(i - 0.5, color='black', lw=1)
    
    for c in range(8):
        r = arr[c]
        ax.text(c, r, 'Q', fontsize=20, ha='center', va='center', color='red')
        
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-0.5, 7.5)
    ax.invert_yaxis()
    plt.title("Solved 8 Queens")
    plt.show()

# CHANGED HEADER (added board states)
print("Run\tInit H\tFinal H\tSteps\tStatus\tInitial Board\tFinal Board")

fails = 0
solved = 0

for x in range(50):
    start_b = []
    for k in range(8):
        start_b.append(random.randint(0, 7))
        
    start_val = calc(start_b)
    e, v, s = run_hc(start_b)
    
    stat = "Fail"
    if v == 0:
        stat = "Solved"
        solved = solved + 1
    else:
        fails = fails + 1
        
    # CHANGED PRINT LINE
    print(str(x+1) + "\t" + str(start_val) + "\t" + str(v) + "\t" + str(s) + "\t" + stat + "\t" + str(start_b) + "\t" + str(e))

print("Failed cases prove local minimum.")

# solve it
print("\nSolving with restarts...")
r_c = 0
while 1:
    b2 = []
    for k in range(8):
        b2.append(random.randint(0, 7))
    e2, v2, s2 = run_hc(b2)
    if v2 == 0:
        print("Done")
        print(e2)
        show_b(e2)
        break
    r_c = r_c + 1