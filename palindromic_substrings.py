
# https://leetcode.com/problems/palindromic-substrings/

class Solution:
	# O(n^2) time, O(n^2) space
	def countSubstrings(self, s: str) -> str:
		dp = [[True] * len(s) for _ in range(len(s))]
		counter = len(s)
		for l in range(2, len(s) + 1):
			for i in range(len(s) - l + 1):
				# dp[i][j] = dp[i][i + l - 1]
				dp[i][i + l - 1] = True if s[i] == s[i + l - 1] and dp[i + 1][i + l - 2] else False
				if dp[i][i + l - 1]: 
					counter += 1
		return counter