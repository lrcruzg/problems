
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque
from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if not root: return []
		ans = []
		q = deque([root])
		while q:
			curr_lev = []
			n = len(q)
			for _ in range(n):
				node = q.popleft()
				curr_lev.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			ans.append(curr_lev)

		return ans