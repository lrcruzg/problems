
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def sumNumbers(self, root: TreeNode) -> int:
		def aux(node, num):
			if not node: return
			if not node.left and not node.right:
				self.ans += num * 10 + node.val
			aux(node.left,  num * 10 + node.val)
			aux(node.right, num * 10 + node.val)
		self.ans = 0
		aux(root, 0)
		return self.ans