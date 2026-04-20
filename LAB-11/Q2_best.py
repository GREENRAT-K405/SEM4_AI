def solve_send_more_money():
    variables = ['D', 'E', 'Y', 'N', 'R', 'O', 'S', 'M']
    all_solutions = [] 
    
    def is_consistent(var, value, assignment):
        if value in assignment.values():
            return False
        if var in ['S', 'M'] and value == 0:
            return False
        return True

    def backtrack(assignment):
        c1 = c2 = c3 = c4 = 0
        
        # Early pruning via column-by-column carry checks
        if all(k in assignment for k in ('D', 'E', 'Y')):
            if (assignment['D'] + assignment['E']) % 10 != assignment['Y']: return
            c1 = (assignment['D'] + assignment['E']) // 10
            
            if all(k in assignment for k in ('N', 'R')):
                if (assignment['N'] + assignment['R'] + c1) % 10 != assignment['E']: return
                c2 = (assignment['N'] + assignment['R'] + c1) // 10
                
                if 'O' in assignment:
                    if (assignment['E'] + assignment['O'] + c2) % 10 != assignment['N']: return
                    c3 = (assignment['E'] + assignment['O'] + c2) // 10
                    
                    if all(k in assignment for k in ('S', 'M')):
                        if (assignment['S'] + assignment['M'] + c3) % 10 != assignment['O']: return
                        c4 = (assignment['S'] + assignment['M'] + c3) // 10
                        if assignment['M'] != c4: return

        # Base case
        if len(assignment) == len(variables):
            all_solutions.append(assignment.copy())
            return
            
        current_var = variables[len(assignment)]
        
        for value in range(10):
            if is_consistent(current_var, value, assignment):
                assignment[current_var] = value
                backtrack(assignment) 
                del assignment[current_var]

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