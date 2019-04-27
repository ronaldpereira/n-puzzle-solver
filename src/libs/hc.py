import numpy as np

import libs.state_node as STTREE


class HillClimbing:
    def __init__(self, initialPuzzle, answerPuzzle, k):
        self.totalExpansions = 0
        self.k = k
        self.answerPuzzle = answerPuzzle.puzzle
        self.frontier = []
        self.frontier.append((STTREE.StateNode(
            initialPuzzle.puzzle, initialPuzzle.n), self.hammingPriority(initialPuzzle.puzzle), 0))
        self.path = []

    def hammingPriority(self, actualPuzzle):
        # Calculates the number of pieces in the wrong position
        totalWrong = 0
        actualPiece = 1
        for x in range(len(actualPuzzle)):
            for y in range(len(actualPuzzle[x])):
                if not (x == len(actualPuzzle)-1 and y == len(actualPuzzle[x])-1):
                    actualCoord = np.where(actualPuzzle == actualPiece)
                    coordX, coordY = actualCoord[0][0], actualCoord[1][0]

                    # Piece is in the wrong spot
                    if abs(x-coordX) != 0 or abs(y-coordY) != 0:
                        totalWrong += 1

                    actualPiece += 1

        return totalWrong

    def checkNodeSolution(self, nodePuzzle):
        return np.array_equal(nodePuzzle, self.answerPuzzle)

    def insertNodeToFrontier(self, node, actualCost):
        # If the node action exists
        if node:
            self.frontier.append(
                (node, self.hammingPriority(node.puzzle), actualCost+1))

    def sortFrontier(self):
        self.frontier = sorted(self.frontier, key=lambda x: x[1])

    def execute(self):
        # Initializing the actual distance with the greater possible value
        actualDistance = float('inf')
        k = self.k
        while len(self.frontier) > 0:
            self.sortFrontier()
            newNode, newDistance, newCost = self.frontier.pop(0)

            # If the avaliation function (Manhattan Distance) of the new node is smaller than the old actual node, reset the k for lateral movements
            if newDistance < actualDistance:
                k = self.k
                actualNode, actualDistance, actualCost = newNode, newDistance, newCost
                self.path.append(actualNode.puzzle)

            elif newDistance == actualDistance:
                # If the remaining lateral movements is greater than 0, move laterally and decrease k by 1
                if k > 0:
                    k -= 1
                    actualNode, actualDistance, actualCost = newNode, newDistance, newCost
                    self.path.append(actualNode.puzzle)

                # If the remaining lateral movements is 0, return the actual node
                else:
                    return actualNode, self.totalExpansions, actualCost
            
            # If no frontier node is better than then actual one, finish the Hill Climbing and return the actual node
            else:
                return actualNode, self.totalExpansions, actualCost

            if self.checkNodeSolution(actualNode.puzzle):
                return actualNode, self.totalExpansions, actualCost

            else:
                actualNode.expand()
                self.totalExpansions += 1

                self.insertNodeToFrontier(actualNode.up, actualCost)
                self.insertNodeToFrontier(actualNode.down, actualCost)
                self.insertNodeToFrontier(actualNode.left, actualCost)
                self.insertNodeToFrontier(actualNode.right, actualCost)

        # If, for some reason, the solver doesn't found a solution, then return the last actual node as an answer
        return actualNode, self.totalExpansions, actualCost
