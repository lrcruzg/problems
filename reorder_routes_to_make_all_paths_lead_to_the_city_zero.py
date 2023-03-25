from typing import List

# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
	# O(n) time. 
	# O(n) space (recursion stack).
	def minReorder(self, n: int, connections: List[List[int]]) -> int:
		Adj_list = [[] for _ in range(n)]
		visited = [False] * n

		for u, v in connections:
			Adj_list[u].append([v, True]) # True if the edge is from u to v (is exiting edge from u)
			Adj_list[v].append([u, False])

		self.ans = 0

		self.dfs(0, Adj_list, visited)

		return self.ans

	def dfs(self, i, Adj_list, visited):
		visited[i] = True
		for neighbor, exiting_edge in Adj_list[i]:
			if not visited[neighbor]:
				if exiting_edge:
					self.ans += 1
				self.dfs(neighbor, Adj_list, visited)
