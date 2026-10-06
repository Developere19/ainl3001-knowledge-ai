"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Week 4 Tutorial
Introducing the Problem Class

In previous weeks, we represented problems directly using
variables and functions.

From this week onwards, we will use a common Problem class
where appropriate.

This tutorial uses the familiar grid world from earlier weeks
to explore the new structure.
"""

from common.problem import Problem


GRID_SIZE = 5


class GridProblem(Problem):
    """
    A simple grid-world problem.

    A state is represented as an (x, y) coordinate.

    Example:

        (0, 0) = top-left corner
        (4, 4) = bottom-right corner
    """

    def actions(self, state):
        """
        Return the valid actions from this state.

        Possible actions:

            UP
            DOWN
            LEFT
            RIGHT

        Remember: an action must not move outside the grid.
        """

        # TODO:
        #
        # 1. Extract x and y from state.
        # 2. Create an empty list of actions.
        # 3. Check which movements are valid.
        # 4. Add valid actions to the list.
        # 5. Return the list.

        x, y = state

        actions = []

        if y > 0:
            actions.append("UP")

        if y < GRID_SIZE - 1:
            actions.append("DOWN")

        if x > 0:
            actions.append("LEFT")

        if x < GRID_SIZE - 1:
            actions.append("RIGHT")

        return actions

    def result(self, state, action):
        """
        Return the new state produced by performing an action.

        Example:

            state  = (0, 0)
            action = "RIGHT"

            result = (1, 0)
        """

        # TODO:
        #
        # 1. Extract x and y from state.
        # 2. Check which action was requested.
        # 3. Return the resulting state.

        x, y = state

        if action == "UP":
            return (x, y - 1)

        if action == "DOWN":
            return (x, y + 1)

        if action == "LEFT":
            return (x - 1, y)

        if action == "RIGHT":
            return (x + 1, y)


# --------------------------------------------------
# CREATE A PROBLEM
# --------------------------------------------------

problem = GridProblem(
    initial=(0, 0),
    goal=(4, 4)
)


# --------------------------------------------------
# EXPLORE THE PROBLEM
# --------------------------------------------------

print("Initial state:", problem.initial)
print("Goal:", problem.goal)


print("\nActions from (0, 0):")

actions = problem.actions((0, 0))

print(actions)


print("\nResults of those actions:")

if actions is not None:
    for action in actions:

        new_state = problem.result(
            (0, 0),
            action
        )

        print(
            action,
            "->",
            new_state
        )


print("\nIs (4, 4) the goal?")

print(
    problem.goal_test((4, 4))
)

"""

REFLECTION QUESTIONS


Tutorial Reflection Questions

1. What information is stored in problem.initial?
problem.initial stores the starting state of the problem.
In this grid example, the starting state is (0, 0).

2. What information is stored in problem.goal?
problem.goal stores the target state that we are trying to reach.
In this grid example, the goal state is (4, 4).

3. What is the difference between actions(state) and result(state, action)?
actions(state) returns the valid actions that can be taken from the current state.
For example, from (0, 0), the valid actions are DOWN and RIGHT.

result(state, action) returns the new state after performing an action.
For example, result((0, 0), "RIGHT") returns (1, 0).

Easy way to remember:
actions() = What can I do?
result() = Where do I end up?

4. Why does the Problem class not know anything about grids?
Problem is designed to be a general problem representation.
It can be reused for many different AI problems, not just grid problems.
The specific subclass defines what the states and actions mean.

5. Why does GridProblem not know anything about search?
GridProblem only describes the problem itself.
It defines the states, valid actions, and the result of taking an action.
The search algorithm is kept separate and decides how the problem is solved.

6. Could the same Problem structure represent something other than a grid?
Yes.
The same Problem structure can represent many different problems.
For example, the N-Queens problem can also use an initial state,
actions, and result, even though its states and actions are different.
"""