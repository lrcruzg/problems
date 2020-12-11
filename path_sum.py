
# https://leetcode.com/problems/path-sum/

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# O(n) time, O(n) space
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		def aux(node, cr):
			if not node: return
			if not node.left and not node.right and node.val + cr == sum:
					self.ans = True
			aux(node.left,  cr + node.val)
			aux(node.right, cr + node.val)
		self.ans = False
		aux(root, 0)
		return self.ans