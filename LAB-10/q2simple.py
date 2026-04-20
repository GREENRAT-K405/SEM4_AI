# State = (Location, A_state, B_state)

actions = ['Suck', 'Left', 'Right']


def goal(state):
    loc, A, B = state
    return A == 'Clean' and B == 'Clean'


# Erratic vacuum results
def result(state, action):

    loc, A, B = state
    outcomes = []

    if action == 'Right':
        outcomes.append(('B', A, B))

    elif action == 'Left':
        outcomes.append(('A', A, B))

    elif action == 'Suck':

        if loc == 'A':

            if A == 'Dirty':
                outcomes.append(('A','Clean',B))
                outcomes.append(('A','Clean','Clean'))

            else:
                outcomes.append(('A','Clean',B))
                outcomes.append(('A','Dirty',B))

        elif loc == 'B':

            if B == 'Dirty':
                outcomes.append(('B',A,'Clean'))
                outcomes.append(('B','Clean','Clean'))

            else:
                outcomes.append(('B',A,'Clean'))
                outcomes.append(('B',A,'Dirty'))

    return outcomes


# OR search
def OR_search(state, visited):

    if goal(state):
        return "Goal"

    if state in visited:
        return "failure"

    visited = visited | {state}

    for action in actions:

        outcomes = result(state, action)
        plan = AND_search(outcomes, visited)

        if plan != "failure":
            return {'action': action, 'branches': plan}

    return "failure"


# AND search
def AND_search(states, visited):

    plans = {}

    for s in states:

        plan = OR_search(s, visited)

        if plan == "failure":
            return "failure"

        plans[s] = plan

    return plans


# Print plan nicely
def print_plan(plan, indent=0):

    space = "  " * indent

    if plan == "Goal":
        print(space + "GOAL")
        return

    action = plan['action']
    print(space + "DO:", action)

    for outcome, subplan in plan['branches'].items():
        print(space + "IF outcome ->", outcome)
        print_plan(subplan, indent+1)


# Initial state
start = ('A','Dirty','Dirty')

plan = OR_search(start, set())

print("Initial State:", start)
print("\nPLAN:\n")

print_plan(plan)