class Puzzle:
	def __init__(self, n=3):
		self.n = n
		self.createPuzzle()
		
		print('original puzzle:')
		print(self.puzzle)

	def createPuzzle(self):
		self.puzzle = [[] for _ in range(self.n)]
		for x in range(self.n):
			self.puzzle[x].extend([i + (self.n*x) for i in range(1, self.n+1)])
		self.puzzle[-1][-1] = 0
