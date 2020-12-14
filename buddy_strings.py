
# https://leetcode.com/problems/buddy-strings/

class Solution:
	# O(n) time, O(1) space
	def buddyStrings(self, A: str, B: str) -> bool:
		if len(A) != len(B) or not A or not B: return False
		if A == B:
			A_counter = [0] * 26
			for c in A:
				A_counter[ord(c) - 97] += 1
			return max(A_counter[i] for i in range(26) if A_counter[i]) > 1
		count_dif = 0
		dif_index = [len(A), -1]
		for i in range(len(A)):
			if A[i] != B[i]:
				count_dif += 1
				if count_dif > 2: return False
				dif_index = [min(dif_index[0], i), max(dif_index[1], i)]
		return A[dif_index[0]] == B[dif_index[1]] and A[dif_index[1]] == B[dif_index[0]]