
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
	# O(n) time, O(n) space
	# n = len(s)
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1: return s
		rows = [""] * numRows
		counter, move = 0, -1
		for i in range(len(s)):
			if counter == 0 or counter == numRows - 1:
				move *= -1
			rows[counter] += s[i]
			print(counter)
			counter += move
		return "".join(rows)