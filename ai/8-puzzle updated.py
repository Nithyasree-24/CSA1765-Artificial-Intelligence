from queue import PriorityQueue

def solve_8_puzzle(initial_state, goal_state):
    pq = PriorityQueue()
    pq.put((0, initial_state, []))
    visited = set()

    while not pq.empty():
        cost, state, path = pq.get()
        if state == goal_state:
            return path
        if state in visited:
            continue
        visited.add(state)

        for next_state, action in get_neighbors(state):
            pq.put((cost + 1, next_state, path + [action]))

    return None

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    if zero_index not in (0, 1, 2):
        neighbors.append((state[:zero_index - 3] + [state[zero_index]] + state[zero_index - 3:zero_index] + state[zero_index + 1:], "Up"))
    if zero_index not in (6, 7, 8):
        neighbors.append((state[:zero_index] + state[zero_index + 3] + state[zero_index + 1:zero_index + 3] + [state[zero_index]] + state[zero_index + 3:], "Down"))
    if zero_index not in (0, 3, 6):
        neighbors.append((state[:zero_index - 1] + [state[zero_index]] + state[zero_index - 1] + state[zero_index + 1:], "Left"))
    if zero_index not in (2, 5, 8):
        neighbors.append((state[:zero_index] + state[zero_index + 1] + [state[zero_index]] + state[zero_index + 2:], "Right"))
    return neighbors

# Example usage
initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

solution = solve_8_puzzle(initial_state, goal_state)
if solution:
    print("Solution found:")
    print(solution)
else:
    print("No solution found.")
