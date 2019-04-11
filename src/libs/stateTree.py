class StateTree:
	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.up = self.moveSpaceUp()
		self.down = self.moveSpaceDown()
		self.left = self.moveSpaceLeft()
		self.right = self.moveSpaceRight()

	def moveSpaceUp(self):
		self.up = self.findEmptySpace()
		print(self.up)

	def moveSpaceDown(self):
		pass

	def moveSpaceLeft(self):
		pass

	def moveSpaceRight(self):
		pass

	def findEmptySpace(self):
		for x in range(len(self.puzzle[0])):
			self.puzzle[x]
			try:
				y = self.puzzle[x].index(0)

				return x, y

			except ValueError:
				continue
