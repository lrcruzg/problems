
# https://leetcode.com/problems/validate-binary-search-tree/

import math

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# O(n) time, O(n) space
	def isValidBST(self, root: TreeNode) -> bool:
		def in_order(root):
			if not root: return []
			return in_order(root.left) + [root.val] + in_order(root.right)
		values_in_order = in_order(root)
		for i in range(1, len(values_in_order)):
			if values_in_order[i] <= values_in_order[i - 1]:
				return False
		return True

	'''
	# O(n) time, O(n) space
	def isValidBST(self, root: TreeNode) -> bool:
		def aux_vbst(root, minimum, maximum):
			if not root: return True
			if root.val <= minimum or maximum <= root.val:
				return False
			return aux_vbst(root.left, minimum, root.val) and aux_vbst(root.right, root.val, maximum)
		return aux_vbst(root, math.inf, - math.inf)
	'''