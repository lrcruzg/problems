
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
	# O(n) time, O(1) space
	# where n = len(s)
	def titleToNumber(self, s: str) -> int:
		n, col = len(s), 0
		for i in range(n):
			col = col + (ord(s[n - i - 1]) - 64) * pow(26, i)
		return col