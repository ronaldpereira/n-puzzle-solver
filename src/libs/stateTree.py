from copy import deepcopy
import numpy as np

class StateTree:
	def __init__(self, puzzle, n):
		self.n = n
		self.puzzle = puzzle
		self.up = None
		self.down = None
		self.left = None
		self.right = None

	def nextMoves(self):
		spaceX, spaceY = self.findEmptySpace()

		if spaceX > 0:
			upPuzzle = self.moveSpaceUp(spaceX, spaceY)
			self.up = StateTree(upPuzzle, self.n)

		if spaceX < self.n-1:
			downPuzzle = self.moveSpaceDown(spaceX, spaceY)
			self.down = StateTree(downPuzzle, self.n)

		if spaceY > 0:
			leftPuzzle = self.moveSpaceLeft(spaceX, spaceY)
			self.left = StateTree(leftPuzzle, self.n)

		if spaceY < self.n-1:
			rightPuzzle = self.moveSpaceRight(spaceX, spaceY)
			self.right = StateTree(rightPuzzle, self.n)
		

	def moveSpaceUp(self, spaceX, spaceY):
		upPuzzle = deepcopy(self.puzzle)
		upPuzzle[spaceX, spaceY], upPuzzle[spaceX-1, spaceY] = upPuzzle[spaceX-1, spaceY], upPuzzle[spaceX, spaceY]

		return upPuzzle

	def moveSpaceDown(self, spaceX, spaceY):
		downPuzzle = deepcopy(self.puzzle)
		downPuzzle[spaceX, spaceY], downPuzzle[spaceX+1, spaceY] = downPuzzle[spaceX+1, spaceY], downPuzzle[spaceX, spaceY]

		return downPuzzle

	def moveSpaceLeft(self, spaceX, spaceY):
		leftPuzzle = deepcopy(self.puzzle)
		leftPuzzle[spaceX, spaceY], leftPuzzle[spaceX, spaceY-1] = leftPuzzle[spaceX, spaceY-1], leftPuzzle[spaceX, spaceY]

		return leftPuzzle

	def moveSpaceRight(self, spaceX, spaceY):
		rightPuzzle = deepcopy(self.puzzle)
		rightPuzzle[spaceX, spaceY], rightPuzzle[spaceX, spaceY+1] = rightPuzzle[spaceX, spaceY+1], rightPuzzle[spaceX, spaceY]

		return rightPuzzle

	def findEmptySpace(self):
		coord = np.where(self.puzzle == 0)
		return coord[0][0], coord[1][0]
