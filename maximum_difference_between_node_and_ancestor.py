
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

import math

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def maxAncestorDiff(self, root: TreeNode) -> int:
		def dfs(root):
			if not root.left and not root.right:
				return (root.val, root.val)
			l, r = (math.inf, -math.inf), (math.inf, -math.inf)
			if root.left:
				l = dfs(root.left)
			if root.right:
				r = dfs(root.right)
			minimum = min(l[0], r[0], root.val)
			maximum = max(l[1], r[1], root.val)
			self.mad = max(self.mad, root.val - minimum, maximum - root.val)
			return (minimum, maximum)
		self.mad = 0
		dfs(root)
		return self.mad