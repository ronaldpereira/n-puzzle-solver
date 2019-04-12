import libs.stateTree as STTREE
from copy import deepcopy

import numpy as np

class IterativeDeepeningSearch:
    def __init__(self, initialPuzzle, answerPuzzle, totalExpansions=0):
        self.totalExpansions = totalExpansions
        self.initialPuzzle = initialPuzzle
        self.answerPuzzle = answerPuzzle
        self.frontier = []
        self.frontier.append((STTREE.StateTree(initialPuzzle.puzzle, initialPuzzle.n), 0, 0))
        self.insertedPuzzles = [initialPuzzle.puzzle]

    def checkNodeSolution(self, nodePuzzle):
        return np.array_equal(nodePuzzle, self.answerPuzzle.puzzle)

    def isPuzzleAlreadyInserted(self, nodePuzzle):
        for insertedPuzzle in self.insertedPuzzles:
            if np.array_equal(nodePuzzle, insertedPuzzle):
                return True

        return False

    def insertNodeToFrontier(self, node, actualCost, actualLevel):
        # If the node action exists and it's not already included in the tree
        if node:
            if not self.isPuzzleAlreadyInserted(node.puzzle):
                self.frontier.append((node, actualCost+1, actualLevel+1))
                self.insertedPuzzles.append(node.puzzle)

    def execute(self):
        actualMaxLevel = 0
        while True:
            while len(self.frontier) > 0:
                actualLevel = float('inf')
                while actualLevel > actualMaxLevel and len(self.frontier) > 0:
                    actualNode, actualCost, actualLevel = self.frontier.pop()
                
                if actualLevel <= actualMaxLevel:
                    if self.checkNodeSolution(actualNode.puzzle):
                        return self.totalExpansions, actualCost

                    else:
                        actualNode.expand()
                        self.totalExpansions += 1

                        # Inverted the insert logic, so it becomes a stack
                        self.insertNodeToFrontier(actualNode.right, actualCost, actualLevel)
                        self.insertNodeToFrontier(actualNode.left, actualCost, actualLevel)
                        self.insertNodeToFrontier(actualNode.down, actualCost, actualLevel)
                        self.insertNodeToFrontier(actualNode.up, actualCost, actualLevel)

            # If no answer has been found on actual maximum level, try again with +1 level                        
            actualMaxLevel += 1
            # Restarts the search from the first state
            self.__init__(deepcopy(self.initialPuzzle), deepcopy(self.answerPuzzle), self.totalExpansions)
