
# https://leetcode.com/problems/max-area-of-island/

from typing import List

class Solution:
	# O(n * m) time, O(n * m) space
	# where n = len(grid) and m = len(grid[0])
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		def is_in_grid_and_is_not_visited_land(i, j):
			return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0]) and grid[i][j] == 1 and not visited[i][j]

		def dfs(i, j):
			area = 1
			if is_in_grid_and_is_not_visited_land(i - 1, j):
				visited[i - 1][j] = True
				area += dfs(i - 1, j)
			if is_in_grid_and_is_not_visited_land(i, j - 1):
				visited[i][j - 1] = True
				area += dfs(i, j - 1)
			if is_in_grid_and_is_not_visited_land(i + 1, j):
				visited[i + 1][j] = True
				area += dfs(i + 1, j)
			if is_in_grid_and_is_not_visited_land(i, j + 1):
				visited[i][j + 1] = True
				area += dfs(i, j + 1)
			return area

		visited = [[False] * len(grid[0]) for _ in range(len(grid))]
		counter = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1 and not visited[i][j]:
					visited[i][j] = True
					counter = max(counter, dfs(i, j))
		return counter

inp = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
]

s = Solution()
print(s.maxAreaOfIsland(inp))