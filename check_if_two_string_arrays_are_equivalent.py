
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

from typing import List

class Solution:
	# O(n) time, O(n) space
	# n = max(len("".join(word1)), len("".join(word2)))
	def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
		return "".join(word1) == "".join(word2)