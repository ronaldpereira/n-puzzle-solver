import numpy as np

import libs.stateTree as STTREE

class BreadthFirstSearch:
    def __init__(self, initialPuzzle, answerPuzzle):
        self.totalExpansions = 0
        self.answerPuzzle = answerPuzzle.puzzle
        self.frontier = []
        self.frontier.append((STTREE.StateTree(initialPuzzle.puzzle, initialPuzzle.n), 0))
        self.exploredPuzzles = [initialPuzzle.puzzle]

    def checkNodeSolution(self, nodePuzzle):
        return np.array_equal(nodePuzzle, self.answerPuzzle)

    def isPuzzleAlreadyInserted(self, nodePuzzle):
        for insertedPuzzle in self.exploredPuzzles:
            if np.array_equal(nodePuzzle, insertedPuzzle):
                return True

        return False

    def insertNodeToFrontier(self, node, actualCost):
        # If the node action exists and it's not already included in the tree
        if node:
            if not self.isPuzzleAlreadyInserted(node.puzzle):
                self.frontier.append((node, actualCost+1))
                self.exploredPuzzles.append(node.puzzle)

    def execute(self):
        while len(self.frontier) > 0:
            actualNode, actualCost = self.frontier.pop(0)

            if self.checkNodeSolution(actualNode.puzzle):
                return self.totalExpansions, actualCost

            else:
                actualNode.expand()
                self.totalExpansions += 1

                self.insertNodeToFrontier(actualNode.up, actualCost)
                self.insertNodeToFrontier(actualNode.down, actualCost)
                self.insertNodeToFrontier(actualNode.left, actualCost)
                self.insertNodeToFrontier(actualNode.right, actualCost)

        # If, for some reason, the problem doesn't have a solution, then return None as an answer
        return None
