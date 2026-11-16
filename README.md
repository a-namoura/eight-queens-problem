# Eight Queens Problem — Hill Climbing vs. Simulated Annealing

A Python implementation of the classic **8-Queens Problem** using two local-search techniques: **Hill Climbing** and **Simulated Annealing**. The project explores how different search strategies attempt to arrange eight queens on a chessboard so that no two queens attack each other.

Developed for the **Artificial Intelligence Lab at Al-Quds University** (11th May, 2025).

## Problem Overview

The goal is to place eight queens on an 8 × 8 chessboard such that no two share the same **row, column, or diagonal**.

The program represents each board as a list of eight integers:

```python
board = [3, 6, 0, 7, 4, 1, 5, 2]
```

Each list index is a column, and the value at that index is the queen's row (numbered `0` through `7`). This representation places **exactly one queen in every column**, so the search only needs to resolve row and diagonal conflicts.

The evaluation function, `evaluate(board)`, counts the number of **pairs of attacking queens**. A smaller score is better:

- **0 attacks:** a valid solution.
- **More than 0 attacks:** one or more queens still threaten each other.

## Algorithms

### 1. Hill Climbing

The implementation uses a greedy, best-neighbor approach:

1. Generate a random initial board.
2. Evaluate every neighbor formed by moving one queen to a different row in its column (56 possible neighbors).
3. Move to the neighbor with the lowest attack count **only if it improves** the current score.
4. Stop when no improving move exists.

Hill climbing is straightforward, but it can get stuck in **local minima or plateaus** and return a board with conflicts.

### 2. Simulated Annealing

Simulated annealing uses randomized moves and a cooling schedule:

1. Generate a random initial board.
2. Select a random neighboring board by moving one queen within its column.
3. Always accept an improvement; otherwise, accept the move with a probability based on the score change and current temperature.
4. Gradually lower the temperature and stop after the cooling threshold is reached.

Occasionally accepting non-improving moves allows the search to explore beyond local minima, although it does **not guarantee** a valid solution.

The code uses these settings:

| Parameter | Value | Purpose |
| --- | --- | --- |
| Initial temperature (`T`) | `1.0` | Starting acceptance temperature |
| Cooling factor (`alpha`) | `0.99` | Multiplies the temperature each iteration |
| Minimum temperature (`T_min`) | `1e-10` | Stopping threshold |

For a worse move, the acceptance probability is `exp((current_attacks - next_attacks) / T)`. Moves with an equal score are accepted as well.

## Getting Started

### Requirements

- Python 3

No third-party dependencies are needed. The script uses the standard-library `random` and `math` modules.

### Run the Program

```bash
git clone https://github.com/a-namoura/eight-queens-problem.git
cd eight-queens-problem
python3 8queensProblem.py
```

On Windows, use `python 8queensProblem.py` if `python3` is unavailable.

Both algorithms run automatically, one after the other. The program prints an 8 × 8 board for each result followed by its number of attacking pairs.

## Example Solution

The following board is one valid arrangement of eight queens:

```text
 .  .  Q  .  .  .  .  .
 .  .  .  .  .  Q  .  .
 .  .  .  .  .  .  .  Q
 Q  .  .  .  .  .  .  .
 .  .  .  .  Q  .  .  .
 .  .  .  .  .  .  Q  .
 .  Q  .  .  .  .  .  .
 .  .  .  Q  .  .  .  .

Number of attacks: 0
```

- `Q` represents a queen.
- `.` represents an empty square.
- A score of `0` means no two queens attack one another.

**Results are random:** your boards and attack counts will differ between runs. Neither implementation is guaranteed to reach zero attacks on every attempt. Run the script several times to observe the different outcomes.

## Comparing the Approaches

| Aspect | Hill Climbing | Simulated Annealing |
| --- | --- | --- |
| Next move | Best improving neighbor | Random neighbor |
| Worse moves | Never accepted | Sometimes accepted |
| Can escape a local minimum? | No, not in this implementation | Potentially, while temperature is sufficiently high |
| Stopping condition | No better neighbor | Temperature reaches the minimum |
| Guaranteed to find a solution? | No | No |

This script illustrates the different search behaviors. It does not currently calculate aggregate success rates, average runtimes, or statistical comparisons. Any performance conclusions would require repeated trials and consistent measurement.

## Customization

Open [`8queensProblem.py`](8queensProblem.py) to experiment with:

- `random_board()` — random starting positions.
- `evaluate(board)` — conflict-counting objective function.
- `hill_climbing()` — best-neighbor search and stopping rule.
- `random_successor(board)` — candidate moves for simulated annealing.
- `simulated_annealing()` — temperature, cooling factor, and acceptance logic.
- `print_board(board)` — console visualization.

The board size is currently fixed at **8 × 8**, and there is no command-line configuration or graphical interface.

## Repository Contents

| File | Description |
| --- | --- |
| [`8queensProblem.py`](8queensProblem.py) | Both algorithms, conflict evaluation, and console board output. |
| [`Comparing Hill Climbing and Simulated Annealing Algorithms to Solve the 8-Queens Problem.pdf`](Comparing%20Hill%20Climbing%20and%20Simulated%20Annealing%20Algorithms%20to%20Solve%20the%208-Queens%20Problem.pdf) | Accompanying project PDF. |
| `README.md` | Project documentation and execution instructions. |

## Educational Scope

This project is a self-contained demonstration of **local search**, **objective functions**, and **probabilistic search** in artificial intelligence. It is intended for learning and experimentation, not as a production chess engine or a general-purpose N-Queens solver.
