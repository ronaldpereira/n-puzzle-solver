import numpy as np

import libs.state_node as STTREE


class AStar:
    def __init__(self, initialPuzzle, answerPuzzle):
        self.totalExpansions = 0
        self.answerPuzzle = answerPuzzle.puzzle
        self.frontier = []
        self.frontier.append((STTREE.StateNode(
            initialPuzzle.puzzle, initialPuzzle.n), self.manhattanDistance(initialPuzzle.puzzle), 0))

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

    def isPuzzleAlreadyInserted(self, nodePuzzle):
        for index in range(len(self.frontier)):
            if np.array_equal(nodePuzzle, self.frontier[index][0].puzzle):
                return True, index

        return False, None

    def insertNodeToFrontier(self, node, actualCost):
        # If the node action exists and it's not already included in the tree
        if node:
            isInserted, insertedIndex = self.isPuzzleAlreadyInserted(
                node.puzzle)
            if not isInserted:
                self.frontier.append(
                    (node, actualCost + 1 + self.manhattanDistance(node.puzzle), actualCost+1))
            # If the node is already inserted, pick the lesser cost one to stay in frontier
            else:
                if actualCost + 1 + self.manhattanDistance(node.puzzle) < self.frontier[insertedIndex][1]:
                    self.frontier[insertedIndex] = (
                        node, actualCost + 1 + self.manhattanDistance(node.puzzle), actualCost+1)

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
