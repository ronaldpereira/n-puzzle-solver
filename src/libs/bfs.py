import numpy as np
from queue import Queue

import libs.stateTree as STTREE

class BreadthFirstSearch:
    def __init__(self, initialPuzzle, answerPuzzle):
        self.answerPuzzle = answerPuzzle.puzzle
        self.frontier = Queue()
        self.frontier.put(STTREE.StateTree(initialPuzzle.puzzle, initialPuzzle.n))
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
                self.frontier.put(node)
                self.insertedPuzzles.append(node.puzzle)

                if self.checkNodeSolution(node.puzzle):
                    return 'solved'

    def execute(self):
        while self.frontier.qsize() > 0:
            actualNode = self.frontier.get()

            if self.checkNodeSolution(actualNode.puzzle):
                return 'solved'

            else:
                actualNode.expand()

                self.checkNode(actualNode.up)
                self.checkNode(actualNode.down)
                self.checkNode(actualNode.left)
                self.checkNode(actualNode.right)

        # If, for some reason, the problem doesn't have a solution, then return None as an answer
        return None