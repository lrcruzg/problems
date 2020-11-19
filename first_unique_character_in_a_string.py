
# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
	# O(n) time, O(n) space
	def firstUniqChar(self, s: str) -> int:
		char_index_repeated = {}
		for i in range(len(s)):
			c = s[i]
			if c not in char_index_repeated:
				char_index_repeated[c] = [i, False] 
			else:
				char_index_repeated[c][1] = True

		min_index = len(s)
		for key, val in char_index_repeated.items():
			if val[1] == False:
				min_index = min(min_index, val[0])

		return min_index if min_index != len(s) else -1