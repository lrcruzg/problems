
# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
	# O(n * m) time, O(n * m) space
	# n = len(text1), m = len(text2)
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		if not text1 or not text2: return 0
		n, m = len(text1), len(text2)
		dp = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if text1[i - 1] == text2[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
		print(dp)
		return dp[-1][-1]