
# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
	# O(n) time, O(n) space
	def containsDuplicate(self, nums: List[int]) -> bool:
		prev_nums = set()
		for n in nums:
			if n in prev_nums:
				return True
			prev_nums.add(n)
		return False