# Teams and rooms
tList = ["P1", "P2", "P3", "P4", "P5", "P6"]
rooms = ["R1", "R2", "R3"]

# Conflicts
conf = {
    "P1": ["P2", "P3", "P6"],
    "P2": ["P1", "P3", "P4"],
    "P3": ["P1", "P2", "P5"],
    "P4": ["P2", "P6"],
    "P5": ["P3", "P6"],
    "P6": ["P1", "P4", "P5"]
}

# Generate arcs
arcs = []
for t1 in tList:
    for t2 in conf[t1]:
        arcs.append((t1, t2))

# Run AC-3 logic
def revised(x, y, d):
    rem = False
    new_d = []
    for v1 in d[x]:
        exists = False
        for v2 in d[y]:
            if v1 != v2:
                exists = True
                break
        if exists:
            new_d.append(v1)
        else:
            rem = True
    d[x] = new_d
    return rem

def run_ac3(d, a_list):
    q = []
    for item in a_list:
        q.append(item)
    
    step_count = 1
    while len(q) > 0:
        x, y = q.pop(0)
        
        # Save the old domain before checking, so we can show the before/after
        old_domain = list(d[x])
        
        if revised(x, y, d):
            # --- THIS IS THE NEW TRACE SECTION ---
            print(f"\n[Check #{step_count}] REDUCTION TRIGGERED on Arc ({x}, {y})")
            print(f"  -> Because of {y}'s limitations, {x} loses a room!")
            print(f"  -> {x}'s domain changed: {old_domain} ---> {d[x]}")
            
            if len(d[x]) == 0:
                print(f"  -> FATAL ERROR: {x} has no valid rooms left. Halting.")
                return False
                
            print(f"  -> Cascade Effect: Re-checking {x}'s neighbors...")
            for nbr in conf[x]:
                if nbr != y:
                    q.append((nbr, x))
                    print(f"     Added Arc ({nbr}, {x}) back to the queue.")
            print("-" * 50)
            # -------------------------------------
            
        step_count += 1
        
    return True


# --- Running the Preemptive Assignment Case ---
print("\n--- Assigning P1 to R1 ---")
doms2 = {}
for t in tList:
    doms2[t] = ["R1", "R2", "R3"]
doms2["P1"] = ["R1"] # Force P1 into R1

print("Starting AC-3 Algorithm...\n")
if run_ac3(doms2, arcs):
    print("\nAC-3 finished successfully. Valid domains remain.")
    print("Final Domains:")
    for t in tList:
        print(f"  {t} : {doms2[t]}")
else:
    print("\nAC-3 detected failure!")