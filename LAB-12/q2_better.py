# Sudoku Hard Puzzle AC-3

grid_rows = [
    "000006000",
    "059000008",
    "200008000",
    "045000000",
    "003000000",
    "006003050",
    "000007000",
    "000000000",
    "000050002"
]
s_grid = "".join(grid_rows)

# vars: 0 to 80
# doms
d = {}
for i in range(81):
    val = int(s_grid[i])
    if val == 0:
        d[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        d[i] = [val]

# Neighbors
def get_nbrs(i):
    res = set()
    r = i // 9
    c = i % 9
    
    # Row
    for col in range(9):
        if col != c:
            res.add(r * 9 + col)
    # Col
    for row in range(9):
        if row != r:
            res.add(row * 9 + c)
    # Box
    br = (r // 3) * 3
    bc = (c // 3) * 3
    for row in range(br, br + 3):
        for col in range(bc, bc + 3):
            idx = row * 9 + col
            if idx != i:
                res.add(idx)
    return res

# Arcs
arcs = []
for i in range(81):
    nbrs = get_nbrs(i)
    for n in nbrs:
        arcs.append((i, n))

def revised(xi, xj):
    rem = False
    new_di = []
    for v1 in d[xi]:
        # is there a v2 in d[xj] such that v1 != v2
        ok = False
        for v2 in d[xj]:
            if v1 != v2:
                ok = True
                break
        if ok:
            new_di.append(v1)
        else:
            rem = True
    d[xi] = new_di
    return rem

# AC-3
q = []
for a in arcs:
    q.append(a)

removed = 0
while len(q) > 0:
    xi, xj = q.pop(0)
    old_len = len(d[xi])
    if revised(xi, xj):
        removed += (old_len - len(d[xi]))
        if len(d[xi]) == 0:
            # Silenced the mid-loop print to keep the final output clean
            break
        for xk in get_nbrs(xi):
            if xk != xj:
                q.append((xk, xi))


# ==========================================
# MODIFIED OUTPUT SECTION
# ==========================================

print("\n" + "="*45)
print("AC-3 ALGORITHM RESULTS")
print("="*45)

# Task 1 Output
print("\nTask 1: Arc Generation")
print(f"- Successfully generated {len(arcs)} directed arcs")
print(f"  (This represents exactly {len(arcs)//2} binary constraints).")

# Task 2 Output
print("\nTask 2: State Tracking")
print(f"- Total values removed from all domains: {removed}")

# Task 3 Output
print("\nTask 3: Visualization (Remaining Domain Sizes)")
for r in range(9):
    if r % 3 == 0 and r != 0:
        print("- - - + - - - + - - -")
    row_str = ""
    for c in range(9):
        if c % 3 == 0 and c != 0:
            row_str += "| "
        row_str += str(len(d[r*9 + c])) + " "
    print(row_str.strip())

# Key Question Output
print("\n" + "="*45)
print("ANSWER TO KEY QUESTION:")

if any(len(d[i]) == 0 for i in range(81)):
    print("- Outcome: AC-3 detected a failure (a domain reached zero).")
    print("- Conclusion: The puzzle is mathematically unsolvable.")
elif all(len(d[i]) == 1 for i in range(81)):
    print("- Outcome: AC-3 solved the puzzle completely (all domains = 1).")
    print("- Conclusion: No human guessing or backtracking is required.")
else:
    print("- Outcome: AC-3 reduced the search space but did NOT solve it.")
    print("- Conclusion: No domain reached zero, but some remain > 1. A human or backtracking algorithm is needed to finish.")
print("="*45 + "\n")