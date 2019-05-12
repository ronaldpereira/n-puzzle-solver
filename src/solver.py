import time
from copy import deepcopy
from multiprocessing import Process

import numpy as np

import libs.arg_parse_config as APC
import libs.astar as ASTAR
import libs.bfs as BFS
import libs.gfs as GFS
import libs.hc as HC
import libs.ids as IDS
import libs.puzzle as PUZZLE
import libs.state_node as STTREE
import libs.ucs as UCS


def execute(algName, algObject, output_path):
    start = time.time()
    print("\nExecuting %s..." % algName)
    answerNode, exps, cost = algObject.execute()
    print("\n%s completed." % algName)
    end = time.time()
    answerNode.printAnswerPath(algName, exps, cost, end - start, output_path)


args = APC.parser()

puzzle = PUZZLE.Puzzle(args.input_file)
answer = PUZZLE.AnswerPuzzle(puzzle.n)

astar = ASTAR.AStar(deepcopy(puzzle), deepcopy(answer))
astarProcess = Process(target=execute, args=("A* Search", astar, args.output_path))

if not args.a_star_only:
    bfs = BFS.BreadthFirstSearch(deepcopy(puzzle), deepcopy(answer))
    bfsProcess = Process(
        target=execute, args=("Breadth-First Search", bfs, args.output_path)
    )

    ucs = UCS.UniformCostSearch(deepcopy(puzzle), deepcopy(answer))
    ucsProcess = Process(
        target=execute, args=("Uniform-Cost Search", ucs, args.output_path)
    )

    ids = IDS.IterativeDeepeningSearch(deepcopy(puzzle), deepcopy(answer))
    idsProcess = Process(
        target=execute, args=("Iterative Deepening Search", ids, args.output_path)
    )

    hc = HC.HillClimbing(deepcopy(puzzle), deepcopy(answer), args.k_hill_climbing)
    hcProcess = Process(
        target=execute,
        args=("Hill Climbing with Lateral Movements Search", hc, args.output_path),
    )

    gfs = GFS.GreedyFirstSearch(deepcopy(puzzle), deepcopy(answer))
    gfsProcess = Process(
        target=execute, args=("Greedy Best-First Search", gfs, args.output_path)
    )

# Starts processes
astarProcess.start()

if not args.a_star_only:
    bfsProcess.start()
    ucsProcess.start()
    idsProcess.start()
    hcProcess.start()
    gfsProcess.start()

# Wait processes to join
astarProcess.join()

if not args.a_star_only:
    bfsProcess.join()
    ucsProcess.join()
    idsProcess.join()
    hcProcess.join()
    gfsProcess.join()
