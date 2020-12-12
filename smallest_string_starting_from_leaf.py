
# https://leetcode.com/problems/smallest-string-starting-from-leaf/

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def smallestFromLeaf(self, root: TreeNode) -> str:
		def aux(node, word):
			if not node: return
			if not node.left and not node.right:
				self.ans = min(self.ans, chr(node.val + 97) + word)
			aux(node.left,  chr(node.val + 97) + word)
			aux(node.right, chr(node.val + 97) + word)
		self.ans = "|"
		aux(root, "")
		return self.ans