import numpy as np

class Puzzle:
	def __init__(self, n, randomize=True):
		self.n = n
		self.createPuzzle(randomize)

		print('original puzzle')
		print(self.puzzle)

	def createPuzzle(self, randomize):
		self.puzzle = np.append(np.arange(1, self.n**2), 0)
		if randomize:
			np.random.shuffle(self.puzzle)
		self.puzzle = self.puzzle.reshape(self.n, self.n)

class AnswerPuzzle(Puzzle):
	def __init__(self, n):
		super(AnswerPuzzle, self).__init__(n, False)
		