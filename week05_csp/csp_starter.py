"""
AINL3001 — Knowledge-Driven AI
Week 5 — Constraint Satisfaction Problems
BSP 2026

Australian map colouring: six regions and three colours.

Tasks
-----
0. Examine an invalid assignment.
1. Understand variables, domains and constraints.
2. Implement constraint checking.
3. Implement backtracking with simple variable selection.
4. Compare backtracking with brute force.
5. Improve variable selection using MRV.

Work in this starter file and commit your progress to your own fork.
"""

# --------------------------------------------------
# TASK 0 — MANUAL EXPLORATION
# --------------------------------------------------

example_assignment = {
    "WA": "Red",
    "NT": "Red",
    "SA": "Green",
    "Q": "Blue",
    "NSW": "Red",
    "V": "Green",
}

print("Manual CSP Exploration")
print(example_assignment)

print("\nQuestions:")

print("1. Is this assignment valid?")
print("No. The assignment is invalid because some neighbouring regions have been assigned the same colour.\n")

print("2. Which neighbouring pairs violate a constraint?")
print("WA and NT violate a constraint because they are both Red. SA and V also violate a constraint because they are both Green.\n")

print("3. How could you correct the assignment?")
print("One way to correct the assignment is to change WA to Blue and V to Blue. This makes each neighbouring pair have different colours.\n")


print("4. Why is it useful to detect violations early?")
print("Detecting violations early prevents the search algorithm from continuing with an assignment that cannot lead to a valid solution. This reduces unnecessary searching and makes the process more efficient.\n")

# --------------------------------------------------
# TASK 1 — CSP REPRESENTATION
# --------------------------------------------------

# Each variable is an Australian region.
variables = ["WA", "NT", "SA", "Q", "NSW", "V"]

# Each region may use one of these three colours.
domains = {
    variable: ["Red", "Green", "Blue"]
    for variable in variables
}

# Each pair of neighbouring regions must have different colours.
constraints = [
    ("WA", "NT"),
    ("WA", "SA"),
    ("NT", "SA"),
    ("NT", "Q"),
    ("SA", "Q"),
    ("SA", "NSW"),
    ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V"),
]

# --------------------------------------------------
# TASK 2 — CONSTRAINT CHECKING
# --------------------------------------------------

def is_valid_assignment(assignment):
    """Return True if a complete OR partial assignment is valid."""
    for region1, region2 in constraints:

        # Only checks the constraint if both regions have already been assigned a color.
        if region1 in assignment and region2 in assignment:
            if assignment[region1] == assignment[region2]:
                return False
    return True


# --------------------------------------------------
# TASK 3 AND TASK 5 — VARIABLE SELECTION
# --------------------------------------------------

def select_unassigned_variable(assignment):
    """Choose the next unassigned region.

    Task 3: First return the FIRST unassigned region.

    Task 5: Replace that approach with MRV (Minimum Remaining Values):
    choose the unassigned region with the FEWEST currently legal
    colours. Break ties by keeping the first region in variables.
    """
    # TASK 3 TODO:
    # Return the first variable not in assignment, or None if all
    # variables have been assigned.
    #
    # TASK 5 TODO (after backtracking works):
    # For each unassigned variable, temporarily try each colour,
    # check is_valid_assignment(), and undo the temporary assignment.
    # Count legal colours and choose the variable with the fewest.
    pass


# --------------------------------------------------
# TASK 3 — BACKTRACKING SEARCH
# --------------------------------------------------

def backtracking_search(assignment):
    """Return a complete valid assignment, or None if none exists."""
    # TODO:
    # 1. If every variable has been assigned, return a COPY.
    # 2. Choose a variable with select_unassigned_variable().
    # 3. For each colour in its domain, temporarily assign it.
    # 4. If the partial assignment is valid, search recursively.
    # 5. Return the recursive result if a solution was found.
    # 6. Otherwise remove the temporary assignment (backtrack).
    # 7. Return None if every colour fails.
    pass


# --------------------------------------------------
# TASK 4 — BRUTE FORCE COMPARISON
# --------------------------------------------------

# Six regions with three possible colours each give 3 ** 6 = 729
# complete assignments. Why can backtracking avoid checking all 729?


# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("WEEK 5 — CONSTRAINT SATISFACTION PROBLEMS")
    print("=" * 50)

    print("\nVariables:", variables)
    print("Domains:", domains)
    print("Constraints:", constraints)

    print("\nExample assignment valid?")
    print(is_valid_assignment(example_assignment))  # Expected: False

    partial_assignment = {"WA": "Red", "NT": "Green"}
    print("\nPartial assignment valid?")
    print(is_valid_assignment(partial_assignment))  # Expected: True

    print("\nSearching for a solution...")
    solution = backtracking_search({})
    print("Solution:", solution)

    if solution is not None:
        print("\nSolution valid?", is_valid_assignment(solution))
        print("\nColour assignment:")
        for region in variables:
            print(f"{region:4} -> {solution[region]}")
    else:
        print("No solution yet. Complete the TODO sections.")

    print("\nPossible complete assignments:", 3 ** len(variables))
    print("\nReflection:")
    print("1. What causes backtracking?")
    print("2. Why can backtracking be faster than brute force?")
    print("3. Why might MRV reduce search?")
    print("4. How could this model represent timetabling?")