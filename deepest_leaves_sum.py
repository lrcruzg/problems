
# https://leetcode.com/problems/deepest-leaves-sum/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# O(n) time, O(n) space
# n = |V|
class Solution:
	def deepestLeavesSum(self, root: TreeNode) -> int:
		if not root: return 0
		deepest_leaves = [root.val]
		q = deque([root])
		while q:
			aux_deepest_leaves = []
			for _ in range(len(q)):
				node = q.popleft()
				if node.left:
					q.append(node.left)
					aux_deepest_leaves.append(node.left.val)
				if node.right:
					q.append(node.right)
					aux_deepest_leaves.append(node.right.val)
			if len(aux_deepest_leaves) != 0:
				deepest_leaves = aux_deepest_leaves
		return sum(deepest_leaves)
