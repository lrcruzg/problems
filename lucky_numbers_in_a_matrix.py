
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

from typing import List
import math

class Solution:
	# O(n * m) time, O(n + m) space
	# n = len(matrix), m = len(matrix[0])
	def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
		ans = []
		max_by_column, min_by_row = [-math.inf] * len(matrix[0]), [math.inf] * len(matrix)
		for r in range(len(matrix)):
			min_by_row[r] = min([matrix[r][j] for j in range(len(matrix[0]))])

		for c in range(len(matrix[0])):
			max_by_column[c] = max([matrix[i][c] for i in range(len(matrix))])

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == min_by_row[i] and matrix[i][j] == max_by_column[j]:
					ans.append(matrix[i][j])
		return ans