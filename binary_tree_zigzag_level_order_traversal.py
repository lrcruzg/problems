
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque
from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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

		for i in range(len(ans)):
			if i % 2 == 1:
				ans[i] = ans[i][::-1]
		return ans