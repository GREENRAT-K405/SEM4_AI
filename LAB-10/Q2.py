# Erratic Vacuum Cleaning Agent - AND-OR Graph Search

ACTIONS = ['Suck', 'Right', 'Left']


# -------------------------------------------------------
# Goal Test
# -------------------------------------------------------
def is_goal(state):
    loc, a, b = state
    return a == 'Clean' and b == 'Clean'


# -------------------------------------------------------
# Erratic Vacuum Transition Model
# -------------------------------------------------------
def results(state, action):

    loc, a, b = state

    if action == 'Right':
        return {('B', a, b)}

    if action == 'Left':
        return {('A', a, b)}

    if action == 'Suck':

        outcomes = set()

        if loc == 'A':

            if a == 'Dirty':
                outcomes.add(('A', 'Clean', b))
                outcomes.add(('A', 'Clean', 'Clean'))

            else:
                outcomes.add(('A', 'Clean', b))
                outcomes.add(('A', 'Dirty', b))

        else:  # loc == B

            if b == 'Dirty':
                outcomes.add(('B', a, 'Clean'))
                outcomes.add(('B', 'Clean', 'Clean'))

            else:
                outcomes.add(('B', a, 'Clean'))
                outcomes.add(('B', a, 'Dirty'))

        return outcomes


def or_search(state, visited):

    if is_goal(state):
        return 'Goal'

    if state in visited:
        return 'failure'

    visited = visited | {state}

    for action in ACTIONS:

        outcome_states = results(state, action)

        plan = and_search(outcome_states, visited)

        if plan != 'failure':
            return {'action': action, 'branches': plan}

    return 'failure'



def and_search(states, visited):

    plans = {}

    for s in states:

        plan = or_search(s, visited)

        if plan == 'failure':
            return 'failure'

        plans[s] = plan

    return plans


def print_plan(plan, state=None, indent=0):

    space = "  " * indent

    if plan == 'Goal':
        print(space + "[GOAL STATE]")
        return

    if plan == 'failure':
        print(space + "[FAILURE]")
        return

    action = plan['action']
    branches = plan['branches']

    # OR node
    if state:
        print(space + f"OR NODE: {state}")

    print(space + f"  Action -> {action}")

    # AND node
    print(space + "  AND NODE outcomes:")

    for outcome, subplan in branches.items():

        print(space + f"    -> {outcome}")

        print_plan(subplan, outcome, indent + 2)



locations = ['A', 'B']
tile_states = ['Clean', 'Dirty']

all_states = [(loc, a, b)
              for loc in locations
              for a in tile_states
              for b in tile_states]


print("=" * 60)
print(" ERRATIC VACUUM AGENT - AND OR GRAPH SEARCH")
print("=" * 60)


# Summary Table
results_table = []

for init in all_states:

    plan = or_search(init, frozenset())

    results_table.append((init, plan))


print(f"\n{'Initial State':<35} {'Plan Found?':>12}")
print("-" * 49)

for init, plan in results_table:

    loc, a, b = init

    label = f"Loc={loc}, A={a}, B={b}"

    found = "YES" if plan != 'failure' else "NO"

    print(f"{label:<35} {found:>12}")


print("\n" + "=" * 60)
print(" DETAILED CONDITIONAL PLANS")
print("=" * 60)

for init, plan in results_table:

    loc, a, b = init

    print(f"\n[Start] Location={loc}  A={a}  B={b}")
    print("-" * 40)

    print_plan(plan, init)