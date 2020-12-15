
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
	# O(n) time, O(n) space
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		prev_nums = {}
		for i in range(len(nums)):
			if target - nums[i] in prev_nums:
				return [prev_nums[target - nums[i]], i]
			prev_nums[nums[i]] = i