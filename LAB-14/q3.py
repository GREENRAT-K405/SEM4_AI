def negate(literal):
    return literal[1:] if literal.startswith('~') else '~' + literal

def resolve(clause1, clause2):
    resolvents = set()
    for l1 in clause1:
        for l2 in clause2:
            if l1 == negate(l2):
                new_clause = (clause1 - {l1}) | (clause2 - {l2})
                if not any(negate(lit) in new_clause for lit in new_clause):
                    resolvents.add(frozenset(new_clause))
    return resolvents

def pl_resolution(kb_clauses, query):
    negated_query = frozenset([negate(query)])
    clauses = set(kb_clauses)
    clauses.add(negated_query)
    
    print(f"Initial Clauses (KB + Negated Query):")
    for c in clauses: print(f"  {set(c)}")
    print("-" * 30)

    new_clauses = set()
    
    while True:
        n = len(clauses)
        clauses_list = list(clauses)
        
        for i in range(n):
            for j in range(i + 1, n):
                resolvents = resolve(clauses_list[i], clauses_list[j])
                
                if frozenset() in resolvents:
                    print(f"[*] Contradiction found! Resolved {set(clauses_list[i])} and {set(clauses_list[j])} -> Empty Clause")
                    return True
                
                new_clauses.update(resolvents)
                
        if new_clauses.issubset(clauses):
            print("[-] No new clauses can be generated. No contradiction exists.")
            return False
            
        clauses.update(new_clauses)


print("=== SOLVING PROBLEM A ===")
kb_a = [
    frozenset(['P', 'Q']),
    frozenset(['~P', 'R']),
    frozenset(['~Q', 'S']),
    frozenset(['~R', 'S'])
]
query_a = 'S'

result_a = pl_resolution(kb_a, query_a)
print(f"Final Conclusion for A: The query '{query_a}' is {'PROVEN' if result_a else 'NOT PROVEN'}.\n")


print("=== SOLVING PROBLEM B ===")
kb_b = [
    frozenset(['~P', 'Q']),
    frozenset(['~Q', 'R']),
    frozenset(['~S', '~R']),
    frozenset(['P'])
]
query_b = 'S'

result_b = pl_resolution(kb_b, query_b)
print(f"Final Conclusion for B: The query '{query_b}' is {'PROVEN' if result_b else 'NOT PROVEN'}.")