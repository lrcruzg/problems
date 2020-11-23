
# https://leetcode.com/problems/island-perimeter/

from typing import List

class Solution:
	# O(n * m) time, O(1) space
	# where n = len(grid) and m = len(grid[0])
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		def is_in_grid_and_is_land(i, j):
			return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0]) and grid[i][j] == 1

		perimeter = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					if not is_in_grid_and_is_land(i - 1, j):
						perimeter += 1
					if not is_in_grid_and_is_land(i, j - 1):
						perimeter += 1
					if not is_in_grid_and_is_land(i + 1, j):
						perimeter += 1
					if not is_in_grid_and_is_land(i, j + 1):
						perimeter += 1

		return perimeter