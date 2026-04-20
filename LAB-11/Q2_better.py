def solve_send_more_money():
    variables = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    all_solutions = [] # List to store all valid assignments
    
    def is_consistent(var, value, assignment):
        if value in assignment.values():
            return False
        if var in ['S', 'M'] and value == 0:
            return False
        return True

    def backtrack(assignment):
        # Base case: all variables are assigned
        if len(assignment) == len(variables):
            s, e, n, d = [assignment[k] for k in ('S', 'E', 'N', 'D')]
            m, o, r, y = [assignment[k] for k in ('M', 'O', 'R', 'Y')]
            
            send = (s * 1000) + (e * 100) + (n * 10) + d
            more = (m * 1000) + (o * 100) + (r * 10) + e
            money = (m * 10000) + (o * 1000) + (n * 100) + (e * 10) + y
            
            # If the equation holds, save a copy of the solution
            if send + more == money:
                all_solutions.append(assignment.copy())
            return
            
        current_var = variables[len(assignment)]
        
        for value in range(10):
            if is_consistent(current_var, value, assignment):
                assignment[current_var] = value
                
                # Continue exploring this branch
                backtrack(assignment) 
                
                # Backtrack: remove the assignment and try the next value
                del assignment[current_var]

    # Start the backtracking with an empty assignment
    backtrack({})
    return all_solutions

if __name__ == '__main__':
    solutions = solve_send_more_money()
    
    print(f"Total solutions found: {len(solutions)}\n")
    
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        print(f"  {solution['S']} {solution['E']} {solution['N']} {solution['D']}")
        print(f"+ {solution['M']} {solution['O']} {solution['R']} {solution['E']}")
        print("-" * 9)
        print(f"{solution['M']} {solution['O']} {solution['N']} {solution['E']} {solution['Y']}\n")