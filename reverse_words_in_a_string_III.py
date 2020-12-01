
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
	# O(n) time, O(n) space
	def reverseWords(self, s: str) -> str:
		ans, ws, i = [], 0, 1
		while i < len(s):
			if s[i] == " " or i == len(s) - 1:
				tmp = s[ws:i] if i != len(s) - 1 else s[ws:]
				ans.append(tmp[::-1])
				ws = i + 1
			i += 1
		return " ".join(ans)