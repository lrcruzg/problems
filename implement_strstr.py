
# https://leetcode.com/problems/implement-strstr/

class Solution:
	# O(n) time, O(1) space
	def strStr(self, haystack: str, needle: str) -> int:
		if not needle: return 0
		if not haystack: return -1
		for i in range(len(haystack) - len(needle) + 1):
			eq = True
			if haystack[i] == needle[0]:
				for j in range(1, len(needle)):
					if haystack[i + j] != needle[j]:
						eq = False
				if eq:
					return i
		return -1