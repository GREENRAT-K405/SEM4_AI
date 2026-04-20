class Symbol:
    def __init__(self, name):
        self.name = name
        self.value = False

def NOT(p):
    return not p

def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def IMPLIES(p, q):
    return (not p) or q

def BICONDITIONAL(p, q):
    return p == q

def truth_table(vars, func, name):
    print("\n", name)
    for v in vars:
        print(v.name, end=" ")
    print("| Result")

    n = len(vars)
    for i in range(2 ** n):
        values = []
        for j in range(n):
            val = (i >> (n - j - 1)) & 1
            vars[j].value = bool(val)
            values.append(vars[j].value)

        for v in vars:
            print("T" if v.value else "F", end=" ")
        print("|", "T" if func(*values) else "F")

P = Symbol('P')
Q = Symbol('Q')
R = Symbol('R')

truth_table([P, Q], lambda p,q: IMPLIES(NOT(p), q), "1. ~P -> Q")

truth_table([P, Q], lambda p,q: AND(NOT(p), NOT(q)), "2. ~P ^ ~Q")

truth_table([P, Q], lambda p,q: OR(NOT(p), NOT(q)), "3. ~P v ~Q")

truth_table([P, Q], lambda p,q: IMPLIES(NOT(p), q), "4. ~P -> Q")

truth_table([P, Q], lambda p,q: BICONDITIONAL(NOT(p), q), "5. ~P <-> Q")

truth_table([P, Q], lambda p,q: AND(OR(p,q), IMPLIES(NOT(p),q)), "6. (P v Q) ^ (~P -> Q)")

truth_table([P, Q, R], lambda p,q,r: IMPLIES(OR(p,q), r), "7. (P v Q) -> R")

truth_table([P, Q, R], lambda p,q,r: BICONDITIONAL(IMPLIES(OR(p,q),r), IMPLIES(AND(p,q),r)),
"8. ((P v Q)->R) <-> ((P ^ Q)->R)")

truth_table([P, Q, R], lambda p,q,r: IMPLIES(AND(OR(p,q), IMPLIES(q,r)), IMPLIES(q,r)),
"9. ((P v Q) ^ (Q->R)) -> (Q->R)")

truth_table([P, Q, R], lambda p,q,r: IMPLIES(IMPLIES(p, OR(q,r)), AND(NOT(p), AND(NOT(q), NOT(r)))),
"10. ((P->(Q v R)) -> (~P ^ ~Q ^ ~R))")