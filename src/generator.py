from random import choice

import numpy as np

import libs.generator_arg_parse_config as GAPC


class Puzzle:
    def __init__(self, n, cost):
        self.n = n
        self.cost = cost
        self.actualCost = cost
        self.lastMovement = ""
        self.puzzle = np.append(np.arange(1, self.n ** 2), 0)
        self.puzzle = self.puzzle.reshape(self.n, self.n)

    def generatePuzzle(self):
        while self.actualCost > 0:
            spaceX, spaceY = self.findEmptySpace()
            possibleMovements = []

            if spaceX > 0 and self.lastMovement != "down":
                possibleMovements.append(self.moveSpaceUp)

            if spaceX < self.n - 1 and self.lastMovement != "up":
                possibleMovements.append(self.moveSpaceDown)

            if spaceY > 0 and self.lastMovement != "right":
                possibleMovements.append(self.moveSpaceLeft)

            if spaceY < self.n - 1 and self.lastMovement != "left":
                possibleMovements.append(self.moveSpaceRight)

            choice(possibleMovements)(spaceX, spaceY)
            self.actualCost -= 1

    def moveSpaceUp(self, spaceX, spaceY):
        self.puzzle[spaceX, spaceY], self.puzzle[spaceX - 1, spaceY] = (
            self.puzzle[spaceX - 1, spaceY],
            self.puzzle[spaceX, spaceY],
        )
        self.lastMovement = "up"

    def moveSpaceDown(self, spaceX, spaceY):
        self.puzzle[spaceX, spaceY], self.puzzle[spaceX + 1, spaceY] = (
            self.puzzle[spaceX + 1, spaceY],
            self.puzzle[spaceX, spaceY],
        )
        self.lastMovement = "down"

    def moveSpaceLeft(self, spaceX, spaceY):
        self.puzzle[spaceX, spaceY], self.puzzle[spaceX, spaceY - 1] = (
            self.puzzle[spaceX, spaceY - 1],
            self.puzzle[spaceX, spaceY],
        )
        self.lastMovement = "left"

    def moveSpaceRight(self, spaceX, spaceY):
        self.puzzle[spaceX, spaceY], self.puzzle[spaceX, spaceY + 1] = (
            self.puzzle[spaceX, spaceY + 1],
            self.puzzle[spaceX, spaceY],
        )
        self.lastMovement = "right"

    def findEmptySpace(self):
        coord = np.where(self.puzzle == 0)
        return coord[0][0], coord[1][0]

    def printPuzzle(self, output_file):
        print(
            "Generated %d-Puzzle (%d X %d) with approximated solution cost = %d"
            % (self.n, self.n, self.n, self.cost)
        )

        with open(output_file, "w") as outputFile:
            np.savetxt(outputFile, self.puzzle, fmt="%d", delimiter="\t")


args = GAPC.parser()
puzzle = Puzzle(args.n_dim, args.approx_cost)
puzzle.generatePuzzle()
puzzle.printPuzzle(args.output_file)
