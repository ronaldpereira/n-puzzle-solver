import numpy as np

import libs.state_node as STTREE


class UniformCostSearch:
    def __init__(self, initialPuzzle, answerPuzzle):
        self.totalExpansions = 0
        self.answerPuzzle = answerPuzzle.puzzle
        self.frontier = []
        self.frontier.append(
            (STTREE.StateNode(initialPuzzle.puzzle, initialPuzzle.n), 0)
        )
        self.exploredPuzzles = [initialPuzzle.puzzle]

    def checkNodeSolution(self, nodePuzzle):
        return np.array_equal(nodePuzzle, self.answerPuzzle)

    def isPuzzleAlreadyInserted(self, nodePuzzle):
        for index in range(len(self.frontier)):
            if np.array_equal(nodePuzzle, self.frontier[index][0].puzzle):
                return True, index

        for insertedPuzzle in self.exploredPuzzles:
            if np.array_equal(nodePuzzle, insertedPuzzle):
                return True, None

        return False, None

    def insertNodeToFrontier(self, node, actualCost):
        # If the node action exists and it's not already included in the tree
        if node:
            isInserted, frontierIndex = self.isPuzzleAlreadyInserted(node.puzzle)
            if not isInserted:
                self.frontier.append((node, actualCost + 1))
                self.exploredPuzzles.append(node.puzzle)

            else:
                if frontierIndex:
                    if actualCost < self.frontier[frontierIndex][1]:
                        self.frontier[frontierIndex] = (node, actualCost + 1)

    def sortFrontier(self):
        self.frontier = sorted(self.frontier, key=lambda x: x[1])

    def execute(self):
        while len(self.frontier) > 0:
            self.sortFrontier()
            actualNode, actualCost = self.frontier.pop(0)

            if self.checkNodeSolution(actualNode.puzzle):
                return actualNode, self.totalExpansions, actualCost

            else:
                actualNode.expand()
                self.totalExpansions += 1

                self.insertNodeToFrontier(actualNode.up, actualCost)
                self.insertNodeToFrontier(actualNode.down, actualCost)
                self.insertNodeToFrontier(actualNode.left, actualCost)
                self.insertNodeToFrontier(actualNode.right, actualCost)

        # If, for some reason, the problem doesn't have a solution, then return None as an answer
        return None
