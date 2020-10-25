
# https://leetcode.com/problems/number-of-good-pairs/

from typing import List

class Solution:
	
	# O(n) time, O(n) space
	def numIdenticalPairs(self, nums: List[int]) -> int:
		counter = 0
		occurrences = {}
		for i in range(len(nums)):
			if nums[i] not in occurrences:
				occurrences[nums[i]] = 1
			else:
				occurrences[nums[i]] += 1

		for i in occurrences.keys():
			tmp = occurrences[i]
			if tmp >= 2:
				counter += (tmp * (tmp - 1)) // 2

		return counter

	'''
	# O(n^2) time, O(1) space
	def numIdenticalPairs(self, nums: List[int]) -> int:
		counter = 0
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] == nums[j]:
					counter += 1
		return counter
	'''