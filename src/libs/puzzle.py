from math import sqrt

import numpy as np


class Puzzle:
    def __init__(self, input_path=None, n=None):
        if input_path:
            self.readPuzzle(input_path)
            print("input puzzle:")
            print(self.puzzle)
        else:
            self.n = n
            self.generateAnswerPuzzle()

    def readPuzzle(self, input_path):
        input_values = []
        with open(input_path, "r") as inputPuzzle:
            for line in inputPuzzle:
                for value in line.split():
                    input_values.append(int(value))

        try:
            self.n = int(sqrt(len(input_values)))
            self.puzzle = np.array(input_values, np.int32).reshape(self.n, self.n)

        except ValueError:
            print("Input puzzle shape is incorrect. Please check the input file.")
            exit(1)

    def generateAnswerPuzzle(self):
        self.puzzle = np.append(np.arange(1, self.n ** 2), 0)
        self.puzzle = self.puzzle.reshape(self.n, self.n)


class AnswerPuzzle(Puzzle):
    def __init__(self, n):
        super(AnswerPuzzle, self).__init__(n=n)
