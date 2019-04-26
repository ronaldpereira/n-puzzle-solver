from copy import deepcopy

import numpy as np

import libs.arg_parse_config as APC
import libs.astar as ASTAR
import libs.bfs as BFS
import libs.gfs as GFS
import libs.hc as HC
import libs.ids as IDS
import libs.puzzle as PUZZLE
import libs.stateTree as STTREE
import libs.ucs as UCS

args = APC.parser()

puzzle = PUZZLE.Puzzle(args.input_file)
answer = PUZZLE.AnswerPuzzle(puzzle.n)

astar = ASTAR.AStar(deepcopy(puzzle), deepcopy(answer))
print('\nExecuting A Star...')
astarAnswerNode, astarExps, astarCost = astar.execute()
print('A Star completed.')
print("\nASTAR statistics\nTotal node expansions: %d\nTotal solution cost: %d" %
      (astarExps, astarCost))
astarAnswerNode.printAnswerPath('astar', args.output_path)

if not args.a_star_only:
    bfs = BFS.BreadthFirstSearch(deepcopy(puzzle), deepcopy(answer))
    print('\nExecuting Breadth First Search...')
    bfsAnswerNode, bfsExps, bfsCost = bfs.execute()
    print('Breadth First Search completed.')
    print("\nBFS statistics\nTotal node expansions: %d\nTotal solution cost: %d" %
          (bfsExps, bfsCost))
    bfsAnswerNode.printAnswerPath('bfs', args.output_path)

    ucs = UCS.UniformCostSearch(deepcopy(puzzle), deepcopy(answer))
    print('\nExecuting Uniform Cost Search...')
    ucsAnswerNode, ucsExps, ucsCost = ucs.execute()
    print('Uniform Cost Search completed.')
    print("\nUCS statistics\nTotal node expansions: %d\nTotal solution cost: %d" %
          (ucsExps, ucsCost))
    ucsAnswerNode.printAnswerPath('ucs', args.output_path)

    ids = IDS.IterativeDeepeningSearch(deepcopy(puzzle), deepcopy(answer))
    print('\nExecuting Iterative Deepening Search...')
    idsAnswerNode, idsExps, idsCost = ids.execute()
    print('Iterative Deepening Search completed.')
    print("\nIDS statistics\nTotal node expansions: %d\nTotal solution cost: %d" %
          (idsExps, idsCost))
    idsAnswerNode.printAnswerPath('ids', args.output_path)

    hc = HC.HillClimbing(deepcopy(puzzle), deepcopy(answer), 10)
    print('\nExecuting Hill Climbing...')
    hcAnswerNode, hcExps, hcCost = hc.execute()
    print('Hill Climbing completed.')
    print("\nHC statistics\nTotal node expansions: %d\nTotal solution cost: %d" %
          (hcExps, hcCost))
    hcAnswerNode.printAnswerPath('hc', args.output_path)

    gfs = GFS.GreedyFirstSearch(deepcopy(puzzle), deepcopy(answer))
    print('\nExecuting Greedy First Search...')
    gfsAnswerNode, gfsExps, gfsCost = gfs.execute()
    print('Greedy First Search completed.')
    print("\nGFS statistics\nTotal node expansions: %d\nTotal solution cost: %d" %
          (gfsExps, gfsCost))
    gfsAnswerNode.printAnswerPath('gfs', args.output_path)
