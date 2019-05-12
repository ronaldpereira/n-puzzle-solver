import argparse


def parser():
    parser = argparse.ArgumentParser(description="Solvable n-puzzle's generator.")

    # Required arguments
    parser.add_argument("output_file", type=str, help="Output file name.")

    # Optional arguments
    parser.add_argument(
        "-n",
        "--n_dim",
        type=int,
        default=3,
        help="n-Puzzle dimension (n X n). (Default: 3)",
    )
    parser.add_argument(
        "-c",
        "--approx_cost",
        type=int,
        default=1,
        help="Approximated optimal solution cost. This must be an\
                              approximation because we can't guarantee the path\
                              followed by the empty space won't be an cycle. (Default: 1)",
    )

    args = parser.parse_args()

    return args
