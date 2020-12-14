
# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
	# O(n) time (sort a fixed size arrray), O(1) space (only 26 letters)
	# n = len(word1) + len(word2)
	def closeStrings(self, word1: str, word2: str) -> bool:
		w1_counter = [0] * 26
		for c in word1:
			w1_counter[ord(c) - 97] += 1

		w2_counter = [0] * 26
		for c in word2:
			w2_counter[ord(c) - 97] += 1

		w1_char_ap = [i for i in range(26) if w1_counter[i]]
		w2_char_ap = [i for i in range(26) if w2_counter[i]]

		return sorted(w1_counter) == sorted(w2_counter) and w1_char_ap == w2_char_ap