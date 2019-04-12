import numpy as np

class Puzzle:
    def __init__(self, n, randomize=True):
        self.n = n
        self.createPuzzle(randomize)
        print('puzzle')
        print(self.puzzle)

    def createPuzzle(self, randomize):
        self.puzzle = np.append(np.arange(1, self.n**2), 0)
        if randomize:
            # np.random.shuffle(self.puzzle)
            # self.puzzle = np.array([1, 2, 3, 4, 5, 6, 7, 0, 8]) # solucao 2 do npuzzle
            self.puzzle = np.array([1, 5, 2, 0, 4, 3, 7, 8, 6]) # solucao 5 do npuzzle
            # self.puzzle = np.array([5, 8, 2, 1, 0, 3, 4, 7, 6]) # solucao 10 do npuzzle
            # self.puzzle = np.array([8, 0, 2, 5, 7, 3, 1, 4, 6]) # solucao 15 do npuzzle
            # self.puzzle = np.array([8, 7, 0, 5, 4, 2, 1, 6, 3]) # solucao 20 do npuzzle
            # self.puzzle = np.array([8, 6, 7, 2, 5, 4, 3, 0, 1]) # solucao 31 do npuzzle
        self.puzzle = self.puzzle.reshape(self.n, self.n)


class AnswerPuzzle(Puzzle):
    def __init__(self, n):
        super(AnswerPuzzle, self).__init__(n, False)
