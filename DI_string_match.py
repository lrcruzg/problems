
# https://leetcode.com/problems/di-string-match/

from typing import List

class Solution:
	# O(n) time, O(1) space (not counting the answer array)
	def diStringMatch(self, S: str) -> List[int]:
		ans = []
		current_min, current_max = 0, len(S)
		for x in S:
			if x == 'I':
				ans.append(current_min)
				current_min += 1
			else:
				ans.append(current_max)
				current_max -= 1
		ans.append(current_min)
		return ans