import numpy as np

import libs.puzzle as PUZZLE
import libs.stateTree as TREE

puzzleMap = PUZZLE.Puzzle(3, False)
answerMap = PUZZLE.AnswerPuzzle(3)

# print(np.array_equal(puzzleMap.puzzle, answerMap.puzzle)) # Compares two array if equals

tree = TREE.StateTree(puzzleMap.puzzle, puzzleMap.n)
tree.nextMoves()

if tree.up:
	print('up')
	print(tree.up.puzzle)
if tree.down:
	print('down')
	print(tree.down.puzzle)
if tree.left:
	print('left')
	print(tree.left.puzzle)
if tree.right:
	print('right')
	print(tree.right.puzzle)