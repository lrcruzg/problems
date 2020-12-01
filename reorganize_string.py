
# https://leetcode.com/problems/reorganize-string/submissions/

class Solution:
	# O(nlog(n)) time, O(n) space
	def reorganizeString(self, S: str) -> str:
		n = len(S)
		counter = [0] * 27

		for c in S:
			counter[ord(c) - 97] += 1

		if max(counter) > (n + 1) / 2:
			return ""

		s_sorted = sorted(S, key= lambda x: (counter[ord(x) - 97], x), reverse= True)

		l1 = s_sorted[:(n + 1) // 2]
		l2 = s_sorted[(n + 1) // 2:]

		for i in range(n):
			if i % 2 == 0:
				s_sorted[i] = l1[i // 2]
			else:
				s_sorted[i] = l2[i // 2]
		return "".join(s_sorted)