
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

import math

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def goodNodes(self, root: TreeNode) -> int:
		def aux(root, max_val):
			if not root: return
			if max_val <= root.val:
				gn[0] += 1
			max_val = max(max_val, root.val)
			aux(root.left, max_val)
			aux(root.right, max_val)

		gn = [0]
		aux(root, -math.inf)
		return gn[0]
