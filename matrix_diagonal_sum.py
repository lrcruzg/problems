
# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List

class Solution:
	# O(n) time, O(1) space
	# n = len(A) = len(A[0])
	def diagonalSum(self, mat: List[List[int]]) -> int:
		ds = 0
		for i in range(len(mat)):
			ds += mat[i][i] + mat[i][len(mat) - i - 1]
		return ds if len(mat) % 2 == 0 else ds - mat[len(mat) // 2][len(mat) // 2]