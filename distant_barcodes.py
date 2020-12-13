
# https://leetcode.com/problems/distant-barcodes/submissions/

from typing import List

class Solution:
	# O(nlog(n)) time, O(n) space
	def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
		n = len(barcodes)
		num_oc = {}
		for b in barcodes:
			if b in num_oc:
				num_oc[b] += 1
			else:
				num_oc[b] = 1

		barcodes.sort(key= lambda x : (num_oc[x], x), reverse= True)

		l1 = barcodes[:(n + 1) // 2]
		l2 = barcodes[(n + 1) // 2:]

		for i in range(n):
			if i % 2 == 0:
				barcodes[i] = l1[i // 2]
			else:
				barcodes[i] = l2[i // 2]
		return barcodes