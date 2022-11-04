from typing import List

# https://leetcode.com/problems/n-queens/

class Solution:
	# O(n!) time.
	# O(n) space.
	def solveNQueens(self, n: int) -> List[List[str]]:
		self.n = n
		self.col = [0] * n
		
		self.boards = []

		self.backtrack(0)

		return self.boards

	def valid_position(self, r, c):
		for i in range(r):
			if self.col[i] == c or abs(r - i) == abs(c - self.col[i]):
				return False
		return True

	def backtrack(self, r):
		if r == self.n:
			self.boards.append(self.create_board())
			return

		for c in range(self.n):
			if self.valid_position(r, c):
				self.col[r] = c
				self.backtrack(r + 1)

	def create_board(self):
		board = []
		for r in range(self.n):
			r_row = "." * self.col[r] + "Q" + "." * (self.n - self.col[r] - 1)
			board.append(r_row)

		return board
