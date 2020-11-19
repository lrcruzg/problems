
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

from typing import List

class Solution:
	# O(n) time, O(1) space
	def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
		counter = 0
		for i in range(len(startTime)):
			if startTime[i] <= queryTime and queryTime <= endTime[i]:
				counter += 1
		return counter