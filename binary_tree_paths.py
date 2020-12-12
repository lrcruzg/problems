
# https://leetcode.com/problems/binary-tree-paths/

from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def binaryTreePaths(self, root: TreeNode) -> List[str]:
		def dfs(node, current_path):
			if not node: return
			if not node.left and not node.right:
				self.paths.append(current_pat + str(node.val))
			dfs(node.left, current_path + str(node.val) + "->")
			dfs(node.right, current_path + str(node.val) + "->")
		self.paths = []
		dfs(root, "")
		return paths
