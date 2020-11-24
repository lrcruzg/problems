
# https://leetcode.com/problems/reshape-the-matrix/

from typing import List

class Solution:
	# O(n * m) time, O(n * m) space
	# n = len(nums), m = len(nums[0])
	def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
		n = len(nums) * len(nums[0])
		if r * c != n: return nums
		rs = [[0] * c for _ in range(r)]
		for i in range(n):
			rs[i // c][i % c] = nums[i // len(nums[0])][i % len(nums[0])]
		return rs