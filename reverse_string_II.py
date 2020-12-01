
# https://leetcode.com/problems/reverse-string-ii/

class Solution:
	# O(n) time, O(n) space (strings are immutable)
	def reverseStr(self, s: str, k: int) -> str:
		s = list(s)
		i = 0
		while i < len(s):
			l = i
			r = i + k - 1 if i + k - 1 < len(s) else len(s) - 1
			while l < r:
				s[l], s[r] = s[r], s[l]
				l += 1
				r -= 1

			i += 2 * k

		return "".join(s)