def pl_bc_entails(rules, known_facts, query):
    def prove(q, path):
        indent = "  " * len(path)
        print(f"{indent}[?] Attempting to prove: '{q}'")
        
        if q in known_facts:
            print(f"{indent}[+] Success: '{q}' is a known fact.")
            return True
            
        if q in path:
            print(f"{indent}[-] Failure: Cycle detected for '{q}'.")
            return False
            
        for premises, conclusion in rules:
            if conclusion == q:
                print(f"{indent}[*] Found relevant rule: {premises} -> {conclusion}")
                
                all_premises_proved = True
                for p in premises:
                    if not prove(p, path + [q]):
                        all_premises_proved = False
                        print(f"{indent}[-] Premise '{p}' failed for rule {premises} -> {conclusion}")
                        break 
                        
                if all_premises_proved:
                    print(f"{indent}[+] Success: Proved '{q}' via rule {premises} -> {conclusion}")
                    return True
                    
        print(f"{indent}[-] Failure: Exhausted all options for '{q}'.")
        return False

    print(f"--- Starting PL-BC-ENTAILS? ---\nTarget Query: {query}")
    result = prove(query, [])
    print(f"\nFinal Result: {'SUCCESS' if result else 'FAILURE'}\n")
    return result

# Problem A
print("=== PROBLEM A ===")
rules_a = [(['P'], 'Q'), (['R'], 'Q'), (['A'], 'P'), (['B'], 'R')]
facts_a = ['A', 'B']
pl_bc_entails(rules_a, facts_a, 'Q')

# Problem B
print("=== PROBLEM B ===")
rules_b = [(['A'], 'B'), (['B', 'C'], 'D'), (['E'], 'C')]
facts_b = ['A', 'E']
pl_bc_entails(rules_b, facts_b, 'D')