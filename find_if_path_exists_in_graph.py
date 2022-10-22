from typing import List

# https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
	# O(n + m) time.
	# O(n + m) space (Adjacency list).
	# where n = number of nodes, m = number of edges in the graph 
	def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
		Adj_list = [[] for _ in range(n)]
		visited = [False for _ in range(n)]

		for u, v in edges:
			Adj_list[u].append(v)
			Adj_list[v].append(u)

		self.exist_path = False

		self.dfs(source, destination, Adj_list, visited)

		return self.exist_path

	def dfs(self, node, destination, Adj_list, visited):
		visited[node] = True
		
		if node == destination:
			self.exist_path = True

		for neighbor in Adj_list[node]:
			if not visited[neighbor]:
				self.dfs(neighbor, destination, Adj_list, visited)
