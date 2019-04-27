from copy import deepcopy
from os import makedirs

import numpy as np


class StateNode:
    def __init__(self, puzzle, n, father=None):
        self.n = n
        self.puzzle = puzzle
        self.father = father
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def expand(self):
        spaceX, spaceY = self.findEmptySpace()

        if spaceX > 0:
            upPuzzle = self.moveSpaceUp(spaceX, spaceY)
            self.up = StateNode(upPuzzle, self.n, self)

        if spaceX < self.n-1:
            downPuzzle = self.moveSpaceDown(spaceX, spaceY)
            self.down = StateNode(downPuzzle, self.n, self)

        if spaceY > 0:
            leftPuzzle = self.moveSpaceLeft(spaceX, spaceY)
            self.left = StateNode(leftPuzzle, self.n, self)

        if spaceY < self.n-1:
            rightPuzzle = self.moveSpaceRight(spaceX, spaceY)
            self.right = StateNode(rightPuzzle, self.n, self)

    def moveSpaceUp(self, spaceX, spaceY):
        upPuzzle = deepcopy(self.puzzle)
        upPuzzle[spaceX, spaceY], upPuzzle[spaceX-1,
                                           spaceY] = upPuzzle[spaceX-1, spaceY], upPuzzle[spaceX, spaceY]

        return upPuzzle

    def moveSpaceDown(self, spaceX, spaceY):
        downPuzzle = deepcopy(self.puzzle)
        downPuzzle[spaceX, spaceY], downPuzzle[spaceX+1,
                                               spaceY] = downPuzzle[spaceX+1, spaceY], downPuzzle[spaceX, spaceY]

        return downPuzzle

    def moveSpaceLeft(self, spaceX, spaceY):
        leftPuzzle = deepcopy(self.puzzle)
        leftPuzzle[spaceX, spaceY], leftPuzzle[spaceX, spaceY -
                                               1] = leftPuzzle[spaceX, spaceY-1], leftPuzzle[spaceX, spaceY]

        return leftPuzzle

    def moveSpaceRight(self, spaceX, spaceY):
        rightPuzzle = deepcopy(self.puzzle)
        rightPuzzle[spaceX, spaceY], rightPuzzle[spaceX, spaceY +
                                                 1] = rightPuzzle[spaceX, spaceY+1], rightPuzzle[spaceX, spaceY]

        return rightPuzzle

    def findEmptySpace(self):
        coord = np.where(self.puzzle == 0)
        return coord[0][0], coord[1][0]

    def printAnswerPath(self, algorithm, expansions, cost, elapsed, output_path):
        try:
            makedirs(output_path)
        except FileExistsError:
            pass

        with open(output_path+algorithm+'.txt', 'w') as outputFile:
            outputFile.write("--- %s statistics ---\n" %algorithm)
            outputFile.write("Total node expansions: %d\n" %expansions)
            outputFile.write("Total solution cost: %d\n" %cost)
            outputFile.write("Time elapsed executing: %.3fs\n" %elapsed)
            outputFile.write('Solution path:\n')

            puzzles = []
            node = self
            while(node):
                puzzles.append(node.puzzle)
                node = node.father

            for i in reversed(range(len(puzzles))):
                outputFile.write('\nStep #%d\n' %(len(puzzles) - i - 1))
                np.savetxt(outputFile, puzzles[i], fmt="%d", delimiter='\t')
