
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/

from typing import List

class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		maximum = max(candies)
		ans = []
		for i in candies:
			ans.append(i + extraCandies >= maximum)
		return ans