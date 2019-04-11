from copy import deepcopy
import numpy as np

import libs.bfs as BFS
import libs.puzzle as PUZZLE
import libs.stateTree as STTREE

puzzle = PUZZLE.Puzzle(3)
answer = PUZZLE.AnswerPuzzle(3)

bfs = BFS.BreadthFirstSearch(deepcopy(puzzle), deepcopy(answer))

print(bfs.execute())
