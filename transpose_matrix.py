
# https://leetcode.com/problems/transpose-matrix/

from typing import List

class Solution:
	# O(n * m) time, O(n * m) space
	# n = len(A), m = len(A[0])
	def transpose(self, A: List[List[int]]) -> List[List[int]]:
		AT = [[0] * len(A) for _ in range(len(A[0]))]
		for i in range(len(A)):
			for j in range(len(A[0])):
				AT[i][j] = A[j][i]
		return AT

