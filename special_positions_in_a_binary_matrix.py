from typing import List

# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
	# O(m * n) time. 
	# O(m + n) space.
	# where mat is a m * n matrix
	def numSpecial(self, mat: List[List[int]]) -> int:
		m, n = len(mat), len(mat[0])
		row = [0 for i in range(m)]
		col = [0 for i in range(n)]

		for i in range(m * n):
			row[i // n] += mat[i // n][i % n]
			col[i % n] += mat[i // n][i % n]

		counter = 0

		for i in range(m):
			for j in range(n):
				if row[i] == 1 and col[j] == 1 and mat[i][j] == 1:
					counter += 1

		return counter
