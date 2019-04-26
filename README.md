# n-Puzzle Solver

n-Puzzle solver using Artificial Intelligence algorithms:

- No-information search:
  - BFS (Breadth-First Search)
  - Iterative Deepening Search
  - Uniform-Cost Search

- Information search:
  - A* search
  - Greedy Best-First Search

- Local search:
  - Hill Climbing (with lateral movements)

Also contains a n-Puzzle generator to generate solvable puzzles.

## Arguments for solver

```text
usage: solver.py [-h] [-o OUTPUT_PATH] [-p PRINT_SOLUTION_PATH]
                 [-a A_STAR_ONLY]
                 input_file

n-puzzle solver using several Artificial Intelligence algorithms.

positional arguments:
  input_file            Input file path.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Output folder path. (Default:"./output/")
  -p PRINT_SOLUTION_PATH, --print_solution_path PRINT_SOLUTION_PATH
                        Print each algorithm solution path found. (Default: 1)
  -a A_STAR_ONLY, --a_star_only A_STAR_ONLY
                        Use only a-star algorithm. Recommended for n-puzzles n
                        > 3. (Default: 0)
```

## Arguments for generator

```text
usage: generator.py [-h] [-n N_DIM] [-c APPROX_COST] output_file

Solvable n-puzzle's generator.

positional arguments:
  output_file           Output file name.

optional arguments:
  -h, --help            show this help message and exit
  -n N_DIM, --n_dim N_DIM
                        n-Puzzle dimension (n X n). (Default: 3)
  -c APPROX_COST, --approx_cost APPROX_COST
                        Approximated optimal solution cost. This must be an
                        approximation because we can't guarantee the path
                        followed by the empty space won't be an cycle.
                        (Default: 1)
```
