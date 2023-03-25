from typing import List

# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
	def __init__(self, N):
		self.N = N
		self.parent = [i for i in range(N)]
		self.rank = [0 for i in range(N)]
		self.set_size = [1 for i in range(N)]

	def find(self, i):
		if self.parent[i] == i: return i
		self.parent[i] = self.find(self.parent[i])
		return self.parent[i]

	def union(self, i, j):
		if self.find(i) != self.find(j):
			rep_i = self.find(i)
			rep_j = self.find(j)
			if self.rank[rep_i] < self.rank[rep_j]:
				self.parent[rep_i] = rep_j
				self.set_size[rep_j] += self.set_size[rep_i]
			else:
				self.parent[rep_j] = rep_i
				self.set_size[rep_i] += self.set_size[rep_j]
				if self.rank[rep_i] == self.rank[rep_j]:
					self.rank[rep_i] += 1

class Solution:
	# O(n) time.
	# O(n) space.
	def countPairs(self, n: int, edges: List[List[int]]) -> int:
		if len(edges) == 0: return (n * (n - 1)) // 2

		uf = UnionFind(n)
		for u, v in edges:
			uf.union(u, v)

		# connected components representatives
		cc_rep = [i for i in range(n) if uf.parent[i] == i]

		ans = 0
		for r in cc_rep:
			ans += (uf.set_size[r]) * (n - uf.set_size[r])

		return ans // 2
