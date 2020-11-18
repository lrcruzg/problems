
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
import heapq

class Solution:
	# O(nlog(k)) time, O(n + k)
	# where n = len(nums)
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		occurrences = {}
		heap = []
		for i in nums:
			if i in occurrences:
				occurrences[i] += 1
			else:
				occurrences[i] = 1

		for key, val in occurrences.items():
			if len(heap) == k:
				heapq.heappushpop(heap, (val, key))
			else:
				heapq.heappush(heap, (val, key))

		return [key for (val, key) in heap]