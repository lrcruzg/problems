
# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
	# O(log(n)) time, O(1) space
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums) - 1
		while l <= r:
			mid = l + (r - l) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				l = mid + 1
			else:
				r = mid - 1
		return -1