from typing import List

# https://leetcode.com/problems/max-area-of-island/

class Solution:
	# O(m * n) time. (amortized)
	# O(m * n) space.
	# where m * n is the size of the grid.
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		def valid_cell(i, j):
			return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]

		directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

		m, n = len(grid), len(grid[0])

		uf = UnionFind(m * n)

		for i in range(m):
			for j in range(n):
				if valid_cell(i, j):
					for r, c in directions:					
						if valid_cell(i + r, j + c):
							uf.union(i * n + j, (i + r) * n + (j + c))
				else: 
					# "water" cells are ignored, its size of are set to zero
					uf.set_size[i * n + j] = 0

		return max(uf.size_of_set(i) for i in range(m * n))


# Union Find disjoint set using union by rank heuristic
class UnionFind:
	def __init__(self, N: int = 0):
		self.rank = [0 for _ in range(N)]
		self.parent = [i for i in range(N)]
		self.set_size = [1 for i in range(N)]
		self.num_sets = N

	def add(self, val: int) -> None:
		self.parent.append(len(self.parent))
		self.rank.append(0)
		self.set_size.append(1)
		self.num_sets += 1

	def find(self, i: int) -> int:
		if self.parent[i] == i: return i
		self.parent[i] = self.find(self.parent[i])
		return self.parent[i]

	def size_of_set(self, i: int) -> int:
		return self.set_size[self.find(i)]

	def union(self, i: int, j: int) -> None:
		if self.find(i) != self.find(j):
			self.num_sets -= 1
			x, y = self.find(i), self.find(j)

			if self.rank[x] > self.rank[y]:
				self.parent[y] = x
				self.set_size[x] += self.set_size[y]
			else:
				self.parent[x] = y
				self.set_size[y] += self.set_size[x]
				if self.rank[x] == self.rank[y]:
					self.rank[y] += 1

