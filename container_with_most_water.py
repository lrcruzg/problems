
# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
	# O(n) time, O(1) space
	def maxArea(self, height: List[int]) -> int:
		l, r = 0, len(height) - 1
		max_water = 0
		while l < r:
			max_water = max(max_water, min(height[l], height[r]) * (r - l))
			if height[r] < height[l]:
				r -= 1
			else:
				l += 1
		return max_water