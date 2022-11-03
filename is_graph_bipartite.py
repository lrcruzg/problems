from typing import List
from collections import deque

# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
	# O(V + E) time.
	# O(V) space.
	# where V is the number of vertices in the graph, 
	# and E is the number of edges in the graph.
	def isBipartite(self, graph: List[List[int]]) -> bool:
		color = [0] * len(graph)  # color[i] == 0 -> node i not visited
		bipartite = True

		for i in range(len(graph)):
			if not color[i]:
				q = deque([i])
				color[i] = 1  # color the i-th node
				while q and bipartite:
					node = q.popleft()
					for neighbor in graph[node]:
						if not color[neighbor]: # neighbor not visited
							color[neighbor] = color[node] * (-1)  # switch color
							q.append(neighbor)
						elif color[neighbor] == color[node]:
								bipartite = False
								break

		return bipartite
