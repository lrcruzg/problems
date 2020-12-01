
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
	# O(n) time, O(n) space
	def maxLengthBetweenEqualCharacters(self, s: str) -> int:
		f_l_oc = {} # fist and last occurrence
		for i in range(len(s)):
			if s[i] in f_l_oc:
				f_l_oc[s[i]] = (f_l_oc[s[i]][0], i)
			else:
				f_l_oc[s[i]] = (i, i)

		length = -1

		for key, val in f_l_oc.items():
			if val[0] != val[1]:
				length = max(length, val[1] - val[0] - 1) 

		return length