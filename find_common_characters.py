
# https://leetcode.com/problems/find-common-characters/

from typing import List

class Solution:
	# O(n * m) time, O(n) space
	# where n = len(A) and m = max([len(a) for a in A])
	def commonChars(self, A: List[str]) -> List[str]:
		set_of_chars = []
		for i in A:
			chars = {}
			for c in i:
				if c not in chars:
					chars[c] = 1
				else:
					chars[c] += 1
			set_of_chars.append(chars)

		ans = []
		
		for i in A[0]:
			append_i = True
			for dic in set_of_chars:
				if i in dic and dic[i] > 0:
					dic[i] -= 1
				else:
					append_i = False
					break
			if append_i:
				ans.append(i)
		return ans