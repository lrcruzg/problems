
# https://leetcode.com/problems/counting-bits/

from typing import List

class Solution:
	# O(n) time, O(n) space
	def countBits(self, num: int) -> List[int]:
		bits = [0] * (num + 1)
		if num > 0: bits[1] = 1
		for i in range(2, num + 1, 2):
			bits[i] = bits[i // 2]
			if i + 1 < num + 1:
				bits[i + 1] = bits[i // 2] + 1
		return bits

inp = 2
s = Solution()
print(s.countBits(inp))
