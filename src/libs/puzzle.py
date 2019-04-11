class Puzzle:
	def __init__(self, n=3):
		self.n = n
		self.create_map()
		print(self.map)

	def create_map(self):
		self.map = [[] for _ in range(self.n)]
		print(self.map)
		for x in range(self.n):
			self.map[x].extend([i + (self.n*x) for i in range(1, self.n+1)])
		self.map[-1][-1] = 0
