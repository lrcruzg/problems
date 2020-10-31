
# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# O(n) time, O(n) space
	def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
		def aux(root):
			if not root: return 0
			if root.val < L:
				return aux(root.right)
			if R < root.val:
				return  aux(root.left)
			return root.val + aux(root.left) + aux(root.right)

		return aux(root)