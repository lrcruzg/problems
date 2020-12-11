
# https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# O(n) time, O(n) space (recursion stack)
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		def diam_aux(node):
			if not node: return 0
			l, r = diam_aux(node.left), diam_aux(node.right)
			# lp := longest path containig node as root
			lp = l + r
			self.diam = max(self.diam, lp)
			return 1 + max(l, r)
		self.diam = 0
		diam_aux(root)
		return self.diam