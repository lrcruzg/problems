
# https://leetcode.com/problems/longest-univalue-path/

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def longestUnivaluePath(self, root: TreeNode) -> int:
		def aux(node):
			if not node: return 0
			l, r = aux(node.left), aux(node.right)
			if node.left and node.left.val != node.val:
				l = 0
			if node.right and node.right.val != node.val:
				r = 0
			self.lup = max(self.lup, 1 + l + r)
			return 1 + max(l, r)

		self.lup = 0
		aux(root)
		return self.lup - 1 if self.lup else 0