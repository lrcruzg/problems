
# https://leetcode.com/problems/length-of-last-word/

class Solution:
	# O(n) time, O(1) space
	def lengthOfLastWord(self, s: str) -> int:
		i = len(s) - 1
		word_end = -1
		found_word = False
		while i >= 0:
			if s[i] != " ":
				word_end = max(word_end, i)
				found_word = True
			elif found_word and s[i] == " ":
				return word_end - i
			i -= 1
		return 0 if not found_word else word_end + 1

'''
	def lengthOfLastWord(self, s: str) -> int:
		words = s.split()
		if len(words) == 0: return 0
		return len(words[-1])
'''