import random

# Function to calculate the number of attacking pairs (each attacking pair adds +1)
def evaluate(board):
    attacking_pairs = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

# Generate a random initial board: each column has a queen in a random row
def random_board():
    return [random.randint(0, 7) for _ in range(8)]

# Hill Climbing algorithm
def hill_climbing():
    current = random_board()
    while True:
        neighbors = []
        current_cost = evaluate(current)

        # Generate all neighbors by moving each queen to all other rows in its column
        for col in range(8):
            for row in range(8):
                if current[col] != row:
                    neighbor = current.copy()
                    neighbor[col] = row
                    neighbors.append(neighbor)

        # Find the best neighbor with the least number of attacks
        best_neighbor = min(neighbors, key=evaluate)
        best_cost = evaluate(best_neighbor)

        # If no better neighbor is found, we stop (we reached a local minimum)
        if best_cost >= current_cost:
            break

        current = best_neighbor
    return current, evaluate(current)

# Function to print the board visually
def print_board(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if board[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print("Number of attacks:", evaluate(board))

# Running Hill Climbing
result, cost = hill_climbing()
print(" Result using Hill Climbing:")
print_board(result)

import math

# Generate a random initial board (same as in Hill Climbing)
def random_board():
    return [random.randint(0, 7) for _ in range(8)]

# Generate a random successor by moving only one queen
def random_successor(board):
    new_board = board.copy()
    col = random.randint(0, 7)
    row = random.randint(0, 7)
    while new_board[col] == row:
        row = random.randint(0, 7)
    new_board[col] = row
    return new_board

# Simulated Annealing algorithm
def simulated_annealing():
    current = random_board()
    T = 1.0          # Initial temperature
    T_min = 1e-10    # Minimum temperature (end of cooling)
    alpha = 0.99     # Rate of temperature decay

    while T > T_min:
        next_state = random_successor(current)
        delta_e = evaluate(current) - evaluate(next_state)

        # If the new state is better → take it directly
        if delta_e > 0:
            current = next_state
        else:
            # Probability of accepting the worse state based on temperature
            probability = math.exp(delta_e / T)
            if random.uniform(0, 1) < probability:
                current = next_state

        T *= alpha  # Gradually decrease the temperature

    return current, evaluate(current)

# Running Simulated Annealing
result_sa, cost_sa = simulated_annealing()
print("\nResult using Simulated Annealing:")
print_board(result_sa)
