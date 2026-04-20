def pl_fc_entails(rules, known_facts, q):
    # Initialize count table for each rule's premises
    count = {i: len(premise) for i, (premise, conclusion) in enumerate(rules)}
    
    # Gather all unique symbols and track inference status
    symbols = set(known_facts)
    for premise, conclusion in rules:
        symbols.update(premise)
        symbols.add(conclusion)
    inferred = {s: False for s in symbols}
    
    queue = list(known_facts)
    
    print(f"--- Starting PL-FC-ENTAILS? ---\nInitial Queue: {queue}\nTarget: {q}\n")
    
    while queue:
        p = queue.pop(0) 
        
        if p == q:
            print(f"\nSuccess! Found '{q}'.")
            return True
            
        if not inferred.get(p, False):
            inferred[p] = True
            print(f"Processing: {p}")
            
            for i, (premise, conclusion) in enumerate(rules):
                if p in premise:
                    count[i] -= 1 
                    if count[i] == 0:
                        print(f"  -> Rule {i} ({premise} -> {conclusion}) satisfied. Queuing '{conclusion}'.")
                        queue.append(conclusion)
                        
    print(f"\nFailure. '{q}' not entailed.")
    return False

# Problem A
print("=== PROBLEM A ===")
rules_a = [(['P'], 'Q'), (['L', 'M'], 'P'), (['A', 'B'], 'L')]
facts_a = ['A', 'B', 'M']
pl_fc_entails(rules_a, facts_a, 'Q')

print("\n")

# Problem B
print("=== PROBLEM B ===")
rules_b = [(['A'], 'B'), (['B'], 'C'), (['C'], 'D'), (['D', 'E'], 'F')]
facts_b = ['A', 'E']
pl_fc_entails(rules_b, facts_b, 'F')