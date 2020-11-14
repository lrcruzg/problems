
# https://leetcode.com/problems/balance-a-binary-search-tree/

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def balanceBST(self, root: TreeNode) -> TreeNode:
		return self.BST_from_sorted_list(self.in_order(root))

	def in_order(self, root):
		if not root: return []
		return self.in_order(root.left) + [root.val] + self.in_order(root.right)

	def BST_from_sorted_list(self, l):
		if len(l) == 0: return None
		mid = len(l) // 2
		root = TreeNode(l[mid])
		root.left = self.BST_from_sorted_list(l[:mid])
		root.right = self.BST_from_sorted_list(l[mid + 1:])
		return root