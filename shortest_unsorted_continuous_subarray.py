
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

from typing import List

class Solution:
	# O(nlog(n)) time, O(n) space
	def findUnsortedSubarray(self, nums: List[int]) -> int:
		nums_sorted = sorted(nums)
		aux = [0] * len(nums)
		f_zero, l_zero = -1, len(nums)

		for i in range(len(nums)):
			if nums[i] == nums_sorted[i]:
				aux[i] = 1

		# find first 0
		for i in range(len(aux)):
			if aux[i] == 0:
				f_zero = i
				break

		# find last 0
		for i in range(len(aux) - 1, -1, -1):
			if aux[i] == 0:
				l_zero = i
				break

		return l_zero - f_zero + 1 if l_zero != len(nums) and f_zero != -1 else 0