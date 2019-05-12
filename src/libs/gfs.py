import numpy as np

import libs.state_node as STTREE


class GreedyFirstSearch:
    def __init__(self, initialPuzzle, answerPuzzle):
        self.totalExpansions = 0
        self.answerPuzzle = answerPuzzle.puzzle
        self.frontier = []
        self.frontier.append(
            (
                STTREE.StateNode(initialPuzzle.puzzle, initialPuzzle.n),
                self.hammingPriority(initialPuzzle.puzzle),
                0,
            )
        )

    def hammingPriority(self, actualPuzzle):
        # Calculates the number of pieces in the wrong position
        totalWrong = 0
        actualPiece = 1
        for x in range(len(actualPuzzle)):
            for y in range(len(actualPuzzle[x])):
                if not (x == len(actualPuzzle) - 1 and y == len(actualPuzzle[x]) - 1):
                    actualCoord = np.where(actualPuzzle == actualPiece)
                    coordX, coordY = actualCoord[0][0], actualCoord[1][0]

                    # Piece is in the wrong spot
                    if abs(x - coordX) != 0 or abs(y - coordY) != 0:
                        totalWrong += 1

                    actualPiece += 1

        return totalWrong

    def checkNodeSolution(self, nodePuzzle):
        return np.array_equal(nodePuzzle, self.answerPuzzle)

    def insertNodeToFrontier(self, node, actualCost):
        # If the node action exists
        if node:
            self.frontier.append(
                (node, self.hammingPriority(node.puzzle), actualCost + 1)
            )

    def sortFrontier(self):
        self.frontier = sorted(self.frontier, key=lambda x: x[1])

    def execute(self):
        while len(self.frontier) > 0:
            self.sortFrontier()
            actualNode, _, actualCost = self.frontier.pop(0)

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
