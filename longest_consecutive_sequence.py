from typing import List

# https://leetcode.com/problems/longest-consecutive-sequence/

class UnionFind:
	def __init__(self, N: int = 0):
		self.rank = [0 for _ in range(N)]
		self.p = [i for i in range(N)]
		self.set_size = [1 for i in range(N)]

	def add(self, val: int) -> None:
		self.p.append(len(self.p))
		self.rank.append(0)
		self.set_size.append(1)

	def find(self, i: int) -> int:
		if self.p[i] == i: return i
		self.p[i] = self.find(self.p[i])
		return self.p[i]

	def size_of_set(self, i: int) -> int:
		return self.set_size[self.find(i)]

	def union(self, i: int, j: int) -> None:
		if self.find(i) != self.find(j):
			x, y = self.find(i), self.find(j)

			if self.rank[x] > self.rank[y]:
				self.p[y] = x
				self.set_size[x] += self.set_size[y]
			else:
				self.p[x] = y
				self.set_size[y] += self.set_size[x]
				if self.rank[x] == self.rank[y]:
					self.rank[y] += 1


class Solution:
	# O(n) time. (amortized)
	# O(n) space.
	def longestConsecutive(self, nums: List[int]) -> int:
		if not nums: return 0
		uf = UnionFind()
		value_index = {}

		for n in nums:
			if not n in value_index:
				value_index[n] = len(uf.p)
				uf.add(value_index[n])

			if n - 1 in value_index:
				uf.union(value_index[n - 1], value_index[n])

			if n + 1 in value_index:
				uf.union(value_index[n], value_index[n + 1])

		return max(uf.size_of_set(i) for i in range(len(uf.p)))
