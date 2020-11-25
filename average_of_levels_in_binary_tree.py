
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque
from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space (queue)
	# n = number of nodes
	def averageOfLevels(self, root: TreeNode) -> List[float]:
		if not root: return []
		q = deque([root])
		avg = []
		while q:
			lev_sum = 0
			n = len(q)
			for _ in range(n):
				node = q.popleft()
				lev_sum += node.val
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			avg.append(lev_sum / n)
		return avg