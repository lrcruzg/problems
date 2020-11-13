
# https://leetcode.com/problems/coin-change/

import math
from typing import List

class Solution:
	# O(n * m) time, O(m) space
	# where n = len(coins) and m = amount
	def coinChange(self, coins: List[int], amount: int) -> int:
		dp = [0] * (amount + 1)

		for i in range(1, len(dp)):
			curr_min = math.inf
			for j in range(len(coins)):
				if i - coins[j] >= 0:
					curr_min = min(curr_min, 1 + dp[i - coins[j]])
			dp[i] = curr_min

		return dp[-1] if dp[-1] != math.inf else -1