
# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List

class Solution:
	# O(n * m) time, O(1) space
	# n = len(matrix), m = len(matrix[0])
	def setZeroes(self, matrix: List[List[int]]) -> None:
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 0:
					self.set_zeroes_hv(i, j, matrix)

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == "#":
					matrix[i][j] = 0

	def set_zeroes_hv(self, i, j, m):
		# horizontal
		for c in range(len(m[0])):
			m[i][c] = "#" if m[i][c] != 0 else 0

		# vertical
		for r in range(len(m)):
			m[r][j] = "#" if m[r][j] != 0 else 0