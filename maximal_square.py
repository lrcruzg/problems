
# https://leetcode.com/problems/maximal-square/

class Solution:
	# O(n * m) time, O(n * m) space
	# dim(matrix) = n * m
	def maximalSquare(self, matrix) -> int:
		dp = matrix.copy()		
		current_max = 0

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				dp[i][j] = int(dp[i][j])
				if dp[i][j] == 1:
					current_max = 1

		for i in range(1, len(matrix)):
			for j in range(1, len(matrix[0])):
				if dp[i][j] == 1:
					dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
				current_max = max(current_max, dp[i][j])
		return current_max * current_max