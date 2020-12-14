
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq
from typing import List
import math

class Solution:
	# O(klog(n)) time, O(n) space
	# n = len(matrix[0])
	def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
		heap = []
		for i in range(len(matrix)):
			heapq.heappush(heap, (matrix[i][0], 0  , i   ))
			#                      value      , col, row

		while k:
			minimum, col, row = heapq.heappop(heap)
			if col + 1 < len(matrix[row]):
				heapq.heappush(heap, (matrix[row][col + 1], col + 1, row))
			k -= 1
		return minimum

	'''
	# O(kn) time, O(1) space
	def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
		current_index = [0] * len(matrix)
		for i in range(k):
			minimum = (math.inf, -1)
			for j in range(len(matrix)):
				if current_index[j] < len(matrix[j]) and matrix[j][current_index[j]] < minimum[0]:
					minimum = (matrix[j][current_index[j]], j)
			current_index[minimum[1]] += 1
			ans = minimum[0]
		return ans
	'''

	'''
	# O(klog(n)) time, O(n) space
	def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
		mat_elements = self.merge(matrix)
		return mat_elements[k - 1]

	def merge(self, lists):
		if len(lists) == 1: return lists[0]
		return self.merge_two_list(self.merge(lists[:(len(lists) + 1) // 2]), self.merge(lists[(len(lists) + 1) // 2:]))

	def merge_two_list(self, l1, l2):
		if not l1: return l2
		if not l2: return l1
		if l1[-1] < l2[-1]:
			return self.merge_two_list(l1, l2[:-1]) + [l2[-1]]
		return self.merge_two_list(l1[:-1], l2) + [l1[-1]]
	'''