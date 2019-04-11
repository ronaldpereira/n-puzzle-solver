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
			self.puzzle = np.array([1, 5, 2, 0, 4, 3, 7, 8, 6]) # solucao 5 do n_puzzles
			self.puzzle = np.array([5, 8, 2, 1, 0, 3, 4, 7, 6]) # solucao 10 do n_puzles
			# self.puzzle = np.array([8, 6, 7, 2, 5, 4, 3, 0, 1]) # solucao 31 do n_puzzles
		self.puzzle = self.puzzle.reshape(self.n, self.n)


class AnswerPuzzle(Puzzle):
	def __init__(self, n):
		super(AnswerPuzzle, self).__init__(n, False)
		