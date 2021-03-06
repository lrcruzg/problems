
# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
	# O(n) time, O(1) space
	def generateTheString(self, n: int) -> str:
		if n % 2 == 1:
			return "a" * n
		return "a" + ("b" * (n - 1))