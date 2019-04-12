import libs.stateTree as STTREE
import numpy as np

class BreadthFirstSearch:
    def __init__(self, initialPuzzle, answerPuzzle):
        self.totalExpansions = 0
        self.answerPuzzle = answerPuzzle.puzzle
        self.frontier = []
        self.frontier.append(STTREE.StateTree(initialPuzzle.puzzle, initialPuzzle.n))
        self.insertedPuzzles = [initialPuzzle.puzzle]

    def checkNodeSolution(self, nodePuzzle):
        return np.array_equal(nodePuzzle, self.answerPuzzle)

    def isPuzzleAlreadyInserted(self, nodePuzzle):
        for insertedPuzzle in self.insertedPuzzles:
            if np.array_equal(nodePuzzle, insertedPuzzle):
                return True

        return False

    def checkNode(self, node):
        # If the node movement exists and it's not already included in the tree
        if node:
            if not self.isPuzzleAlreadyInserted(node.puzzle):
                self.frontier.append(node)
                self.insertedPuzzles.append(node.puzzle)

                if self.checkNodeSolution(node.puzzle):
                    return self.totalExpansions

    def execute(self):
        while len(self.frontier) > 0:
            actualNode = self.frontier.pop(0)

            if self.checkNodeSolution(actualNode.puzzle):
                return self.totalExpansions

            else:
                actualNode.expand()
                self.totalExpansions += 1

                self.checkNode(actualNode.up)
                self.checkNode(actualNode.down)
                self.checkNode(actualNode.left)
                self.checkNode(actualNode.right)

        # If, for some reason, the problem doesn't have a solution, then return None as an answer
        return None
