import numpy as np

class Puzzle:
	def __init__(self, n=3):
		self.n = n
		self.createPuzzle()

		print('original puzzle')
		print(self.puzzle)

	def createPuzzle(self):
		self.puzzle = np.arange(0, self.n**2)
		np.random.shuffle(self.puzzle)
		self.puzzle = self.puzzle.reshape(self.n, self.n)
