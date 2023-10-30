from collections import deque

# Define the initial and goal states
initial_state = (3, 3, 1)  # (missionaries on the left, cannibals on the left, boat position)
goal_state = (0, 0, 0)

# Define valid actions for moving people
def valid_actions(state):
    m, c, boat = state
    actions = []

    if boat == 1:  # Boat is on the left side
        for m_delta in range(3):
            for c_delta in range(3):
                if 1 <= m_delta + c_delta <= 2 and m - m_delta >= 0 and c - c_delta >= 0:
                    actions.append((m - m_delta, c - c_delta, 0))
    else:  # Boat is on the right side
        for m_delta in range(3):
            for c_delta in range(3):
                if 1 <= m_delta + c_delta <= 2 and 3 - m + m_delta >= 0 and 3 - c + c_delta >= 0:
                    actions.append((m + m_delta, c + c_delta, 1))

    return actions

# Perform a breadth-first search to find a solution
def solve_missionaries_and_cannibals(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        if current_state == goal_state:
            return path + [current_state]

        for action in valid_actions(current_state):
            if action not in visited:
                queue.append((action, path + [current_state]))

    return None

solution = solve_missionaries_and_cannibals(initial_state, goal_state)

if solution:
    for state in solution:
        m, c, boat = state
        print(f"Missionaries on the left: {m}, Cannibals on the left: {c}, Boat position: {'Left' if boat == 1 else 'Right'}")
else:
    print("No solution found.")
