from typing import List

# https://leetcode.com/problems/subsets/

class Solution:
	# O(n*2^n) time.
	# O(2^n) space.
	# where n = len(nums).
	def subsets(self, nums: List[int]) -> List[List[int]]:
		subsets = []
		for i in range(2 ** len(nums)):
			curr_set = []
			for j in range(len(nums)):
				if 1 << j & i:
					curr_set.append(nums[j])
			subsets.append(curr_set)

		return subsets
