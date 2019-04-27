# Execution guidelines

## Arguments for solver

```text
usage: solver.py [-h] [-o OUTPUT_PATH] [-a] input_file

n-puzzle solver using several Artificial Intelligence algorithms.

positional arguments:
  input_file            Input file path.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Output folder path. (Default:"./output/")
  -a, --a_star_only     Use only a-star algorithm. Recommended for n-puzzles,
                        n > 3. (Default: False)
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

## Input format

- n x n matrix forming the entire puzzle board
- **The empty space is represented by the integer 0**
- Input Example for a 8-puzzle (3x3 board):

```text
0   5   2
1   8   3
4   7   6
```

## Output format

- Statistics printed on the top of the file
    1. Name of the algorithm
    2. Total node expansions executed to find the solution
    3. Total solution cost
    4. Sequence of solution path found
- Output Example for a 8-puzzle (3x3 board):
```text
***astar statistics***
Total node expansions: 8
Total solution cost: 8
Solution path:

Step #0
0   5   2
1   8   3
4   7   6

Step #1
1   5   2
0   8   3
4   7   6

Step #2
1   5   2
4   8   3
0   7   6

Step #3
1   5   2
4   8   3
7   0   6

Step #4
1   5   2
4   0   3
7   8   6

Step #5
1   0   2
4   5   3
7   8   6

Step #6
1   2   0
4   5   3
7   8   6

Step #7
1   2   3
4   5   0
7   8   6

Step #8
1   2   3
4   5   6
7   8   0
```
