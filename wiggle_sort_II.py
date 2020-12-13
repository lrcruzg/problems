
# https://leetcode.com/problems/wiggle-sort-ii/

from typing import List

class Solution:
	# O(nlog(n)) time, O(n) time
	def wiggleSort(self, nums: List[int]) -> None:
		n = len(nums)
		aux = sorted(nums)
		l1 = aux[:(n + 1) // 2][::-1]
		l2 = aux[(n + 1) // 2:][::-1]

		for i in range(n):
			if i % 2 == 0:
				nums[i] = l1[i // 2]
			else:
				nums[i] = l2[i // 2]