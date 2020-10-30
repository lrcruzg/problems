
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def sumEvenGrandparent(self, root: TreeNode) -> int:
		ans = [0]
		def aux(root, parent_value, grandparent_value):
			if not root: return
			if grandparent_value % 2 == 0:
				ans[0] += root.val
			aux(root.left, root.val, parent_value)
			aux(root.right, root.val, parent_value)
		aux(root, -1, -1)
		return ans[0]