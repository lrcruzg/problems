
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

from typing import List

class Solution:
	# O(n) time, O(1) space
	def numPairsDivisibleBy60(self, time: List[int]) -> int:
		counter = 0
		remainder = [0] * 60
		for t in time:
			remainder[t % 60] += 1

		for i in range(1,30):
			if min(remainder[i], remainder[60 - i]):
				counter += remainder[i] * remainder[60 - i]

		counter += (remainder[0] * (remainder[0] - 1)) // 2 + (remainder[30] * (remainder[30] - 1)) // 2
		return counter