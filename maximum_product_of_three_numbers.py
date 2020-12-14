
# https://leetcode.com/problems/maximum-product-of-three-numbers/

import heapq
from typing import List

class Solution:
	# O(n) time, O(1) space
	def maximumProduct(self, nums: List[int]) -> int:
		# minHeap
		max3nums = []
		# maxHeap
		min2nums = []

		for n in nums:
			if len(max3nums) == 3:
				heapq.heappushpop(max3nums, n)
			else:
				heapq.heappush(max3nums, n)

			if len(min2nums) == 2:
				heapq.heappushpop(min2nums, -n)
			else:
				heapq.heappush(min2nums, -n)

		return max(max(max3nums) * min2nums[0] * min2nums[1], max3nums[0] * max3nums[1] * max3nums[2])