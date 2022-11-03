from typing import List

# https://leetcode.com/problems/redundant-connection/

class Solution:
	# O(V + E) time.
	# O(V) space.
	# where V = number of nodes, E = number of edges.
	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
		uf = UnionFind(len(edges) + 1)
		disjoint_sets = uf.num_sets

		for u, v in edges:
			uf.union(u, v)
			if uf.num_sets == disjoint_sets:
				return [u, v]
			disjoint_sets = uf.num_sets

		return []


class UnionFind:
	def __init__(self, N):
		self.parent = [i for i in range(N)]
		self.rank = [0 for _ in range(N)]
		self.num_sets = N

	def find(self, i):
		if self.parent[i] == i:
			return i

		self.parent[i] = self.find(self.parent[i])
		return self.parent[i]

	def union(self, i, j):
		if self.find(i) != self.find(j):
			self.num_sets -= 1
			x, y = self.find(i), self.find(j)
			if self.rank[x] > self.rank[y]:
				self.parent[y] = x
			else:
				self.parent[x] = y
				if self.rank[x] == self.rank[y]:
					self.rank[y] += 1
