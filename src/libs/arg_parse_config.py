import argparse


def parser():
    parser = argparse.ArgumentParser(
        description='n-puzzle solver using several Artificial Intelligence algorithms.')

    # Required arguments
    parser.add_argument('input_file', type=str, help='Input file path.')

    # Optional arguments
    parser.add_argument('-o', '--output_path', type=str, default='./output/',
                        help='Output folder path. (Default:"./output/")')
    parser.add_argument('-a', '--a_star_only', type=int, default=0,
                        help='Use only a-star algorithm. Recommended for n-puzzles n > 3. (Default: 0)')

    args = parser.parse_args()

    return args
