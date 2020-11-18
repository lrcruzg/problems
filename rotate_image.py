
# https://leetcode.com/problems/rotate-image/

from typing import List

class Solution:
	# O(n * m) time, O(1) space
	# where n * m is the dimension of the matrix, i.e. len(matrix) * len(matrix[0])
	def rotate(self, matrix: List[List[int]]) -> None:
		self.transpose(matrix)
		self.vertical_flip(matrix)

	def transpose(self, matrix):
		for i in range(len(matrix)):
			for j in range(i, len(matrix[0])):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	def vertical_flip(self, matrix):
		n = len(matrix[0])
		for i in range(len(matrix)):
			for j in range(n // 2):
				matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]