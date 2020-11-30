
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

from typing import List

class Solution:
	# O(n) time, O(1) space
	def findLengthOfLCIS(self, nums: List[int]) -> int:
		if len(nums) == 0: return 0
		length, curr_l = 1, 1
		for i in range(1, len(nums)):
			if nums[i - 1] < nums[i]:
				curr_l += 1
			else:
				length = max(length, curr_l)
				curr_l = 1
		length = max(length, curr_l)
		return length