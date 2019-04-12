from copy import deepcopy

import numpy as np

import libs.bfs as BFS
import libs.ids as IDS
import libs.puzzle as PUZZLE
import libs.stateTree as STTREE
import libs.ucs as UCS
import libs.astar as ASTAR

puzzle = PUZZLE.Puzzle(3)
answer = PUZZLE.AnswerPuzzle(3)

bfs = BFS.BreadthFirstSearch(deepcopy(puzzle), deepcopy(answer))
exps, cost = bfs.execute()
print("\nBFS\nTotal node expansions: %d\nTotal cost: %d" %(exps, cost))

ucs = UCS.UniformCostSearch(deepcopy(puzzle), deepcopy(answer))
exps, cost = ucs.execute()
print("\nUCS\nTotal node expansions: %d\nTotal cost: %d" %(exps, cost))

ids = IDS.IterativeDeepeningSearch(deepcopy(puzzle), deepcopy(answer))
exps, cost = ids.execute()
print("\nIDS\nTotal node expansions: %d\nTotal cost: %d" %(exps, cost))

astar = ASTAR.AStar(deepcopy(puzzle), deepcopy(answer))
exps, cost = astar.execute()
print("\nASTAR\nTotal node expansions: %d\nTotal cost: %d" %(exps, cost))
