
# https://leetcode.com/problems/richest-customer-wealth/submissions/

from typing import List

class Solution:
	# O(n) time, O(1) time
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		mw = 0
		for i in range(len(accounts)):
			mw = max(mw, sum(accounts[i][j] for j in range(len(accounts[i]))))
		return mw
