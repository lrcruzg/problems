
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
	# O(n) time, O(1) space
	def freqAlphabets(self, s: str) -> str:
		ans = []
		i = len(s) - 1
		while i >= 0:
			if s[i] == "#":
				num = int(s[i - 1]) + int(s[i - 2]) * 10
				ans.append(chr(num + 96))
				i -= 3
			else:
				ans.append(chr(int(s[i]) + 96))
				i -= 1
		return "".join(ans[::-1])