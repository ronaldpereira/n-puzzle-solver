import libs.puzzle as PUZZLE
import libs.stateTree as TREE

puzzleMap = PUZZLE.Puzzle()
tree = TREE.StateTree(puzzleMap.puzzle, puzzleMap.n)
tree.nextMoves()

if tree.up:
	print(tree.up.puzzle)
if tree.left:
	print(tree.left.puzzle)