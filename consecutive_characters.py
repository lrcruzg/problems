
# https://leetcode.com/problems/consecutive-characters/

class Solution:
	# O(n) time, O(n) space
	def maxPower(self, s: str) -> int:
		power = [1] * len(s)
		for i in range(1, len(s)):
			if s[i] == s[i - 1]:
				power[i] = 1 + power[i - 1]
		return max(power)