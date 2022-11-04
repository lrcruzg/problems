from typing import List

# https://leetcode.com/problems/n-queens-ii/

class Solution:
	# O(n!) time.
	# O(n) space.
	def totalNQueens(self, n: int) -> int:
		self.n = n
		self.col = [0] * n
		
		self.num_boards = 0

		self.backtrack(0)

		return self.num_boards

	def valid_position(self, r, c):
		for i in range(r):
			if self.col[i] == c or abs(r - i) == abs(c - self.col[i]):
				return False
		return True

	def backtrack(self, r):
		if r == self.n:
			self.num_boards += 1
			return

		for c in range(self.n):
			if self.valid_position(r, c):
				self.col[r] = c
				self.backtrack(r + 1)
