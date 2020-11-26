
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

from typing import List

class Solution:
	# O(nlog(n)) time, O(1) space
	def minMoves(self, nums: List[int]) -> int:
		if len(nums) < 2: return 0
		nums.sort()
		ans, prev = 0, 0
		for i in range(1, len(nums)):
			ans += prev + nums[i] - nums[i - 1]
			prev += nums[i] - nums[i - 1]
		return ans