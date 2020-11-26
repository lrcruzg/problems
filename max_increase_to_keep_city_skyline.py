
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List

class Solution:
	# O(n * m) time, O(n + m) space
	# n = len(grid), m = len(grid[0])
	def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
		increase = 0
		height_by_row, height_by_column = [0] * len(grid), [0] * len(grid[0])
		for r in range(len(grid)):
			height_by_row[r] = max(grid[r][j] for j in range(len(grid[0])))

		for c in range(len(grid[0])):
			height_by_column[c] = max(grid[i][c] for i in range(len(grid)))

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				increase += min(height_by_column[j], height_by_row[i]) - grid[i][j]

		return increase