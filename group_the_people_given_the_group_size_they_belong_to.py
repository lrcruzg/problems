
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import List

class Solution:
	# O(n) time, O(n) space
	def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
		persons_in_a_group_of_size = {}
		for i in range(len(groupSizes)):
			if groupSizes[i] not in persons_in_a_group_of_size:
				persons_in_a_group_of_size[groupSizes[i]] = [i]
			else:
				persons_in_a_group_of_size[groupSizes[i]].append(i)

		ans = []

		for size in persons_in_a_group_of_size.keys():
			tmp = persons_in_a_group_of_size[size]
			for i in range(0, len(tmp), size):
				ans.append(tmp[i: i + size])
		return ans