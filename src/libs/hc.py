import numpy as np

import libs.stateTree as STTREE


class HillClimbing:
    def __init__(self, initialPuzzle, answerPuzzle, k):
        self.totalExpansions = 0
        self.k = k
        self.answerPuzzle = answerPuzzle.puzzle
        self.frontier = []
        self.frontier.append((STTREE.StateTree(
            initialPuzzle.puzzle, initialPuzzle.n), self.manhattanDistance(initialPuzzle.puzzle), 0))
        self.path = []

    def manhattanDistance(self, actualPuzzle):
        # Calculates the Manhattan Distance: sum of the distances of each piece to it's correct position
        totalDist = 0
        actualPiece = 1
        for x in range(len(actualPuzzle)):
            for y in range(len(actualPuzzle[x])):
                if not (x == len(actualPuzzle)-1 and y == len(actualPuzzle[x])-1):
                    actualCoord = np.where(actualPuzzle == actualPiece)
                    coordX, coordY = actualCoord[0][0], actualCoord[1][0]

                    totalDist += abs(x-coordX) + abs(y-coordY)

                    actualPiece += 1

        return totalDist

    def checkNodeSolution(self, nodePuzzle):
        return np.array_equal(nodePuzzle, self.answerPuzzle)

    def insertNodeToFrontier(self, node, actualCost):
        # If the node action exists
        if node:
            self.frontier.append(
                (node, self.manhattanDistance(node.puzzle), actualCost+1))

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

            else:
                # If the remaining lateral movements is greater than 0, move laterally and decrease k by 1
                if k > 0:
                    k -= 1
                    actualNode, actualDistance, actualCost = newNode, newDistance, newCost
                    self.path.append(actualNode.puzzle)

                # If the remaining lateral movements is 0, return None answer
                else:
                    return None

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
