from copy import deepcopy

import libs.bfs as BFS
import libs.puzzle as PUZZLE
import libs.stateTree as STTREE
import numpy as np

puzzle = PUZZLE.Puzzle(3)
answer = PUZZLE.AnswerPuzzle(3)

bfs = BFS.BreadthFirstSearch(deepcopy(puzzle), deepcopy(answer))

print("Total node expansions: %d" %bfs.execute())
